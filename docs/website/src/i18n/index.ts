import { createI18n } from 'vue-i18n'
import en from '../../res/i18n/en.json'
import ru from '../../res/i18n/ru.json'

const SUPPORTED = ['en', 'ru']
const STORAGE_KEY = 'mmmcp-locale'

const savedLocale = typeof localStorage !== 'undefined' ? localStorage.getItem(STORAGE_KEY) : null
const browserLocale = typeof navigator !== 'undefined' ? navigator.language : 'en'

function detectLocale(): string {
  if (savedLocale && SUPPORTED.includes(savedLocale)) {
    return savedLocale
  }
  if (browserLocale.startsWith('ru')) return 'ru'
  return 'en'
}

const i18n = createI18n({
  legacy: false,
  locale: detectLocale(),
  fallbackLocale: 'en',
  messages: {
    en,
    ru,
  },
})

export default i18n
