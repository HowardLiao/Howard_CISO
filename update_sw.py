target_file = "/Users/howardliao/Desktop/Howard/Howard_CISO/sw.js"

with open(target_file, "r", encoding="utf-8") as f:
    sw = f.read()

sw = sw.replace(
    "'./Howard_Liao_CISO_Resume.docx',",
    "'./Howard_Liao_CISO_Resume.docx',\n  './Howard_Liao_CISO_Resume_EN.docx',\n  './Howard_Liao_CISO_Resume_ZH.docx',\n  './Howard_Liao_CISO_Resume_JA.docx',"
)

with open(target_file, "w", encoding="utf-8") as f:
    f.write(sw)

print("Updated sw.js with all 3 trilingual docx files!")
