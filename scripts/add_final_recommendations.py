#!/usr/bin/env python3
"""
Add Final Recommendation sections to review pages that don't have them.
"""

import os
import re

REVIEWS_DIR = "src/pages/reviews"

# Final Recommendation content for each camera
RECOMMENDATIONS = {
    "nikon-z8-review.astro": {
        "name": "Nikon Z8",
        "summary": """The Nikon Z8 delivers Z9-level performance in a smaller, lighter body.
          With 45.7MP resolution, 8K video, and professional-grade autofocus, it's
          the flagship camera for photographers who want maximum capability without
          the bulk. Build quality and reliability are exceptional.""",
        "buy_if": """You need flagship performance in a compact body. Perfect for
          wildlife, sports, weddings, and commercial work where 8K video and high-speed
          shooting matter.""",
        "skip_if": """You prioritize value (consider Z6 III) or don't need the
          extreme resolution and video specs. The Z8 is overkill for casual use."""
    },
    "panasonic-s5-ii-review.astro": {
        "name": "Panasonic S5 II",
        "summary": """The Panasonic S5 II finally brings phase-detection autofocus to
          Panasonic full-frame cameras. Combined with incredible video features,
          unlimited recording, and excellent stabilization, it's a filmmaker's
          dream at a reasonable price point.""",
        "buy_if": """You prioritize video quality and features above all else.
          Perfect for documentary work, interviews, and indie filmmaking where
          reliability and color science matter.""",
        "skip_if": """You need class-leading autofocus for fast action (Sony/Canon
          are better), or you primarily shoot stills and want maximum resolution."""
    },
    "fujifilm-x-t5-review.astro": {
        "name": "Fujifilm X-T5",
        "summary": """The Fujifilm X-T5 is a photographer's camera through and through.
          With 40MP resolution, classic controls, and Fujifilm's legendary color
          science, it captures images with character you won't find elsewhere.
          The retro design isn't just aesthetic—it's genuinely functional.""",
        "buy_if": """You love the photographic process and want a camera that
          inspires creativity. Perfect for street, portrait, and travel photography
          where Fujifilm colors shine.""",
        "skip_if": """You need advanced video features (consider X-S20 or X-H2S),
          or prefer modern touchscreen-first interfaces."""
    },
    "canon-eos-r8-review.astro": {
        "name": "Canon EOS R8",
        "summary": """The Canon EOS R8 puts R5-level autofocus in an incredibly
          affordable full-frame body. For photographers who prioritize AF
          performance over video specs, it's an exceptional value proposition.
          The lightweight build makes it ideal for all-day shooting.""",
        "buy_if": """You want top-tier autofocus without the flagship price tag.
          Perfect for portraits, events, and travel where subject tracking
          and Eye AF are critical.""",
        "skip_if": """You need professional video features (R6 III is better),
          weather sealing, or dual card slots for redundancy."""
    },
    "dji-osmo-pocket-3-review.astro": {
        "name": "DJI Osmo Pocket 3",
        "summary": """The DJI Osmo Pocket 3 is the ultimate vlogging companion.
          With a 1-inch sensor, rotating screen, and 3-axis gimbal stabilization,
          it captures professional-quality content in your pocket. The convenience
          factor is unmatched by any traditional camera.""",
        "buy_if": """You create content on the go and value portability above all.
          Perfect for vloggers, travel creators, and anyone who wants gimbal
          smoothness without the bulk.""",
        "skip_if": """You need interchangeable lenses, maximum low-light performance,
          or professional audio without adapters."""
    },
    "sony-a7-v-review.astro": {
        "name": "Sony A7 V",
        "summary": """The Sony A7 V represents the pinnacle of all-around mirrorless
          cameras. With AI-powered autofocus, excellent 4K video, and the most
          refined ergonomics in the A7 lineup, it handles any shooting scenario
          with confidence. This is Sony's most complete hybrid camera.""",
        "buy_if": """You want a do-everything camera that excels at both stills
          and video. Perfect for professionals who need reliability and
          cutting-edge AF technology.""",
        "skip_if": """You're satisfied with the A7 IV and don't need the AI AF
          improvements, or you're strictly budget-focused."""
    },
    "sony-a7c-ii-review.astro": {
        "name": "Sony A7C II",
        "summary": """The Sony A7C II proves that compact doesn't mean compromise.
          With A7 IV-level image quality in a rangefinder-style body, it's the
          perfect travel and street photography companion. The new AI autofocus
          handles any subject with remarkable precision.""",
        "buy_if": """You prioritize portability but refuse to sacrifice full-frame
          image quality. Perfect for travel, street photography, and everyday
          carry where size matters.""",
        "skip_if": """You need the ergonomics of a traditional grip for heavy
          lenses, or you require dual card slots for professional backup."""
    },
    "sony-zv-e10-review.astro": {
        "name": "Sony ZV-E10",
        "summary": """The Sony ZV-E10 democratizes content creation. With excellent
          autofocus, product showcase mode, and creator-friendly features, it
          makes professional-looking video accessible to everyone. The price-to-
          performance ratio is exceptional in the vlogging category.""",
        "buy_if": """You're starting your content creation journey and want
          interchangeable lenses. Perfect for YouTube, streaming, and social
          media content on a budget.""",
        "skip_if": """You need advanced stabilization (consider ZV-E10 II), want
          an EVF for traditional shooting, or need weather sealing."""
    },
    "om-system-om-1-ii-review.astro": {
        "name": "OM System OM-1 Mark II",
        "summary": """The OM System OM-1 Mark II maximizes what Micro Four Thirds
          can achieve. With incredible computational features, blazing-fast shooting,
          and legendary weather sealing, it excels in conditions that challenge
          larger cameras. The size advantage is genuinely meaningful.""",
        "buy_if": """You value portability and weather resistance for outdoor
          adventures. Perfect for wildlife, bird photography, and travel where
          size and reach matter.""",
        "skip_if": """You need maximum low-light performance or the shallow depth
          of field only larger sensors provide."""
    },
}

