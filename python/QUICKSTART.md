# Quick Start Guide - Python TTS

Get up and running with Text-to-Speech audio generation in 5 minutes!

## Step 1: Install Dependencies

```bash
# Navigate to the python directory
cd python

# Create a virtual environment (recommended)
python3 -m venv .venv

# Activate the virtual environment
# On macOS/Linux:
source .venv/bin/activate
# On Windows:
# .venv\Scripts\activate

# Install required packages
pip install -r requirements.txt
```

## Step 2: Generate Audio Files

### English Audio (Google TTS - Recommended)

```bash
python tts/text_to_speech.py scripts/legal_rights_en.txt output/ --engine gtts
```

### Spanish Audio

```bash
python tts/text_to_speech.py scripts/legal_rights_es.txt output/ --engine gtts --lang es
```

### Offline Mode (No Internet Required)

```bash
python tts/text_to_speech.py scripts/legal_rights_en.txt output/ --engine pyttsx3
```

## Step 3: Find Your Audio Files

Generated MP3 files will be in the `output/` directory:

```bash
ls -lh output/
```

You should see:
- `legal_rights_en_segment_01.mp3`
- `legal_rights_en_segment_02.mp3`
- ... and more

## Step 4: Use the Audio Files

### For iOS Shortcuts

1. Upload the audio files to iCloud Drive
2. In the Shortcuts app, use the "Get File" action to retrieve the audio
3. Use the "Play Sound" action to play the audio

### For Android Tasker

1. Copy the MP3 files to your Android device (e.g., `/sdcard/GoodTrouble/audio/`)
2. In Tasker, use the "Music Play" action
3. Specify the file path and playback options

### For Testing Locally

Just open the MP3 files with your default music player!

## Common Options

### Generate Individual Segments Only

```bash
python tts/text_to_speech.py scripts/legal_rights_en.txt output/ --engine gtts --no-combine
```

### Adjust Speech Rate (pyttsx3 only)

```bash
# Slower speech
python tts/text_to_speech.py scripts/legal_rights_en.txt output/ --engine pyttsx3 --rate 130

# Faster speech
python tts/text_to_speech.py scripts/legal_rights_en.txt output/ --engine pyttsx3 --rate 180
```

## Troubleshooting

### "ModuleNotFoundError"

Make sure you've installed the dependencies and activated the virtual environment:

```bash
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### "gTTS token fetch failed"

Check your internet connection. Google TTS requires internet access.

Try the offline engine instead:

```bash
python tts/text_to_speech.py scripts/legal_rights_en.txt output/ --engine pyttsx3
```

### Need Help?

See the full [README.md](README.md) for detailed documentation, or open an issue on GitHub.

---

**That's it!** You now have legal rights audio files ready to use in your safety automations. 🎉
