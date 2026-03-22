#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
HD Video Downloader - Setup and Check Script
Checks and installs dependencies: yt-dlp, you-get, moviepy
"""

import subprocess
import sys
import os

# Fix Unicode encoding for Windows console
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')


def check_package(package_name, import_name=None):
    """
    Check if a package is already installed

    Args:
        package_name: Package name for pip install
        import_name: Module name to verify (defaults to package_name)

    Returns:
        bool: True if installed, False otherwise
    """
    if import_name is None:
        import_name = package_name.replace("-", "_")

    try:
        __import__(import_name)
        return True
    except ImportError:
        return False


def install_package(package_name, import_name=None):
    """
    Install a Python package using pip

    Args:
        package_name: Package name for pip install
        import_name: Module name to verify installation (defaults to package_name)

    Returns:
        bool: True if installation successful, False otherwise
    """
    if import_name is None:
        import_name = package_name.replace("-", "_")

    try:
        # Install the package
        subprocess.check_call([
            sys.executable, "-m", "pip", "install", package_name,
            "--upgrade", "--quiet"
        ])
        return True
    except subprocess.CalledProcessError:
        return False


def get_version(package_name, import_name=None):
    """
    Get the version of an installed package

    Args:
        package_name: Package name for pip install
        import_name: Module name to verify (defaults to package_name)

    Returns:
        str: Version string or None if not installed
    """
    if import_name is None:
        import_name = package_name.replace("-", "_")

    try:
        module = __import__(import_name)
        version = getattr(module, '__version__', 'unknown')
        return version
    except ImportError:
        return None


def check_and_install_dependencies():
    """
    Check and install all required dependencies
    """
    # Required dependencies
    dependencies = [
        {
            'name': 'yt-dlp',
            'import': 'yt_dlp',
            'description': 'Primary video downloader (1000+ sites)'
        },
        {
            'name': 'you-get',
            'import': 'you_get',
            'description': 'Fallback video downloader (80+ sites)'
        },
        {
            'name': 'moviepy',
            'import': 'moviepy',
            'description': 'Video/audio merging tool'
        },
    ]

    print("\n" + "="*70)
    print("HD Video Downloader - Dependency Check & Install")
    print("="*70)

    # Check what's installed
    print("\n[1/3] Checking installed packages...")
    print("-" * 70)

    to_install = []
    for dep in dependencies:
        installed = check_package(dep['name'], dep['import'])
        version = get_version(dep['name'], dep['import']) if installed else None

        if installed:
            print(f"  ✓ {dep['name']:<15} {version or 'installed':<10} - {dep['description']}")
        else:
            print(f"  ✗ {dep['name']:<15} not installed  - {dep['description']}")
            to_install.append(dep)

    # If all installed, we're done
    if not to_install:
        print("\n" + "="*70)
        print("✓ All dependencies are already installed!")
        print("="*70)
        print("\nYou can start downloading videos right away!")
        return True

    # Show what will be installed
    print("\n[2/3] Installing missing packages...")
    print("-" * 70)
    print(f"Packages to install: {len(to_install)}")

    results = {}
    for dep in to_install:
        print(f"\n  → Installing {dep['name']}...")
        print(f"    {dep['description']}")

        success = install_package(dep['name'], dep['import'])

        # Verify installation
        if success:
            if check_package(dep['name'], dep['import']):
                version = get_version(dep['name'], dep['import'])
                print(f"  ✓ Successfully installed {dep['name']} ({version})")
                results[dep['name']] = True
            else:
                print(f"  ✗ {dep['name']} installed but cannot be imported")
                results[dep['name']] = False
        else:
            print(f"  ✗ Failed to install {dep['name']}")
            results[dep['name']] = False

    # Summary
    print("\n[3/3] Installation Summary")
    print("-" * 70)

    success_count = sum(1 for v in results.values() if v)
    total_count = len(to_install)

    for package, success in results.items():
        status = "✓ SUCCESS" if success else "✗ FAILED"
        print(f"  {package:<15} {status}")

    print(f"\nInstalled: {success_count}/{total_count} packages")

    if success_count == total_count:
        print("\n" + "="*70)
        print("✓ All dependencies installed successfully!")
        print("="*70)
        print("\nYou can now use the HD Video Downloader skill.")
        print("\nQuick start:")
        print("  1. Provide a video URL (YouTube, Bilibili, etc.)")
        print("  2. The skill will automatically download in 1080p (optimized)")
        print("  3. Video and audio will be merged automatically")
        return True
    else:
        print("\n" + "="*70)
        print("✗ Some dependencies failed to install")
        print("="*70)
        print("\nPlease try installing manually:")
        print("  pip install yt-dlp you-get moviepy")
        print("\nOr check your internet connection and try again.")
        return False


def main():
    """Main function"""
    try:
        success = check_and_install_dependencies()
        return 0 if success else 1
    except KeyboardInterrupt:
        print("\n\nSetup cancelled by user.")
        return 1
    except Exception as e:
        print(f"\n✗ An error occurred: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
