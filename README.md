# Good Trouble Safety Main - Build Guide

This guide walks you through building the Good Trouble Safety Main shortcut step-by-step in the iOS Shortcuts app.

## Overview

**Name**: Good Trouble Safety Main
**Purpose**: Emergency alert system that sends GPS location to trusted contacts
**Complexity**: Intermediate
**Time to Build**: 15-20 minutes
**iOS Version**: 15.0+

---

## What This Shortcut Does

1. Gets your current GPS location
2. Formats an emergency alert message with location
3. Sends the message to 1-3 trusted contacts via Messages
4. Optionally launches video recording
5. Optionally plays legal rights audio

---

## Before You Start

**Prerequisites**:
- iPhone with iOS 15.0 or later
- Shortcuts app (pre-installed)
- Contacts app with emergency contacts saved
- Messages app

**Prepare**:
- Decide on 1-3 trusted emergency contacts
- Have their phone numbers ready
- Choose your emergency alert message text

---

## Step-by-Step Build Instructions

### Part 1: Create New Shortcut

1. Open **Shortcuts** app
2. Tap **+** (top right) to create new shortcut
3. Tap the shortcut name at top and rename to: **Good Trouble Safety Main**

---

### Part 2: Get Current Location

**Action 1: Get Current Location**

4. Tap **Add Action**
5. Search for: **Get Current Location**
6. Tap **Get Current Location** to add it
7. This action requires no configuration

> **What it does**: Retrieves your current GPS coordinates

---

### Part 3: Format Location for Sharing

**Action 2: Get URLs from Current Location**

8. Tap **+** below the first action
9. Search for: **Get URLs from Input**
10. Tap to add **Get URLs from Input**
11. Tap **Input** → Select **Current Location** (from previous action)

> **What it does**: Converts GPS coordinates to a shareable maps URL

---

###Part 4: Create Emergency Message

**Action 3: Text**

12. Tap **+** below previous action
13. Search for: **Text**
14. Tap **Text** to add a text block
15. In the text field, type your emergency message. Example:

```
🚨 EMERGENCY ALERT 🚨

I may need assistance. My current location is:
```

16. After your text, tap the **Variables** button
17. Select **URLs** (from the previous Get URLs action)
18. This inserts the location link into your message

**Result**: Your message will look like:
```
🚨 EMERGENCY ALERT 🚨
I may need assistance. My current location is:
https://maps.apple.com/?ll=XX.XXXX,YY.YYYY
```

> **Customization**: Adjust the message text as needed. Keep it clear and concise.

---

### Part 5: Ask for Contacts (First-Time Setup)

**Action 4: Ask for Input (Contact 1)**

19. Tap **+** to add another action
20. Search for: **Ask for Input**
21. Tap **Ask for Input**
22. Configure it:
    - **Question**: "Emergency Contact 1 - Phone Number"
    - **Input Type**: Tap **Text** → change to **Phone Number**
    - **Default Answer**: Leave blank

**Action 5: Set Variable (Contact 1)**

23. Tap **+** below the Ask for Input
24. Search for: **Set Variable**
25. Tap **Set Variable**
26. Configure:
    - **Variable Name**: Type **EmergencyContact1**
    - **Value**: Should already be **Provided Input** (from Ask action)

**Action 6: Get Variable (Contact 1) - for immediate use**

27. Tap **+**
28. Search for: **Get Variable**
29. Tap **Get Variable**
30. Tap **Variable** → select **EmergencyContact1**

> **Repeat for Contact 2** (optional but recommended):
>   - Add another "Ask for Input" → Question: "Emergency Contact 2 - Phone Number"
>   - Add "Set Variable" → Name it **EmergencyContact2**
>   - Add "Get Variable" → Select **EmergencyContact2**

> **Repeat for Contact 3** (optional):
>   - Same pattern for **EmergencyContact3**

> **Why this approach**: The shortcut will ask for contacts on first run and save them as variables. On subsequent runs, it will use the saved values.

---

### Part 6: Send Messages

**Action 7: Send Message**

31. Tap **+** to add action
32. Search for: **Send Message**
33. Tap **Send Message**
34. Configure:
    - **Message**: Tap in the field → Select **Text** (your emergency message from Action 3)
    - **Recipients**: Tap **Add** → Select **EmergencyContact1** variable
35. Tap **Show More** (if needed)
36. Enable **Show When Run** if you want confirmation prompt (recommended for safety)

> **Add more Send Message actions for Contact 2 and Contact 3** if you configured them:
>   - Duplicate the Send Message action
>   - Change Recipients to EmergencyContact2 and EmergencyContact3

---

### Part 7: Optional Video Recording

**Action 8: Run Shortcut (Video)**

