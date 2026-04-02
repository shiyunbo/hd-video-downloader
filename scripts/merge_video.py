#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Merge video and audio files using moviepy library with built-in ffmpeg
Supports multiple audio formats: .m4a, .webm, .aac, .ogg, .opus
"""

import os
import sys
from pathlib import Path

# Fix Unicode encoding for Windows console
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

def merge_video_audio(video_file, audio_file, output_file):
    """
    Merge video and audio files into a single MP4 file
    Fully automated - no user confirmation required

    Args:
        video_file: Path to video file
        audio_file: Path to audio file
        output_file: Path to output merged file
    """
    try:
        from moviepy import VideoFileClip, AudioFileClip
        import os

        # Delete output file if it exists (overwrite without confirmation)
        if os.path.exists(output_file):
            os.remove(output_file)

        print(f"Loading video: {video_file}")
        video = VideoFileClip(video_file)

        print(f"Loading audio: {audio_file}")
        audio = AudioFileClip(audio_file)

        print("Merging video and audio...")
        final_clip = video.with_audio(audio)

        print(f"Writing output file: {output_file}")
        # Use logger=None to suppress interactive progress bars
        final_clip.write_videofile(
            output_file,
            codec='libx264',
            audio_codec='aac',
            bitrate='8000k',
            logger=None  # Suppress progress output for automation
        )

        file_size = os.path.getsize(output_file) / (1024*1024)
        print(f"SUCCESS! Output: {output_file}")
        print(f"File size: {file_size:.2f} MB")

        # Cleanup original files automatically
        try:
            os.remove(video_file)
            os.remove(audio_file)
            print(f"Cleaned up original files")
        except:
            pass  # Ignore cleanup errors

        # Cleanup
        video.close()
        audio.close()
        final_clip.close()

        return True

    except ImportError as e:
        print(f"ERROR: moviepy not installed - {e}")
        print("Please run: pip install moviepy")
        return False
    except Exception as e:
        print(f"ERROR: Merge failed - {e}")
        import traceback
        traceback.print_exc()
        return False

def find_video_audio_pairs(directory="."):
    """
    Find video and audio file pairs in directory
    Supports multiple audio formats: .m4a, .webm, .aac, .ogg, .opus
    """
    dir_path = Path(directory)

    # Find all video files (yt-dlp format)
    video_files = list(dir_path.glob("*.f*.mp4")) + list(dir_path.glob("*.f*.webm"))

    # Find all audio files (support multiple formats)
    audio_extensions = ["m4a", "webm", "aac", "ogg", "opus"]
    audio_files = []
    for ext in audio_extensions:
        audio_files.extend(dir_path.glob(f"*.f*.{ext}"))

    pairs = []

    for video in video_files:
        # Extract base name (remove format suffix, e.g., .f123.mp4 -> base name)
        base_name = video.name.split('.f')[0]

        # Find matching audio file
        for audio in audio_files:
            audio_base = audio.name.split('.f')[0]
            if audio_base == base_name:
                # Found matching audio file
                output_file = f"{base_name}.mp4"
                pairs.append((video, audio, output_file))
                break

    return pairs

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage 1: python merge_video.py <video_file> <audio_file> <output_file>")
        print("Usage 2: python merge_video.py --auto  # Auto-merge all video/audio pairs in directory")
        sys.exit(1)

    if sys.argv[1] == "--auto":
        # Auto-merge mode
        print("Searching for video and audio files...")
        pairs = find_video_audio_pairs(".")

        if not pairs:
            print("ERROR: No video/audio pairs found")
            sys.exit(1)

        print(f"Found {len(pairs)} video/audio pair(s)")

        success_count = 0
        for video, audio, output in pairs:
            print(f"\nProcessing: {video.stem} + {audio.stem} -> {output}")
            if merge_video_audio(str(video), str(audio), output):
                success_count += 1

        print(f"\nSuccessfully merged {success_count}/{len(pairs)} files")

    else:
        # Manual specification mode
        video_file = sys.argv[1]
        audio_file = sys.argv[2]
        output_file = sys.argv[3] if len(sys.argv) > 3 else "output.mp4"

        merge_video_audio(video_file, audio_file, output_file)
