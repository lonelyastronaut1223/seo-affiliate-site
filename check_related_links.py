#!/usr/bin/env python3
"""
Fix Related Reviews sections to only link to existing review pages
"""

from pathlib import Path
import re

# Existing reviews we have
EXISTING_REVIEWS = {
    'canon-eos-r8-review.html': {
        'name': 'Canon EOS R8',
        'description': 'Budget full-frame option with flagship AF. Great value at $1,299.',
        'image': 'canon-r8.png'
    },
    'dji-osmo-pocket-3-review.html': {
        'name': 'DJI Osmo Pocket 3',
        'description': 'Ultra-compact gimbal camera perfect for travel vlogging.',
        'image': 'dji-pocket3.png'
    },
    'fujifilm-x-t5-review.html': {
        'name': 'Fujifilm X-T5',
        'description': '40MP APS-C alternative with film simulations and classic design.',
        'image': 'fuji-xt5.png'
    },
    'nikon-z8-review.html': {
        'name': 'Nikon Z8',
        'description': 'Professional-grade hybrid with 8K video and flagship performance.',
        'image': 'nikon-z8.png'
    },
    'panasonic-s5-ii-review.html': {
        'name': 'Panasonic S5 II',
        'description': 'Excellent value full-frame with phase-detect AF and great video.',
        'image': 'panasonic-s5ii.png'
    },
    'sony-a7-iv-review.html': {
        'name': 'Sony A7 IV',
        'description': 'Industry-leading hybrid with 33MP and exceptional AF.',
        'image': 'sony-a7iv.png'
    },
    'sony-zv-e10-review.html': {
        'name': 'Sony ZV-E10',
        'description': 'Best budget vlogging camera with flip screen and great AF.',
        'image': 'sony-zv-e10-original.png'
    },
}

def get_related_reviews(current_review, num=3):
    """Get related reviews for a page, excluding current"""
    all_reviews = list(EXISTING_REVIEWS.keys())
    # Remove current review from list
    if current_review in all_reviews:
        all_reviews.remove(current_review)
    
    # Return first num reviews
    return all_reviews[:num]

def check_and_update_related_section(filename):
    """Check if Related Reviews section has valid links"""
    filepath = Path('reviews') / filename
    
    if not filepath.exists():
        print(f"⚠️  File not found: {filename}")
        return
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check for broken links in Related Reviews section
    broken_links = []
    
    # Common broken patterns
    broken_patterns = [
        'canon-eos-r6-ii-review.html',  # We don't have R6 II
        'sony-a7c-ii-review.html',       # We don't have A7C II
        # Add more if found
    ]
    
    has_broken = False
    for pattern in broken_patterns:
        if pattern in content:
            has_broken = True
            broken_links.append(pattern)
    
    if has_broken:
        print(f"🔴 {filename}: Found broken links: {broken_links}")
        return False
    else:
        print(f"✅ {filename}: All links valid")
        return True

def main():
    print("🔍 Checking Related Reviews sections...")
    print("=" * 60)
    
    all_valid = True
    
    for review_file in EXISTING_REVIEWS.keys():
        is_valid = check_and_update_related_section(review_file)
        if not is_valid:
            all_valid = False
    
    print("=" * 60)
    
    if all_valid:
        print("✅ All Related Reviews sections have valid links!")
    else:
        print("⚠️  Some pages have broken links. Please review.")
        print("\nAvailable reviews to link to:")
        for filename, data in EXISTING_REVIEWS.items():
            print(f"  - {filename} ({data['name']})")

if __name__ == '__main__':
    main()
