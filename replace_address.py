import os
import re

dir_path = r"c:\Users\RUDRANSH\OneDrive\Desktop\stenmeds"

new_address_inline = "Kh No 1301, Shri Ram Complex, Modinagar, Uttar Pradesh 201204"
new_address_br = "Kh No 1301, Shri Ram Complex,<br>\n          Modinagar,<br>\n          Uttar Pradesh 201204"
new_address_map = "Kh+No+1301,+Shri+Ram+Complex,+Modinagar,+Uttar+Pradesh+201204"

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

            # Replace standard inline variations
            content = re.sub(r'Greater Noida, Gautam Buddha Nagar, Uttar Pradesh', new_address_inline, content, flags=re.IGNORECASE)
            content = re.sub(r'42, Pharma Hub, Phase II, Bengaluru [—-] 560058', new_address_inline, content, flags=re.IGNORECASE)
            content = re.sub(r'42, Pharma Hub, Phase II, Bengaluru — 560058', new_address_inline, content, flags=re.IGNORECASE)
            content = re.sub(r'Greater Noida,\s*<br>\s*Gautam Buddha Nagar,.*Uttar Pradesh', new_address_br, content, flags=re.IGNORECASE | re.DOTALL)
            
            # For footers that might still say the bengaluru address
            content = re.sub(r'<span>Greater Noida, Gautam Buddha Nagar, Uttar Pradesh</span>', f'<span>{new_address_inline}</span>', content)

            # Map embed link in contact.html
            content = re.sub(r'q=Greater\+Noida,\+Gautam\+Buddha\+Nagar,\+Uttar\+Pradesh', f'q={new_address_map}', content)

            if content != original_content:
                try:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print(f"Replaced address in: {filepath}")
                except Exception as e:
                    print(f"Failed to write {filepath}: {e}")

print("Address replacement complete.")
