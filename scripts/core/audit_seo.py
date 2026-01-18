#!/usr/bin/env python3
"""
SEO Health Audit Tool 
Comprehensive white-hat SEO analysis for the camera review site.

Checks:
1. Meta tags completeness (title, description, OG tags, etc.)
2. Schema.org markup validation
3. Affiliate link format consistency
4. Image alt tags
5. Heading structure
6. Internal/external link ratio
7. Mobile-friendliness indicators

Usage:
    python scripts/seo/audit_seo.py [--verbose] [--report]
"""

from pathlib import Path
from collections import defaultdict
import re
import json
import argparse
from datetime import datetime

BASE_DIR = Path(__file__).parent.parent.parent
HTML_DIRS = [BASE_DIR, BASE_DIR / 'de', BASE_DIR / 'reviews', BASE_DIR / 'guides', 
             BASE_DIR / 'compare', BASE_DIR / 'de/bewertungen', BASE_DIR / 'de/ratgeber',
             BASE_DIR / 'de/vergleiche']

# ============================================================================
# SEO CHECK CATEGORIES
# ============================================================================

class SEOAudit:
    def __init__(self):
        self.results = {
            'meta_tags': [],
            'schema': [],
            'affiliate_links': [],
            'images': [],
            'headings': [],
            'links': [],
            'performance': [],
            'mobile': []
        }
        self.scores = {}
        self.total_files = 0
        
    def audit_file(self, file_path: Path) -> dict:
        """Run all audits on a single file."""
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        relative_path = file_path.relative_to(BASE_DIR)
        issues = {
            'file': str(relative_path),
            'meta': self.check_meta_tags(content, relative_path),
            'schema': self.check_schema(content, relative_path),
            'affiliate': self.check_affiliate_links(content, relative_path),
            'images': self.check_images(content, relative_path),
            'headings': self.check_headings(content, relative_path),
            'links': self.check_links(content, relative_path)
        }
        
        return issues
    
    def check_meta_tags(self, content: str, file_path: Path) -> dict:
        """Check meta tag completeness."""
        issues = []
        checks = {
            'title': bool(re.search(r'<title[^>]*>.+</title>', content, re.DOTALL)),
            'meta_description': bool(re.search(r'<meta\s+name=["\']description["\']', content, re.I)),
            'og_title': bool(re.search(r'<meta\s+property=["\']og:title["\']', content, re.I)),
            'og_description': bool(re.search(r'<meta\s+property=["\']og:description["\']', content, re.I)),
            'og_image': bool(re.search(r'<meta\s+property=["\']og:image["\']', content, re.I)),
            'og_url': bool(re.search(r'<meta\s+property=["\']og:url["\']', content, re.I)),
            'twitter_card': bool(re.search(r'<meta\s+name=["\']twitter:card["\']', content, re.I)),
            'canonical': bool(re.search(r'<link\s+rel=["\']canonical["\']', content, re.I)),
            'viewport': bool(re.search(r'<meta\s+name=["\']viewport["\']', content, re.I)),
            'lang': bool(re.search(r'<html[^>]*\slang=["\']', content, re.I)),
        }
        
        # Check title length
        title_match = re.search(r'<title[^>]*>(.+?)</title>', content, re.DOTALL)
        if title_match:
            title_len = len(title_match.group(1).strip())
            if title_len > 60:
                issues.append(f"Title too long ({title_len} chars, recommended < 60)")
            elif title_len < 30:
                issues.append(f"Title too short ({title_len} chars, recommended 30-60)")
        
        # Check meta description length
        desc_match = re.search(r'<meta\s+name=["\']description["\']\s+content=["\']([^"\']+)["\']', content, re.I)
        if desc_match:
            desc_len = len(desc_match.group(1).strip())
            if desc_len > 160:
                issues.append(f"Meta description too long ({desc_len} chars, recommended < 160)")
            elif desc_len < 70:
                issues.append(f"Meta description too short ({desc_len} chars, recommended 70-160)")
        
        missing = [k for k, v in checks.items() if not v]
        if missing:
            issues.append(f"Missing: {', '.join(missing)}")
            
        return {'checks': checks, 'issues': issues, 'score': sum(checks.values()) / len(checks) * 100}
    
    def check_schema(self, content: str, file_path: Path) -> dict:
        """Check Schema.org structured data."""
        issues = []
        schema_types = []
        
        # Find all JSON-LD schema blocks
        schema_blocks = re.findall(r'<script\s+type=["\']application/ld\+json["\'][^>]*>(.*?)</script>', content, re.DOTALL)
        
        for block in schema_blocks:
            try:
                data = json.loads(block)
                if isinstance(data, dict):
                    schema_type = data.get('@type', 'Unknown')
                    schema_types.append(schema_type)
                elif isinstance(data, list):
                    for item in data:
                        if isinstance(item, dict):
                            schema_types.append(item.get('@type', 'Unknown'))
            except json.JSONDecodeError as e:
                issues.append(f"Invalid JSON-LD: {str(e)[:50]}")
        
        # Check for recommended schema types based on page type
        file_str = str(file_path)
        recommended = []
        
        if 'review' in file_str or 'bewertung' in file_str or 'testbericht' in file_str:
            recommended = ['Product', 'Review', 'BreadcrumbList', 'FAQPage']
        elif 'guide' in file_str or 'ratgeber' in file_str:
            recommended = ['Article', 'BreadcrumbList', 'FAQPage']
        elif 'compare' in file_str or 'vergleich' in file_str:
            recommended = ['Article', 'BreadcrumbList']
        elif 'index' in file_str:
            recommended = ['WebSite', 'Organization']
        
        missing_schema = [s for s in recommended if s not in schema_types]
        if missing_schema:
            issues.append(f"Recommended schema missing: {', '.join(missing_schema)}")
        
        return {
            'found_types': schema_types,
            'issues': issues,
            'count': len(schema_blocks),
            'score': 100 if not issues else max(0, 100 - len(issues) * 20)
        }
    
    def check_affiliate_links(self, content: str, file_path: Path) -> dict:
        """Check affiliate link consistency and compliance."""
        issues = []
        
        # Find all affiliate-style links
        amazon_links = re.findall(r'href=["\']([^"\']*(?:amazon|amzn)[^"\']*)["\']', content, re.I)
        btn_buy_links = re.findall(r'<a[^>]*class=["\'][^"\']*btn-buy[^"\']*["\'][^>]*>', content, re.I)
        sponsored_links = re.findall(r'rel=["\'][^"\']*sponsored[^"\']*["\']', content)
        nofollow_links = re.findall(r'rel=["\'][^"\']*nofollow[^"\']*["\']', content)
        
        total_affiliate = len(amazon_links) + len(btn_buy_links)
        
        # Check if affiliate links have proper rel attributes
        for link in btn_buy_links:
            if 'rel=' not in link:
                issues.append("Buy button missing rel attribute")
            elif 'sponsored' not in link and 'nofollow' not in link:
                issues.append("Buy button should have rel='sponsored' or rel='nofollow'")
        
        # Check for disclosure
        has_disclosure = bool(re.search(r'affiliate|provision|commission|partner', content, re.I))
        if total_affiliate > 0 and not has_disclosure:
            issues.append("Affiliate links found but no disclosure statement")
        
        return {
            'amazon_count': len(amazon_links),
            'buy_buttons': len(btn_buy_links),
            'sponsored_attrs': len(sponsored_links),
            'has_disclosure': has_disclosure,
            'issues': issues,
            'score': 100 if not issues else max(0, 100 - len(issues) * 25)
        }
    
    def check_images(self, content: str, file_path: Path) -> dict:
        """Check image optimization."""
        issues = []
        
        # Find all images
        images = re.findall(r'<img\s+([^>]+)>', content, re.I)
        
        missing_alt = 0
        missing_loading = 0
        no_webp = 0
        
        for img in images:
            if 'alt=' not in img:
                missing_alt += 1
            if 'loading=' not in img:
                missing_loading += 1
            if '.webp' not in img.lower() and 'data:' not in img:
                no_webp += 1
        
        total = len(images)
        if total > 0:
            if missing_alt > 0:
                issues.append(f"{missing_alt}/{total} images missing alt text")
            if missing_loading > total * 0.5:
                issues.append(f"{missing_loading}/{total} images missing lazy loading")
            if no_webp > total * 0.3:
                issues.append(f"{no_webp}/{total} images not using WebP format")
        
        alt_score = (1 - missing_alt/max(total, 1)) * 100 if total > 0 else 100
        
        return {
            'total_images': total,
            'missing_alt': missing_alt,
            'missing_loading': missing_loading,
            'no_webp': no_webp,
            'issues': issues,
            'score': alt_score
        }
    
    def check_headings(self, content: str, file_path: Path) -> dict:
        """Check heading structure."""
        issues = []
        
        h1_count = len(re.findall(r'<h1[^>]*>', content, re.I))
        h2_count = len(re.findall(r'<h2[^>]*>', content, re.I))
        h3_count = len(re.findall(r'<h3[^>]*>', content, re.I))
        
        if h1_count == 0:
            issues.append("Missing H1 tag")
        elif h1_count > 1:
            issues.append(f"Multiple H1 tags ({h1_count}), should have only 1")
        
        if h2_count == 0:
            issues.append("No H2 tags found - consider adding subheadings")
        
        return {
            'h1_count': h1_count,
            'h2_count': h2_count,
            'h3_count': h3_count,
            'issues': issues,
            'score': 100 if h1_count == 1 else (50 if h1_count > 0 else 0)
        }
    
    def check_links(self, content: str, file_path: Path) -> dict:
        """Check internal/external link balance."""
        issues = []
        
        all_links = re.findall(r'href=["\']([^"\']+)["\']', content)
        
        internal = 0
        external = 0
        broken_format = 0
        
        for link in all_links:
            if link.startswith('#') or link.startswith('/') or link.startswith('./') or link.startswith('../'):
                internal += 1
            elif link.startswith('http://') or link.startswith('https://'):
                if 'kameraupick' in link.lower() or 'cameraupick' in link.lower():
                    internal += 1
                else:
                    external += 1
            elif link.startswith('mailto:') or link.startswith('tel:'):
                pass
            else:
                # Relative links
                internal += 1
        
        total = internal + external
        if total > 0 and internal == 0:
            issues.append("No internal links found")
        
        return {
            'internal': internal,
            'external': external,
            'total': total,
            'ratio': f"{internal}:{external}",
            'issues': issues,
            'score': 100 if not issues else 70
        }

    def run_audit(self, verbose: bool = False) -> dict:
        """Run full audit on all HTML files."""
        all_issues = []
        category_scores = defaultdict(list)
        
        for html_dir in HTML_DIRS:
            if not html_dir.exists():
                continue
            for html_file in html_dir.glob('*.html'):
                self.total_files += 1
                result = self.audit_file(html_file)
                all_issues.append(result)
                
                # Collect scores
                for key in ['meta', 'schema', 'affiliate', 'images', 'headings', 'links']:
                    if key in result and 'score' in result[key]:
                        category_scores[key].append(result[key]['score'])
        
        # Calculate average scores
        self.scores = {
            k: sum(v) / len(v) if v else 0 
            for k, v in category_scores.items()
        }
        self.scores['overall'] = sum(self.scores.values()) / len(self.scores) if self.scores else 0
        
        return {
            'files_audited': self.total_files,
            'all_issues': all_issues,
            'scores': self.scores
        }
    
    def print_report(self, results: dict, verbose: bool = False):
        """Print a formatted audit report."""
        print("\n" + "="*70)
        print("📊 SEO HEALTH AUDIT REPORT")
        print(f"   Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
        print("="*70)
        
        print(f"\n📁 Files Audited: {results['files_audited']}")
        
        print("\n🎯 CATEGORY SCORES:")
        print("-"*40)
        
        score_labels = {
            'meta': '📝 Meta Tags',
            'schema': '🔗 Schema Markup',
            'affiliate': '💰 Affiliate Links',
            'images': '🖼️  Images',
            'headings': '📑 Headings',
            'links': '🔗 Links',
            'overall': '⭐ OVERALL'
        }
        
        for key, label in score_labels.items():
            if key in results['scores']:
                score = results['scores'][key]
                bar = self._score_bar(score)
                emoji = "✅" if score >= 80 else ("⚠️" if score >= 50 else "❌")
                print(f"  {label}: {bar} {score:.1f}% {emoji}")
        
        # Print issues summary
        print("\n⚠️  ISSUES FOUND:")
        print("-"*40)
        
        issue_count = 0
        for file_result in results['all_issues']:
            file_issues = []
            for key in ['meta', 'schema', 'affiliate', 'images', 'headings', 'links']:
                if key in file_result and file_result[key].get('issues'):
                    file_issues.extend(file_result[key]['issues'])
            
            if file_issues and verbose:
                print(f"\n📄 {file_result['file']}")
                for issue in file_issues:
                    print(f"   • {issue}")
                    issue_count += 1
            elif file_issues:
                issue_count += len(file_issues)
        
        if not verbose and issue_count > 0:
            print(f"  {issue_count} issues found across all files")
            print("  Run with --verbose to see details")
        elif issue_count == 0:
            print("  ✅ No major issues found!")
        
        print("\n" + "="*70)
        
        # Final verdict
        overall = results['scores'].get('overall', 0)
        if overall >= 90:
            print("🏆 SEO HEALTH: EXCELLENT")
        elif overall >= 75:
            print("✅ SEO HEALTH: GOOD")
        elif overall >= 50:
            print("⚠️  SEO HEALTH: NEEDS IMPROVEMENT")
        else:
            print("❌ SEO HEALTH: CRITICAL ISSUES")
        
        print("="*70 + "\n")
    
    def _score_bar(self, score: float, width: int = 20) -> str:
        """Generate a visual progress bar."""
        filled = int(score / 100 * width)
        return f"[{'█' * filled}{'░' * (width - filled)}]"


def main():
    parser = argparse.ArgumentParser(description='SEO Health Audit Tool')
    parser.add_argument('--verbose', '-v', action='store_true', help='Show detailed issues per file')
    parser.add_argument('--report', '-r', action='store_true', help='Generate JSON report file')
    args = parser.parse_args()
    
    audit = SEOAudit()
    results = audit.run_audit(verbose=args.verbose)
    audit.print_report(results, verbose=args.verbose)
    
    if args.report:
        report_path = BASE_DIR / 'seo_audit_report.json'
        with open(report_path, 'w', encoding='utf-8') as f:
            # Simplify for JSON serialization
            json_results = {
                'generated': datetime.now().isoformat(),
                'files_audited': results['files_audited'],
                'scores': results['scores'],
                'summary': {
                    'total_issues': sum(
                        len(fr.get(k, {}).get('issues', []))
                        for fr in results['all_issues']
                        for k in ['meta', 'schema', 'affiliate', 'images', 'headings', 'links']
                    )
                }
            }
            json.dump(json_results, f, indent=2)
        print(f"📄 Report saved to: {report_path}")


if __name__ == '__main__':
    main()
