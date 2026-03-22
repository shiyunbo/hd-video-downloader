---
name: hd-video-downloader
description: Download HD videos from 1000+ platforms using yt-dlp (YouTube, TikTok,Bilibili, Vimeo, Twitter/X, Instagram, etc.) and you-get (80+ sites including Douyin, Weibo, Youku, iQIYI, Tencent Video, etc.). Automatically downloads in high quality and merges separated video/audio streams. **Always use this skill whenever the user provides a video link, URL from any video platform, or asks to download/save/rip/extract videos from websites** — even if they don't explicitly mention the tool name. This includes phrases like "download this video" or "get this video", or when sharing any video URL.
---

# HD Video Downloader Skill

This skill helps you download **high-definition videos** from 1000+ popular video platforms using a **two-tier approach**:
1. **Primary**: `yt-dlp` - Most actively maintained, supports 1000+ websites, highest quality downloads
2. **Fallback**: `you-get` - Backup option with 80+ site support when yt-dlp doesn't support a platform

## How it Works

**yt-dlp** (Primary - Try First):
- Most actively maintained (110K+ GitHub stars)
- Supports 1000+ websites
- Automatically handles merged video/audio
- Best for YouTube, Bilibili, Douyin, and most platforms

**you-get** (Fallback):
- Classic tool with 80+ site support
- Useful for sites not yet supported by yt-dlp
- Automatic video/audio merging with ffmpeg

Both tools automatically detect the highest quality, download video/audio streams, and merge them into a single file.

## Prerequisites

**⚠️ CRITICAL: moviepy is MANDATORY**

This skill requires THREE dependencies:
1. **yt-dlp** - Primary download tool
2. **you-get** - Fallback download tool
3. **moviepy** - **REQUIRED for merging video and audio (includes built-in ffmpeg)**

### Why moviepy is REQUIRED

Modern video platforms often separate video and audio streams. Without moviepy:
- ❌ You will get separate files (video-only and audio-only)
- ❌ Cannot play the complete video
- ❌ Download is incomplete and unusable

**With moviepy:**
- ✅ Automatic merging of video and audio
- ✅ Single, complete, playable video file
- ✅ Proper A/V synchronization
- ✅ **Built-in ffmpeg** (no separate installation needed)
- ✅ Pure Python (easy to install)

### Installation

**🎯 Automatic Installation (Recommended)**

```bash
# Navigate to skill directory
cd <path-to-skill-directory>

# Run automatic installer
python scripts/setup.py
```

**📝 Manual Installation**

```bash
pip install yt-dlp you-get moviepy
```

**✅ Verify Installation**

```bash
python -c "from moviepy import VideoFileClip; print('✓ moviepy installed')"
python -c "import yt_dlp; print('✓ yt-dlp installed')"
python -c "import you_get; print('✓ you-get installed')"
```

**⚠️ DO NOT proceed with downloads if moviepy is not installed.**

## Download Workflow

### Complete Workflow

1. **Verify dependencies** - Run `python scripts/setup.py` if not done
2. **Parse URL** - Extract video URL from user message
3. **Try yt-dlp** - Use optimized 1080p default (best speed/quality balance)
4. **Fallback to you-get** - If yt-dlp fails or reports "Unsupported URL"
5. **Auto-merge** - Run `python scripts/merge_video.py --auto` if files are separated
6. **Verify output** - Check file exists and is playable

### Download Commands

**yt-dlp (Primary - Always try first)**

```bash
# Get video info (optional)
python -m yt_dlp --print "%(title)s\n%(duration)s\n%(uploader)s" "URL"

# DEFAULT: Download 1080p (best speed/quality balance)
python -m yt_dlp -f "bestvideo[height<=?1080]+bestaudio/best" --merge-output-format mp4 -o "%(title)s.%(ext)s" "URL"

# Alternative: Download 720p (faster, smaller)
python -m yt_dlp -f "bestvideo[height<=?720]+bestaudio/best" --merge-output-format mp4 -o "%(title)s.%(ext)s" "URL"

# Optional: Download highest quality including 4K (slower)
python -m yt_dlp -f "bestvideo+bestaudio/best" --merge-output-format mp4 -o "%(title)s.%(ext)s" "URL"

# With cookies (for restricted content)
python -m yt_dlp --cookies-from-browser chrome -f "bestvideo[height<=?1080]+bestaudio/best" --merge-output-format mp4 -o "%(title)s.%(ext)s" "URL"
```

