# iOS Deployment & Trigger Setup Guide

## Overview

This directory contains documentation for deploying the Good Trouble Safety Automation shortcut to your iPhone and configuring iOS-specific triggers.

## Important: Mac Desktop First

**This shortcut is built on Mac Desktop**, not directly on iPhone. The Mac development approach provides:
- Better development experience with larger screen and full keyboard
- Apple Intelligence features to optimize your emergency shortcut
- Easier testing and debugging before deployment
- Automatic sync to all your iOS devices via iCloud

**See `/doc/mac/`** for complete shortcut creation instructions.

## This Guide Covers

Once you've built your shortcut on Mac Desktop, this guide helps you:

1. **Verify iCloud Sync** - Confirm shortcut appears on iPhone
2. **Configure iOS Triggers** - Set up quick activation methods
3. **Grant Permissions** - Enable Location, Camera, Contacts access
4. **Test on iOS** - Verify everything works on your iPhone
5. **Troubleshoot Issues** - Resolve iOS-specific problems

## Prerequisites

Before using this guide:

### Mac Desktop Setup (Required First)
- [ ] Shortcut created on Mac Desktop (see `/doc/mac/`)
- [ ] iCloud account with Shortcuts sync enabled
- [ ] Shortcut tested and working on Mac

### iPhone Requirements
- iPhone running **iOS 15.0** or later
- Same **iCloud account** as your Mac
- **iCloud Shortcuts sync** enabled
- Sufficient storage for audio files and video recordings

## Quick Start

### Step 1: Verify Shortcut Synced to iPhone

1. Open **Shortcuts app** on iPhone
2. Look for your emergency shortcut in "All Shortcuts"
3. If not visible after 5 minutes, check:
   - iCloud sync is enabled: **Settings > [Your Name] > iCloud > Shortcuts**
   - Both devices connected to internet
   - Mac has completed upload (check Shortcuts app on Mac)

### Step 2: Configure iOS Triggers

iOS offers multiple ways to quickly activate your emergency shortcut. Choose the methods that work best for you:

#### Recommended Triggers (Choose 1-2)

1. **Back Tap** (Fastest, Most Discreet)
   - **Settings > Accessibility > Touch > Back Tap**
   - Set **Double Tap** or **Triple Tap** to run your shortcut
   - Works even with screen locked
   - **Most recommended for emergencies**

2. **Siri Voice Command**
   - Say "Hey Siri, [shortcut name]"
   - Works hands-free
   - May not be discreet in all situations

3. **Home Screen Widget**
   - Add Shortcuts widget to home screen
   - Single tap to activate
   - Visible and easy to access

4. **Control Center**
   - **Settings > Control Center**
   - Add "Shortcuts" control
   - Swipe down, tap shortcut

#### Additional Trigger Options

5. **Automation Trigger**
   - Open Shortcuts app > **Automation** tab
   - Create automation based on:
     - Time of day
     - Arriving/leaving location
     - Connecting to specific WiFi
     - Opening specific app

6. **Lock Screen Widget** (iOS 16+)
   - Long press lock screen to customize
   - Add Shortcuts widget
   - Access before unlocking

### Step 3: Grant Required Permissions

On first run, iOS will request permissions:

1. **Location Services**
   - Required for GPS coordinates
   - Choose: **While Using the App** or **Always**

2. **Contacts**
   - Required to send messages to emergency contacts
   - Tap **Allow**

3. **Camera & Photos**
   - Required for video recording
   - Choose **Allow** for both

4. **Notifications** (Optional)
   - Helpful for confirmation messages
   - Recommended: **Allow**

### Step 4: Test Your Setup

**Important**: Test with real contacts who are aware you're testing!

1. Trigger shortcut using your chosen method
2. Verify:
   - Location is captured
   - Messages sent to contacts
   - Audio plays correctly
   - Video recording starts
3. Ask contacts to confirm they received the message

## Documentation Contents

This directory contains (or will contain):

- [ ] **iCloud Sync Verification Guide** (PDF/Word)
- [ ] **iOS Trigger Setup Guide** (PDF/Word) - All trigger methods with screenshots
- [ ] **iOS Permissions Configuration** (PDF/Word)
- [ ] **iOS Testing Procedures** (PDF/Word)
- [ ] **iOS Troubleshooting Guide** (PDF/Word)

### Current Files

