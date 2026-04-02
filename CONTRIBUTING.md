# Contributing to HD Video Downloader

Thank you for your interest in contributing to HD Video Downloader! This document provides guidelines and instructions for contributing.

## 🤝 How to Contribute

### Reporting Bugs

Before creating bug reports, please check existing issues to avoid duplicates. When creating a bug report, include:

- **Clear title and description** of the problem
- **Steps to reproduce** the issue
- **Expected behavior** vs actual behavior
- **Environment information**:
  - Python version
  - OS (Windows/Linux/Mac)
  - Versions of yt-dlp, you-get, moviepy
- **Error messages** or logs
- **Sample URLs** (if applicable and not private)

### Suggesting Enhancements

Enhancement suggestions are welcome! Please provide:

- **Clear description** of the suggested feature
- **Use cases** for the feature
- **Potential implementation** approach (if known)
- **Alternatives considered**

### Pull Requests

1. **Fork the repository** and create your branch
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes**:
   - Write clean, commented code
   - Follow existing code style
   - Update documentation as needed
   - Test your changes thoroughly

3. **Commit your changes**:
   ```bash
   git commit -m "Add: your feature description"
   ```

4. **Push and create PR**:
   ```bash
   git push origin feature/your-feature-name
   ```

## 📝 Code Style

### Python Code

- Follow PEP 8 guidelines
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Keep functions focused and modular
- Maximum line length: 100 characters

### Example

```python
def download_video(url: str, output_dir: str = ".") -> bool:
    """
    Download video from given URL

    Args:
        url: Video URL to download
        output_dir: Directory to save downloaded video

    Returns:
        True if successful, False otherwise
    """
    try:
        # Implementation here
        pass
    except Exception as e:
        logger.error(f"Download failed: {e}")
        return False
```

## 🧪 Testing

### Before Submitting

1. **Test your changes**:
   - Download videos from different platforms
   - Test with various video qualities
   - Verify merge functionality
   - Check error handling

2. **Run manual tests**:
   ```bash
   # Test YouTube download
   python -m yt_dlp -f "bestvideo+bestaudio/best" "YOUTUBE_URL"

   # Test merge functionality
   python scripts/merge_video.py --auto
   ```

3. **Verify dependencies**:
   ```bash
   python -c "import yt_dlp; print('yt-dlp OK')"
   python -c "import you_get; print('you-get OK')"
   python -c "from moviepy import VideoFileClip; print('moviepy OK')"
   ```

## 📚 Documentation

### When to Update Docs

Update documentation when you:
- Add new features
- Change existing behavior
- Fix bugs affecting users
- Update dependencies
- Change installation process

### Documentation Files

- **README.md**: Main user-facing documentation
- **SKILL.md**: Claude Code skill configuration
- **CONTRIBUTING.md**: This file
- **LICENSE**: MIT License

## 🎯 Development Areas

### High Priority

- [ ] Add support for more platforms
- [ ] Improve error messages and user feedback
- [ ] Add batch download functionality
- [ ] Optimize merge performance
- [ ] Add download progress indicators

### Medium Priority

- [ ] Create GUI wrapper
- [ ] Add download queue management
- [ ] Support for subtitles downloading
- [ ] Add quality presets
- [ ] Implement download resume

### Low Priority

- [ ] Create browser extension
- [ ] Add download scheduling
- [ ] Support for live streams
- [ ] Video format conversion
- [ ] Metadata editing

## 🐛 Bug Fix Process

1. Reproduce the bug
2. Identify root cause
3. Write test case (if applicable)
4. Implement fix
5. Test thoroughly
6. Update documentation
7. Submit PR with description

## 💡 Feature Request Process

1. Check existing issues and PRs
2. Discuss approach in issue (if major feature)
3. Implement feature
4. Add tests
5. Update documentation
6. Submit PR

## 📧 Communication

- Use GitHub Issues for bugs and feature requests
- Use GitHub Discussions for questions and ideas
- Be respectful and constructive
- Follow the [Code of Conduct](#code-of-conduct)

## ⚖️ Code of Conduct

### Our Pledge

We are committed to providing a welcoming and inclusive environment for all contributors.

### Our Standards

- Use welcoming and inclusive language
- Be respectful of differing viewpoints
- Gracefully accept constructive criticism
- Focus on what is best for the community
- Show empathy towards other community members

### Unacceptable Behavior

- Harassment or discriminatory language
- Personal attacks or insulting comments
- Public or private harassment
- Publishing others' private information
- Unprofessional conduct

## 📜 License

By contributing, you agree that your contributions will be licensed under the MIT License.

## 🙏 Thank You

Every contribution, no matter how small, is valuable and appreciated!

---

**Questions?** Feel free to open an issue or discussion!