37. Tap **+**
38. Search for: **Run Shortcut**
39. Tap **Run Shortcut**
40. Configure:
    - **Shortcut**: Will show "Choose" initially. You'll select **Good Trouble Video Recording** after you create that shortcut
    - For now, you can leave it unconfigured or delete this action if not using video

> **Alternative**: Instead of Run Shortcut, you can use **Open App**:
>   - Search for **Open App**
>   - Select **Camera**
>   - This immediately opens the Camera app

---

### Part 8: Optional Legal Rights Audio

**Action 9: Run Shortcut (Audio)**

41. Tap **+**
42. Search for: **Run Shortcut**
43. Tap **Run Shortcut**
44. Configure:
    - **Shortcut**: Choose **Good Trouble Legal Rights Audio** (after you create it)
    - Or leave unconfigured for now

---

### Part 9: Final Configuration

**Shortcut Settings**:

45. Tap the settings icon (sliders) at bottom right
46. Configure:
    - **Icon**: Choose a red or emergency-themed icon
    - **Color**: Red (for emergency)
    - **Show in Share Sheet**: OFF (this isn't a share action)
    - **Pin in Shortcuts**: ON (for quick access)
47. Tap **Done** to save

---

## Complete Action List Summary

Your shortcut should have these actions in order:

1. **Get Current Location**
2. **Get URLs from** → Current Location
3. **Text** → Your emergency message + URLs variable
4. **Ask for Input** → Emergency Contact 1 Phone Number (first run only)
5. **Set Variable** → EmergencyContact1
6. **Get Variable** → EmergencyContact1
7. **Send Message** → Text message to EmergencyContact1
8. *(Optional)* Repeat 4-7 for Contact 2 and 3
9. *(Optional)* **Run Shortcut** → Good Trouble Video Recording
10. *(Optional)* **Run Shortcut** → Good Trouble Legal Rights Audio

---

## Testing

### Test Mode (Airplane Mode)

1. Enable **Airplane Mode** on your iPhone
2. Run the shortcut
3. It will get location (from last known position)
4. It will ask for contacts (if first run)
5. It will TRY to send messages but fail (no network)
6. This lets you verify the flow without sending real messages

### Safe Test (Non-Emergency Contact)

1. Use your own phone number or a trusted friend as test contact
2. Run shortcut
3. Verify:
   - Location is accurate
   - Message is formatted correctly
   - Message is received

### Full Test

1. Inform your emergency contacts you're testing
2. Run the shortcut
3. Verify they receive the message
4. Check the maps link works correctly
5. Test video recording (if enabled)
6. Test audio playback (if enabled)

---

## Troubleshooting

**"Shortcuts does not have permission to access your location"**
- Go to Settings → Privacy → Location Services → Shortcuts
- Enable location access (While Using the App)

**Messages not sending**
- Check you have cellular or WiFi connection
- Verify contacts are in correct format
- Ensure Messages app is working normally

**Variables not saving**
- Variables persist across runs automatically
- If you want to reset, delete and recreate the shortcut

**Contact asks every time**
- Check that "Set Variable" actions are present
- Ensure variable names are exact (case-sensitive)

---

## Security Checklist

Before sharing this shortcut:

- [ ] Remove your personal contact phone numbers
- [ ] Replace with "Ask Each Time" prompts
- [ ] Test that no personal data is embedded
- [ ] Export and inspect for sensitive information
- [ ] Verify location permissions are clearly documented

---

## Customization Ideas

**Message Customization**:
- Add your name to the message
- Include medical information (allergies, conditions)
- Add multiple languages
- Include timestamp

**Additional Actions**:
- Turn on flashlight
- Take a photo
- Record audio note
- Share to additional apps (Signal, WhatsApp)

**Advanced**:
- Add conditional logic (if location unavailable, use last known)
- Add confirmation prompt before sending
- Add ability to cancel within 5 seconds

---

## Export for Sharing

Once your shortcut is complete and tested:

1. Long-press the shortcut in the app
2. Tap **Share**
3. Choose **Copy iCloud Link** to get a shareable URL
4. OR choose **Export File** to get the .shortcut file

**Remember**: Remove all personal data before sharing!

---

## Next Steps

Now that you've built the main shortcut, you can:

1. **Add Video Recording**: Create a simple shortcut that opens the Camera app or records video
2. **Add Legal Rights Audio**: Import the provided MP3 files and create a shortcut to play them
3. **Configure Triggers**: Set up automation triggers in iOS (Back Tap, Voice Command, etc.)
4. **Test Thoroughly**: Make sure all contacts receive messages and location links work

---

**Need Help?** Open an issue on GitHub or reach out to the community.
