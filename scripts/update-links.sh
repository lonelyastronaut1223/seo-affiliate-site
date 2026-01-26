#!/bin/bash
# =============================================================================
# update-links.sh - Affiliate Link Update Script
# =============================================================================
# Usage: ./scripts/update-links.sh
# 
# This script:
# 1. Minifies links.js → links.min.js
# 2. Updates the version parameter in all HTML files (cache-busting)
# 3. Commits and pushes changes to GitHub
# =============================================================================

set -e  # Exit on error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Get script directory and project root
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"

cd "$PROJECT_ROOT"

echo -e "${YELLOW}📦 Affiliate Link Update Script${NC}"
echo "=================================="

# Step 1: Check if terser is available
echo -e "\n${YELLOW}[1/4] Checking dependencies...${NC}"
if ! command -v npx &> /dev/null; then
    echo -e "${RED}❌ npx not found. Please install Node.js${NC}"
    exit 1
fi

# Step 2: Sync and Minify links.js
echo -e "${YELLOW}[2/4] Syncing and Minifying links.js...${NC}"
node scripts/core/sync_links.js
npx -y terser public/assets/js/links.js -o public/assets/js/links.min.js -c -m
echo -e "${GREEN}✅ Synced and Created links.min.js${NC}"

# Step 3: Update version parameter in all HTML files
echo -e "${YELLOW}[3/4] Updating cache-busting version...${NC}"
NEW_VERSION=$(date +%Y%m%d%H%M)
OLD_PATTERN='links\.min\.js\?v=[0-9]*'
NEW_VALUE="links.min.js?v=${NEW_VERSION}"

# Count files to update
FILE_COUNT=$(find . -name "*.html" -type f | wc -l | tr -d ' ')

# Update all HTML files
find . -name "*.html" -type f -exec sed -i '' "s/${OLD_PATTERN}/${NEW_VALUE}/g" {} \;
echo -e "${GREEN}✅ Updated ${FILE_COUNT} HTML files with version ${NEW_VERSION}${NC}"

# Step 4: Show git status
echo -e "\n${YELLOW}[4/4] Git status:${NC}"
git status --short

# Ask for confirmation to commit
echo ""
read -p "Do you want to commit and push these changes? (y/n): " CONFIRM

if [[ "$CONFIRM" == "y" || "$CONFIRM" == "Y" ]]; then
    git add -A
    git commit -m "🔗 Update affiliate links (v${NEW_VERSION})"
    git push origin main
    echo -e "\n${GREEN}✅ Changes pushed to GitHub!${NC}"
    echo -e "${GREEN}🌐 Site will update in ~1 minute${NC}"
else
    echo -e "\n${YELLOW}⏸️  Changes not committed. Run 'git add -A && git commit' when ready.${NC}"
fi

echo -e "\n${GREEN}Done!${NC}"
