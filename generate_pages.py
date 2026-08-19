import os
import re

# Image mapping: product name -> image filename
IMAGE_MAP = {
    "Stencuf": "stencuf.jpg",
    "Mefenik": "mefenik.jpg",
    "Stengut": "stengut.jpg",
    "Hepto B6": "hepto-b6.jpg",
    "Bacinik": "bacinik.jpg",
    "Rezenik Syrup and Drop": None,  # No image available
    "Sten Phase 500 Inj": "sten-phase-500.jpg",
    "Falroz-XT": "falroz-xt.jpg",
    "Sten DSR": "sten-dsr.jpg",
    "Calsical LC": "calsical-lc.jpg",
    "My Protine Protein Powder": "my-protine.jpg",
    "Stenzi Pro Energy Drink": "stenzi-pro.jpg",
    "Hepto B6 Syp": "hepto-b6.jpg",
    "Stenliv DS Syp": "stenliv-ds.jpg",
    "Gasomed Syp": "gasomed.jpg",
    "DOXOFER-DX": None,  # No image available
    "Stenzi Pro": "stenzi-pro.jpg",
}

categories = [
    {
        "id": "pediatrics",
        "title": "Pediatrics",
        "desc": "Specialized formulations for infants and children.",
        "icon": "fa-baby",
        "color": "#ec4899",
        "products": [
            {"name": "Stencuf", "comp": "Levosalbutamol, Ambroxol & Guaiphenesin Syrup", "use": "Cough and cold relief"},
            {"name": "Mefenik", "comp": "Paracetamol & Mefenamic Acid Suspension", "use": "Pain and fever relief"},
            {"name": "Stengut", "comp": "Prebiotic, Probiotics, Zinc Gluconate & LB Suspension", "use": "Gastrointestinal support"},
            {"name": "Hepto B6", "comp": "Silymarin, L-Ornithine L-Aspartate, Folic Acid, Co-Enzyme Q10 Syrup", "use": "Hepatoprotective liver tonic"},
            {"name": "Bacinik", "comp": "Bacillus Clausii Spores Suspension", "use": "Probiotic oral suspension"},
            {"name": "Rezenik Syrup and Drop", "comp": "Pediatric formulation", "use": "Anti-allergic / Nutritional"}
        ]
    },
    {
        "id": "gynecologist",
        "title": "Gynecologist",
        "desc": "Complete women's health products.",
        "icon": "fa-person-pregnant",
        "color": "#a855f7",
        "products": [
            {"name": "Sten Phase 500 Inj", "comp": "Hydroxyprogesterone Caproate Injection I.P.", "use": "Hormonal injection for women's health"},
            {"name": "Falroz-XT", "comp": "Ferrous Ascorbate, Folic Acid & Zinc Tablets", "use": "Iron deficiency anemia"},
            {"name": "Sten DSR", "comp": "Pantoprazole Sodium & Domperidone Prolonged-release Capsules IP", "use": "Acid reflux & morning sickness"},
            {"name": "Calsical LC", "comp": "Calcium Citrate, L-Carnitine, Vitamin E, Zinc Sulphate & Folic Acid Tablets", "use": "Bone health & nutrition"},
            {"name": "My Protine Protein Powder", "comp": "Protein Powder with DHA (Sugar Free)", "use": "Maternal health and vitality"},
            {"name": "Stenzi Pro Energy Drink", "comp": "Dextrose, Sucrose, Vitamin C, D3, Zinc & Electrolyte Powder", "use": "Energy & electrolyte replacement"}
        ]
    },
    {
        "id": "gastro",
        "title": "Gastro",
        "desc": "Digestive health and liver care syrups.",
        "icon": "fa-pills",
        "color": "#0d9488",
        "products": [
            {"name": "Hepto B6 Syp", "comp": "Silymarin, L-Ornithine L-Aspartate, Folic Acid, Co-Enzyme Q10 Syrup", "use": "Hepatoprotective liver tonic"},
            {"name": "Stenliv DS Syp", "comp": "Double-strength liver syrup", "use": "Fatty liver, liver disorder, improve digestion"},
            {"name": "Sten DSR", "comp": "Pantoprazole Sodium & Domperidone Prolonged-release Capsules IP", "use": "GERD and acidity"},
            {"name": "Gasomed Syp", "comp": "Antacid suspension", "use": "Quick relief from acidity & gas"}
        ]
    },
    {
        "id": "physician",
        "title": "Physician",
        "desc": "General physician prescriptions.",
        "icon": "fa-user-doctor",
        "color": "#0284c7",
        "products": [
            {"name": "Hepto B6", "comp": "Silymarin, L-Ornithine L-Aspartate, Folic Acid, Co-Enzyme Q10 Syrup", "use": "General liver support"},
            {"name": "DOXOFER-DX", "comp": "Doxofylline Tablets", "use": "Asthma and bronchitis"},
            {"name": "Sten DSR", "comp": "Pantoprazole Sodium & Domperidone Prolonged-release Capsules IP", "use": "Acidity and indigestion"},
            {"name": "Gasomed Syp", "comp": "Antacid suspension", "use": "Antacid & anti-flatulent"},
            {"name": "Stenzi Pro", "comp": "Dextrose, Sucrose, Vitamin C, D3, Zinc & Electrolyte Powder", "use": "Instant energy & electrolytes"},
            {"name": "Calsical LC", "comp": "Calcium Citrate, L-Carnitine, Vitamin E, Zinc Sulphate & Folic Acid Tablets", "use": "Calcium supplementation"},
            {"name": "My Protine Protein Powder", "comp": "Protein Powder with DHA (Sugar Free)", "use": "General wellness"}
        ]
    }
]

