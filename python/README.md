# Python Text-to-Speech (TTS) Tools

This directory contains Python tools for generating audio files from text scripts, specifically designed for creating legal rights reminder audio prompts.

## 🎯 Purpose

Generate high-quality audio files that can be:
- Played through iOS Shortcuts
- Used in Android Tasker automations
- Distributed as downloadable audio files
- Customized for different languages

## 📁 Directory Structure

```
python/
├── tts/
│   └── text_to_speech.py    # Main TTS conversion script
├── scripts/
│   ├── legal_rights_en.txt  # English legal rights script
│   └── legal_rights_es.txt  # Spanish legal rights script
├── output/                   # Generated audio files (git-ignored)
└── requirements.txt          # Python dependencies
```

## 🚀 Quick Start

### 1. Install Dependencies

```bash
# Navigate to python directory
cd python

# Install required packages
pip install -r requirements.txt
```

**Note**: For `pydub` to work properly, you also need `ffmpeg` installed on your system:

**macOS**:
```bash
brew install ffmpeg
```

**Ubuntu/Debian**:
```bash
sudo apt-get install ffmpeg
```

**Windows**:
Download from [ffmpeg.org](https://ffmpeg.org/download.html)

### 2. Generate Audio Files

**English (Google TTS - Recommended)**:
```bash
python tts/text_to_speech.py scripts/legal_rights_en.txt output/ --engine gtts
```

**Spanish**:
```bash
python tts/text_to_speech.py scripts/legal_rights_es.txt output/ --engine gtts --lang es
```

**Offline Mode (No Internet Required)**:
```bash
python tts/text_to_speech.py scripts/legal_rights_en.txt output/ --engine pyttsx3
```

### 3. Find Your Audio Files

Generated files will be in the `output/` directory:
- `legal_rights_en_segment_01.mp3`, `legal_rights_en_segment_02.mp3`, etc. (individual segments)
- `legal_rights_en_complete.mp3` (all segments combined)

## 🎙️ TTS Engines

### Google TTS (gTTS) - Recommended

**Pros**:
- ✅ High-quality, natural-sounding voices
- ✅ Supports 50+ languages
- ✅ Free to use
- ✅ Simple to implement

**Cons**:
- ❌ Requires internet connection
- ❌ Rate-limited by Google
- ❌ Cannot customize voice characteristics

**Supported Languages**: en, es, fr, de, it, pt, zh-CN, ar, hi, ja, ko, and many more

### pyttsx3 (Offline TTS)

**Pros**:
- ✅ Works offline (no internet required)
- ✅ Cross-platform (Windows, macOS, Linux)
- ✅ Adjustable speech rate and volume
- ✅ Multiple voices available

**Cons**:
- ❌ Lower quality than Google TTS
- ❌ Limited language support
- ❌ Voice quality depends on OS

**Best for**: Testing, offline use, privacy-conscious users

## 📝 Creating Custom Scripts

### Script Format

Create a `.txt` file in the `scripts/` directory:

```
# Comments start with # and are ignored

# This is the first audio segment
This will be converted to speech.

# Empty lines separate segments
This will be a separate audio file.

# You can have multiple segments
Each non-empty, non-comment line becomes an audio segment.
```

### Example: Create a Custom Script

```bash
# Create a new script file
cat > scripts/my_custom_script.txt << 'EOF'
# Custom Safety Reminder

Hello, this is your safety reminder.

Remember to stay aware of your surroundings.

Keep your phone charged and accessible.

Share your location with trusted contacts.
EOF

# Generate audio
python tts/text_to_speech.py scripts/my_custom_script.txt output/ --engine gtts
```

## 🔧 Advanced Usage

### Adjust Speech Rate (pyttsx3 only)

```bash
# Slower speech (130 words per minute)
python tts/text_to_speech.py scripts/legal_rights_en.txt output/ --engine pyttsx3 --rate 130

# Faster speech (180 words per minute)
python tts/text_to_speech.py scripts/legal_rights_en.txt output/ --engine pyttsx3 --rate 180
```

### Generate Individual Segments Only

```bash
# Don't combine segments into a single file
python tts/text_to_speech.py scripts/legal_rights_en.txt output/ --no-combine
```

### Multiple Languages

```bash
# French
python tts/text_to_speech.py scripts/legal_rights_fr.txt output/ --engine gtts --lang fr

# Mandarin Chinese
python tts/text_to_speech.py scripts/legal_rights_zh.txt output/ --engine gtts --lang zh-CN

# Arabic
python tts/text_to_speech.py scripts/legal_rights_ar.txt output/ --engine gtts --lang ar
```

## 🌍 Language Support

### gTTS Language Codes

| Language | Code | Example |
|----------|------|---------|
| English | `en` | `--lang en` |
| Spanish | `es` | `--lang es` |
| French | `fr` | `--lang fr` |
| German | `de` | `--lang de` |
| Italian | `it` | `--lang it` |
| Portuguese | `pt` | `--lang pt` |
| Mandarin | `zh-CN` | `--lang zh-CN` |
| Arabic | `ar` | `--lang ar` |
| Hindi | `hi` | `--lang hi` |
| Japanese | `ja` | `--lang ja` |
| Korean | `ko` | `--lang ko` |
| Russian | `ru` | `--lang ru` |
| Vietnamese | `vi` | `--lang vi` |
| Tagalog | `tl` | `--lang tl` |

See full list: [gTTS Language Support](https://gtts.readthedocs.io/en/latest/module.html#languages-gtts-lang)

## 📱 Using Generated Audio in Automations

### iOS Shortcuts

1. Upload generated MP3 files to iCloud Drive
2. In Shortcuts app, use "Get File" action to retrieve audio
3. Use "Play Sound" action to play the audio

**Example Shortcut Flow**:
```
Get File from iCloud Drive: legal_rights_en_complete.mp3
Play Sound: [File from previous action]
Set Volume: 80%
```

### Android Tasker

1. Copy generated MP3 files to device storage (e.g., `/sdcard/GoodTrouble/audio/`)
2. In Tasker, use "Music Play" action
3. Specify file path and playback options

**Example Tasker Task**:
```
A1: Music Play
    File: /sdcard/GoodTrouble/audio/legal_rights_en_complete.mp3
    Start: 0
    Loop: Yes
```

## 🔒 Privacy & Security

**Data Privacy**:
- **pyttsx3**: All processing happens locally on your device
- **gTTS**: Text is sent to Google's servers for conversion
  - No personal data is included in the text scripts
  - Audio generation is done via Google's public API
  - No user account or authentication required

**Recommendation**: Use pyttsx3 for maximum privacy, or gTTS for better quality if privacy is less of a concern for non-sensitive text.

## 🐛 Troubleshooting

### "ModuleNotFoundError: No module named 'pyttsx3'"

Install dependencies:
```bash
pip install -r requirements.txt
```

### "pydub.exceptions.CouldntDecodeError"

Install ffmpeg:
```bash
# macOS
brew install ffmpeg

# Ubuntu/Debian
sudo apt-get install ffmpeg
```

### pyttsx3 "No module named 'win32com'" (Windows)

Install pywin32:
```bash
pip install pywin32
```

### pyttsx3 "NSInvalidArgumentException" (macOS)

This is a known issue with pyttsx3 on newer macOS versions. Use gTTS instead:
```bash
python tts/text_to_speech.py scripts/legal_rights_en.txt output/ --engine gtts
```

### gTTS "gTTS token fetch failed"

Check your internet connection. gTTS requires internet access to Google's servers.

### Audio quality is poor (pyttsx3)

Try adjusting the speech rate:
```bash
python tts/text_to_speech.py scripts/legal_rights_en.txt output/ --engine pyttsx3 --rate 140
```

Or switch to gTTS for higher quality:
```bash
python tts/text_to_speech.py scripts/legal_rights_en.txt output/ --engine gtts
```

## 🤝 Contributing

### Adding New Language Scripts

1. Create a new script file: `scripts/legal_rights_[lang_code].txt`
2. Translate the legal rights statements
3. Test audio generation:
   ```bash
   python tts/text_to_speech.py scripts/legal_rights_[lang_code].txt output/ --engine gtts --lang [lang_code]
   ```
4. Submit a pull request with the new script

See [CONTRIBUTING.md](../CONTRIBUTING.md) for detailed guidelines.

### Script Translation Guidelines

- Use clear, simple language
- Maintain the same structure as English script
- Include comments for context
- Test with native speakers if possible
- Verify pronunciation is clear and accurate

## 📋 To-Do / Future Enhancements

- [ ] Add more language scripts (French, Mandarin, Arabic, etc.)
- [ ] Create pre-generated audio files for common languages
- [ ] Add voice selection options for pyttsx3
- [ ] Implement batch processing for multiple scripts
- [ ] Add audio post-processing (normalize volume, add silence)
- [ ] Create GUI version for non-technical users
- [ ] Add support for SSML (Speech Synthesis Markup Language)
- [ ] Create audio file metadata (title, artist, album art)

## 📜 License

This tool is part of the Safety Automation Toolkit and is licensed under the MIT License. See [../LICENSE](../LICENSE) for details.

## 🙏 Acknowledgments

- **gTTS**: Google Text-to-Speech library
- **pyttsx3**: Cross-platform offline TTS library
- **pydub**: Audio manipulation library

---

**Questions or issues?** Open an issue on [GitHub](../../issues) or see our [Discussions](../../discussions).
