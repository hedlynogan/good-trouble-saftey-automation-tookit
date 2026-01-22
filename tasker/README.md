# Tasker Setup for Good Trouble Safety Automation

This directory contains importable Tasker task files for Android users.

## Prerequisites

- Android 7.0 or later
- [Tasker app](https://play.google.com/store/apps/details?id=net.dinglisch.android.taskerm) (paid app)
- Required permissions granted (see below)

## Files Included

| File | Description |
|------|-------------|
| `GoodTrouble_Main.tsk.xml` | Main emergency workflow task |
| `GoodTrouble_Audio.tsk.xml` | Audio playback task (called by main task) |

## Quick Setup

### Step 1: Copy Audio Files

1. Download the audio files from the `audio/` directory
2. Create a folder on your Android device: `/sdcard/GoodTrouble/audio/`
3. Copy the audio files to this folder:
   - `legal_rights_en_complete.mp3` (English)
   - `legal_rights_es_complete.mp3` (Spanish)

### Step 2: Import Tasks into Tasker

1. Copy the `.tsk.xml` files to your Android device
2. Open Tasker
3. Long-press on the "Tasks" tab at the bottom
4. Select "Import Task"
5. Navigate to and select `GoodTrouble_Audio.tsk.xml`
6. Repeat to import `GoodTrouble_Main.tsk.xml`

### Step 3: Configure Emergency Contacts

1. In Tasker, tap on "Good Trouble Emergency" task
2. Find the "Send SMS" actions (Actions 6, 7, 8)
3. Replace `CONTACT1_PHONE`, `CONTACT2_PHONE`, `CONTACT3_PHONE` with actual phone numbers
4. Delete any unused contact actions if you have fewer than 3 contacts

### Step 4: Grant Permissions

Tasker needs these permissions to work properly:

1. **Location**: Settings > Apps > Tasker > Permissions > Location > "Allow all the time"
2. **SMS**: Settings > Apps > Tasker > Permissions > SMS > Allow
3. **Camera**: Settings > Apps > Tasker > Permissions > Camera > Allow
4. **Microphone**: Settings > Apps > Tasker > Permissions > Microphone > Allow
5. **Storage**: Settings > Apps > Tasker > Permissions > Files and media > Allow

### Step 5: Disable Battery Optimization

Many Android manufacturers aggressively kill background apps. To ensure Tasker runs reliably:

1. Settings > Apps > Tasker > Battery > "Don't optimize" or "Unrestricted"
2. For Samsung: Settings > Battery > App power management > Add Tasker to "Apps that won't be put to sleep"
3. For Xiaomi: Settings > Battery > App battery saver > Tasker > No restrictions

## Creating a Trigger

To run the task quickly in an emergency, set up a trigger:

### Option 1: Home Screen Widget
1. Long-press on your home screen
2. Add Widget > Tasker > Task Shortcut
3. Select "Good Trouble Emergency"

### Option 2: Quick Settings Tile
1. In Tasker, go to Preferences > Action > Quick Settings Tasks
2. Add "Good Trouble Emergency"
3. The tile will appear in your Quick Settings panel

### Option 3: Gesture (requires AutoInput plugin)
1. Install AutoInput from Play Store
2. Create a profile triggered by a gesture
3. Link it to "Good Trouble Emergency" task

## Customization

### Change Audio Language

In the "Good Trouble Audio" task, find Action 2 "Set Language" and change:
- `en` for English
- `es` for Spanish

### Modify the Emergency Message

In the "Good Trouble Emergency" task, find Action 5 "Create Emergency Message" and edit the message text.

### Change Audio File Location

If you store audio files in a different location, update the path in "Good Trouble Audio" task, Action 3.

## Testing

**Important:** Test the workflow before you need it!

1. In Tasker, tap the "Good Trouble Emergency" task
2. Press the Play button to run it
3. Verify:
   - SMS messages are sent to your contacts
   - Audio plays at full volume
   - Video recording starts

Consider sending test messages to yourself first, or warn your emergency contacts that you're testing.

## Troubleshooting

### Task doesn't run
- Check that Tasker is not being killed by battery optimization
- Ensure all permissions are granted
- Check Tasker notification shows "Tasker" is running

### Location not working
- Ensure GPS is enabled
- Grant "Allow all the time" location permission
- Wait a few seconds for GPS lock

### Audio doesn't play
- Check the audio file path is correct
- Verify the MP3 files are in the right location
- Check media volume is not muted

### SMS not sending
- Verify phone numbers are correct (include country code if needed)
- Check SMS permission is granted
- Ensure you have cellular signal

## Need Help?

Open an issue on the GitHub repository with:
- Your Android version
- Device manufacturer and model
- Description of the problem
- Any error messages from Tasker