# Use the existing pediatrics.html as template (it was already generated with the new nav)
template_path = r"c:\Users\RUDRANSH\OneDrive\Desktop\stenmeds\products\pediatrics.html"
with open(template_path, 'r', encoding='utf-8') as f:
    template = f.read()

# Fix: strip out the admin script block at the bottom
template = re.sub(r'<!-- Admin-added products loader.*?</script>', '', template, flags=re.DOTALL)

# Generate the shared sidebar HTML
sidebar_html = '<aside class="category-sidebar" aria-label="Product categories">\n  <div class="sidebar-heading">All Categories</div>\n  <nav aria-label="Product category navigation">\n'
for cat in categories:
    sidebar_html += f'    <a href="{cat["id"]}.html" class="sidebar-link"><i class="fa-solid {cat["icon"]} fa-fw" aria-hidden="true" style="color:{cat["color"]}"></i> {cat["title"]}</a>\n'
sidebar_html += '    <div style="border-top:1px solid var(--color-border);margin:var(--spacing-sm) 0"></div>\n    <a href="/products.html" class="sidebar-link" style="color:var(--color-primary);font-weight:600"><i class="fa-solid fa-arrow-right fa-fw" aria-hidden="true"></i> All Products</a>\n  </nav>\n</aside>'

# Replace the sidebar in template
template = re.sub(
    r'<aside class="category-sidebar"[^>]*>.*?</aside>',
    sidebar_html,
    template,
    flags=re.DOTALL
)

for cat in categories:
    page_content = template

    # Active sidebar link
    page_content = page_content.replace(f'href="{cat["id"]}.html" class="sidebar-link"', f'href="{cat["id"]}.html" class="sidebar-link active"')

    # Title & Meta
    page_content = re.sub(r'<title>.*?</title>', f'<title>{cat["title"]} — STENMEDS BIOTECH</title>', page_content)
    page_content = re.sub(r'<meta name="description" content=".*?">', f'<meta name="description" content="{cat["desc"]}">', page_content)

    # Banner
    page_content = re.sub(
        r'<h1 class="page-banner-title">.*?</h1>',
        f'<h1 class="page-banner-title"><i class="fa-solid {cat["icon"]} fa-fw" aria-hidden="true" style="color:{cat["color"]}"></i> {cat["title"]}</h1>',
        page_content
    )
    page_content = re.sub(
        r'<span aria-current="page">.*?</span>',
        f'<span aria-current="page">{cat["title"]}</span>',
        page_content
    )

    # Category search placeholder
    page_content = re.sub(
        r'id="category-search" class="filter-search" placeholder=".*?"',
        f'id="category-search" class="filter-search" placeholder="Search {cat["title"].lower()} products…"',
        page_content
    )

    # Products count
    product_count_text = f"{len(cat['products'])} products" if len(cat['products']) > 1 else "1 product"
    page_content = re.sub(
        r'<span class="products-count" id="products-count" aria-live="polite">.*?</span>',
        f'<span class="products-count" id="products-count" aria-live="polite">{product_count_text}</span>',
        page_content
    )

    # Generate products HTML
    products_html = f'<div class="products-grid" id="products-grid" aria-label="{cat["title"]} products">\n'
    for product in cat['products']:
        img_file = IMAGE_MAP.get(product['name'])
        if img_file:
            img_html = f'''<div class="product-img-wrap" style="background:#fff;border-bottom:1px solid var(--color-border);">
              <img src="/assets/images/products/{img_file}" alt="{product['name']}" style="width:100%;height:220px;object-fit:contain;padding:12px;background:#fff;">
            </div>'''
        else:
            img_html = f'''<div class="product-img-wrap" style="background:#fff;border-bottom:1px solid var(--color-border);display:flex;align-items:center;justify-content:center;height:220px;">
              <i class="fa-solid fa-pills" style="font-size:48px;color:#cbd5e1"></i>
            </div>'''

        products_html += f'''
          <article class="product-card" data-name="{product['name']}">
            {img_html}
            <div class="product-card-body">
              <span class="badge badge-rx product-card-form">Rx — {cat['title']}</span>
              <h2 class="product-card-name">{product['name']}</h2>
              <div class="product-composition">
                <i class="fa-solid fa-flask-vial fa-fw" aria-hidden="true"></i>
                <span><strong>Composition:</strong> {product['comp']}</span>
              </div>
              <div class="product-uses">
                <i class="fa-solid fa-kit-medical fa-fw" aria-hidden="true"></i>
                <span><strong>Indication:</strong> {product['use']}</span>
              </div>
              <div class="product-card-footer">
                <a href="/contact.html" class="btn btn-primary btn-sm product-inquire-btn" data-product="{product['name']}">
                  <i class="fa-solid fa-paper-plane" aria-hidden="true"></i> Inquire Now
                </a>
              </div>
            </div>
          </article>'''
    products_html += '\n</div>'

    # Replace products grid
    page_content = re.sub(
        r'<div class="products-grid" id="products-grid".*?>.*?</div>\s*</div>\s*</div>',
        products_html + '\n      </div>\n    </div>',
        page_content,
        flags=re.DOTALL
    )

    # Save the file
    out_path = os.path.join(r"c:\Users\RUDRANSH\OneDrive\Desktop\stenmeds\products", f"{cat['id']}.html")
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(page_content)
    print(f"Generated {out_path}")

print("\nAll pages generated with product images!")