**you-get (Fallback - Use when yt-dlp fails)**

```bash
# Download with auto-merge
python -c "import sys; sys.argv = ['you-get', 'URL']; from you_get import main; main()"
```

### Auto-Merge Separated Files

**Many platforms download video and audio as separate files. If this happens:**

```bash
# Automatic merge (detects and merges all separated files)
python scripts/merge_video.py --auto

# Manual merge (for specific files)
python scripts/merge_video.py <video_file> <audio_file> <output_file>
```

**Supported formats:**
- Audio: `.m4a`, `.webm`, `.aac`, `.ogg`, `.opus`
- Video: `.mp4`, `.webm`

**Merge script features:**
- ✅ Automatic format detection
- ✅ **Converts ALL audio to AAC** (maximum player compatibility)
- ✅ High bitrate (8000k) for quality preservation
- ✅ Automatic cleanup of original files
- ✅ Uses moviepy's built-in ffmpeg (no system ffmpeg required)

## Supported Platforms

### yt-dlp (Primary)
**Chinese**: Bilibili, Douyin, Kuaishou, Weibo, Zhihu, Youku, iQIYI, Tencent Video
**International**: YouTube, Vimeo, Twitter/X, Instagram, Facebook, TikTok, Dailymotion, TED, Reddit, Twitch

### you-get (Fallback)
**Best for**: Haokan Video, Baidu platforms, some niche Chinese sites

**Note**: Platform support changes frequently. Always try yt-dlp first.

## Examples

**Template (works for all platforms)**

```bash
# Step 1: Verify dependencies (run once)
python scripts/setup.py

# Step 2: Download with yt-dlp (1080p default)
python -m yt_dlp -f "bestvideo[height<=?1080]+bestaudio/best" --merge-output-format mp4 -o "%(title)s.%(ext)s" "URL"

# Step 3: If yt-dlp fails, try you-get
python -c "import sys; sys.argv = ['you-get', 'URL']; from you_get import main; main()"

# Step 4: Auto-merge if files are separated
python scripts/merge_video.py --auto
```

**Example URLs** (replace "URL" in template above):
- Bilibili: `https://www.bilibili.com/video/BV1xx411c7mD`
- YouTube: `https://youtube.com/watch?v=abc123`
- Douyin: `https://v.douyin.com/xyz123`
- TikTok: `https://www.tiktok.com/@user/video/1234567890`

**Playlist Download**

```bash
# Download entire playlist
python -m yt_dlp -f "bestvideo[height<=?1080]+bestaudio/best" --merge-output-format mp4 -o "%(playlist_index)s-%(title)s.%(ext)s" "PLAYLIST_URL"
```

## Error Handling

### Common yt-dlp Errors

**1. "Unsupported URL"**
- Action: Fall back to you-get
- Reason: Platform not yet supported by yt-dlp

**2. "WARNING: ffmpeg is not installed"**
- SEVERITY: NOT CRITICAL
- Action: Proceed with download, then merge with moviepy
- Solution: `python scripts/merge_video.py --auto`

**3. "HTTP Error 403: Forbidden"**
- Try with cookies: `--cookies-from-browser chrome`
- Check if video is public or requires authentication

**4. Separated video/audio files**
- Run: `python scripts/merge_video.py --auto`
- Result: Single merged .mp4 file

### Common you-get Errors

**1. "you-get not found"**
- Install: `pip install you-get`

**2. Merging issues**
- Run: `python scripts/merge_video.py --auto`

**3. Extraction errors**
- May need cookies for authentication
- Video might be private or deleted

### Graceful Fallback Workflow

