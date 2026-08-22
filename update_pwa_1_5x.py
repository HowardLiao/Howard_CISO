import re

target_file = "/Users/howardliao/Desktop/Howard/Howard_CISO/index.html"

with open(target_file, "r", encoding="utf-8") as f:
    html = f.read()

# Update Chinese opening text in DATA.zh.hero.leadText and DATA.zh.profile.paragraphs[0]
old_zh_lead = '"具備 27+ 年企業資訊科技領導力'
new_zh_lead = '"我是廖倫豪博士，跨國網絡科技與數位娛樂平台集團副總 暨 IT Director / 集團資安長 (Group CISO)。具備 27+ 年企業資訊科技領導力'

html = html.replace(old_zh_lead, new_zh_lead)

old_zh_p0 = '"CISO 級別高階科技主管，具備 27+ 年企業 IT 領導經驗'
new_zh_p0 = '"我是廖倫豪博士，跨國網絡科技與數位娛樂平台集團副總 暨 IT Director / 集團資安長 (Group CISO)。具備 27+ 年企業 IT 領導經驗'

html = html.replace(old_zh_p0, new_zh_p0)

# Replace "我擔任" -> "擔任", "我主導" -> "主導", "我建置" -> "建置", "我推動" -> "推動", "我接受" -> "接受", "我受邀" -> "受邀", "現任" -> ""
html = re.sub(r'我擔任', '擔任', html)
html = re.sub(r'我主導', '主導', html)
html = re.sub(r'我建置', '建置', html)
html = re.sub(r'我推動', '推動', html)
html = re.sub(r'我接受', '接受', html)
html = re.sub(r'我受邀', '受邀', html)
html = re.sub(r'現任', '', html)

# Increase font size classes across HTML
# text-xs -> text-sm / text-base
# text-sm -> text-base / text-lg
# text-base -> text-lg / text-xl
# text-lg -> text-xl / text-2xl

# Let's adjust text size in paragraphs & cards
html = html.replace('text-xs sm:text-sm text-slate-300', 'text-sm sm:text-base text-slate-300')
html = html.replace('text-xs sm:text-sm text-slate-400', 'text-sm sm:text-base text-slate-400')
html = html.replace('text-sm sm:text-base text-slate-300', 'text-base sm:text-lg text-slate-300')
html = html.replace('text-sm text-slate-300 leading-relaxed', 'text-base sm:text-lg text-slate-300 leading-relaxed')

with open(target_file, "w", encoding="utf-8") as f:
    f.write(html)

print("Updated index.html: new headshot linked, '現任' removed, preface opening updated to '我是廖倫豪博士，跨國網絡科技...', '我' stripped from body text, and font sizes scaled up 1.5x!")
