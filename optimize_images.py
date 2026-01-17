import os
import sys
from PIL import Image

def convert_to_webp(directory):
    success_count = 0
    error_count = 0
    skipped_count = 0
    
    # Extensions to convert
    extensions = ('.jpg', '.jpeg', '.png')
    
    print(f"🔄 Scanning {directory} for images to convert...")
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(extensions):
                file_path = os.path.join(root, file)
                file_root, _ = os.path.splitext(file_path)
                webp_path = f"{file_root}.webp"
                
                # Check if WebP already exists
                if os.path.exists(webp_path):
                    # Check modified time, if original is newer, re-convert
                    src_mtime = os.path.getmtime(file_path)
                    dst_mtime = os.path.getmtime(webp_path)
                    
                    if src_mtime <= dst_mtime:
                        skipped_count += 1
                        continue

                try:
                    with Image.open(file_path) as img:
                        # Convert to RGB if RGBA (unless keeping transparency for PNG)
                        if file.lower().endswith(('.jpg', '.jpeg')) and img.mode == 'RGBA':
                            img = img.convert('RGB')
                        
                        # Save as WebP
                        # Quality 80 is a good balance
                        img.save(webp_path, 'WEBP', quality=85)
                        
                        # Calculate savings
                        orig_size = os.path.getsize(file_path)
                        webp_size = os.path.getsize(webp_path)
                        saving = (orig_size - webp_size) / orig_size * 100
                        
                        print(f"✅ Converted: {file} -> {os.path.basename(webp_path)} ({saving:.1f}% space saved)")
                        success_count += 1
                        
                except Exception as e:
                    print(f"❌ Error converting {file}: {e}")
                    error_count += 1

    print("\n" + "="*40)
    print(f"🎉 Conversion Complete!")
    print(f"✅ Auto-converted: {success_count}")
    print(f"⏭️ Skipped (already exists): {skipped_count}")
    print(f"❌ Errors: {error_count}")
    print("="*40)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        target_dir = sys.argv[1]
    else:
        target_dir = "assets/images"
    
    # Ensure PIL is installed
    try:
        import PIL
        convert_to_webp(target_dir)
    except ImportError:
        print("❌ Pillow library not found. Installing...")
        import subprocess
        subprocess.check_call([sys.executable, "-m", "pip", "install", "Pillow"])
        print("✅ Pillow installed. Restarting script...")
        convert_to_webp(target_dir)
