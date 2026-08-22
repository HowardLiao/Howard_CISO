import re

target_file = "/Users/howardliao/Desktop/Howard/Howard_CISO/index.html"

with open(target_file, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Add root font scaling in style
style_scale = """
    html {
      font-size: 18px;
    }
    @media (min-width: 640px) {
      html {
        font-size: 19px;
      }
    }
    body {
      font-family: 'Plus Jakarta Sans', 'Noto Sans TC', 'Noto Sans JP', sans-serif;
      font-size: 1rem;
      line-height: 1.6;
    }
"""

html = html.replace("body {\n      font-family: 'Plus Jakarta Sans', 'Noto Sans TC', 'Noto Sans JP', sans-serif;\n    }", style_scale.strip())

# 2. Update JavaScript rendering templates to use enlarged text classes
# Replace profile rendering
html = html.replace(
    'pContainer.innerHTML = d.profile.paragraphs.map((p, idx) => `\n        <div class="flex items-start gap-3.5 p-3 rounded-2xl bg-slate-900/40 border border-slate-800/60 hover:border-cyan-500/30 transition-colors">\n          <div class="w-7 h-7 rounded-xl bg-slate-900 border border-slate-800 flex items-center justify-center flex-shrink-0 mt-0.5 shadow-sm">\n            ${profileBulletIcons[idx % profileBulletIcons.length]}\n          </div>\n          <p class="text-slate-300 leading-relaxed text-sm sm:text-base">${p}</p>\n        </div>\n      `).join(\'\');',
    'pContainer.innerHTML = d.profile.paragraphs.map((p, idx) => `\n        <div class="flex items-start gap-4 p-4 rounded-2xl bg-slate-900/50 border border-slate-800/80 hover:border-cyan-500/40 transition-colors shadow-sm">\n          <div class="w-9 h-9 rounded-xl bg-slate-900 border border-slate-700/80 flex items-center justify-center flex-shrink-0 mt-1 shadow-md">\n            ${profileBulletIcons[idx % profileBulletIcons.length]}\n          </div>\n          <p class="text-slate-200 leading-relaxed text-base sm:text-lg">${p}</p>\n        </div>\n      `).join(\'\');'
)

# Replace value pillars rendering
html = html.replace(
    '<h4 class="font-bold text-white text-sm sm:text-base group-hover:text-cyan-400 transition-colors">${item.title}</h4>',
    '<h4 class="font-bold text-white text-base sm:text-lg group-hover:text-cyan-400 transition-colors">${item.title}</h4>'
)
html = html.replace(
    '<p class="text-xs sm:text-sm text-slate-300 leading-relaxed pl-1">${item.desc}</p>',
    '<p class="text-sm sm:text-base text-slate-300 leading-relaxed pl-1">${item.desc}</p>'
)

# Replace competencies rendering
html = html.replace(
    '<h3 class="font-bold text-white text-sm sm:text-base group-hover:text-cyan-400 transition-colors">${dom.title}</h3>',
    '<h3 class="font-bold text-white text-base sm:text-lg group-hover:text-cyan-400 transition-colors">${dom.title}</h3>'
)
html = html.replace(
    '<ul class="space-y-2 text-xs sm:text-sm text-slate-300">',
    '<ul class="space-y-2.5 text-sm sm:text-base text-slate-300 leading-relaxed">'
)

# Replace experience rendering
html = html.replace(
    '<h3 class="text-lg sm:text-xl font-extrabold text-white group-hover:text-cyan-400 transition-colors">${exp.role}</h3>',
    '<h3 class="text-xl sm:text-2xl font-extrabold text-white group-hover:text-cyan-400 transition-colors">${exp.role}</h3>'
)
html = html.replace(
    '<p class="text-xs sm:text-sm font-semibold text-slate-400 mt-0.5">${exp.groupNote || \'\'}</p>',
    '<p class="text-sm sm:text-base font-semibold text-slate-400 mt-1">${exp.groupNote || \'\'}</p>'
)
html = html.replace(
    '<p class="text-xs sm:text-sm text-cyan-300/90 font-medium mt-0.5">${exp.company}</p>',
    '<p class="text-sm sm:text-base text-cyan-300/90 font-medium mt-1">${exp.company}</p>'
)
html = html.replace(
    '<p class="text-sm text-slate-200 italic leading-relaxed pl-1">${exp.desc}</p>',
    '<p class="text-base sm:text-lg text-slate-200 italic leading-relaxed pl-1">${exp.desc}</p>'
)
html = html.replace(
    '<ul class="space-y-1.5 text-xs sm:text-sm text-slate-300">',
    '<ul class="space-y-2 text-sm sm:text-base text-slate-300 leading-relaxed">'
)

# Replace certs & edu rendering
html = html.replace(
    '<span class="font-medium text-slate-200 text-xs sm:text-sm">${c}</span>',
    '<span class="font-medium text-slate-200 text-sm sm:text-base">${c}</span>'
)
html = html.replace(
    '<h4 class="font-bold text-white text-sm sm:text-base">${e.degree}</h4>',
    '<h4 class="font-bold text-white text-base sm:text-lg">${e.degree}</h4>'
)
html = html.replace(
    '<p class="text-xs font-semibold text-slate-400 pl-9">${e.school}</p>',
    '<p class="text-sm sm:text-base font-semibold text-slate-400 pl-9">${e.school}</p>'
)
html = html.replace(
    '<p class="text-xs text-slate-300 leading-relaxed pl-9">${e.desc}</p>',
    '<p class="text-sm sm:text-base text-slate-300 leading-relaxed pl-9">${e.desc}</p>'
)

# Replace speaking rendering
html = html.replace(
    '<h4 class="font-bold text-white text-base leading-snug group-hover:text-cyan-400 transition-colors flex items-start gap-2">',
    '<h4 class="font-bold text-white text-lg sm:text-xl leading-snug group-hover:text-cyan-400 transition-colors flex items-start gap-2">'
)
html = html.replace(
    '<p class="text-xs font-semibold text-slate-300 mt-1">${item.topic}</p>',
    '<p class="text-sm sm:text-base font-semibold text-slate-300 mt-1">${item.topic}</p>'
)
html = html.replace(
    '<p class="text-xs text-slate-400 leading-relaxed">${item.desc}</p>',
    '<p class="text-sm sm:text-base text-slate-300 leading-relaxed">${item.desc}</p>'
)

with open(target_file, "w", encoding="utf-8") as f:
    f.write(html)

print("Webpage typography substantially enlarged (1.5x scale) with enhanced readability across all sections!")