- `ShortcutTutorial.pdf` - Tutorial for building shortcuts (Note: Now use Mac Desktop instead)
- `WorkflowTutorial.pdf` - Workflow tutorial
- `ScreenShots/` - Screenshots for reference
- `Adobe Acrobat.html` - Additional documentation

**Note**: Existing tutorials may reference building shortcuts directly on iOS. The current recommended approach is to build on Mac Desktop (see `/doc/mac/`) and deploy via iCloud sync.

## iOS-Specific Features

### Back Tap (Most Important)

The **Back Tap** feature is the fastest way to trigger your emergency shortcut:

- Works with screen **locked**
- **No** unlocking required
- Discreet (no visible indication)
- Accessible in any situation

**Setup**: Settings > Accessibility > Touch > Back Tap > Double Tap > [Your Shortcut]

### Siri Voice Activation

Hands-free activation:
- "Hey Siri, run Good Trouble" (or your shortcut name)
- Works with screen locked if enabled in settings
- Less discreet than Back Tap

**Setup**: Just say the command - Siri learns your shortcut names automatically

### Lock Screen Access (iOS 16+)

Quick access from lock screen:
- No unlocking required
- Visible widget for one-tap access
- Customizable appearance

## Troubleshooting

### Shortcut Not Appearing on iPhone

1. **Check iCloud Sync**
   - Settings > [Your Name] > iCloud > **Shortcuts** (ensure ON)
   - Wait 5-10 minutes after saving on Mac
   - Ensure both devices connected to internet

2. **Force Sync**
   - On Mac: Make small edit to shortcut and save
   - On iPhone: Open Shortcuts app and pull down to refresh

3. **Check Storage**
   - Settings > General > iPhone Storage
   - Ensure sufficient space for shortcut and audio files

### Shortcut Won't Run on iOS

1. **Grant Permissions**
   - Settings > Privacy & Security
   - Review Location, Contacts, Camera permissions
   - Ensure Shortcuts has access

2. **Update iOS**
   - Settings > General > Software Update
   - Requires iOS 15.0 minimum

3. **Rebuild Sync**
   - Remove shortcut from iPhone
   - Wait for re-sync from Mac
   - Or manually import again

### Location Not Working

1. **Enable Location Services**
   - Settings > Privacy & Security > Location Services > ON
   - Settings > Privacy & Security > Location Services > **Shortcuts** > While Using

2. **Test GPS Signal**
   - Open Maps app
   - Verify your location appears
   - May need to step outside for better signal

### Messages Not Sending

1. **Check Contact Format**
   - Ensure phone numbers include country code (+1 for US)
   - Verify email addresses are correct
   - Test contacts exist in Contacts app

2. **Network Connection**
   - SMS requires cellular connection
   - Email requires WiFi or cellular data
   - Check signal strength

### Audio Not Playing

1. **Check Audio Files**
   - Verify files synced with shortcut
   - Check iPhone storage has space
   - Try playing files in Files app first

2. **Volume Settings**
   - Check volume slider
   - Disable silent mode
   - Check Do Not Disturb settings

## iOS Limitations

Be aware of these iOS-specific limitations:

1. **Notification Required**: Some triggers may show notification before running
2. **Lock Screen**: Not all shortcuts run fully with screen locked
3. **Low Power Mode**: May delay some actions
4. **Background Execution**: Video recording may require foreground
5. **Cellular Data**: Large audio files may need WiFi to sync initially

## Safety Considerations

When configuring triggers for emergency use:

1. **Choose discreet triggers**: Back Tap is least obvious
2. **Test in realistic conditions**: Try with one hand, while moving, etc.
3. **Have backup triggers**: Configure 2+ activation methods
4. **Practice activation**: Muscle memory helps in stressful situations
5. **Inform trusted contacts**: They should recognize your emergency messages

## Next Steps

After deploying to iOS:

1. **Practice regularly** - Ensure triggers work reliably
2. **Update emergency contacts** - Keep contact list current
3. **Test periodically** - Verify location accuracy, message delivery
4. **Stay updated** - iOS updates may affect trigger behavior
5. **Review messages** - Consider updating message templates for clarity

## Contributing

Have suggestions for iOS deployment documentation? See `/CONTRIBUTING.md` for how to contribute.

---

**Remember**: Test your emergency shortcut regularly to ensure it works when you need it. This toolkit may be used in critical situations - reliability is paramount.
