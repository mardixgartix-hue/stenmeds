import os
import re

dir_path = r"c:\Users\RUDRANSH\OneDrive\Desktop\stenmeds"

replacement_html = '''    <div class="social-icons">
      <a href="https://wa.me/917417350021" target="_blank" rel="noopener noreferrer" aria-label="Chat with us on WhatsApp"><i class="fa-brands fa-whatsapp" aria-hidden="true" style="font-size: 1.25rem;"></i></a>
    </div>'''

footer_replacement_html = '''        <div class="social-icons" style="margin-top:var(--spacing-md)">
          <a href="https://wa.me/917417350021" target="_blank" rel="noopener noreferrer" aria-label="Chat with us on WhatsApp"><i class="fa-brands fa-whatsapp" aria-hidden="true" style="font-size: 1.25rem;"></i></a>
        </div>'''

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

            # Replace topbar social icons
            content = re.sub(
                r'<div class="social-icons">\s*<a href="https://facebook\.com/".*?<i class="fa-brands fa-x-twitter".*?</a>\s*</div>',
                replacement_html,
                content,
                flags=re.DOTALL
            )
            
            # Replace footer social icons
            content = re.sub(
                r'<div class="social-icons"[^>]*>\s*<a href="https://facebook\.com/".*?<i class="fa-brands fa-x-twitter".*?</a>\s*</div>',
                footer_replacement_html,
                content,
                flags=re.DOTALL
            )

            try:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Processed: {filepath}")
            except Exception as e:
                print(f"Failed to write {filepath}: {e}")

print("Social links replaced.")
