#!/bin/bash
#
# Demo script for Python TTS functionality
# Generates sample audio files in English and Spanish
#

set -e  # Exit on error

echo "🎙️  Safety Automation Toolkit - TTS Demo"
echo "========================================"
echo ""

# Check if virtual environment exists
if [ ! -d ".venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv .venv
    echo "✅ Virtual environment created"
    echo ""
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source .venv/bin/activate

# Install dependencies if needed
echo "📥 Checking dependencies..."
pip install -q -r requirements.txt
echo "✅ Dependencies ready"
echo ""

# Generate English audio
echo "🔊 Generating English audio files..."
python tts/text_to_speech.py scripts/legal_rights_en.txt output/ --engine gtts --no-combine
echo ""

# Generate Spanish audio
echo "🔊 Generating Spanish audio files..."
python tts/text_to_speech.py scripts/legal_rights_es.txt output/ --engine gtts --lang es --no-combine
echo ""

# List generated files
echo "📂 Generated files:"
echo ""
ls -lh output/*.mp3 | awk '{print "  - " $9 " (" $5 ")"}'
echo ""

# Summary
total_files=$(ls -1 output/*.mp3 | wc -l | tr -d ' ')
total_size=$(du -sh output | awk '{print $1}')

echo "✅ Demo complete!"
echo ""
echo "Summary:"
echo "  Files generated: $total_files"
echo "  Total size: $total_size"
echo "  Location: output/"
echo ""
echo "🎧 You can now play these files with any audio player!"
echo ""
echo "Next steps:"
echo "  1. Test the audio files to ensure quality"
echo "  2. Upload to iCloud Drive or copy to Android device"
echo "  3. Integrate with iOS Shortcuts or Android Tasker"
echo ""