def add_final_recommendation(filepath):
    """Add Final Recommendation section before Author Box."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    filename = os.path.basename(filepath)
    
    if filename not in RECOMMENDATIONS:
        print(f"○ No recommendation data: {filename}")
        return False
    
    if "Final Recommendation" in content:
        print(f"○ Already has recommendation: {filename}")
        return False
    
    rec = RECOMMENDATIONS[filename]
    
    recommendation_html = f'''
    <!-- Final Recommendation -->
    <section class="section">
      <div class="final-verdict">
        <h2>Final Recommendation</h2>
        <p>
          {rec["summary"]}
        </p>
        <p>
          <strong>Buy it if:</strong> {rec["buy_if"]}
        </p>
        <p>
          <strong>Skip it if:</strong> {rec["skip_if"]}
        </p>
      </div>
    </section>

'''
    
    # Insert before Author Box
    author_box_pattern = r'(\s*<!-- Author Box -->)'
    if re.search(author_box_pattern, content):
        content = re.sub(author_box_pattern, recommendation_html + r'\1', content)
    else:
        # Try alternate pattern without comment
        content = re.sub(
            r'(\s*<section class="section author-box")',
            recommendation_html + r'\1',
            content
        )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✓ Added recommendation: {filename}")
    return True

def main():
    added_count = 0
    for filename in RECOMMENDATIONS.keys():
        filepath = os.path.join(REVIEWS_DIR, filename)
        if os.path.exists(filepath):
            if add_final_recommendation(filepath):
                added_count += 1
        else:
            print(f"✗ Not found: {filename}")
    
    print(f"\n✓ Added {added_count} Final Recommendation sections")

if __name__ == "__main__":
    main()
