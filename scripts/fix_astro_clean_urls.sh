#!/bin/bash
# Fix Astro clean URLs - remove .html extensions from all internal links in Astro files

echo "🔧 Fixing Astro clean URLs..."

# Fix Header.astro
sed -i '' 's|href="/guides/\([^"]*\)\.html"|href="/guides/\1"|g' src/components/Header.astro
sed -i '' 's|href="/lenses/\([^"]*\)\.html"|href="/lenses/\1"|g' src/components/Header.astro
sed -i '' 's|href="/gear/\([^"]*\)\.html"|href="/gear/\1"|g' src/components/Header.astro
sed -i '' 's|href="/deals\.html"|href="/deals"|g' src/components/Header.astro
sed -i '' 's|href="/about\.html"|href="/about"|g' src/components/Header.astro
sed -i '' 's|href="/contact\.html"|href="/contact"|g' src/components/Header.astro
sed -i '' 's|href="/privacy\.html"|href="/privacy"|g' src/components/Header.astro
sed -i '' 's|href="/terms\.html"|href="/terms"|g' src/components/Header.astro

# Fix Footer.astro
sed -i '' 's|href="/\([^"]*\)\.html"|href="/\1"|g' src/components/Footer.astro

# Fix all Astro pages
find src/pages -name "*.astro" -exec sed -i '' 's|href="/guides/\([^"]*\)\.html"|href="/guides/\1"|g' {} +
find src/pages -name "*.astro" -exec sed -i '' 's|href="/lenses/\([^"]*\)\.html"|href="/lenses/\1"|g' {} +
find src/pages -name "*.astro" -exec sed -i '' 's|href="/gear/\([^"]*\)\.html"|href="/gear/\1"|g' {} +
find src/pages -name "*.astro" -exec sed -i '' 's|href="/reviews/\([^"]*\)\.html"|href="/reviews/\1"|g' {} +
find src/pages -name "*.astro" -exec sed -i '' 's|href="/compare/\([^"]*\)\.html"|href="/compare/\1"|g' {} +
find src/pages -name "*.astro" -exec sed -i '' 's|href="/deals\.html"|href="/deals"|g' {} +
find src/pages -name "*.astro" -exec sed -i '' 's|href="/about\.html"|href="/about"|g' {} +
find src/pages -name "*.astro" -exec sed -i '' 's|href="/contact\.html"|href="/contact"|g' {} +
find src/pages -name "*.astro" -exec sed -i '' 's|href="/privacy\.html"|href="/privacy"|g' {} +
find src/pages -name "*.astro" -exec sed -i '' 's|href="/terms\.html"|href="/terms"|g' {} +

# Fix relative links without leading slash
find src/pages -name "*.astro" -exec sed -i '' 's|href="guides/\([^"]*\)\.html"|href="/guides/\1"|g' {} +
find src/pages -name "*.astro" -exec sed -i '' 's|href="lenses/\([^"]*\)\.html"|href="/lenses/\1"|g' {} +
find src/pages -name "*.astro" -exec sed -i '' 's|href="gear/\([^"]*\)\.html"|href="/gear/\1"|g' {} +
find src/pages -name "*.astro" -exec sed -i '' 's|href="reviews/\([^"]*\)\.html"|href="/reviews/\1"|g' {} +
find src/pages -name "*.astro" -exec sed -i '' 's|href="compare/\([^"]*\)\.html"|href="/compare/\1"|g' {} +
find src/pages -name "*.astro" -exec sed -i '' 's|href="deals\.html"|href="/deals"|g' {} +
find src/pages -name "*.astro" -exec sed -i '' 's|href="about\.html"|href="/about"|g' {} +
find src/pages -name "*.astro" -exec sed -i '' 's|href="contact\.html"|href="/contact"|g' {} +
find src/pages -name "*.astro" -exec sed -i '' 's|href="privacy\.html"|href="/privacy"|g' {} +
find src/pages -name "*.astro" -exec sed -i '' 's|href="terms\.html"|href="/terms"|g' {} +

# Fix relative navigation links like ../about.html
find src/pages -name "*.astro" -exec sed -i '' 's|href="../\([^"]*\)\.html"|href="/\1"|g' {} +

echo "✅ Astro clean URLs fixed!"
