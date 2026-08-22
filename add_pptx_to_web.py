target_file = "/Users/howardliao/Desktop/Howard/Howard_CISO/index.html"

with open(target_file, "r", encoding="utf-8") as f:
    html = f.read()

# Add a PPTX download button into the Trilingual Resume Download Banner
old_btn_group = '<div class="flex flex-wrap items-center justify-center gap-2.5 text-xs font-semibold">'
new_btn_group = '''<div class="flex flex-wrap items-center justify-center gap-2.5 text-xs font-semibold">
          <a href="Howard_Liao_CISO_10Min_Executive_Presentation.pptx" download="Howard_Liao_CISO_10Min_Executive_Presentation.pptx" class="px-4 py-2.5 rounded-xl bg-gradient-to-r from-amber-600 to-amber-700 hover:from-amber-500 hover:to-amber-600 text-white font-bold border border-amber-500 shadow-lg transition-all flex items-center gap-2 hover:scale-105 active:scale-95">
            <span>📊</span>
            <span>10分鐘高階面試簡報 (.pptx)</span>
          </a>'''

html = html.replace(old_btn_group, new_btn_group, 1)

# Add to sw.js cache list as well
with open(target_file, "w", encoding="utf-8") as f:
    f.write(html)

print("Updated index.html with PPTX download button!")
