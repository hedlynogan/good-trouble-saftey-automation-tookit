#!/usr/bin/env python3
"""
Text-to-Speech Converter for Safety Automation Toolkit

Supports multiple TTS engines:
- pyttsx3 (offline, cross-platform)
- gTTS (online, Google TTS, higher quality)

Usage:
    python text_to_speech.py input.txt output.mp3 --engine gtts
    python text_to_speech.py input.txt output.mp3 --engine pyttsx3
"""

import argparse
import os
import sys
from pathlib import Path
from typing import List, Optional


def check_dependencies():
    """Check if required dependencies are installed."""
    missing = []

    try:
        import pyttsx3
    except ImportError:
        missing.append("pyttsx3")

    try:
        from gtts import gTTS
    except ImportError:
        missing.append("gTTS")

    if missing:
        print(f"⚠️  Missing dependencies: {', '.join(missing)}")
        print(f"Install with: pip install {' '.join(missing)}")
        return False

    return True


def read_script(script_file: str) -> List[str]:
    """
    Read script file and return list of text segments.

    Skips:
    - Empty lines
    - Lines starting with #
    - Lines with only whitespace

    Args:
        script_file: Path to text file

    Returns:
        List of text segments to convert
    """
    segments = []

    with open(script_file, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            # Skip empty lines and comments
            if line and not line.startswith('#'):
                segments.append(line)

    return segments


def generate_tts_pyttsx3(text: str, output_file: str, rate: int = 150, volume: float = 1.0):
    """
    Generate TTS using pyttsx3 (offline engine).

    Args:
        text: Text to convert to speech
        output_file: Output audio file path
        rate: Speech rate (words per minute), default 150
        volume: Volume level (0.0 to 1.0), default 1.0
    """
    import pyttsx3

    engine = pyttsx3.init()

    # Configure engine
    engine.setProperty('rate', rate)
    engine.setProperty('volume', volume)

    # Get available voices
    voices = engine.getProperty('voices')

    # Try to set a better voice if available
    # Prefer female voices for clarity
    for voice in voices:
        if 'female' in voice.name.lower() or 'zira' in voice.name.lower():
            engine.setProperty('voice', voice.id)
            break

    # Save to file
    engine.save_to_file(text, output_file)
    engine.runAndWait()


def generate_tts_gtts(text: str, output_file: str, lang: str = 'en', slow: bool = False):
    """
    Generate TTS using gTTS (Google TTS, online).

    Args:
        text: Text to convert to speech
        output_file: Output audio file path
        lang: Language code (en, es, fr, etc.)
        slow: Use slow speech mode
    """
    from gtts import gTTS

    tts = gTTS(text=text, lang=lang, slow=slow)
    tts.save(output_file)


def combine_audio_segments(segments: List[str], output_file: str, pause_duration: int = 1000):
    """
    Combine multiple audio segments with pauses.

    Args:
        segments: List of audio file paths
        output_file: Output combined audio file
        pause_duration: Pause between segments in milliseconds
    """
    try:
        from pydub import AudioSegment
        from pydub.playback import play

        combined = AudioSegment.empty()
        pause = AudioSegment.silent(duration=pause_duration)

        for i, segment_file in enumerate(segments):
            print(f"  Adding segment {i+1}/{len(segments)}: {Path(segment_file).name}")
            audio = AudioSegment.from_file(segment_file)
            combined += audio

            # Add pause between segments (but not after the last one)
            if i < len(segments) - 1:
                combined += pause

        # Export combined audio
        combined.export(output_file, format='mp3')
        print(f"✅ Combined audio saved to: {output_file}")

    except ImportError:
        print("⚠️  pydub not installed. Cannot combine audio segments.")
        print("Install with: pip install pydub")
        print("Note: Also requires ffmpeg to be installed on your system")


def convert_script_to_speech(
    script_file: str,
    output_dir: str,
    engine: str = 'gtts',
    lang: str = 'en',
    combine: bool = True,
    rate: int = 150
):
    """
    Convert a script file to speech audio files.

    Args:
        script_file: Path to script text file
        output_dir: Directory to save audio files
        engine: TTS engine ('gtts' or 'pyttsx3')
        lang: Language code for gTTS
        combine: Whether to combine segments into one file
        rate: Speech rate for pyttsx3
    """
    # Ensure output directory exists
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    # Read script
    print(f"📖 Reading script: {script_file}")
    segments = read_script(script_file)

    if not segments:
        print("❌ No text segments found in script file")
        return

    print(f"✅ Found {len(segments)} text segments")

    # Generate audio for each segment
    segment_files = []
    base_name = Path(script_file).stem

    for i, text in enumerate(segments, 1):
        segment_file = output_path / f"{base_name}_segment_{i:02d}.mp3"
        print(f"🔊 Generating segment {i}/{len(segments)}: {text[:50]}...")

        try:
            if engine == 'gtts':
                generate_tts_gtts(text, str(segment_file), lang=lang)
            elif engine == 'pyttsx3':
                # pyttsx3 saves as WAV, convert filename
                segment_file = segment_file.with_suffix('.wav')
                generate_tts_pyttsx3(text, str(segment_file), rate=rate)
            else:
                print(f"❌ Unknown engine: {engine}")
                return

            segment_files.append(str(segment_file))
            print(f"   ✓ Saved to: {segment_file}")

        except Exception as e:
            print(f"❌ Error generating segment {i}: {e}")
            continue

    # Combine segments if requested
    if combine and len(segment_files) > 1:
        combined_file = output_path / f"{base_name}_complete.mp3"
        print(f"\n🎵 Combining {len(segment_files)} segments...")
        combine_audio_segments(segment_files, str(combined_file))

    print(f"\n✅ All done! Audio files saved to: {output_dir}")


def main():
    """Main entry point for CLI."""
    parser = argparse.ArgumentParser(
        description='Convert text scripts to speech audio files',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Generate English audio using Google TTS
  python text_to_speech.py scripts/legal_rights_en.txt output/ --engine gtts

  # Generate Spanish audio using Google TTS
  python text_to_speech.py scripts/legal_rights_es.txt output/ --engine gtts --lang es

  # Generate audio using offline TTS (no internet required)
  python text_to_speech.py scripts/legal_rights_en.txt output/ --engine pyttsx3

  # Generate without combining segments
  python text_to_speech.py scripts/legal_rights_en.txt output/ --no-combine

  # Adjust speech rate for pyttsx3
  python text_to_speech.py scripts/legal_rights_en.txt output/ --engine pyttsx3 --rate 130
        """
    )

    parser.add_argument(
        'script',
        help='Path to script text file'
    )

    parser.add_argument(
        'output',
        help='Output directory for audio files'
    )

    parser.add_argument(
        '--engine',
        choices=['gtts', 'pyttsx3'],
        default='gtts',
        help='TTS engine to use (default: gtts)'
    )

    parser.add_argument(
        '--lang',
        default='en',
        help='Language code for gTTS (en, es, fr, etc.). Default: en'
    )

    parser.add_argument(
        '--no-combine',
        action='store_true',
        help='Do not combine segments into a single file'
    )

    parser.add_argument(
        '--rate',
        type=int,
        default=150,
        help='Speech rate for pyttsx3 (words per minute). Default: 150'
    )

    args = parser.parse_args()

    # Check dependencies
    if not check_dependencies():
        sys.exit(1)

    # Validate input file
    if not os.path.exists(args.script):
        print(f"❌ Script file not found: {args.script}")
        sys.exit(1)

    # Convert script to speech
    try:
        convert_script_to_speech(
            script_file=args.script,
            output_dir=args.output,
            engine=args.engine,
            lang=args.lang,
            combine=not args.no_combine,
            rate=args.rate
        )
    except KeyboardInterrupt:
        print("\n\n⚠️  Interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
