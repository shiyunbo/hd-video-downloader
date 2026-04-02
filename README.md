# HD Video Downloader

[中文说明](#中文说明) | English Documentation Below

🎬 **Download high-definition videos from 1000+ platforms - optimized for speed and quality**

A powerful video downloader skill compatible with **Claude Code and other AI tools**. Supports YouTube, Bilibili, TikTok, and 1000+ more platforms. **Optimized to download 1080p by default** for the best balance of quality and download speed. Automatically merges separated video/audio streams.

/ 适配 **Claude Code 和其他 AI 工具** 的强大视频下载技能。支持 YouTube、Bilibili、抖音等 1000+ 平台。默认优化下载 1080p，自动合并分离的视频音频流。

---

## ✨ Features / 功能特性

- 🤖 **Multi-AI Compatibility**: Compatible with Claude Code, Cursor, and other AI assistants
  - **多 AI 兼容**: 适配 Claude Code、Cursor 和其他 AI 助手
- 🚀 **Multi-Platform Support**: Downloads from 1000+ websites via yt-dlp and 80+ sites via you-get
  - **多平台支持**: 支持 1000+ 网站 (yt-dlp) 和 80+ 网站 (you-get)
- 🎯 **Optimized Quality**: Downloads 1080p by default (best balance of quality and speed)
  - **优化画质**: 默认下载 1080p (画质与速度的最佳平衡)
- ⚡ **Fast Downloads**: Avoids slow 4K downloads unless explicitly requested
  - **快速下载**: 避免缓慢的 4K 下载，除非明确要求
- 🎵 **Audio Compatibility**: **Automatically converts ALL audio to AAC** for universal player support
  - **音频兼容**: **自动将所有音频转换为 AAC** 格式，支持所有播放器
- 🔄 **Auto-Merge**: Automatically merges separated video and audio streams into single MP4 files
  - **自动合并**: 自动将分离的视频和音频流合并为单个 MP4 文件
- 🌍 **Global Platforms**: Supports both international and Chinese video platforms
  - **全球平台**: 支持国际和中文视频平台
- 🔄 **Smart Fallback**: Tries yt-dlp first, falls back to you-get if needed
  - **智能回退**: 优先使用 yt-dlp，失败时自动切换到 you-get
- 📦 **Easy Setup**: One-command automatic dependency installation
  - **简易安装**: 一键自动安装依赖
- 🎨 **Format Support**: Handles multiple audio formats (.m4a, .webm, .aac, .ogg, .opus)
  - **格式支持**: 支持多种音频格式 (.m4a, .webm, .aac, .ogg, .opus)
- 📁 **Default Save Location**: Videos are saved in the current working directory
  - **保存位置**: 视频默认保存在当前工作目录

## 🌐 Supported Platforms / 支持的平台

### International Platforms / 国际平台 (via yt-dlp)
- YouTube, Vimeo, Dailymotion, Twitch
- Twitter/X, Instagram, Facebook, TikTok
- TED, Reddit, VK, and 1000+ more

### Chinese & Asian Platforms / 中文及亚洲平台 (via you-get)
- Bilibili (哔哩哔哩), Douyin (抖音), Kuaishou (快手)
- Weibo (微博), Youku (优酷), Tudou (土豆), iQIYI (爱奇艺)
- Tencent Video (腾讯视频), Miaopai, and 70+ more

## 📋 Prerequisites / 环境要求

- Python 3.6 or higher / Python 3.6 或更高版本
- pip (Python package manager)
- Claude Code (for using as a skill) / Claude Code（用于作为技能使用）

## 📦 Installation / 安装

### Option 1: Install as Claude Code Skill / 方式 1：作为 Claude Code 技能安装

**Recommended / 推荐** - This allows you to use the skill directly in Claude Code:
/ 推荐方式 - 可直接在 Claude Code 中使用此技能：

```bash
# Clone the repository to your skills directory / 克隆仓库到你的技能目录
git clone https://github.com/shiyunbo/hd-video-downloader.git ~/.claude/skills/hd-video-downloader

# On Windows, use: / Windows 系统使用：
git clone https://github.com/shiyunbo/hd-video-downloader.git %USERPROFILE%\.claude\skills\hd-video-downloader

# Or manually download from GitHub / 或从 GitHub 手动下载
# Visit: https://github.com/shiyunbo/hd-video-downloader
# Download and extract to: ~/.claude/skills/hd-video-downloader
```

**Verify installation / 验证安装:**
```bash
# The skill should appear in Claude Code's skill list
# 技能应出现在 Claude Code 的技能列表中
```

### Option 2: Manual Download / 方式 2：手动下载

1. Visit the GitHub repository: https://github.com/shiyunbo/hd-video-downloader
   / 访问 GitHub 仓库
2. Download the ZIP file or clone the repository
   / 下载 ZIP 文件或克隆仓库
3. Extract to your desired location
   / 解压到你想要的位置
4. Follow the "Quick Start" guide below
   / 按照下面的"快速开始"指南操作

## 🚀 Quick Start / 快速开始

### 1. Install Dependencies / 安装依赖

**⚡ Automatic Setup (Recommended) / 自动安装（推荐）:**

The setup script automatically checks and installs only missing dependencies:
/ 安装脚本会自动检查并仅安装缺失的依赖：

```bash
cd scripts
python setup.py
```

**What it does / 功能说明:**
- ✅ Checks installed packages (yt-dlp, you-get, moviepy) / 检查已安装的包
- ✅ Installs only missing packages / 仅安装缺失的包
- ✅ Verifies installation success / 验证安装成功
- ✅ Shows version information / 显示版本信息
- ✅ No redundant downloads / 无重复下载

**Example output / 示例输出:**
```
[1/3] Checking installed packages...
----------------------------------------------------------------------
  ✓ yt-dlp         2024.1.1    - Primary video downloader (1000+ sites)
  ✗ you-get        not installed  - Fallback video downloader (80+ sites)
  ✓ moviepy        1.0.3       - Video/audio merging tool

[2/3] Installing missing packages...
Packages to install: 1

  → Installing you-get...
    Fallback video downloader (80+ sites)
  ✓ Successfully installed you-get (0.4.1700)

[3/3] Installation Summary
----------------------------------------------------------------------
  you-get         ✓ SUCCESS

Installed: 1/1 packages

✓ All dependencies installed successfully!
/ ✓ 所有依赖安装成功！
```

**Manual Installation (if setup fails) / 手动安装（如果自动安装失败）:**
```bash
pip install yt-dlp you-get moviepy
```

### 2. Download Videos / 下载视频

**📁 Default Save Location / 默认保存位置:**
Downloaded videos are saved in the **current working directory** by default. You can specify a custom location by adding `-o "path/%(title)s.%(ext)s"` to the command.
/ 下载的视频默认保存在**当前工作目录**。可以通过添加 `-o "path/%(title)s.%(ext)s"` 到命令来指定自定义位置。

**Using with AI Assistants / 使用 AI 助手:**

This skill works seamlessly with **Claude Code and other AI assistants**. Simply provide a video URL in your conversation:
/ 此技能与 **Claude Code和其他 AI 助手** 无缝协作。只需在对话中提供视频链接：

**With Claude Code / 使用 Claude Code:**
```
Download this video: https://www.youtube.com/watch?v=xxxxx
/ 下载这个视频: https://www.youtube.com/watch?v=xxxxx
```

**With Cursor / 使用 Cursor:**
```
Please download: https://www.youtube.com/watch?v=xxxxx
/ 请下载：https://www.youtube.com/watch?v=xxxxx
```

**With other AI tools / 使用其他 AI 工具:**
Just share the video URL and ask to download it.
/ 只需分享视频链接并要求下载即可。

---

**Or use the tools directly / 或直接使用工具：**

```
Download this video: https://www.youtube.com/watch?v=xxxxx
/ 下载这个视频: https://www.youtube.com/watch?v=xxxxx
```

Or use the tools directly:
/ 或直接使用工具：

**Using yt-dlp (Primary) / 使用 yt-dlp（主要工具）:**
```bash
# DEFAULT: Download 1080p (optimized for speed) / 默认：下载 1080p（速度优化）
yt-dlp -f "bestvideo[height<=?1080]+bestaudio/best" --merge-output-format mp4 -o "%(title)s.%(ext)s" "URL"

# Alternative: Download 720p (faster, smaller file) / 备选：下载 720p（更快，文件更小）
yt-dlp -f "bestvideo[height<=?720]+bestaudio/best" --merge-output-format mp4 -o "%(title)s.%(ext)s" "URL"

# Optional: Download highest quality including 4K (slower) / 可选：下载最高画质包括 4K（较慢）
yt-dlp -f "bestvideo+bestaudio/best" --merge-output-format mp4 -o "%(title)s.%(ext)s" "URL"
```

**Using you-get (Fallback) / 使用 you-get（备用工具）:**
```bash
you-get "URL"
```

### 3. Merge Separated Files (if needed) / 合并分离的文件（如需要）

If video and audio are downloaded separately:
/ 如果视频和音频分别下载：

```bash
# Auto-merge all separated files in directory / 自动合并目录中所有分离的文件
python scripts/merge_video.py --auto

# Or merge specific files manually / 或手动合并指定文件
python scripts/merge_video.py video.mp4 audio.m4a output.mp4
```

## 📁 Project Structure / 项目结构

```
hd-video-downloader/
├── README.md                 # This file / 本文件
├── SKILL.md                  # Claude Code skill configuration / Claude Code 技能配置
├── .gitignore               # Git ignore rules
├── scripts/
│   ├── setup.py               # Automatic dependency checker & installer / 自动依赖检查和安装
│   └── merge_video.py         # Video/audio merger / 视频音频合并工具
└── evals/
    └── evals.json            # Skill evaluation tests / 技能评估测试
```

## 🛠️ How It Works / 工作原理

### Download Workflow / 下载工作流

1. **Try yt-dlp first** (primary tool) / **首先尝试 yt-dlp**（主要工具）
   - Downloads in highest quality: `bestvideo+bestaudio` / 下载最高画质
   - Supports 1000+ websites / 支持 1000+ 网站
   - Most actively maintained / 最活跃维护

2. **Fall back to you-get** (if yt-dlp fails) / **回退到 you-get**（如果 yt-dlp 失败）
   - Supports 80+ sites / 支持 80+ 网站
   - Useful for specific platforms / 适用于特定平台
   - Reliable backup option / 可靠的备用选项

3. **Auto-merge if needed** / **自动合并（如需要）**
   - Detects separated video/audio files / 检测分离的视频音频文件
   - Uses moviepy for merging / 使用 moviepy 合并
   - Supports multiple audio formats / 支持多种音频格式
   - High bitrate (8000k) to preserve quality / 高码率保持画质

### Quality Preservation / 画质保持

- ✅ Downloads separate video and audio streams (highest quality) / 下载分离的视频音频流（最高画质）
- ✅ Uses container-level merging (no re-encoding) / 容器级合并（无重编码）
- ✅ High bitrate output (8000k) / 高码率输出
- ✅ Preserves original video quality / 保持原始画质

## 📝 Usage Examples / 使用示例

### Example 1: YouTube Video
```
Download: https://www.youtube.com/watch?v=dQw4w9WgXcQ
```

### Example 2: Bilibili Video / B站视频
```
Download this Bilibili video: https://www.bilibili.com/video/BV1xx411c7mD
/ 下载这个B站视频: https://www.bilibili.com/video/BV1xx411c7mD
```

### Example 3: TikTok/Instagram / 抖音/Instagram
```
Save this video: https://www.tiktok.com/@user/video/1234567890
/ 保存这个视频: https://www.tiktok.com/@user/video/1234567890
```

### Example 4: Manual Merging / 手动合并
```bash
# If you have separated files like: / 如果你有分离的文件如：
# video.f302.mp4 (video only / 仅视频)
# video.f251.webm (audio only / 仅音频)

# Run auto-merge / 运行自动合并
python scripts/merge_video.py --auto

# Output: video.mp4 (merged) / 输出: video.mp4 (已合并)
```

## 🎯 Why This Skill? / 为什么使用此技能？

### Problem Solved / 解决的问题

Modern video platforms often deliver video and audio as separate streams. Standard downloaders either:
/ 现代视频平台通常将视频和音频作为分离的流传输。标准下载器要么：
- Download only low-quality pre-merged files / 仅下载低质量的预合并文件
- Leave you with unplayable separated files / 留下无法播放的分离文件
- Require complex ffmpeg setup / 需要复杂的 ffmpeg 设置
- Download slow 4K videos when 1080p is sufficient / 在 1080p 就足够时下载缓慢的 4K 视频

### Our Solution / 我们的解决方案

- ✅ Downloads 1080p by default (best quality/speed balance) / 默认下载 1080p（最佳画质速度平衡）
- ✅ Avoids slow 4K downloads unless requested / 避免缓慢的 4K 下载，除非要求
- ✅ **Converts ALL audio to AAC format** (universal compatibility) / **将所有音频转换为 AAC 格式**（通用兼容性）
- ✅ Automatically merges with moviepy (built-in ffmpeg) / 使用 moviepy 自动合并（内置 ffmpeg）
- ✅ No system-level dependencies required / 无需系统级依赖
- ✅ Pure Python - easy to install and use / 纯 Python - 易于安装和使用

## 🎵 Audio Compatibility / 音频兼容性

**Problem / 问题:** Modern platforms use various audio codecs that many players don't support:
/ 现代平台使用许多播放器不支持的各种音频编解码器：
- YouTube: Opus (often unsupported by Windows Media Player) / Opus（Windows Media Player 常不支持）
- Older platforms: Vorbis, Ogg, etc. / 较老平台：Vorbis, Ogg 等
- Result: Video plays but no sound! / 结果：视频播放但无声音！

**Our Solution / 我们的解决方案:** Automatic audio conversion to AAC / 自动音频转换为 AAC

| Audio Codec / 音频编解码器 | Compatibility / 兼容性 | Converted to AAC / 转换为 AAC |
| -------------- | ----------------- | -------------------- |
| **Opus**       | ❌ Limited support / 有限支持 | ✅ Yes / 是 |
| **Vorbis/Ogg** | ❌ Limited support / 有限支持 | ✅ Yes / 是 |
| **WebM audio** | ❌ Limited support / 有限支持 | ✅ Yes / 是 |
| **AAC**        | ✅ Universal / 通用 | ✅ Already compatible / 已兼容 |

**Benefits / 优势:**
- ✅ **Works on ALL media players** (Windows Media Player, VLC, QuickTime, etc.) / **适用于所有媒体播放器**
- ✅ **Works on ALL devices** (Windows, Mac, iOS, Android, smart TVs) / **适用于所有设备**
- ✅ **192kbps bitrate** (high quality audio) / **192kbps 码率**（高质量音频）
- ✅ **No manual conversion needed** - happens automatically during merge / **无需手动转换** - 合并时自动进行

## 🚀 Speed vs Quality / 速度与画质

### Why 1080p by Default? / 为什么默认 1080p？

We've optimized this tool to download 1080p by default instead of 4K for several reasons:
/ 我们优化此工具默认下载 1080p 而非 4K，原因如下：

| Resolution / 分辨率 | File Size / 文件大小 | Download Speed / 下载速度 | Quality / 画质 | Best For / 最适合 |
| ------------------- | ---------- | -------------- | --------- | ------------------------------ |
| **720p**            | ~500MB-1GB | ⚡⚡⚡ Fastest / 最快 | Good / 良好 | Mobile devices, quick preview / 移动设备，快速预览 |
| **1080p** (DEFAULT) | ~1GB-3GB   | ⚡⚡ Fast / 快 | Excellent / 优秀 | Most screens, sharing, storage / 大多数屏幕，分享，存储 |
| **4K**              | ~5GB-15GB  | ⚡ Slow / 慢 | Best / 最佳 | Large 4K TVs, archiving / 大屏 4K TV，存档 |

**Benefits of 1080p default / 1080p 默认的优势:**
- 🚀 **3-5x faster downloads** compared to 4K / **比 4K 快 3-5 倍**
- 💾 **Saves 80-90% storage space** / **节省 80-90% 存储空间**
- 👁️ **Virtually identical quality** on most screens (phones, tablets, laptops) / **在大多数屏幕上画质几乎相同**
- 🌐 **Less bandwidth usage** - better for shared networks / **更少带宽使用** - 适合共享网络
- ⏱️ **Faster processing** during merge / **合并时处理更快**

### When to Use Different Resolutions? / 何时使用不同分辨率？

**Use 720p when / 使用 720p 当:**
- Quick preview needed / 需要快速预览
- Limited storage space / 存储空间有限
- Slow internet connection / 网络连接较慢
- Mobile device playback / 移动设备播放

**Use 1080p (DEFAULT) when / 使用 1080p（默认）当:**
- Regular viewing on TV/monitor / 在电视/显示器上常规观看
- Sharing with others / 与他人分享
- General purpose archiving / 通用存档
- **Most use cases ✅ / **大多数使用场景 ✅

**Use 4K when / 使用 4K 当:**
- Large 4K TV display / 大屏 4K TV 显示
- Professional archiving / 专业存档
- Video editing/production / 视频编辑/制作
- You have time and storage space ⏳ / 你有时间和存储空间 ⏳

## 🔧 Configuration / 配置

### Video Quality Selection / 视频画质选择

**Default behavior (1080p - recommended) / 默认行为（1080p - 推荐）:**
```bash
-f "bestvideo[height<=?1080]+bestaudio/best"
```

**Faster downloads (720p) / 更快下载（720p）:**
```bash
-f "bestvideo[height<=?720]+bestaudio/best"
```

**Highest quality including 4K (slower) / 最高画质包括 4K（较慢）:**
```bash
-f "bestvideo+bestaudio/best"
```

### Merge Settings / 合并设置

Default merge settings (in `merge_video.py`) / 默认合并设置（在 `merge_video.py` 中）:
```python
final_clip.write_videofile(
    output_file,
    codec='libx264',
    audio_codec='aac',
    bitrate='8000k'  # High bitrate to preserve quality / 高码率保持画质
)
```

## 🐛 Troubleshooting / 故障排除

### Issue: "moviepy not installed" / 问题："moviepy 未安装"
**Solution / 解决方案:**
```bash
# Run the automatic setup (checks and installs missing dependencies) / 运行自动安装（检查并安装缺失依赖）
python scripts/setup.py

# Or install manually / 或手动安装
pip install moviepy
```

### Issue: Separated video/audio files / 问题：分离的视频音频文件
**Solution / 解决方案:**
```bash
python scripts/merge_video.py --auto
```

### Issue: "Unsupported URL" / 问题："不支持的 URL"
**Solution / 解决方案:** The platform might not be supported. Check: / 平台可能不支持。检查：
- yt-dlp supported sites: https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md
- you-get supported sites: https://github.com/soimort/you-get/wiki/%E6%94%AF%E6%8C%81%E7%9A%84%E7%BD%91%E7%AB%99

### Issue: Download slow or fails / 问题：下载缓慢或失败
**Possible solutions / 可能的解决方案:**
- You're downloading 4K by accident - use 1080p instead: `-f "bestvideo[height<=?1080]+bestaudio/best"` / 你可能意外在下载 4K - 改用 1080p
- Try even faster 720p: `-f "bestvideo[height<=?720]+bestaudio/best"` / 尝试更快的 720p
- Check your internet connection / 检查网络连接
- Try with cookies: `--cookies-from-browser chrome` / 尝试使用 cookies
- Video might be geo-restricted or private / 视频可能受地域限制或为私密
- Update tools: `pip install --upgrade yt-dlp you-get` / 更新工具

### Issue: Video plays but no sound / "unsupported audio codec" / 问题：视频播放但无声音 / "不支持的音频编解码器"
**Cause / 原因:** Audio uses Opus or other codecs not supported by your player / 音频使用播放器不支持的 Opus 或其他编解码器

**Solution 1: Re-encode with AAC audio (recommended) / 解决方案 1：用 AAC 音频重新编码（推荐）**
```python
from moviepy import VideoFileClip

# Load the video / 加载视频
video = VideoFileClip('your_video.mp4')

# Re-encode with AAC audio / 用 AAC 音频重新编码
video.write_videofile(
    'your_video_aac.mp4',
    codec='libx264',
    audio_codec='aac',  # Universal compatibility / 通用兼容性
    bitrate='2000k',
    audio_bitrate='192k'
)
```

**Solution 2: Use a better player / 解决方案 2：使用更好的播放器**
- VLC Media Player (supports all codecs) / VLC 媒体播放器（支持所有编解码器）
- PotPlayer (Windows)
- MPV (cross-platform / 跨平台)

**Prevention / 预防:** The merge script automatically converts to AAC, so this shouldn't happen with new downloads / 合并脚本会自动转换为 AAC，所以新下载不应出现此问题

## 📚 Dependencies / 依赖

| Package / 包 | Version / 版本 | Purpose / 用途 |
| ----------- | ------- | ---------------------------------------- |
| **yt-dlp**  | Latest / 最新 | Primary video downloader (1000+ sites) / 主要视频下载器（1000+ 网站） |
| **you-get** | Latest / 最新 | Fallback downloader (80+ sites) / 备用下载器（80+ 网站） |
| **moviepy** | Latest / 最新 | Video/audio merging with built-in ffmpeg / 视频音频合并（内置 ffmpeg） |

## 🤝 Contributing / 贡献

Contributions are welcome! Feel free to: / 欢迎贡献！请随时：
- Report bugs / 报告错误
- Suggest new features / 建议新功能
- Submit pull requests / 提交拉取请求
- Improve documentation / 改进文档

## 📄 License / 许可证

This project is provided as-is for personal and educational use. / 本项目按原样提供，供个人和教育使用。

Please respect the terms of service of the video platforms you download from. / 请遵守您从中下载视频的视频平台的服务条款。

## ⚠️ Disclaimer / 免责声明

This tool is for personal use only. Please: / 此工具仅供个人使用。请：
- Respect copyright and intellectual property laws / 尊重版权和知识产权法
- Follow the terms of service of video platforms / 遵守视频平台的服务条款
- Do not use for commercial purposes without permission / 未经许可不得用于商业目的
- Be mindful of content creators' rights / 注意内容创作者的权利

## 🔗 Links / 链接

### Project Repository / 项目仓库
- **GitHub Repository**: https://github.com/shiyunbo/hd-video-downloader
  - Report issues / 报告问题: https://github.com/shiyunbo/hd-video-downloader/issues
  - Submit pull requests / 提交拉取请求: https://github.com/shiyunbo/hd-video-downloader/pulls

### Dependencies / 依赖工具
- [yt-dlp GitHub](https://github.com/yt-dlp/yt-dlp) - Primary video downloader / 主要视频下载器
- [you-get GitHub](https://github.com/soimort/you-get) - Fallback video downloader / 备用视频下载器
- [moviepy Documentation](https://zulko.github.io/moviepy/) - Video/audio merging library / 视频音频合并库
- [Claude Code](https://claude.ai/code) - AI-powered development environment / AI 驱动的开发环境

## 📞 Support / 支持

For issues or questions: / 如有问题或疑问：
1. Check the Troubleshooting section above / 查看上述故障排除部分
2. Visit the respective project repositories / 访问相应的项目仓库
3. Open an issue on GitHub / 在 GitHub 上开启问题

---

**Made with ❤️ for the video downloading community**
**为视频下载社区用心制作 ❤️**

*Last updated: March 2026 / 最后更新：2026年3月*

---

<a name="中文说明"></a>
## 中文说明

### 简介 / Introduction

这是一个强大的视频下载技能，**兼容 Claude Code、Cursor 和其他 AI 助手**。支持从 YouTube、Bilibili、抖音等 1000+ 平台下载高清视频。默认优化为下载 1080p，自动合并分离的视频和音频流。

**GitHub 仓库**: https://github.com/shiyunbo/hd-video-downloader

### 核心功能 / Core Features

- **🤖 多 AI 兼容**: 适配 Claude Code、Cursor 和其他 AI 工具
- **🚀 多平台支持**: 支持 1000+ 网站
- **🎯 画质优化**: 默认下载 1080p，平衡画质与速度
- **🎵 音频兼容**: 自动将所有音频转换为 AAC 格式
- **🔄 自动合并**: 自动合并分离的视频音频文件
- **📦 简易安装**: 一键安装所有依赖
- **📁 保存位置**: 视频默认保存在当前工作目录

### 快速开始 / Quick Start

```bash
# 1. 安装依赖 / Install dependencies
cd scripts
python setup.py

# 2. 下载视频 / Download video
# 在任意 AI 助手中提供视频链接即可
# Just provide a video URL in any AI assistant
# 注意：视频默认保存在当前工作目录
# Note: Videos are saved in the current working directory by default

# 示例 / Examples:
# - Claude Code: "Download this video: https://..."
# - Cursor: "Please download: https://..."


# 3. 合并文件（如需要）/ Merge files (if needed)
python scripts/merge_video.py --auto
```

### 支持的平台 / Supported Platforms

**国际平台 / International**: YouTube, Vimeo, TikTok, Instagram, Twitter, Facebook, Twitch, TED, Reddit 等

**中文平台 / Chinese**: B站 (Bilibili)、抖音 (Douyin)、快手 (Kuaishou)、微博 (Weibo)、优酷 (Youku)、爱奇艺 (iQIYI)、腾讯视频 等

### 常见问题 / FAQ

**Q: 为什么默认下载 1080p 而不是 4K？**
A: 1080p 在大多数屏幕上画质几乎相同，但下载速度快 3-5 倍，节省 80-90% 存储空间。

**Q: 视频播放但没有声音怎么办？**
A: 运行 `python scripts/merge_video.py --auto` 重新合并为 AAC 音频格式。

**Q: 如何下载 4K 视频？**
A: 使用命令: `yt-dlp -f "bestvideo+bestaudio/best" --merge-output-format mp4 "URL"`
