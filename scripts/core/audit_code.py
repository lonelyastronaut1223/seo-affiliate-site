#!/usr/bin/env python3
"""
Comprehensive code quality and optimization audit script
Analyzes HTML, CSS, JS, images, and provides actionable recommendations
"""

import os
import re
import json
from pathlib import Path
from collections import defaultdict
import mimetypes

BASE_DIR = Path(__file__).parent.parent.parent
IGNORE_DIRS = {'.git', '.venv', 'node_modules', '.github', '__pycache__', '.gemini'}

class CodeAuditor:
    def __init__(self):
        self.issues = defaultdict(list)
        self.stats = defaultdict(int)
        
    def audit_html_files(self):
        """Audit all HTML files for common issues"""
        print("📄 Auditing HTML files...")
        
        html_files = list(BASE_DIR.rglob('*.html'))
        html_files = [f for f in html_files if not any(ignore in f.parts for ignore in IGNORE_DIRS)]
        
        self.stats['total_html'] = len(html_files)
        
        for html_file in html_files:
            self._audit_single_html(html_file)
    
    def _audit_single_html(self, file_path: Path):
        """Audit a single HTML file"""
        try:
            content = file_path.read_text(encoding='utf-8')
            rel_path = file_path.relative_to(BASE_DIR)
            
            # Check for missing meta descriptions
            if '<meta name="description"' not in content:
                self.issues['missing_meta_description'].append(str(rel_path))
            
            # Check for missing OG tags
            if '<meta property="og:' not in content:
                self.issues['missing_og_tags'].append(str(rel_path))
            
            # Check for inline styles (should be minimal)
            inline_styles = re.findall(r'style="[^"]*"', content)
            if len(inline_styles) > 10:
                self.issues['excessive_inline_styles'].append(f"{rel_path} ({len(inline_styles)} instances)")
            
            # Check for images without alt text
            imgs_without_alt = re.findall(r'<img(?![^>]*alt=)[^>]*>', content)
            if imgs_without_alt:
                self.issues['images_without_alt'].append(f"{rel_path} ({len(imgs_without_alt)} images)")
            
            # Check for external links without rel containing "noopener"
            external_links = re.findall(r'<a[^>]+href="https?://[^"]*"[^>]*target="_blank"[^>]*>', content)
            for link in external_links:
                # Check if noopener appears anywhere in rel attribute
                if 'noopener' not in link.lower():
                    self.issues['external_links_no_noopener'].append(str(rel_path))
                    break
            
            # Check for duplicate IDs
            ids = re.findall(r'id="([^"]+)"', content)
            id_counts = {}
            for id_val in ids:
                id_counts[id_val] = id_counts.get(id_val, 0) + 1
            duplicates = [id_val for id_val, count in id_counts.items() if count > 1]
            if duplicates:
                self.issues['duplicate_ids'].append(f"{rel_path}: {', '.join(duplicates)}")
            
            # Check for broken internal links
            internal_links = re.findall(r'(?:href|src)="([^"#]+(?:\.html|\.css|\.js|\.png|\.jpg|\.webp|\.svg))"', content)
            for link in internal_links:
                if link.startswith('http'):
                    continue
                # Resolve relative path
                link_path = (file_path.parent / link).resolve()
                if not link_path.exists():
                    self.issues['broken_links'].append(f"{rel_path} → {link}")
            
        except Exception as e:
            self.issues['html_read_errors'].append(f"{file_path}: {str(e)}")
    
    def audit_images(self):
        """Audit image files for optimization opportunities"""
        print("🖼️  Auditing images...")
        
        image_dir = BASE_DIR / 'assets' / 'images'
        if not image_dir.exists():
            return
        
        image_extensions = {'.jpg', '.jpeg', '.png', '.webp', '.gif', '.svg'}
        total_size = 0
        large_images = []
        
        for img_file in image_dir.rglob('*'):
            if img_file.is_file() and img_file.suffix.lower() in image_extensions:
                self.stats['total_images'] += 1
                size_mb = img_file.stat().st_size / (1024 * 1024)
                total_size += size_mb
                
                # Flag images > 500KB
                if size_mb > 0.5:
                    large_images.append(f"{img_file.relative_to(BASE_DIR)} ({size_mb:.2f}MB)")
                
                # Check if PNG should be WebP
                if img_file.suffix.lower() == '.png':
                    webp_version = img_file.with_suffix('.webp')
                    if not webp_version.exists():
                        self.issues['png_without_webp'].append(str(img_file.relative_to(BASE_DIR)))
        
        self.stats['total_image_size_mb'] = total_size
        if large_images:
            self.issues['large_images'] = large_images
    
    def audit_css_js(self):
        """Audit CSS and JS files"""
        print("🎨 Auditing CSS/JS files...")
        
        css_files = list((BASE_DIR / 'assets' / 'css').rglob('*.css'))
        js_files = list((BASE_DIR / 'assets' / 'js').rglob('*.js'))
        
        # Check for minified versions
        for css_file in css_files:
            if not css_file.name.endswith('.min.css'):
                min_version = css_file.parent / f"{css_file.stem}.min.css"
                if not min_version.exists():
                    self.issues['css_not_minified'].append(str(css_file.relative_to(BASE_DIR)))
        
        for js_file in js_files:
            if not js_file.name.endswith('.min.js') and js_file.name != 'sw.js':
                min_version = js_file.parent / f"{js_file.stem}.min.js"
                if not min_version.exists():
                    self.issues['js_not_minified'].append(str(js_file.relative_to(BASE_DIR)))
    
    def audit_seo_consistency(self):
        """Check SEO consistency across pages"""
        print("🔍 Auditing SEO consistency...")
        
        # Check sitemap exists
        sitemap = BASE_DIR / 'sitemap.xml'
        if not sitemap.exists():
            self.issues['missing_sitemap'].append("sitemap.xml not found")
        
        # Check robots.txt
        robots = BASE_DIR / 'robots.txt'
        if not robots.exists():
            self.issues['missing_robots'].append("robots.txt not found")
    
    def generate_report(self):
        """Generate comprehensive audit report"""
        print("\n" + "="*80)
        print("📊 CODE AUDIT REPORT")
        print("="*80)
        
        # Statistics
        print("\n📈 Statistics:")
        print(f"  • Total HTML files: {self.stats.get('total_html', 0)}")
        print(f"  • Total images: {self.stats.get('total_images', 0)}")
        print(f"  • Total image size: {self.stats.get('total_image_size_mb', 0):.2f} MB")
        
        # Issues by category
        print("\n🔴 Issues Found:\n")
        
        categories = {
            'SEO & Meta Tags': [
                'missing_meta_description',
                'missing_og_tags',
                'missing_sitemap',
                'missing_robots'
            ],
            'Accessibility': [
                'images_without_alt',
                'duplicate_ids'
            ],
            'Security': [
                'external_links_no_noopener'
            ],
            'Performance': [
                'large_images',
                'png_without_webp',
                'css_not_minified',
                'js_not_minified',
                'excessive_inline_styles'
            ],
            'Code Quality': [
                'broken_links',
                'html_read_errors'
            ]
        }
        
        total_issues = 0
        
        for category, issue_types in categories.items():
            category_issues = []
            for issue_type in issue_types:
                if issue_type in self.issues and self.issues[issue_type]:
                    category_issues.append((issue_type, self.issues[issue_type]))
            
            if category_issues:
                print(f"  {category}:")
                for issue_type, items in category_issues:
                    issue_name = issue_type.replace('_', ' ').title()
                    total_issues += len(items)
                    print(f"    ❌ {issue_name} ({len(items)})")
                    # Show first 3 examples
                    for item in items[:3]:
                        print(f"       - {item}")
                    if len(items) > 3:
                        print(f"       ... and {len(items) - 3} more")
                print()
        
        # Summary
        print("="*80)
        if total_issues == 0:
            print("✅ No issues found! Code is in great shape.")
        else:
            print(f"⚠️  Total Issues: {total_issues}")
            print("\nPriority Recommendations:")
            print("  1. Fix accessibility issues (alt text, duplicate IDs)")
            print("  2. Optimize large images (compress or use WebP)")
            print("  3. Add missing meta tags for better SEO")
            print("  4. Minify CSS/JS files that aren't minified")
            print("  5. Fix broken internal links")
        print("="*80)
        
        # Save detailed report
        report_file = BASE_DIR / 'scripts' / 'core' / 'audit_report.json'
        with open(report_file, 'w') as f:
            json.dump({
                'stats': dict(self.stats),
                'issues': {k: v for k, v in self.issues.items()}
            }, f, indent=2)
        print(f"\n💾 Detailed report saved to: {report_file.relative_to(BASE_DIR)}")

def main():
    print("🚀 Starting Comprehensive Code Audit...\n")
    
    auditor = CodeAuditor()
    auditor.audit_html_files()
    auditor.audit_images()
    auditor.audit_css_js()
    auditor.audit_seo_consistency()
    auditor.generate_report()

if __name__ == '__main__':
    main()
