# Good Trouble Safety Automation Toolkit - Project Plan

## Vision

Make the Good Trouble Safety Automation Toolkit accessible to everyone, regardless of their mobile platform, while maintaining simplicity and reliability.

---

## Current Status

- [x] Project structure created
- [x] README with overview and prerequisites
- [x] Legal rights audio files (English, Spanish)
- [x] Community standards (CODE_OF_CONDUCT, CONTRIBUTING, SECURITY)
- [x] GitHub issue templates
- [x] Claude Code configuration
- [x] Cross-platform directory structure (doc/ios, doc/android, tasker)
- [x] Tasker task files for Android
- [x] Python TTS audio generation tools

---

## Phase 1: iOS Documentation

Create step-by-step build guides with screenshots in `doc/ios/`.

### Deliverables
- [ ] PDF guide with screenshots for building the main shortcut
- [ ] Word document version (editable)
- [ ] PDF guide for audio playback shortcut setup
- [ ] Screenshots for each step of the shortcut build process

### Content Outline
1. Introduction and prerequisites
2. Part 1: Create new shortcut
3. Part 2: Get current location
4. Part 3: Format location for sharing
5. Part 4: Create emergency message
6. Part 5: Configure emergency contacts
7. Part 6: Send messages
8. Part 7: Audio playback setup
9. Part 8: Video recording
10. Part 9: Final configuration and triggers
11. Testing guide
12. Troubleshooting

---

## Phase 2: Android Support (Current)

Add Tasker-based workflow for Android users.

### Deliverables
- [x] Tasker directory structure
- [x] GoodTrouble_Main.tsk.xml - Main emergency workflow
- [x] GoodTrouble_Audio.tsk.xml - Audio playback task
- [x] tasker/README.md - Import instructions
- [x] Update SECURITY.md for Android permissions
- [x] Update CONTRIBUTING.md for Tasker contributions

### Documentation (doc/android/)
- [ ] PDF guide for Tasker setup
- [ ] Word document version (editable)
- [ ] Screenshots for import and configuration
- [ ] Permission configuration guide
- [ ] Trigger setup instructions (widget, gesture, etc.)

---

## Phase 3: TTS Audio Generation Tools (Complete)

Python-based text-to-speech tooling for generating legal rights audio files.

### Deliverables
- [x] Python TTS script for audio generation
- [x] Script documentation and usage guide
- [x] Text templates for legal rights scripts (English, Spanish)
- [x] Audio post-processing (segment combining via pydub)

### Directory Structure
```
python/
├── tts/
│   └── text_to_speech.py   # Main TTS generation script
├── scripts/
│   ├── legal_rights_en.txt # English text template
│   └── legal_rights_es.txt # Spanish text template
├── requirements.txt        # Python dependencies
├── README.md               # Full documentation
├── QUICKSTART.md           # Quick start guide
└── demo.sh                 # Demo script
```

### Features
- Support for multiple TTS engines (gTTS online, pyttsx3 offline)
- Batch generation for multiple languages
- Configurable speech rate and language settings
- Segment combining with configurable pauses
- Output in MP3 format for cross-platform compatibility

---

## Phase 4: Additional Languages

Expand audio support beyond English and Spanish using TTS tools.

### Potential Languages
- [ ] French
- [ ] Mandarin Chinese
- [ ] Arabic
- [ ] Portuguese
- [ ] Vietnamese
- [ ] Korean

### Requirements per Language
- Accurate legal rights information for relevant jurisdictions
- Text template reviewed by someone familiar with local laws
- TTS generation or native speaker recording
- Quality review of generated audio

---

## Phase 5: Distribution

Make the toolkit easy to install and share.

### Options to Explore
- [ ] Pre-built iOS .shortcut file for direct import
- [ ] iCloud sharing link for iOS
- [ ] Direct Tasker import links for Android
- [ ] QR codes for quick access
- [ ] Website landing page

---

## Phase 6: Enhancements

Future feature ideas (community-driven).

### Both Platforms
- [ ] Multiple message templates (customizable)
- [ ] Integration with other messaging apps (Signal, WhatsApp)
- [ ] Automated location updates (periodic)
- [ ] Silent/stealth mode option

### iOS-Specific
- [ ] Apple Watch companion shortcut
- [ ] Siri activation improvements

### Android-Specific
- [ ] Home screen widget
- [ ] Quick Settings tile
- [ ] Wear OS companion (if community interest)

---

## Notes

- Priority is documentation - must be complete before wider distribution
- Audio files require careful legal review before adding new languages
- Keep user experience simple - this may be used in stressful situations
- Test on actual devices before finalizing any platform-specific features
- Community feedback drives enhancement priorities
