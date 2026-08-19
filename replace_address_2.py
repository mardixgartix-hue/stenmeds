import os
import re

dir_path = r"c:\Users\RUDRANSH\OneDrive\Desktop\stenmeds"

new_address_inline = "Kh No 1301, Shri Ram Complex, Modinagar, Uttar Pradesh 201204"

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

            # Replace any span following a location dot icon
            # Example: <i class="fa-solid fa-location-dot" aria-hidden="true"></i>\n          <span>...</span>
            content = re.sub(
                r'(<i class="fa-solid fa-location-dot" aria-hidden="true"></i>\s*<span.*?>).*?(</span>)',
                fr'\g<1>{new_address_inline}\g<2>',
                content,
                flags=re.IGNORECASE | re.DOTALL
            )
            
            # Also catch any remaining <span>Kh No 1301, Shri Ram Complex,<br>Modinagar, Uttar Pradesh 201204,</span>
            content = re.sub(
                r'Kh No 1301, Shri Ram Complex,\s*<br>\s*Modinagar, Uttar Pradesh 201204,',
                new_address_inline,
                content,
                flags=re.IGNORECASE | re.DOTALL
            )

            if content != original_content:
                try:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print(f"Replaced address in: {filepath}")
                except Exception as e:
                    print(f"Failed to write {filepath}: {e}")

print("Address replacement sweep 2 complete.")
