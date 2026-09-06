# AGENTS.md — Rules for AI Agents (minecraft-mod-mcp)

> This file governs every AI agent / subagent / coding tool working in this
> repository. It was adapted on **2026-09-03** from the Celestia workspace
> rules (`/mnt/codespace/AGENTS.md` on the yuzu-linux daemon host), keeping
> only the parts that apply to this repo. Where the Celestia workspace rules
> conflict with this repo's own conventions ([CONTRIBUTING.md](CONTRIBUTING.md)),
> **this repo's conventions win**; every deliberate deviation is listed in §9.
>
> **Headline change (2026-09-06, maintainer directive): direct commits and
> pushes to `master` are allowed. Pull requests and feature branches are
> optional; PRs are not used unless the maintainer explicitly asks. The old
> `dev` integration branch remains retired.**

---

## 1. Branch model

- `master` — the only long-lived branch. Direct commits and pushes are allowed;
  commit subjects must pass the `lint` check. Force-pushes and deletions remain
  blocked for everyone including the maintainer.
- `dev` — **retired on 2026-09-03** (branch deleted). Before deletion,
  `master` was fast-forwarded to the final `dev` tip, so no history was lost.
  Do not recreate `dev`; old `dev`-based local branches should be rebased onto
  `master`.
- Feature branches (`feat/<name>`, `fix/<name>`, `chore/<name>`,
  `refactor/<name>`) are optional and branch from `master`.

## 2. Commit message format (CI-enforced)

```
<Capitalized English one-sentence summary ending with a period.>
```

- One plain English sentence: capitalized first letter, ends with exactly one
  `.`, printable ASCII only (no CJK).
- PR titles should follow the same rule only when the maintainer explicitly requests a PR.
- `Revert "..."` subjects produced by `git revert` are exempt.
- Squash-merge suffix ` (#123)` is allowed.
- Local check before pushing: `just lint-commits` (validates
  `origin/master..HEAD`). CI runs the same linter (`scripts/commit_lint.py`)
  on every new commit pushed to `master` and on PR titles when a PR is used.

## 3. Push workflow

1. **Verify locally before pushing**: `just full` for build changes (or at
   minimum the touched package: `just mcp-build`, `just mcp-lint`, relevant
   `just build-mod`), `just lint-commits` always. Run `just smoke <version>`
   when behavior can only be proven in-game.
   Maintainer scope is MC 26.2 Fabric and Forge only: use `just build-mod 26.2
   fabric` or `just build-mod 26.2 forge` (or direct Gradle here); do not build
   the full matrix locally. `generate_mods.py` only generates on demand; keep
   other mod packages.
2. **Commit and push** directly to `master` on `origin`, the maintainer's fork.
   Never push to `upstream`.
3. Never create, comment on, update, merge, or otherwise touch a PR unless the
   maintainer explicitly instructs that exact action in this conversation.
4. **Version bumps belong with the feature/fix**: bump
   `packages/minecraft-mod-mcp/package.json` inside the feature/fix that
   warrants a release; never open standalone version-bump PRs. Releases are
   then tag-driven (`git tag vX.Y.Z && git push --tags`).

## 4. Git push discipline

- Push only to `origin` (`https://github.com/gasada-dev/minecraft-mod-mcp`),
  the maintainer's fork. Never push to `upstream` (`https://github.com/langyo/minecraft-mod-mcp.git`).
- **NEVER use bare `git push --force`** — no exceptions for "convenience".
- Prefer `git push --force-with-lease` for rebase/amend recovery on your own
  feature branch.
- If `--force-with-lease` is rejected (stale remote-tracking ref), **STOP**.
  Never fall back to `--force`: fetch, inspect with
  `git log origin/<branch>..HEAD` and `git log HEAD..origin/<branch>`, and ask
  the maintainer if anything is unaccounted for.
- Force-pushes of any kind to `master` are forbidden.
- This applies to all agents, subagents, and interactive sessions.

## 5. Sensitive information red line (hard rule)

> Learned from a real incident in the Celestia family: a live SSH password
> committed to a repo required history rewriting. Treat a violation here as an
> incident of the same severity.

1. **Never put real passwords / keys / tokens / internal IPs into the git
   tree** — any file, branch, comment, example, test fixture, or doc. This
   includes the Celestia workspace files (`/mnt/codespace/AGENTS.md`,
   `PLAN.md`), which contain real credentials: read them for context if you
   must, but **never copy their values into any file of this repo** (including
   this AGENTS.md).
