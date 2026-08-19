import os
import re

dir_path = r"c:\Users\RUDRANSH\OneDrive\Desktop\stenmeds"

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

            content = re.sub(r'info@stenmedsbiotech\.com', 'Stenmedbiotech@gmail.com', content, flags=re.IGNORECASE)
            content = re.sub(r'orders@stenmedsbiotech\.com', 'Stenmedbiotech@gmail.com', content, flags=re.IGNORECASE)

            if content != original_content:
                try:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print(f"Replaced emails in: {filepath}")
                except Exception as e:
                    print(f"Failed to write {filepath}: {e}")

print("Email replacement complete.")
