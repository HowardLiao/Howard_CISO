import re

target_file = "/Users/howardliao/Desktop/Howard/Howard_CISO/index.html"

with open(target_file, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Remove the floating status badge under the photo
# Find `<div class="absolute -bottom-3 inset-x-0 flex justify-center">...</div>`
html = re.sub(
    r'<div class="absolute -bottom-3 inset-x-0 flex justify-center">.*?</div>\s*</div>',
    '</div>',
    html,
    flags=re.DOTALL
)

# 2. Update DATA objects to remove any "status" fields if present
html = re.sub(r'status:\s*"[^"]*",?\s*', '', html)

# 3. Update the JavaScript rendering for Profile paragraphs, Competencies, Experience, and Pillars

# Profile paragraphs icons
profile_icons_js = """
      // Profile Paragraphs with Distinct Small Icons (No numbers)
      const profileBulletIcons = [
        '<svg class="w-4 h-4 text-cyan-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"></path></svg>',
        '<svg class="w-4 h-4 text-indigo-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 7a2 2 0 012 2m4 0a6 6 0 01-7.743 5.743L11 17H9v2H7v2H4a1 1 0 01-1-1v-2.586a1 1 0 01.293-.707l5.964-5.964A6 6 0 1121 9z"></path></svg>',
        '<svg class="w-4 h-4 text-emerald-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>',
        '<svg class="w-4 h-4 text-amber-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"></path></svg>',
        '<svg class="w-4 h-4 text-purple-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"></path></svg>'
      ];

      const pContainer = document.getElementById('profile-paragraphs');
      pContainer.innerHTML = d.profile.paragraphs.map((p, idx) => `
        <div class="flex items-start gap-3.5 p-3 rounded-2xl bg-slate-900/40 border border-slate-800/60 hover:border-cyan-500/30 transition-colors">
          <div class="w-7 h-7 rounded-xl bg-slate-900 border border-slate-800 flex items-center justify-center flex-shrink-0 mt-0.5 shadow-sm">
            ${profileBulletIcons[idx % profileBulletIcons.length]}
          </div>
          <p class="text-slate-300 leading-relaxed text-sm sm:text-base">${p}</p>
        </div>
      `).join('');
"""

# Replace Profile Paragraphs rendering block
html = re.sub(
    r'// Update Profile Paragraphs with Icons.*?pContainer\.innerHTML = d\.profile\.paragraphs\.map\(.*?\)\.join\(\'\'\);',
    profile_icons_js.strip(),
    html,
    flags=re.DOTALL
)

# Competencies: Remove `#0${idx+1} Domain` and replace with pure small icon tag
html = html.replace(
    '<span class="text-cyan-400 text-xs font-mono font-bold">#0${idx+1} Domain</span>',
    '<span class="text-cyan-400 text-xs font-semibold flex items-center gap-1"><svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg> Core Domain</span>'
)

# Experience: Remove `Milestone 0${idx+1}` and replace with pure small icon badge
html = html.replace(
    '<span class="w-1.5 h-1.5 rounded-full bg-cyan-400 animate-ping"></span>\n                  Milestone 0${idx+1}',
    '<svg class="w-3.5 h-3.5 text-cyan-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 13.255A23.931 23.931 0 0112 15c-3.183 0-6.22-.62-9-1.745M16 6V4a2 2 0 00-2-2H-4a2 2 0 00-2 2v2m4 6h.01M5 20h14a2 2 0 002-2V8a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path></svg> Leadership Milestone'
)

with open(target_file, "w", encoding="utf-8") as f:
    f.write(html)

print("Updated index.html: removed 隨時履新高階主管 and replaced all 01 02 03 markers with sleek small icons!")