2. Need a secret in code? Use environment variables / untracked config files,
   or obvious placeholders (`<your-token>`, `CHANGE_ME`, `sk-xxx`). Example
   addresses use RFC 5737 documentation ranges (192.0.2.x / 198.51.100.x /
   203.0.113.x) and example values (`test-password`).
3. If a real credential is genuinely required, **ask the maintainer first**;
   never write it on your own authority.
4. **Before committing** anything touching config/deploy/scripts/fixtures:
   grep your diff for `password|secret|token|api_key` and for `192.168.` /
   `10.` internal addresses; replace hits per the rules above.
5. If a leak happens anyway: remove it from the branch/PR, assess the blast
   radius (tags/branches/forks), report to the maintainer, and treat the
   credential as public — rotate it regardless of any history rewrite.

## 6. Verification & CI usage

- CI runs on GitHub-hosted runners (public repo → free; unlike the Celestia
  self-hosted fleet, there is no shared-runner quota to protect, but the
  Windows mod matrix is slow — see below).
- Every workflow already sets `concurrency` + `cancel-in-progress`, so stale
  runs are cancelled automatically; do not add workflows without a
  `concurrency` group.
- **What runs where**: pushes to `master` run the full pipeline including
  smoke/screenshot/E2E tests and the push-format guard. Explicitly requested
  PRs run the build matrix (`ci.yml`) and fast commit/PR-title lint (`commit-lint.yml`).
- **CI is a gate for code failures, not a tea ceremony**: for docs/config-only
  changes you may push once the lint check is green and relevant code checks
  pass, without waiting out the full Windows build matrix. Never push over a
  real compile/test failure; if checks are merely queued, wait or re-run.
- Do not sit and watch CI. If a run is stuck queued for an unusually long
  time, investigate (`gh run list`, `gh run cancel <id>`) instead of stacking
  more pushes on top.

## 7. CHANGELOG policy

- **Never create a CHANGELOG / revision-history file in this repo.** Git
  history is the changelog; commit subjects and PR descriptions provide detail,
  and `git log` serves any granularity.
- Release notes live on the git tag / GitHub Releases page (written per
  release, never per commit) — the `release.yml` workflow already does this.

## 8. Local lint recipe

```bash
just lint-commits                     # validate origin/master..HEAD
just lint-commits v0.2.0..master      # validate any range
python scripts/commit_lint.py --subject "Add a new tool."     # one subject
```

## 9. Deliberately NOT adopted from the Celestia workspace rules

| Celestia rule | Why not here |
|---|---|
| §0.6 large-download / sing-box proxy discipline | Specific to the yuzu-linux NAT/proxy network and its airport-quota incidents; this repo builds on GitHub-hosted runners and the maintainer's Windows machine. |
| §1 node table, passwords, NFS layout | Workspace infrastructure — and per §5 above, its credentials must never be copied into this repo. |
| §2 Celestia-island repo layout | Different family of repositories. |
| §7 Rust/pnpm/CARGO_HOME & self-hosted runner ops | This is a Gradle/npm/Python repo on hosted runners. |
| §7 "CI 是参考不是门禁" waiver culture | Softened: hosted CI is the real gate here; only documented waivers for docs-only changes (§6). |
| §8 node-2/3 deployment & malkuth supervision | No deployment fleet; releases are tag-driven GitHub Releases. |
| §9 pnpm registry / sibling links / worktree symlink discipline | NFS multi-agent infra that does not exist here. |

> The Celestia §5 PR-only and squash-merge model is **not adopted** here;
> `dev` remains retired — see §1.

## 10. Local test instances (Prism)

- Use these for live MCP testing against clients; they complement, not replace,
  `just smoke`. Both use the local Folia server at `127.0.0.1:25565` (log:
  `/home/gasada/ai/vanillabox/vnbx-dev/server/logs/latest.log`) and have mod
  build `0.3.1-wayland` (Fabric, MC 26.2) installed.
- `test` — player `gasada`, mod HTTP endpoint `http://127.0.0.1:9876`.
- `test2` — player `faint_sound`, mod HTTP endpoint `http://127.0.0.1:9875`.
- Launch with `PrismLauncher-Linux-x86_64.AppImage --appimage-extract-and-run --launch test`
  (replace `test` with `test2`). Prism is single-instance: a second invocation
  forwards to its running process; see `docs/guides/en/WAYLAND.md`.
- Verify readiness: `curl -s http://127.0.0.1:9876/api/status`.
