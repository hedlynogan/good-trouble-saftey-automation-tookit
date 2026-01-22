# Good Trouble Safety Automation Toolkit

An emergency alert system for iOS and Android that helps keep you safe during encounters by automatically notifying trusted contacts and documenting interactions.

## Overview

**Name**: Good Trouble Safety Automation Toolkit
**Purpose**: Emergency alert system that sends GPS location to trusted contacts
**Platforms**: iOS (Shortcuts) and Android (Tasker)

---

## What This Toolkit Does

When triggered, the automation workflow:

1. Gets your current GPS location
2. Formats an emergency alert message with location
3. Sends the message to 1-3 trusted contacts
4. Plays legal rights audio (English or Spanish)
5. Starts video recording to document the interaction

---

## Choose Your Platform

### iOS (iPhone)

**Requirements:**
- iPhone with iOS 15.0 or later
- Shortcuts app (pre-installed)
- Contacts app with emergency contacts saved
- Messages app

**Documentation:** See `doc/ios/` for step-by-step build instructions with screenshots.

### Android

**Requirements:**
- Android device running Android 7.0 or later
- Tasker app (paid, available on Google Play)
- Contacts with emergency contacts saved
- Default SMS app

**Quick Start:** Import the pre-built Tasker tasks from the `tasker/` directory. See `tasker/README.md` for import instructions.

**Documentation:** See `doc/android/` for detailed setup guides.

> **Note:** Unlike iOS, Android does not have a built-in automation app. Complex workflows require third-party apps like Tasker. See `tasker/README.md` for alternatives including MacroDroid and Automate.

---

## Audio Files Included

This toolkit includes legal rights audio recordings in two languages:

- **English**: `audio/legal_rights_en_complete.mp3`
- **Spanish**: `audio/legal_rights_es_complete.mp3`

These audio files work on both iOS and Android platforms.

---

## Project Structure

```
.
├── audio/              # Shared audio files (both platforms)
├── doc/
│   ├── ios/            # iOS Shortcuts guides
│   └── android/        # Tasker guides
├── tasker/             # Importable Tasker files for Android
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── LICENSE
├── README.md
└── SECURITY.md
```

---

## Security Checklist

Before sharing your workflow with others:

- [ ] Remove your personal contact phone numbers
- [ ] Replace with prompts that ask for input
- [ ] Test that no personal data is embedded
- [ ] Export and inspect for sensitive information
- [ ] Verify location permissions are clearly documented

See [SECURITY.md](SECURITY.md) for platform-specific privacy considerations.

---

## Contributing

We welcome contributions for both platforms. See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

---

## License

See [LICENSE](LICENSE) for details.

---

**Need Help?** Open an issue on GitHub or reach out to the community.
