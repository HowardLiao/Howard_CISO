import re

target_file = "/Users/howardliao/Desktop/Howard/Howard_CISO/index.html"

with open(target_file, "r", encoding="utf-8") as f:
    html = f.read()

# Update navbar download button with ID
html = html.replace(
    '<a href="Howard_Liao_CISO_Resume.docx" download="Howard_Liao_CISO_Resume.docx" class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs font-semibold bg-gradient-to-r from-cyan-600 to-blue-600',
    '<a id="nav-download-btn" href="Howard_Liao_CISO_Resume_EN.docx" download="Howard_Liao_CISO_Resume_EN.docx" class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs font-semibold bg-gradient-to-r from-cyan-600 to-blue-600'
)

# Update hero action download button with ID
html = html.replace(
    '<a href="Howard_Liao_CISO_Resume.docx" download="Howard_Liao_CISO_Resume.docx" class="px-5 py-2.5 rounded-xl bg-blue-600/20 hover:bg-blue-600/30 text-blue-300 border border-blue-500/30 text-sm font-semibold transition-all flex items-center gap-2">\n                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"></path></svg>\n                📥 1-Click .DOCX\n              </a>',
    '<a id="hero-download-btn" href="Howard_Liao_CISO_Resume_EN.docx" download="Howard_Liao_CISO_Resume_EN.docx" class="px-5 py-2.5 rounded-xl bg-blue-600/20 hover:bg-blue-600/30 text-blue-300 border border-blue-500/30 text-sm font-semibold transition-all flex items-center gap-2 shadow-sm">\n                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"></path></svg>\n                <span id="hero-download-text">📥 Download English .DOCX</span>\n              </a>'
)

# Add a dedicated Trilingual Download Section right above footer or under Hero
trilingual_download_box = """
    <!-- TRILINGUAL EXECUTIVE RESUME DOWNLOAD BANNER -->
    <section class="glass-card rounded-3xl p-6 sm:p-8 border border-slate-800 relative overflow-hidden bg-gradient-to-r from-slate-900/90 via-obsidian-900/90 to-slate-900/90">
      <div class="flex flex-col lg:flex-row items-center justify-between gap-6">
        <div class="flex items-center gap-4 text-center lg:text-left">
          <div class="w-12 h-12 rounded-2xl bg-cyan-500/10 border border-cyan-500/30 flex items-center justify-center text-cyan-400 flex-shrink-0 shadow-lg">
            <svg class="w-6 h-6 animate-pulse" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"></path></svg>
          </div>
          <div>
            <h3 class="text-base sm:text-lg font-bold text-white flex items-center justify-center lg:justify-start gap-2">
              <span id="banner-download-title">Executive Resume (.docx) — Dedicated Trilingual Versions</span>
            </h3>
            <p class="text-xs sm:text-sm text-slate-400 mt-0.5" id="banner-download-sub">
              Targeted for Board of Directors, Chairman, President & CEO (董事長、總經理、CEO 專用)
            </p>
          </div>
        </div>

        <!-- 3 Quick Download Buttons -->
        <div class="flex flex-wrap items-center justify-center gap-2.5 text-xs font-semibold">
          <a href="Howard_Liao_CISO_Resume_ZH.docx" download="Howard_Liao_CISO_Resume_ZH.docx" class="px-4 py-2.5 rounded-xl bg-slate-800 hover:bg-cyan-600 text-slate-200 hover:text-white border border-slate-700 hover:border-cyan-500 transition-all flex items-center gap-2 shadow-md">
            <span>🇹🇼</span>
            <span>繁體中文版 (.docx)</span>
          </a>
          <a href="Howard_Liao_CISO_Resume_EN.docx" download="Howard_Liao_CISO_Resume_EN.docx" class="px-4 py-2.5 rounded-xl bg-slate-800 hover:bg-cyan-600 text-slate-200 hover:text-white border border-slate-700 hover:border-cyan-500 transition-all flex items-center gap-2 shadow-md">
            <span>🇬🇧</span>
            <span>English Version (.docx)</span>
          </a>
          <a href="Howard_Liao_CISO_Resume_JA.docx" download="Howard_Liao_CISO_Resume_JA.docx" class="px-4 py-2.5 rounded-xl bg-slate-800 hover:bg-cyan-600 text-slate-200 hover:text-white border border-slate-700 hover:border-cyan-500 transition-all flex items-center gap-2 shadow-md">
            <span>🇯🇵</span>
            <span>日本語版 (.docx)</span>
          </a>
        </div>
      </div>
    </section>
"""

# Insert before </main>
html = html.replace('</main>', trilingual_download_box + '\n  </main>')

# Update JavaScript setLang to dynamically adjust download links
js_download_logic = """
      // Dynamic Resume Download Links per Language
      const navDownloadBtn = document.getElementById('nav-download-btn');
      const heroDownloadBtn = document.getElementById('hero-download-btn');
      const heroDownloadText = document.getElementById('hero-download-text');
      const bannerTitle = document.getElementById('banner-download-title');
      const bannerSub = document.getElementById('banner-download-sub');

      if (lang === 'zh') {
        const file = 'Howard_Liao_CISO_Resume_ZH.docx';
        if (navDownloadBtn) {
          navDownloadBtn.href = file;
          navDownloadBtn.download = file;
        }
        if (heroDownloadBtn) {
          heroDownloadBtn.href = file;
          heroDownloadBtn.download = file;
        }
        if (heroDownloadText) heroDownloadText.textContent = '📥 下載繁中高階履歷 (.docx)';
        if (bannerTitle) bannerTitle.textContent = '董事長、總經理、CEO 專用高階履歷 (.docx)';
        if (bannerSub) bannerSub.textContent = '含完整資安戰略治理、重大專案效益、學術論文與權威查證出處';
      } else if (lang === 'ja') {
        const file = 'Howard_Liao_CISO_Resume_JA.docx';
        if (navDownloadBtn) {
          navDownloadBtn.href = file;
          navDownloadBtn.download = file;
        }
        if (heroDownloadBtn) {
          heroDownloadBtn.href = file;
          heroDownloadBtn.download = file;
        }
        if (heroDownloadText) heroDownloadText.textContent = '📥 日本語履歴書 (.docx)';
        if (bannerTitle) bannerTitle.textContent = '取締役会・代表取締役社長・CEO 向け 日本語エグゼクティブ職務経歴書';
        if (bannerSub) bannerSub.textContent = 'セキュリティ戦略、多国籍プロジェクト実績、学術論文、実名検証済み記録を網羅';
      } else {
        const file = 'Howard_Liao_CISO_Resume_EN.docx';
        if (navDownloadBtn) {
          navDownloadBtn.href = file;
          navDownloadBtn.download = file;
        }
        if (heroDownloadBtn) {
          heroDownloadBtn.href = file;
          heroDownloadBtn.download = file;
        }
        if (heroDownloadText) heroDownloadText.textContent = '📥 Download English .DOCX';
        if (bannerTitle) bannerTitle.textContent = 'Executive Resume (.docx) — Dedicated Trilingual Versions';
        if (bannerSub) bannerSub.textContent = 'Targeted for Board of Directors, Chairman, President & CEO';
      }
"""

# Insert js_download_logic inside setLang right before renderSpeakingCards
html = html.replace('renderSpeakingCards(currentSpeakingFilter);', js_download_logic + '\n      renderSpeakingCards(currentSpeakingFilter);')

with open(target_file, "w", encoding="utf-8") as f:
    f.write(html)

print("Updated index.html: Added trilingual dynamic download links and interactive download banner!")
