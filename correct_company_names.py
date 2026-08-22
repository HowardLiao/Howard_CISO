import re
import os

target_dir = "/Users/howardliao/Desktop/Howard/Howard_CISO"

# 1. Update index.html
index_path = os.path.join(target_dir, "index.html")
with open(index_path, "r", encoding="utf-8") as f:
    html = f.read()

# Fix Chinese
html = html.replace("光南集團 / 峰晨集團 – 艾居電腦 (總部在台中，並在台北、深圳、上海、張家港設有據點 / 光南集團)", "光男集團 / 峰晨集團 – 艾鉅電腦 (總部在台中，並在台北、深圳、上海、張家港設有據點)")
html = html.replace("光南集團 / 峰晨集團 – 艾居電腦 (總部在台中，並在台北、深圳、上海、張家港都設有據點 / 光南集團)", "光男集團 / 峰晨集團 – 艾鉅電腦 (總部在台中，並在台北、深圳、上海、張家港都設有據點)")
html = html.replace("光南集團 / 峰晨集團 – 艾居電腦", "光男集團 / 峰晨集團 – 艾鉅電腦")
html = html.replace("光南集團", "光男集團")
html = html.replace("光南", "光男")
html = html.replace("艾居電腦", "艾鉅電腦")
html = html.replace("艾居", "艾鉅")

# Fix English duplicate
html = html.replace("Kuang Nan Group / Fengchen Group – Aiju Computer (Headquartered in Taichung with offices in Taipei, Shenzhen, Shanghai, Zhangjiagang / 光南集團)", "Kuang Nan Group / Fengchen Group – Aiju Computer (Headquartered in Taichung with offices in Taipei, Shenzhen, Shanghai, Zhangjiagang)")
html = html.replace("Kuang Nan Group / Fengchen Group – Aiju Computer (Headquartered in Taichung with offices in Taipei, Shenzhen, Shanghai, Zhangjiagang / 光男集團)", "Kuang Nan Group / Fengchen Group – Aiju Computer (Headquartered in Taichung with offices in Taipei, Shenzhen, Shanghai, Zhangjiagang)")

# Fix Japanese duplicate
html = html.replace("Kuang Nan Group / Fengchen Group – Aiju Computer (台中本社、台北・深セン・上海・張家港拠点 / 光南集團)", "Kuang Nan Group / Fengchen Group – Aiju Computer (光男集團 / 峰晨集團 – 艾鉅電腦 / 台中本社、台北・深セン・上海・張家港拠点)")
html = html.replace("Kuang Nan Group / Fengchen Group – Aiju Computer (台中本社、台北・深セン・上海・張家港拠点 / 光男集團)", "Kuang Nan Group / Fengchen Group – Aiju Computer (光男集團 / 峰晨集團 – 艾鉅電腦 / 台中本社、台北・深セン・上海・張家港拠点)")

with open(index_path, "w", encoding="utf-8") as f:
    f.write(html)
print("Updated index.html company names successfully!")

# 2. Update restore_standard_docx.py and rebuild docx
docx_script = os.path.join(target_dir, "restore_standard_docx.py")
with open(docx_script, "r", encoding="utf-8") as f:
    code = f.read()

code = code.replace("光南集團 / 峰晨集團 – 艾居電腦 (總部在台中，並在台北、深圳、上海、張家港設有據點 / 光南集團)", "光男集團 / 峰晨集團 – 艾鉅電腦 (總部在台中，並在台北、深圳、上海、張家港都設有據點)")
code = code.replace("光南集團 / 峰晨集團 – 艾居電腦 (總部在台中，並在台北、深圳、上海、張家港都設有據點 / 光南集團)", "光男集團 / 峰晨集團 – 艾鉅電腦 (總部在台中，並在台北、深圳、上海、張家港都設有據點)")
code = code.replace("光南集團 / 峰晨集團 – 艾居電腦", "光男集團 / 峰晨集團 – 艾鉅電腦")
code = code.replace("光南集團", "光男集團")
code = code.replace("光南", "光男")
code = code.replace("艾居電腦", "艾鉅電腦")
code = code.replace("艾居", "艾鉅")
code = code.replace("/ 光男集團", "")
code = code.replace("/ 光南集團", "")

with open(docx_script, "w", encoding="utf-8") as f:
    f.write(code)

# 3. Update build_all_resumes.py
bar_script = os.path.join(target_dir, "build_all_resumes.py")
if os.path.exists(bar_script):
    with open(bar_script, "r", encoding="utf-8") as f:
        c = f.read()
    c = c.replace("光南集團 / 峰晨集團 – 艾居電腦 (總部在台中，並在台北、深圳、上海、張家港設有據點 / 光南集團)", "光男集團 / 峰晨集團 – 艾鉅電腦 (總部在台中，並在台北、深圳、上海、張家港都設有據點)")
    c = c.replace("光南集團 / 峰晨集團 – 艾居電腦", "光男集團 / 峰晨集團 – 艾鉅電腦")
    c = c.replace("光南集團", "光男集團")
    c = c.replace("光南", "光男")
    c = c.replace("艾居電腦", "艾鉅電腦")
    c = c.replace("艾居", "艾鉅")
    c = c.replace("/ 光男集團", "")
    c = c.replace("/ 光南集團", "")
    with open(bar_script, "w", encoding="utf-8") as f:
        f.write(c)

# 4. Update generate_presentation.py
ppt_script = os.path.join(target_dir, "generate_presentation.py")
if os.path.exists(ppt_script):
    with open(ppt_script, "r", encoding="utf-8") as f:
        c = f.read()
    c = c.replace("光南集團", "光男集團")
    c = c.replace("光南", "光男")
    c = c.replace("艾居電腦", "艾鉅電腦")
    c = c.replace("艾居", "艾鉅")
    with open(ppt_script, "w", encoding="utf-8") as f:
        f.write(c)
