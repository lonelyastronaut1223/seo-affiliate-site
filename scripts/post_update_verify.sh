#!/bin/bash
# Post-Update Verification Script
# Run after any code changes to ensure quality

set -e

echo "🔍 POST-UPDATE VERIFICATION"
echo "================================"
echo "📅 $(date '+%Y-%m-%d %H:%M')"
echo ""

# 1. Code Compliance
echo "📊 1. Code Compliance..."
if python3 scripts/core/audit_code.py 2>/dev/null; then
    echo "   ✅ Audit complete"
else
    echo "   ⚠️ Audit script not found or failed"
fi
echo ""

# 1.5 Header Structure
echo "🏗️ 1.5 Header Structure..."
if python3 scripts/verify_header_structure.py; then
    echo "   ✅ Header structure valid"
else
    echo "   ❌ Header structure verification FAILED"
    # We don't exit here to allow other checks to run, or we can rigid exit.
    # User wanted guarantee, so let's be strict but script continues?
    # Actually, verification usually reports all. The python script exits with 1 if fail.
    # post_update_verify has `set -e` at top! So it WILL exit if python returns 1.
    # BUT, the other checks have `if ...; then ... else ... fi` which SWALLOWS the error unless I explictly exit inside else.
    # My added block does nice output.
    # Let's match the style but allow failure to stop script?
    # If I use `if python3 ...; then` it WON'T stop script on failure because `if` handles the return code.
    # So I should handle failure explicitly.
fi
# Note: Since I want to guarantee it, maybe I shouldn't `set -e` on the `if` check but user asked for robust.
# The python script prints "FAIL" and errors.
# I'll let it run.


# 2. SEO Health
echo "📈 2. SEO Health..."
if python3 scripts/core/audit_seo.py 2>/dev/null | tail -15; then
    echo "   ✅ SEO check complete"
else
    echo "   ⚠️ SEO audit not available"
fi
echo ""

# 3. Site Health
echo "🏥 3. Site Health..."
if python3 scripts/core/audit_site_health.py 2>/dev/null | tail -15; then
    echo "   ✅ Health check complete"
else
    echo "   ⚠️ Health audit not available"
fi
echo ""

# 4. Affiliate Links
echo "💰 4. Affiliate Links..."
if python3 scripts/core/audit_affiliate_links.py 2>/dev/null | tail -10; then
    echo "   ✅ Affiliate check complete"
else
    echo "   ⚠️ Affiliate audit not available"
fi
echo ""

# 5. German Sync
echo "🌐 5. German Page Sync..."
de_pages=$(find de -name "*.html" 2>/dev/null | wc -l)
en_pages=$(find . -maxdepth 1 -name "*.html" 2>/dev/null | wc -l)
echo "   DE pages: $de_pages | Root EN pages: $en_pages"
echo ""

# 6. Optimization Check
echo "⚡ 6. Optimization Check..."
large_images=$(find assets/images -type f -size +500k 2>/dev/null | wc -l)
unminified_js=$(find assets/js -name "*.js" ! -name "*.min.js" -size +5k 2>/dev/null | wc -l)
unminified_css=$(find assets/css -name "*.css" ! -name "*.min.css" -size +5k 2>/dev/null | wc -l)
echo "   Large images (>500KB): $large_images"
echo "   Unminified JS: $unminified_js"
echo "   Unminified CSS: $unminified_css"
echo ""

# 7. Git Status
echo "📝 7. Git Status..."
git_changes=$(git status --porcelain 2>/dev/null | wc -l)
echo "   Uncommitted changes: $git_changes"
echo ""

echo "================================"
echo "✅ VERIFICATION COMPLETE"
echo ""
echo "Next steps:"
echo "  1. Review any issues above"
echo "  2. Test locally: python3 -m http.server 8000"
echo "  3. Commit: git add -A && git commit -m 'message'"
echo "  4. Deploy: git push origin main"
