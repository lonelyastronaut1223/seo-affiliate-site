#!/bin/bash
# Batch update all card images to responsive srcset
# For mobile image optimization Phase 2

FILE="src/pages/index.astro"

echo "Updating $FILE with responsive srcset..."

# Buying Guides Section
sed -i '' 's|srcset="/assets/images/guides/vlog\.webp"|srcset="/assets/images/guides/vlog-sm.webp 600w, /assets/images/guides/vlog.webp 1200w"\n                sizes="(max-width: 768px) 100vw, 50vw"|' "$FILE"

sed -i '' 's|srcset="/assets/images/guides/budget\.webp"|srcset="/assets/images/guides/budget-sm.webp 600w, /assets/images/guides/budget.webp 1200w"\n                sizes="(max-width: 768px) 100vw, 50vw"|' "$FILE"

sed -i '' 's|srcset="/assets/images/guides/hybrid\.webp"|srcset="/assets/images/guides/hybrid-sm.webp 600w, /assets/images/guides/hybrid.webp 1200w"\n                sizes="(max-width: 768px) 100vw, 50vw"|' "$FILE"

sed -i '' 's|srcset="/assets/images/guides/fullframe-video\.webp"|srcset="/assets/images/guides/fullframe-video-sm.webp 600w, /assets/images/guides/fullframe-video.webp 1200w"\n                sizes="(max-width: 768px) 100vw, 50vw"|' "$FILE"

sed -i '' 's|srcset="/assets/images/guides/action-360\.webp"|srcset="/assets/images/guides/action-360-sm.webp 600w, /assets/images/guides/action-360.webp 1200w"\n                sizes="(max-width: 768px) 100vw, 50vw"|' "$FILE"

echo "✅ Buying Guides section updated"

# Now add srcset to <img> tags for JPEG fallbacks
sed -i '' 's|src="/assets/images/guides/travel\.jpg?v=20260111"|src="/assets/images/guides/travel.jpg"\n                srcset="/assets/images/guides/travel-sm.jpg 600w, /assets/images/guides/travel.jpg 1200w"\n                sizes="(max-width: 768px) 100vw, 50vw"|' "$FILE"

sed -i '' 's|src="/assets/images/guides/vlog\.jpg?v=20260111"|src="/assets/images/guides/vlog.jpg"\n                srcset="/assets/images/guides/vlog-sm.jpg 600w, /assets/images/guides/vlog.jpg 1200w"\n                sizes="(max-width: 768px) 100vw, 50vw"|' "$FILE"

sed -i '' 's|src="/assets/images/guides/budget\.jpg?v=20260111"|src="/assets/images/guides/budget.jpg"\n                srcset="/assets/images/guides/budget-sm.jpg 600w, /assets/images/guides/budget.jpg 1200w"\n                sizes="(max-width: 768px) 100vw, 50vw"|' "$FILE"

sed -i '' 's|src="/assets/images/guides/hybrid\.jpg?v=20260111"|src="/assets/images/guides/hybrid.jpg"\n                srcset="/assets/images/guides/hybrid-sm.jpg 600w, /assets/images/guides/hybrid.jpg 1200w"\n                sizes="(max-width: 768px) 100vw, 50vw"|' "$FILE"

sed -i '' 's|src="/assets/images/guides/fullframe-video\.jpg?v=20260111"|src="/assets/images/guides/fullframe-video.jpg"\n                srcset="/assets/images/guides/fullframe-video-sm.jpg 600w, /assets/images/guides/fullframe-video.jpg 1200w"\n                sizes="(max-width: 768px) 100vw, 50vw"|' "$FILE"

sed -i '' 's|src="/assets/images/guides/action-360\.jpg?v=20260111"|src="/assets/images/guides/action-360.jpg"\n                srcset="/assets/images/guides/action-360-sm.jpg 600w, /assets/images/guides/action-360.jpg 1200w"\n                sizes="(max-width: 768px) 100vw, 50vw"|' "$FILE"

echo "✅ All Buying Guides cards updated with responsive srcset"
echo "Done!"
