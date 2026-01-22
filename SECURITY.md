# Security Policy

## About This Project

This toolkit consists of automation workflows (iOS Shortcuts and Android Tasker) and audio files. It does not include executable code or server-side components.

## Security Considerations

### Personal Data

The automation workflow handles sensitive information:

- **GPS location data** - Shared with your designated emergency contacts
- **Contact phone numbers** - Stored locally in your device's apps
- **Video recordings** - Saved to your device's storage

**Before sharing this workflow with others:**

- Remove all personal contact information
- Replace hardcoded values with prompts that ask for input
- Test that no personal data is embedded in the exported workflow

---

## Platform-Specific Permissions

### iOS (Shortcuts)

The shortcut requires the following iOS permissions:

| Permission | Purpose |
|------------|---------|
| Location Services | Gets GPS coordinates for emergency message |
| Messages | Sends alerts to emergency contacts |
| Camera | Records video to document the interaction |
| Files | Plays legal rights audio files |

**How to review:** Settings > Privacy & Security > [Permission Type]

### Android (Tasker)

The Tasker workflow requires the following Android permissions:

| Permission | Purpose |
|------------|---------|
| Location (Fine) | Gets precise GPS coordinates |
| SMS | Sends text messages to emergency contacts |
| Camera | Records video to document the interaction |
| Microphone | Required for video recording with audio |
| Storage | Reads audio files and saves recordings |
| Run in Background | Ensures workflow completes even if screen locks |

**How to grant:** Settings > Apps > Tasker > Permissions

**Important Android Notes:**
- Some manufacturers (Samsung, Xiaomi, etc.) have aggressive battery optimization that may prevent Tasker from running. You may need to disable battery optimization for Tasker.
- Android 10+ requires granting location permission "Allow all the time" for background location access.
- Some features may require the AutoInput plugin (separate app).

---

## Reporting a Security Issue

If you discover a security vulnerability or privacy concern:

1. **Do not** open a public issue
2. Contact the maintainers privately via GitHub (use the "Security" tab to report a vulnerability)
3. Provide details about the issue and steps to reproduce
4. Allow time for the issue to be addressed before public disclosure

## Responsible Use

This toolkit is designed for personal safety. Please use it responsibly and in accordance with local laws regarding:

- Recording consent (one-party vs. two-party consent states/countries)
- Emergency communications
- Location sharing

---

## Data Storage Summary

| Data Type | iOS Storage | Android Storage |
|-----------|-------------|-----------------|
| Contact numbers | Shortcuts app | Tasker variables |
| GPS coordinates | Transmitted only, not stored | Transmitted only, not stored |
| Video recordings | Photos app | Device storage (DCIM or Movies) |
| Audio files | iCloud/Files app | Device storage |

No data is transmitted to external servers. All data stays on your device and is only shared with your designated emergency contacts when the workflow is triggered.
