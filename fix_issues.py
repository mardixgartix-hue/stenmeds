import os

directory = r"c:\Users\RUDRANSH\OneDrive\Desktop\stenmeds"

footer_bad = '<h3 class="footer-heading">Categories</h3><nav class="footer-links"><a href="/products/diabetic.html">Diabetic Care</a><a href="/products/cardiac.html">Cardiac Care</a><a href="/products/gastric.html">Gastric Care</a><a href="/products/antibiotic.html">Antibiotics</a></nav>'

footer_good = '<h3 class="footer-heading">Product Categories</h3><nav class="footer-links"><a href="/products/respiratory-pulmonology.html">Respiratory &amp; Pulmonology</a><a href="/products/gastrointestinal-digestive.html">Gastrointestinal &amp; Digestive Health</a><a href="/products/hepatology-liver-care.html">Hepatology (Liver Care)</a><a href="/products/bone-health-minerals.html">Bone Health &amp; Mineral Supplements</a><a href="/products/pediatric-care.html">Pediatric Care / Pain &amp; Fever Relief</a><a href="/products/critical-care-injectables.html">Critical Care / Injectables</a><a href="/products/nutritional-energy-supplements.html">Nutritional &amp; Energy Supplements</a></nav>'

for root, dirs, files in os.walk(directory):
    if '.git' in root or 'node_modules' in root:
        continue
    for file in files:
        if file.endswith(('.html', '.xml', '.txt')):
            path = os.path.join(root, file)
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            new_content = content.replace('YOUR_DOMAIN.com', 'www.stenmedbiotech.com')
            new_content = new_content.replace(footer_bad, footer_good)
            
            if new_content != content:
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated {path}")
