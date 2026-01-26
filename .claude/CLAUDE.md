# Good Trouble Safety Automation Toolkit

## Project Overview

This is a cross-platform emergency alert toolkit designed to help people stay safe during encounters. The toolkit enables users to quickly notify trusted contacts of their location and document interactions.

**Supported Platforms:**
- **Mac Desktop** (primary development platform - Shortcuts app with Apple Intelligence)
- **iOS** (deployment platform via iCloud sync)
- **Android** (using Tasker)

**This is NOT a traditional software project** - it consists of:
- Documentation for building automation workflows on Mac Desktop
- iOS deployment and trigger configuration guides
- Pre-recorded legal rights audio files
- Importable Tasker task files for Android
- Python TTS tools for generating audio files
- Community and contribution guidelines

## Purpose

The automation workflow performs these actions when triggered:
1. Gets current GPS location
2. Sends emergency alert with location to trusted contacts
3. Plays legal rights audio (English or Spanish)
4. Starts video recording to document the interaction

## Directory Structure

```
.
├── .claude/            # Claude Code configuration
│   ├── CLAUDE.md       # This file
│   └── PLAN.md         # Project roadmap
├── .github/
│   └── ISSUE_TEMPLATE/ # GitHub issue templates
├── audio/              # Shared legal rights audio files (MP3)
├── doc/
│   ├── mac/            # Mac Desktop shortcut creation guides (PRIMARY)
│   ├── ios/            # iOS deployment and trigger setup guides
│   └── android/        # Tasker guides (PDF/Word)
├── python/             # Python TTS audio generation tools
│   ├── tts/            # TTS conversion scripts
│   ├── scripts/        # Text templates for audio generation
│   ├── requirements.txt
│   └── README.md
├── tasker/             # Importable Tasker files
│   ├── GoodTrouble_Main.tsk.xml
│   ├── GoodTrouble_Audio.tsk.xml
│   └── README.md
├── CODE_OF_CONDUCT.md  # Contributor Covenant
├── CONTRIBUTING.md     # Contribution guidelines
├── LICENSE             # Project license
├── README.md           # Project overview
├── SECURITY.md         # Security policy and data handling
└── TEST_PLAN.md        # Comprehensive testing procedures
```

## Key Files

| File | Purpose |
|------|---------|
| `README.md` | Project overview, prerequisites, and pointer to documentation |
| `doc/mac/` | Mac Desktop shortcut creation guides (PRIMARY PLATFORM) |
| `doc/ios/` | iOS deployment, trigger setup, and usage guides |
| `doc/android/` | Tasker setup guides with screenshots |
| `tasker/*.tsk.xml` | Importable Tasker task files |
| `tasker/README.md` | Tasker import instructions |
| `python/tts/text_to_speech.py` | TTS audio generation script |
| `python/scripts/*.txt` | Text templates for audio generation |
| `python/README.md` | TTS tool documentation |
| `audio/legal_rights_en_complete.mp3` | English legal rights audio |
| `audio/legal_rights_es_complete.mp3` | Spanish legal rights audio |
| `SECURITY.md` | Privacy considerations for all platforms |
| `TEST_PLAN.md` | Comprehensive test plan for all platforms |

## Guidelines for AI Assistants

### Do
- Keep documentation clear and accessible to non-technical users
- Maintain bilingual support (English/Spanish) where applicable
- Consider privacy implications when suggesting changes
- Remember this is for personal safety - accuracy matters
- Keep platform-specific documentation in the appropriate subdirectory
- Maintain valid Tasker XML format in `.tsk.xml` files
- Document Mac Desktop Apple Intelligence features where applicable
- Emphasize iCloud sync setup for Mac-to-iOS workflow

### Don't
- Add executable code beyond Tasker XML exports
- Remove or modify the legal rights audio content without explicit request
- Add dependencies or build systems
- Over-engineer - keep it simple for end users
- Mix Mac Desktop creation and iOS deployment instructions in the same document
- Mix iOS and Android instructions in the same document

### When Adding Documentation
- Use clear, step-by-step instructions
- Include screenshots where helpful
- Consider users who may be stressed when using this toolkit
- Test instructions on actual devices when possible
- Place Mac Desktop creation docs in `doc/mac/`
- Place iOS deployment/trigger docs in `doc/ios/`
- Place Android docs in `doc/android/`
- Highlight Mac Desktop advantages (larger screen, Apple Intelligence, better debugging)

### Audio File Conventions
- Format: MP3 (compatible with both platforms)
- Naming: `legal_rights_[language_code]_complete.mp3`
- Languages should have accurate legal information reviewed by appropriate experts

### Tasker File Conventions
- Task files: `*.tsk.xml`
- Profile files: `*.prf.xml`
- Use descriptive names prefixed with `GoodTrouble_`
- Include comments in XML for clarity
- Test exports before committing

### Python TTS Conventions
- Text templates: `python/scripts/legal_rights_[lang_code].txt`
- One statement per line in text templates
- Comments start with `#` and are ignored
- Output audio format: MP3
- Support both gTTS (online) and pyttsx3 (offline) engines

## Platform-Specific Notes

### Mac Desktop (Primary Development Platform)
- Requires macOS 13.0 (Ventura) or later for full Apple Intelligence features
- Uses built-in Shortcuts app
- **Apple Intelligence Features**:
  - **Use Model**: Access AI models to optimize shortcut logic and messages
  - **Writing Tools**: Refine emergency message templates with AI assistance
  - **Create Image**: Generate visual aids, QR codes, or documentation graphics
- **Development Advantages**:
  - Full keyboard and larger screen for complex shortcut building
  - Better debugging and testing capabilities
  - iCloud sync automatically deploys to iOS devices
- Documentation should include Mac Shortcuts app screenshots
- Shortcut files sync via iCloud (cannot be directly included in repo)

### iOS (Deployment Platform)
- Requires iOS 15.0+
- Receives shortcuts via iCloud sync from Mac
- Uses built-in Shortcuts app
- **iOS-specific features**:
  - Back Tap gesture trigger
  - Siri voice activation
  - Home screen widgets
  - Automation triggers based on time/location
- Documentation focuses on deployment, triggers, and usage (not creation)
- Required permissions: Location, Camera, Contacts, Notifications

### Android (Tasker)
- Requires Android 7.0+
- Requires Tasker app (paid)
- Task XML files can be imported directly
- Required permissions: Location, SMS, Camera, Storage, Microphone
- May need AutoInput or similar plugins for some features

## Sensitive Considerations

This toolkit handles:
- GPS location data
- Emergency contact information
- Video recordings of potentially sensitive situations

Always consider privacy and security implications when making changes. See `SECURITY.md` for platform-specific security guidance.
