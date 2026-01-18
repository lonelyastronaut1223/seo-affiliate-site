#!/usr/bin/env python3
"""
Resize oversized guide images for optimal mobile loading performance.
Reduces massive 30-40MP images to max 1200px width while maintaining quality.
"""

import os
import subprocess
from pathlib import Path

# Configuration
GUIDES_DIR = Path("assets/images/guides")
MAX_WIDTH = 1200
QUALITY_JPG = 85
QUALITY_WEBP = 85

# Specific images to resize (known problematic ones)
TARGET_IMAGES = [
    "vlog.jpg",
    "vlog.webp",
    "fullframe-video.jpg",
    "fullframe-video.webp",
    "hybrid.jpg",
    "hybrid.webp",
    "budget.jpg",
    "budget.webp",
]


def get_image_dimensions(image_path):
    """Get image width and height using sips."""
    try:
        result = subprocess.run(
            ["sips", "-g", "pixelWidth", "-g", "pixelHeight", str(image_path)],
            capture_output=True,
            text=True,
            check=True,
        )
        lines = result.stdout.strip().split("\n")
        width = int([l for l in lines if "pixelWidth" in l][0].split(":")[1].strip())
        height = int([l for l in lines if "pixelHeight" in l][0].split(":")[1].strip())
        return width, height
    except Exception as e:
        print(f"Error getting dimensions for {image_path}: {e}")
        return None, None


def resize_image(image_path, max_width=MAX_WIDTH):
    """Resize image to max width while maintaining aspect ratio."""
    width, height = get_image_dimensions(image_path)

    if not width or not height:
        print(f"Skipping {image_path}: Could not get dimensions")
        return False

    if width <= max_width:
        print(f"Skipping {image_path}: Already optimized ({width}x{height})")
        return False

    # Calculate new height maintaining aspect ratio
    new_width = max_width
    new_height = int(height * (max_width / width))

    print(f"\n{'=' * 60}")
    print(f"Resizing: {image_path.name}")
    print(f"  Original: {width}x{height} ({width * height / 1_000_000:.1f}MP)")
    print(f"  New:      {new_width}x{new_height} ({new_width * new_height / 1_000_000:.1f}MP)")

    # Create backup
    backup_path = image_path.with_suffix(image_path.suffix + ".backup")
    if not backup_path.exists():
        print(f"  Creating backup: {backup_path.name}")
        subprocess.run(["cp", str(image_path), str(backup_path)], check=True)

    # Resize based on format
    if image_path.suffix.lower() in [".jpg", ".jpeg"]:
        # Resize JPG
        cmd = [
            "sips",
            "-z",
            str(new_height),
            str(new_width),
            "-s",
            "formatOptions",
            str(QUALITY_JPG),
            str(image_path),
        ]
    elif image_path.suffix.lower() == ".webp":
        # For WebP, convert to PNG first, resize, then back to WebP
        temp_png = image_path.with_suffix(".temp.png")
        temp_resized = image_path.with_suffix(".temp_resized.png")

        # Step 1: Convert WebP to PNG
        subprocess.run(
            ["sips", "-s", "format", "png", str(image_path), "--out", str(temp_png)],
            check=True,
        )

        # Step 2: Resize PNG
        subprocess.run(
            [
                "sips",
                "-z",
                str(new_height),
                str(new_width),
                str(temp_png),
                "--out",
                str(temp_resized),
            ],
            check=True,
        )

        # Step 3: Convert back to WebP using cwebp if available
        try:
            subprocess.run(
                [
                    "cwebp",
                    "-q",
                    str(QUALITY_WEBP),
                    str(temp_resized),
                    "-o",
                    str(image_path),
                ],
                check=True,
            )
            print(f"  ✓ Converted to WebP using cwebp")
        except FileNotFoundError:
            # Fallback: just use the PNG conversion (sips doesn't support WebP output well)
            subprocess.run(
                [
                    "sips",
                    "-s",
                    "format",
                    "png",
                    str(temp_resized),
                    "--out",
                    str(image_path),
                ],
                check=True,
            )
            print(f"  ⚠ cwebp not found, keeping as WebP (may not be optimal)")

        # Cleanup temp files
        temp_png.unlink(missing_ok=True)
        temp_resized.unlink(missing_ok=True)

        return True
    else:
        print(f"  Skipping: Unsupported format {image_path.suffix}")
        return False

    # Execute resize command for JPG
    try:
        subprocess.run(cmd, check=True, capture_output=True)
        print(f"  ✓ Resized successfully")

        # Verify new dimensions
        new_w, new_h = get_image_dimensions(image_path)
        if new_w and new_h:
            print(f"  Verified: {new_w}x{new_h}")

        return True
    except subprocess.CalledProcessError as e:
        print(f"  ✗ Error: {e}")
        return False


def main():
    """Main function to resize all target images."""
    print("=" * 60)
    print("Guide Images Resize Optimizer")
    print("=" * 60)
    print(f"Target directory: {GUIDES_DIR}")
    print(f"Max width: {MAX_WIDTH}px")
    print(f"Quality (JPG): {QUALITY_JPG}")
    print(f"Quality (WebP): {QUALITY_WEBP}")

    resized_count = 0
    skipped_count = 0

    for image_name in TARGET_IMAGES:
        image_path = GUIDES_DIR / image_name

        if not image_path.exists():
            print(f"\n⚠ Not found: {image_name}")
            continue

        if resize_image(image_path):
            resized_count += 1
        else:
            skipped_count += 1

    print(f"\n{'=' * 60}")
    print("Summary:")
    print(f"  Resized: {resized_count}")
    print(f"  Skipped: {skipped_count}")
    print("=" * 60)

    if resized_count > 0:
        print("\n✓ Optimization complete!")
        print("  Backups saved with .backup extension")
        print("  Test the images on mobile to verify loading performance")
    else:
        print("\n→ No images needed resizing")


if __name__ == "__main__":
    main()
