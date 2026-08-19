import os
import re

dir_path = r"c:\Users\RUDRANSH\OneDrive\Desktop\stenmeds"

# Target numbers
target_href = "+917417350021"
target_display = "+91 74173 50021"

# Regex patterns to replace
patterns_href = [
    r"\+918047828756",
    r"\+918043805318",
    r"\+911234567890",
    r"\+911234567891"
]

patterns_display = [
    r"\+91 80478 28756",
    r"\+91 80438 05318",
    r"\+91 12345 67890",
    r"\+91 12345 67891"
]

for root, _, files in os.walk(dir_path):
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
            except UnicodeDecodeError:
                with open(filepath, 'r', encoding='latin-1') as f:
                    content = f.read()

            original_content = content

            # Replace hrefs
            for p in patterns_href:
                content = re.sub(p, target_href, content)

            # Replace displays
            for p in patterns_display:
                content = re.sub(p, target_display, content)

            if content != original_content:
                try:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print(f"Replaced numbers in: {filepath}")
                except Exception as e:
                    print(f"Failed to write {filepath}: {e}")

print("Phone number replacement complete.")