```
1. Try yt-dlp
   │
   ├─→ Success → Report success
   │
   └─→ Failure → Check error type
       │
       ├─→ "Unsupported URL" → Try you-get
       │                        │
       │                        ├─→ Success → Report success (note: used you-get)
       │                        └─→ Failure → Report both tools failed
       │
       ├─→ Network/Auth error → Inform user of specific issue
       │
       └─→ Other error → Try you-get as last resort
```

## Advanced Usage

### Download Specific Quality

```bash
# List available formats
python -m yt_dlp --list-formats "URL"

# Download specific format
python -m yt_dlp -f "FORMAT_ID" "URL"

# Download 1080p or better
python -m yt_dlp -f "bestvideo[height<=1080]+bestaudio" "URL"
```

### Proxy and Network Options

```bash
# Use proxy
python -m yt_dlp --proxy http://127.0.0.1:7890 "URL"

# Set timeout
python -m yt_dlp --socket-timeout 60 "URL"
```

## Best Practices

**Quality Preservation**
1. **⚠️ ALWAYS verify moviepy is installed before downloading**
   - Check: `python -c "from moviepy import VideoFileClip"`
   - Install if missing: `pip install moviepy`

2. **⚠️ Use optimized 1080p default for best speed/quality balance**
   - Default: `-f "bestvideo[height<=?1080]+bestaudio/best"`
   - Avoids slow 4K downloads unless explicitly requested

3. **⚠️ ALWAYS auto-merge if files are separated**
   - Run: `python scripts/merge_video.py --auto`
   - Ensures single, playable output file

**General Workflow**
4. Always try yt-dlp first, fall back to you-get on failure
5. Download to current working directory
6. Verify downloads are complete (file exists, merged, reasonable size)
7. Report which tool was used to user
8. Update tools regularly: `pip install --upgrade yt-dlp you-get moviepy`

## Limitations

**Both tools:**
- **DRM-protected content**: Cannot download DRM-protected videos
- **Private videos**: Require authentication/cookies
- **Live streams**: Limited support
- **Platform changes**: Sites update APIs frequently
- **Regional restrictions**: Geo-blocked content

## Safety and Legal

**Important:**
- Only download videos you have the right to access
- Respect copyright and platform terms of service
- This tool is for personal use and fair use scenarios
- Do not redistribute copyrighted content without permission
- Some downloads may violate platform ToS
- Be aware of your local copyright laws

Always inform users about these considerations when downloading.

## Summary

This skill provides a robust video downloading experience with **guaranteed merged video output**:

1. **⚠️ CRITICAL: moviepy is REQUIRED**
   - MUST be installed before any download
   - Required for merging video and audio streams
   - Includes built-in ffmpeg (no separate installation)
   - Without moviepy: incomplete downloads (separate files)

2. **Primary: yt-dlp** (try first)
   - Most actively maintained (110K+ stars)
   - Supports 1000+ websites
   - Optimized for 1080p (best speed/quality balance)

3. **Fallback: you-get** (use when yt-dlp fails)
   - Classic tool with 80+ sites
   - Good backup option

4. **Automatic merge** (if files are separated)
   - Check for `.f*.mp4` and `.f*.m4a` files
   - Use moviepy to merge automatically
   - Clean up original files
   - Output single `.mp4` file

5. **Key features**
   - Requires moviepy (easy pip install)
   - Built-in ffmpeg (no system setup needed)
   - Auto-merges separated files
   - Optimized for 1080p (3-5x faster than 4K)
   - Supports 1000+ platforms
   - Graceful error handling

6. **Output guarantee**
   - ✅ Single merged video file (.mp4)
   - ✅ Video and audio combined
   - ✅ Ready to play
   - ✅ **AAC audio** (maximum compatibility)
   - ❌ NO separate video/audio files (auto-merged)

**Remember:**
- **ALWAYS verify moviepy is installed before downloading**
- **ALWAYS use 1080p default** (unless user requests 4K)
- **ALWAYS auto-merge if files are separated**
- Start with yt-dlp, fall back to you-get if needed
