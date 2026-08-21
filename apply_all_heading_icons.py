import re

file_path = "/Users/howardliao/Desktop/Howard/Howard_CISO/index.html"

with open(file_path, "r", encoding="utf-8") as f:
    html = f.read()

# Let's define the icon mapping for Value Pillars, Competency Domains, Experience, Certs, Edu, Speaking
# Update the JS render functions inside index.html

new_render_js = """
      // Update Profile Paragraphs
      const pContainer = document.getElementById('profile-paragraphs');
      pContainer.innerHTML = d.profile.paragraphs.map((p, idx) => `
        <div class="flex items-start gap-3">
          <div class="w-6 h-6 rounded-lg bg-cyan-500/10 flex items-center justify-center text-cyan-400 text-xs font-bold font-mono flex-shrink-0 mt-0.5">
            0${idx+1}
          </div>
          <p class="text-slate-300 leading-relaxed">${p}</p>
        </div>
      `).join('');

      // Pillar Icons Mapping
      const pillarIcons = [
        '<svg class="w-4 h-4 text-cyan-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"></path></svg>',
        '<svg class="w-4 h-4 text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 12a9 9 0 01-9 9m9-9a9 9 0 00-9-9m9 9H3m9 9a9 9 0 01-9-9m9 9c1.657 0 3-4.03 3-9s-1.343-9-3-9m0 18c-1.657 0-3-4.03-3-9s1.343-9 3-9m-9 9a9 9 0 019-9"></path></svg>',
        '<svg class="w-4 h-4 text-emerald-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"></path></svg>',
        '<svg class="w-4 h-4 text-indigo-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 15a4 4 0 004 4h9a5 5 0 10-.1-9.999 5.002 5.002 0 00-9.78 2.096A4.001 4.001 0 003 15z"></path></svg>',
        '<svg class="w-4 h-4 text-purple-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg>',
        '<svg class="w-4 h-4 text-amber-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"></path></svg>'
      ];

      // Update Value Pillars with Icons
      const vContainer = document.getElementById('value-cards');
      vContainer.innerHTML = d.value.pillars.map((item, idx) => `
        <div class="glass-card rounded-2xl p-5 border border-slate-800 hover:border-cyan-500/40 transition-all flex flex-col justify-between group hover:-translate-y-1">
          <div class="space-y-2.5">
            <div class="flex items-center gap-2.5">
              <div class="w-8 h-8 rounded-xl bg-slate-900 border border-slate-800 flex items-center justify-center flex-shrink-0 group-hover:scale-110 transition-transform">
                ${pillarIcons[idx % pillarIcons.length]}
              </div>
              <h4 class="font-bold text-white text-sm sm:text-base group-hover:text-cyan-400 transition-colors">${item.title}</h4>
            </div>
            <p class="text-xs sm:text-sm text-slate-300 leading-relaxed pl-1">${item.desc}</p>
          </div>
        </div>
      `).join('');

      // Competency Domain Icons Mapping (8 Domains)
      const domainIcons = [
        '<svg class="w-4 h-4 text-cyan-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"></path></svg>',
        '<svg class="w-4 h-4 text-emerald-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 7v10c0 2 1.5 3 3.5 3h9c2 0 3.5-1 3.5-3V7c0-2-1.5-3-3.5-3h-9C5.5 4 4 5 4 7zM9 12h6M9 16h4"></path></svg>',
        '<svg class="w-4 h-4 text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 7a2 2 0 012 2m4 0a6 6 0 01-7.743 5.743L11 17H9v2H7v2H4a1 1 0 01-1-1v-2.586a1 1 0 01.293-.707l5.964-5.964A6 6 0 1121 9z"></path></svg>',
        '<svg class="w-4 h-4 text-indigo-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 15a4 4 0 004 4h9a5 5 0 10-.1-9.999 5.002 5.002 0 00-9.78 2.096A4.001 4.001 0 003 15z"></path></svg>',
        '<svg class="w-4 h-4 text-rose-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"></path></svg>',
        '<svg class="w-4 h-4 text-amber-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 20l4-16m4 4l4 4-4 4M6 16l-4-4 4-4"></path></svg>',
        '<svg class="w-4 h-4 text-purple-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg>',
        '<svg class="w-4 h-4 text-teal-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z"></path></svg>'
      ];

      // Update Competencies with Icons
      const cContainer = document.getElementById('competency-domains');
      cContainer.innerHTML = d.comp.domains.map((dom, idx) => `
        <div class="glass-card rounded-2xl p-6 border border-slate-800 hover:border-blue-500/40 transition-all space-y-3.5 group">
          <div class="flex items-center gap-3 border-b border-slate-800 pb-3">
            <div class="w-8 h-8 rounded-xl bg-slate-900 border border-slate-800 flex items-center justify-center flex-shrink-0 group-hover:scale-110 transition-transform">
              ${domainIcons[idx % domainIcons.length]}
            </div>
            <div class="flex-1">
              <span class="text-cyan-400 text-xs font-mono font-bold">#0${idx+1} Domain</span>
              <h3 class="font-bold text-white text-sm sm:text-base group-hover:text-cyan-400 transition-colors">${dom.title}</h3>
            </div>
          </div>
          <ul class="space-y-2 text-xs sm:text-sm text-slate-300">
            ${dom.bullets.map(b => `<li class="flex items-start gap-2"><span class="text-cyan-400 mt-1 flex-shrink-0">•</span><span>${b}</span></li>`).join('')}
          </ul>
        </div>
      `).join('');

      // Experience Milestone Icons
      const expIcons = [
        '<svg class="w-5 h-5 text-amber-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 3v4M3 5h4M6 17v4m-2-2h4m5-16l2.286 6.857L21 12l-5.714 2.143L13 21l-2.286-6.857L5 12l5.714-2.143L13 3z"></path></svg>',
        '<svg class="w-5 h-5 text-cyan-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 5v2m0 4v2m0 4v2M5 5a2 2 0 00-2 2v3a2 2 0 110 4v3a2 2 0 002 2h14a2 2 0 002-2v-3a2 2 0 110-4V7a2 2 0 00-2-2H5z"></path></svg>',
        '<svg class="w-5 h-5 text-emerald-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"></path></svg>',
        '<svg class="w-5 h-5 text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 12a9 9 0 01-9 9m9-9a9 9 0 00-9-9m9 9H3m9 9a9 9 0 01-9-9m9 9c1.657 0 3-4.03 3-9s-1.343-9-3-9m0 18c-1.657 0-3-4.03-3-9s1.343-9 3-9m-9 9a9 9 0 019-9"></path></svg>',
        '<svg class="w-5 h-5 text-indigo-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 11V7a4 4 0 00-8 0v4M5 9h14l1 12H4L5 9z"></path></svg>',
        '<svg class="w-5 h-5 text-purple-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 20l4-16m4 4l4 4-4 4M6 16l-4-4 4-4"></path></svg>',
        '<svg class="w-5 h-5 text-rose-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 7v10c0 2 1.5 3 3.5 3h9c2 0 3.5-1 3.5-3V7c0-2-1.5-3-3.5-3h-9C5.5 4 4 5 4 7zM9 12h6M9 16h4"></path></svg>'
      ];

      // Update Experience with Section Icons
      const eContainer = document.getElementById('experience-list');
      eContainer.innerHTML = d.exp.items.map((exp, idx) => `
        <div class="glass-card rounded-3xl p-6 sm:p-8 border border-slate-800 hover:border-cyan-500/40 transition-all space-y-4 relative overflow-hidden group">
          <div class="flex flex-col sm:flex-row sm:items-start justify-between gap-3 border-b border-slate-800 pb-4">
            <div class="flex items-start gap-3.5">
              <div class="w-10 h-10 rounded-2xl bg-slate-900 border border-slate-800 flex items-center justify-center flex-shrink-0 group-hover:scale-110 transition-transform mt-0.5">
                ${expIcons[idx % expIcons.length]}
              </div>
              <div>
                <div class="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded-full text-xs font-semibold bg-cyan-500/10 text-cyan-400 border border-cyan-500/20 mb-1.5">
                  <span class="w-1.5 h-1.5 rounded-full bg-cyan-400 animate-ping"></span>
                  Milestone 0${idx+1}
                </div>
                <h3 class="text-lg sm:text-xl font-extrabold text-white group-hover:text-cyan-400 transition-colors">${exp.role}</h3>
                <p class="text-xs sm:text-sm font-semibold text-slate-400 mt-0.5">${exp.groupNote || ''}</p>
                <p class="text-xs sm:text-sm text-cyan-300/90 font-medium mt-0.5">${exp.company}</p>
              </div>
            </div>
            <span class="px-3.5 py-1.5 rounded-xl bg-slate-900 border border-slate-800 text-cyan-400 font-mono text-xs font-bold whitespace-nowrap self-start shadow-sm">
              ${exp.period}
            </span>
          </div>

          <p class="text-sm text-slate-200 italic leading-relaxed pl-1">${exp.desc}</p>

          ${exp.scope ? `
            <div class="space-y-2 bg-slate-900/50 p-4 rounded-2xl border border-slate-800/80">
              <h4 class="text-xs font-bold uppercase tracking-wider text-slate-300 flex items-center gap-1.5">
                <svg class="w-3.5 h-3.5 text-cyan-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg>
                <span>Leadership Scope</span>
              </h4>
              <ul class="space-y-1.5 text-xs sm:text-sm text-slate-300">
                ${exp.scope.map(s => `<li class="flex items-start gap-2"><span class="text-cyan-400 mt-0.5">▹</span><span>${s}</span></li>`).join('')}
              </ul>
            </div>
          ` : ''}

          <div class="space-y-2">
            <h4 class="text-xs font-bold uppercase tracking-wider text-cyan-400 flex items-center gap-1.5">
              <svg class="w-3.5 h-3.5 text-emerald-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
              <span>Selected Achievements & Impact</span>
            </h4>
            <ul class="space-y-1.5 text-xs sm:text-sm text-slate-300">
              ${exp.achievements.map(a => `<li class="flex items-start gap-2"><span class="text-emerald-400 font-bold mt-0.5 flex-shrink-0">✓</span><span>${a}</span></li>`).join('')}
            </ul>
          </div>

          ${exp.additionalContext ? `
            <div class="text-xs text-slate-400 bg-slate-900/30 p-3 rounded-xl border border-slate-800/50 flex items-start gap-2">
              <svg class="w-4 h-4 text-cyan-400 flex-shrink-0 mt-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
              <div><strong class="text-slate-300">Additional Context:</strong> ${exp.additionalContext}</div>
            </div>
          ` : ''}

          ${exp.leaving ? `
            <div class="text-xs text-slate-400 border-t border-slate-800/60 pt-3 flex items-center gap-2">
              <svg class="w-3.5 h-3.5 text-amber-400 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1"></path></svg>
              <div><strong class="text-slate-300">Reason for Leaving:</strong> <span class="italic">${exp.leaving}</span></div>
            </div>
          ` : ''}
        </div>
      `).join('');

      // Certifications List with Icons
      const certList = document.getElementById('cert-list');
      certList.innerHTML = d.cred.certs.map(c => `
        <li class="flex items-center gap-3 p-3 rounded-xl bg-slate-900/50 border border-slate-800 hover:border-cyan-500/40 transition-colors">
          <div class="w-7 h-7 rounded-lg bg-cyan-500/10 flex items-center justify-center text-cyan-400 flex-shrink-0">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"></path></svg>
          </div>
          <span class="font-medium text-slate-200 text-xs sm:text-sm">${c}</span>
        </li>
      `).join('');

      // Education List with Degree Icons
      const eduIcons = [
        '<svg class="w-4 h-4 text-purple-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 14l9-5-9-5-9 5 9 5z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 14l6.16-3.422a12.083 12.083 0 01.665 6.479A11.952 11.952 0 0012 20.055a11.952 11.952 0 00-6.824-2.998 12.078 12.078 0 01.665-6.479L12 14z"></path></svg>',
        '<svg class="w-4 h-4 text-indigo-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"></path></svg>',
        '<svg class="w-4 h-4 text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.75 17L9 20l-1 1h8l-1-1-.75-3M3 13h18M5 17h14a2 2 0 002-2V5a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path></svg>'
      ];

      const eduList = document.getElementById('edu-list');
      eduList.innerHTML = d.cred.edu.map((e, idx) => `
        <div class="p-4 rounded-2xl bg-slate-900/50 border border-slate-800 space-y-2 hover:border-purple-500/40 transition-colors">
          <div class="flex items-start justify-between gap-2">
            <div class="flex items-center gap-2.5">
              <div class="w-7 h-7 rounded-lg bg-slate-900 border border-slate-800 flex items-center justify-center flex-shrink-0">
                ${eduIcons[idx % eduIcons.length]}
              </div>
              <h4 class="font-bold text-white text-sm sm:text-base">${e.degree}</h4>
            </div>
            <span class="text-xs font-mono text-cyan-400 whitespace-nowrap px-2 py-0.5 rounded-md bg-cyan-500/10 border border-cyan-500/20">${e.period}</span>
          </div>
          <p class="text-xs font-semibold text-slate-400 pl-9">${e.school}</p>
          <p class="text-xs text-slate-300 leading-relaxed pl-9">${e.desc}</p>
        </div>
      `).join('');
"""

# Replace in update_local_pwa.py and rebuild
with open("/Users/howardliao/Desktop/Howard/Howard_CISO/update_local_pwa.py", "r", encoding="utf-8") as f:
    orig_script = f.read()

# Replace the render block
old_start = orig_script.find("// Update Profile Paragraphs")
old_end = orig_script.find("// Update Speaking")

if old_start != -1 and old_end != -1:
    new_script = orig_script[:old_start] + new_render_js + "\n      " + orig_script[old_end:]
    with open("/Users/howardliao/Desktop/Howard/Howard_CISO/update_local_pwa.py", "w", encoding="utf-8") as f:
        f.write(new_script)
    print("Updated update_local_pwa.py with all heading icons successfully!")
else:
    print("Could not find markers, manual check needed.")
