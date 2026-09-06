plugins {
    `java`
    `maven-publish`
}

group = "xyz.langyo.minecraft.mcp"
version = "0.4.0-wayland.2"

java {
    toolchain { languageVersion = JavaLanguageVersion.of(25) }
    sourceCompatibility = JavaVersion.VERSION_25
    targetCompatibility = JavaVersion.VERSION_25
}

repositories {
    mavenCentral()
}

dependencies {
    implementation("com.google.code.gson:gson:2.11.0")
}

publishing {
    publications {
        create<MavenPublication>("maven") {
            from(components["java"])
        }
    }
    repositories {
        maven {
            url = uri(layout.projectDirectory.dir("../../.maven-local"))
        }
    }
}
