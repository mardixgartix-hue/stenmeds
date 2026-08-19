import shutil
import os

src = r"c:\Users\RUDRANSH\OneDrive\Desktop\stenmeds\pics"
dst = r"c:\Users\RUDRANSH\OneDrive\Desktop\stenmeds\assets\images\products"

os.makedirs(dst, exist_ok=True)

# Mapping: source filename -> destination filename
mapping = {
    "WhatsApp Image 2026-08-15 at 8.55.39 PM (1).jpeg": "stengut.jpg",
    "WhatsApp Image 2026-08-15 at 8.55.39 PM.jpeg": "mefenik.jpg",
    "WhatsApp Image 2026-08-15 at 8.55.40 PM (1).jpeg": "bacinik.jpg",
    "WhatsApp Image 2026-08-15 at 8.55.40 PM.jpeg": "stencuf.jpg",
    "WhatsApp Image 2026-08-15 at 8.57.52 PM (1).jpeg": "falroz-xt.jpg",
    "WhatsApp Image 2026-08-15 at 8.57.52 PM (2).jpeg": "sten-dsr.jpg",
    "WhatsApp Image 2026-08-15 at 8.57.52 PM.jpeg": "calsical-lc.jpg",
    "WhatsApp Image 2026-08-15 at 8.57.53 PM (1).jpeg": "my-protine.jpg",
    "WhatsApp Image 2026-08-15 at 8.57.53 PM.jpeg": "sten-phase-500.jpg",
    "WhatsApp Image 2026-08-15 at 8.57.54 PM.jpeg": "stenzi-pro.jpg",
    "WhatsApp Image 2026-08-15 at 8.59.56 PM (1).jpeg": "stenliv-ds.jpg",
    "WhatsApp Image 2026-08-15 at 8.59.56 PM (2).jpeg": "gasomed.jpg",
    "WhatsApp Image 2026-08-15 at 8.59.56 PM.jpeg": "hepto-b6.jpg",
}

for src_name, dst_name in mapping.items():
    src_path = os.path.join(src, src_name)
    dst_path = os.path.join(dst, dst_name)
    if os.path.exists(src_path):
        shutil.copy2(src_path, dst_path)
        print(f"Copied: {src_name} -> {dst_name}")
    else:
        print(f"MISSING: {src_name}")

print("\nDone! All images copied.")
