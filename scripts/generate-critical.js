/**
 * Generate Critical CSS using the Critical library (ESM version)
 * This extracts ALL above-the-fold CSS, not just partial
 */

import { generate } from 'critical';
import { writeFileSync } from 'fs';

async function generateCriticalCSS() {
    console.log('🔍 Analyzing page and extracting critical CSS...\n');

    try {
        const result = await generate({
            // Use built HTML file
            src: 'dist/index.html',

            // Target dimensions (mobile and desktop)
            dimensions: [
                { width: 375, height: 812 },   // Mobile
                { width: 768, height: 1024 },  // Tablet
                { width: 1440, height: 900 }   // Desktop
            ],

            // Inline CSS (we'll extract and use it manually)
            inline: false,

            // Extract CSS from these files
            css: [
                'dist/assets/css/style.min.css',
                'dist/assets/css/mega-menu.min.css',
                'dist/assets/css/footer-enhancements.min.css',
                'dist/assets/css/loaders.min.css'
            ],

            // Ignore certain rules
            ignore: {
                atrule: ['@font-face'],
            },

            // Penthouse options
            penthouse: {
                timeout: 30000,
                renderWaitTime: 100
            }
        });

        // Save critical CSS
        const criticalCSSPath = 'src/critical-generated.css';
        writeFileSync(criticalCSSPath, result.css);

        const size = (result.css.length / 1024).toFixed(2);
        console.log(`✅ Critical CSS generated: ${criticalCSSPath}`);
        console.log(`📊 Size: ${size} KB`);
        console.log('\nNext: Inline this CSS into BaseLayout.astro');

    } catch (error) {
        console.error('❌ Error generating critical CSS:', error.message);
        process.exit(1);
    }
}

generateCriticalCSS();
