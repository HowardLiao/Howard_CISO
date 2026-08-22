import re

target_file = "/Users/howardliao/Desktop/Howard/Howard_CISO/index.html"

with open(target_file, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Adjust main top padding to prevent sticky header from overlapping hero
html = html.replace(
    '<main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 sm:py-12 space-y-16 relative z-10">',
    '<main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pt-10 sm:pt-14 pb-16 space-y-16 relative z-10">'
)

# 2. Adjust hero card internal padding and photo margin
# In hero card:
html = html.replace(
    '<div class="glass-card rounded-3xl p-6 sm:p-10 relative overflow-hidden border border-slate-800 shadow-2xl">',
    '<div class="glass-card rounded-3xl p-6 sm:p-12 relative overflow-hidden border border-slate-800 shadow-2xl mt-4 sm:mt-6">'
)

# Photo container margin and styling:
html = html.replace(
    '<div class="flex flex-col lg:flex-row items-center lg:items-start gap-8 sm:gap-12 relative z-10">',
    '<div class="flex flex-col lg:flex-row items-center lg:items-start gap-8 sm:gap-12 relative z-10 pt-2 sm:pt-4">'
)

# 3. Enhance Section Headings so they explicitly have colorful icon boxes and emoji icons
section_headers_map = [
    # Profile
    (
        '<span data-i18n="profile.heading">Executive Profile & Leadership Value Proposition</span>',
        '<span class="flex items-center gap-2"><span>🛡️</span><span data-i18n="profile.heading">Executive Profile & Leadership Value Proposition</span></span>'
    ),
    # Radar
    (
        '<span data-i18n="radar.heading">Security Maturity & Strategic Governance Radar</span>',
        '<span class="flex items-center gap-2"><span>📡</span><span data-i18n="radar.heading">Security Maturity & Strategic Governance Radar</span></span>'
    ),
    # Competencies
    (
        '<span data-i18n="comp.heading">Core Competencies & Technical Governance</span>',
        '<span class="flex items-center gap-2"><span>🎯</span><span data-i18n="comp.heading">Core Competencies & Technical Governance</span></span>'
    ),
    # Experience
    (
        '<span data-i18n="exp.heading">Professional Career & Leadership Experience</span>',
        '<span class="flex items-center gap-2"><span>🏢</span><span data-i18n="exp.heading">Professional Career & Leadership Experience</span></span>'
    ),
    # Credentials
    (
        '<span data-i18n="cred.heading">Professional Certifications & Academic Degrees</span>',
        '<span class="flex items-center gap-2"><span>🎓</span><span data-i18n="cred.heading">Professional Certifications & Academic Degrees</span></span>'
    ),
    # Speaking
    (
        '<span data-i18n="speak.heading">Awards, Keynotes, Publications & Speaking</span>',
        '<span class="flex items-center gap-2"><span>🎤</span><span data-i18n="speak.heading">Awards, Keynotes, Publications & Speaking</span></span>'
    ),
]

for old_h, new_h in section_headers_map:
    if old_h in html:
        html = html.replace(old_h, new_h)

# 4. Enhance Competency Domain Titles to include distinct colored icon boxes in the JavaScript renderer
# In setLang():
# Let's inspect the competency rendering block
competency_render_code = """
      // Competency Domain Icons & Colors (8 Domains)
      const domainStyles = [
        { icon: '<svg class="w-4 h-4 text-cyan-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"></path></svg>', badge: '🛡️ Strategy & Risk', color: 'border-cyan-500/40 bg-cyan-500/10 text-cyan-400' },
        { icon: '<svg class="w-4 h-4 text-emerald-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 7v10c0 2 1.5 3 3.5 3h9c2 0 3.5-1 3.5-3V7c0-2-1.5-3-3.5-3h-9C5.5 4 4 5 4 7zM9 12h6M9 16h4"></path></svg>', badge: '🔐 Trust & Audit', color: 'border-emerald-500/40 bg-emerald-500/10 text-emerald-400' },
        { icon: '<svg class="w-4 h-4 text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 7a2 2 0 012 2m4 0a6 6 0 01-7.743 5.743L11 17H9v2H7v2H4a1 1 0 01-1-1v-2.586a1 1 0 01.293-.707l5.964-5.964A6 6 0 1121 9z"></path></svg>', badge: '🆔 IAM & Zero Trust', color: 'border-blue-500/40 bg-blue-500/10 text-blue-400' },
        { icon: '<svg class="w-4 h-4 text-indigo-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 15a4 4 0 004 4h9a5 5 0 10-.1-9.999 5.002 5.002 0 00-9.78 2.096A4.001 4.001 0 003 15z"></path></svg>', badge: '☁️ Cloud & AppSec', color: 'border-indigo-500/40 bg-indigo-500/10 text-indigo-400' },
        { icon: '<svg class="w-4 h-4 text-rose-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"></path></svg>', badge: '🚨 SecOps & SIEM', color: 'border-rose-500/40 bg-rose-500/10 text-rose-400' },
        { icon: '<svg class="w-4 h-4 text-amber-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 20l4-16m4 4l4 4-4 4M6 16l-4-4 4-4"></path></svg>', badge: '⚙️ DevSecOps & CI/CD', color: 'border-amber-500/40 bg-amber-500/10 text-amber-400' },
        { icon: '<svg class="w-4 h-4 text-purple-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg>', badge: '🧠 AI Governance', color: 'border-purple-500/40 bg-purple-500/10 text-purple-400' },
        { icon: '<svg class="w-4 h-4 text-teal-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z"></path></svg>', badge: '👔 Executive Leadership', color: 'border-teal-500/40 bg-teal-500/10 text-teal-400' }
      ];

      // Update Competencies with Icons & Badges
      const cContainer = document.getElementById('competency-domains');
      cContainer.innerHTML = d.comp.domains.map((dom, idx) => {
        const style = domainStyles[idx % domainStyles.length];
        return `
        <div class="glass-card rounded-2xl p-6 border border-slate-800 hover:border-blue-500/40 transition-all space-y-3.5 group">
          <div class="flex items-center gap-3 border-b border-slate-800 pb-3">
            <div class="w-9 h-9 rounded-xl bg-slate-900 border border-slate-800 flex items-center justify-center flex-shrink-0 group-hover:scale-110 transition-transform shadow-md">
              ${style.icon}
            </div>
            <div class="flex-1">
              <div class="inline-flex items-center gap-1 px-2 py-0.5 rounded-md text-[10px] font-bold border mb-1 ${style.color}">
                <span>${style.badge}</span>
              </div>
              <h3 class="font-bold text-white text-sm sm:text-base group-hover:text-cyan-400 transition-colors">${dom.title}</h3>
            </div>
          </div>
          <ul class="space-y-2 text-xs sm:text-sm text-slate-300">
            ${dom.bullets.map(b => `<li class="flex items-start gap-2"><span class="text-cyan-400 mt-1 flex-shrink-0">🔹</span><span>${b}</span></li>`).join('')}
          </ul>
        </div>
      `;
      }).join('');
"""

# Replace the competency rendering block
html = re.sub(
    r'// Competency Domain Icons Mapping.*?cContainer\.innerHTML = d\.comp\.domains\.map\(.*?\)\.join\(\'\'\);',
    competency_render_code.strip(),
    html,
    flags=re.DOTALL
)

with open(target_file, "w", encoding="utf-8") as f:
    f.write(html)

print("Layout refined: Main padding adjusted, photo unclipped, and all section headings & competencies enriched with icons!")
