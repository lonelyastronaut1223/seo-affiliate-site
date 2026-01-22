#!/bin/bash

# Mobile Image Optimization Script
# Purpose: Generate responsive image variants for better mobile performance
# Target: Reduce LCP from 15.2s to < 2.5s

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${GREEN}🖼️  Mobile Image Optimization Script${NC}"
echo "================================================"

# Check dependencies
if ! command -v cwebp &> /dev/null; then
    echo -e "${RED}❌ cwebp not found. Installing...${NC}"
    brew install webp
fi

if ! command -v convert &> /dev/null; then
    echo -e "${RED}❌ ImageMagick not found. Installing...${NC}"
    brew install imagemagick
fi

# Configuration
SOURCE_DIR="${1:-public/assets/images}"
TEMP_DIR="./temp_optimized"
SIZES=(600 900 1280)  # Mobile, Tablet, Desktop

echo -e "${YELLOW}📁 Source directory: $SOURCE_DIR${NC}"
echo -e "${YELLOW}🎯 Target sizes: ${SIZES[@]}px${NC}"
echo ""

# Create temp directory
mkdir -p "$TEMP_DIR"

# Counter
processed=0
skipped=0

# Find all images (jpg, jpeg, png)
find "$SOURCE_DIR" -type f \( -iname "*.jpg" -o -iname "*.jpeg" -o -iname "*.png" \) | while read -r img; do
    # Get filename and directory
    filename=$(basename "$img")
    dirname=$(dirname "$img")
    basename="${filename%.*}"
    ext="${filename##*.}"
    
    # Skip if already optimized (contains size suffix)
    if [[ $basename =~ -[0-9]{3,4}$ ]]; then
        echo -e "${YELLOW}⏭️  Skipping (already sized): $filename${NC}"
        ((skipped++)) || true
        continue
    fi
    
    echo -e "${GREEN}🔄 Processing: $filename${NC}"
    
    # Get original dimensions
    original_width=$(identify -format "%w" "$img")
    original_height=$(identify -format "%h" "$img")
    echo "   Original: ${original_width}x${original_height}px"
    
    # Generate responsive variants
    for size in "${SIZES[@]}"; do
        # Only generate if original is larger
        if [ "$original_width" -gt "$size" ]; then
            output_base="${dirname}/${basename}-${size}"
            
            # Generate WebP
            echo "   📦 Creating ${size}px WebP..."
            convert "$img" -resize ${size}x -quality 85 -strip "${output_base}.webp"
            
            # Generate JPEG fallback
            echo "   📦 Creating ${size}px JPEG..."
            convert "$img" -resize ${size}x -quality 85 -strip "${output_base}.jpg"
            
            # Get file sizes
            webp_size=$(du -h "${output_base}.webp" | cut -f1)
            jpg_size=$(du -h "${output_base}.jpg" | cut -f1)
            echo "   ✅ ${size}px: WebP=$webp_size, JPEG=$jpg_size"
        else
            echo "   ⚠️  Skipping ${size}px (original too small)"
        fi
    done
    
    # Optimize original as well
    echo "   🔧 Optimizing original..."
    cwebp -q 85 "$img" -o "${dirname}/${basename}.webp" 2>/dev/null || \
        convert "$img" -quality 85 "${dirname}/${basename}.webp"
    
    ((processed++)) || true
    echo ""
done

echo "================================================"
echo -e "${GREEN}✅ Optimization complete!${NC}"
echo "   Processed: $processed images"
echo "   Skipped: $skipped images"
echo ""
echo -e "${YELLOW}Next steps:${NC}"
echo "1. Update HTML to use <picture> elements"
echo "2. Test with PageSpeed Insights"
echo "3. Monitor LCP improvement"
