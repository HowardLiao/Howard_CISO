import re
import os

target_dir = "/Users/howardliao/Desktop/Howard/Howard_CISO"

# 1. Update index.html
index_file = os.path.join(target_dir, "index.html")
with open(index_file, "r", encoding="utf-8") as f:
    html = f.read()

# Remove the PPTX download button
pptx_btn_pattern = r'<a href="Howard_Liao_CISO_10Min_Executive_Presentation\.pptx".*?</a>\s*'
html = re.sub(pptx_btn_pattern, '', html, flags=re.DOTALL)

with open(index_file, "w", encoding="utf-8") as f:
    f.write(html)
print("Removed PPTX button from index.html")

# 2. Update sw.js if present
sw_file = os.path.join(target_dir, "sw.js")
if os.path.exists(sw_file):
    with open(sw_file, "r", encoding="utf-8") as f:
        sw = f.read()
    sw = re.sub(r"'\./Howard_Liao_CISO_10Min_Executive_Presentation\.pptx',\s*", '', sw)
    with open(sw_file, "w", encoding="utf-8") as f:
        f.write(sw)
    print("Cleaned sw.js")

# 3. Update README.md if present
readme_file = os.path.join(target_dir, "README.md")
if os.path.exists(readme_file):
    with open(readme_file, "r", encoding="utf-8") as f:
        readme = f.read()
    readme = readme.replace("10-minute executive presentation", "Executive C-Level Portfolio")
    with open(readme_file, "w", encoding="utf-8") as f:
        f.write(readme)
    print("Cleaned README.md")
