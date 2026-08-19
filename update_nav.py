import os
import re

directory = r"c:\Users\RUDRANSH\OneDrive\Desktop\stenmeds"

desktop_pattern = re.compile(
    r'<ul class="dropdown"[^>]*>.*?<li><a href="[^"]*respiratory-pulmonology\.html".*?<li class="dropdown-divider"></li>', 
    re.DOTALL
)
desktop_replacement = r'''<ul class="dropdown" role="list">
              <li><a href="/products/pediatrics.html" class="dropdown-link"><i class="fa-solid fa-baby fa-fw" aria-hidden="true"></i> Pediatrics</a></li>
              <li><a href="/products/gynecologist.html" class="dropdown-link"><i class="fa-solid fa-person-pregnant fa-fw" aria-hidden="true"></i> Gynecologist</a></li>
              <li><a href="/products/gastro.html" class="dropdown-link"><i class="fa-solid fa-pills fa-fw" aria-hidden="true"></i> Gastro</a></li>
              <li><a href="/products/physician.html" class="dropdown-link"><i class="fa-solid fa-user-doctor fa-fw" aria-hidden="true"></i> Physician</a></li>
              <li class="dropdown-divider"></li>'''

mobile_pattern = re.compile(
    r'<ul class="mobile-dropdown" id="mobile-products-dropdown">.*?<li><a href="[^"]*respiratory-pulmonology\.html".*?<li><a href="[^"]*products\.html" class="mobile-dropdown-link all-link">',
    re.DOTALL
)
mobile_replacement = r'''<ul class="mobile-dropdown" id="mobile-products-dropdown">
        <li><a href="/products/pediatrics.html" class="mobile-dropdown-link">Pediatrics</a></li>
        <li><a href="/products/gynecologist.html" class="mobile-dropdown-link">Gynecologist</a></li>
        <li><a href="/products/gastro.html" class="mobile-dropdown-link">Gastro</a></li>
        <li><a href="/products/physician.html" class="mobile-dropdown-link">Physician</a></li>
        <li><a href="/products.html" class="mobile-dropdown-link all-link">'''

footer_pattern = re.compile(
    r'<nav class="footer-links" aria-label="Product categories"><a href="[^"]*respiratory-pulmonology\.html">.*?Nutritional &amp; Energy Supplements</a></nav>',
    re.DOTALL
)
footer_replacement = r'''<nav class="footer-links" aria-label="Product categories"><a href="/products/pediatrics.html">Pediatrics</a><a href="/products/gynecologist.html">Gynecologist</a><a href="/products/gastro.html">Gastro</a><a href="/products/physician.html">Physician</a></nav>'''

footer_list_pattern = re.compile(
    r'<ul class="footer-links">\s*<li><a href="[^"]*respiratory-pulmonology\.html".*?<li><a href="[^"]*nutritional-energy-supplements\.html".*?</a></li>\s*</ul>',
    re.DOTALL
)
footer_list_replacement = r'''<ul class="footer-links">
          <li><a href="/products/pediatrics.html" class="dropdown-link"><i class="fa-solid fa-baby fa-fw" aria-hidden="true"></i> Pediatrics</a></li>
          <li><a href="/products/gynecologist.html" class="dropdown-link"><i class="fa-solid fa-person-pregnant fa-fw" aria-hidden="true"></i> Gynecologist</a></li>
          <li><a href="/products/gastro.html" class="dropdown-link"><i class="fa-solid fa-pills fa-fw" aria-hidden="true"></i> Gastro</a></li>
          <li><a href="/products/physician.html" class="dropdown-link"><i class="fa-solid fa-user-doctor fa-fw" aria-hidden="true"></i> Physician</a></li>
        </ul>'''


for root, dirs, files in os.walk(directory):
    if '.git' in root or 'node_modules' in root:
        continue
    for file in files:
        if file.endswith('.html'):
            path = os.path.join(root, file)
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            new_content = desktop_pattern.sub(desktop_replacement, content)
            new_content = mobile_pattern.sub(mobile_replacement, new_content)
            new_content = footer_pattern.sub(footer_replacement, new_content)
            new_content = footer_list_pattern.sub(footer_list_replacement, new_content)
            
            if new_content != content:
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated {path}")
