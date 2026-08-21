import os

target_file = "/Users/howardliao/Desktop/Howard/Howard_CISO/index.html"

html_code = """<!DOCTYPE html>
<html lang="en" class="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Howard Liao, Ph.D. | Group CISO - Dynamic Executive PWA</title>
  <meta name="description" content="Executive Interactive Portfolio of Howard Liao, Ph.D. - Group Chief Information Security Officer (CISO)">
  <meta name="theme-color" content="#020617">
  
  <!-- PWA Manifest & Icons -->
  <link rel="manifest" href="manifest.json">
  <link rel="apple-touch-icon" href="assets/icon-192.png">
  <link rel="icon" type="image/png" sizes="192x192" href="assets/icon-192.png">
  
  <!-- Tailwind CSS CDN -->
  <script src="https://cdn.tailwindcss.com"></script>
  <!-- Chart.js for Dynamic Interactive Security Radar -->
  <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

  <script>
    tailwind.config = {
      darkMode: 'class',
      theme: {
        extend: {
          colors: {
            obsidian: {
              950: '#020617',
              900: '#0b1120',
              850: '#0f172a',
              800: '#1e293b',
              700: '#334155',
            },
            cyan: {
              400: '#38bdf8',
              500: '#0ea5e9',
              600: '#0284c7',
            },
            emerald: {
              400: '#34d399',
              500: '#10b981',
            }
          },
          animation: {
            'pulse-slow': 'pulse 4s cubic-bezier(0.4, 0, 0.6, 1) infinite',
            'float': 'float 6s ease-in-out infinite',
            'spin-slow': 'spin 12s linear infinite',
            'radar': 'radar 3s linear infinite',
            'glow': 'glow 2s ease-in-out infinite alternate',
          },
          keyframes: {
            float: {
              '0%, 100%': { transform: 'translateY(0px)' },
              '50%': { transform: 'translateY(-8px)' },
            },
            radar: {
              '0%': { transform: 'rotate(0deg)' },
              '100%': { transform: 'rotate(360deg)' },
            },
            glow: {
              '0%': { filter: 'drop-shadow(0 0 4px rgba(56, 189, 248, 0.4))' },
              '100%': { filter: 'drop-shadow(0 0 14px rgba(56, 189, 248, 0.9))' },
            }
          }
        }
      }
    }
  </script>

  <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Noto+Sans+TC:wght@300;400;500;700;900&family=Noto+Sans+JP:wght@300;400;500;700;900&display=swap');

    body {
      font-family: 'Plus Jakarta Sans', 'Noto Sans TC', 'Noto Sans JP', sans-serif;
    }

    .glass-card {
      background: rgba(15, 23, 42, 0.72);
      backdrop-filter: blur(14px);
      -webkit-backdrop-filter: blur(14px);
      border: 1px solid rgba(255, 255, 255, 0.08);
      transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }

    .glass-card:hover {
      border-color: rgba(56, 189, 248, 0.35);
      box-shadow: 0 12px 30px -10px rgba(14, 165, 233, 0.18);
    }

    .light .glass-card {
      background: rgba(255, 255, 255, 0.92);
      backdrop-filter: blur(14px);
      -webkit-backdrop-filter: blur(14px);
      border: 1px solid rgba(0, 0, 0, 0.08);
    }

    .light .glass-card:hover {
      border-color: rgba(14, 165, 233, 0.4);
      box-shadow: 0 12px 30px -10px rgba(0, 0, 0, 0.08);
    }

    .glass-nav {
      background: rgba(2, 6, 23, 0.85);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      border-bottom: 1px solid rgba(255, 255, 255, 0.08);
    }

    .light .glass-nav {
      background: rgba(248, 250, 252, 0.9);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      border-bottom: 1px solid rgba(0, 0, 0, 0.08);
    }

    .text-gradient {
      background: linear-gradient(135deg, #38bdf8 0%, #818cf8 50%, #c084fc 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }

    /* Cyber Canvas Background */
    #cyber-canvas {
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      pointer-events: none;
      z-index: 0;
      opacity: 0.35;
    }

    .light #cyber-canvas {
      opacity: 0.15;
    }

    /* Radar scan effect */
    .radar-sweep {
      background: conic-gradient(from 0deg, rgba(56, 189, 248, 0.4) 0deg, rgba(56, 189, 248, 0) 60deg);
    }

    /* Custom Scrollbar */
    ::-webkit-scrollbar {
      width: 8px;
      height: 8px;
    }
    ::-webkit-scrollbar-track {
      background: #020617;
    }
    ::-webkit-scrollbar-thumb {
      background: #334155;
      border-radius: 4px;
    }
    ::-webkit-scrollbar-thumb:hover {
      background: #475569;
    }
  </style>
</head>
<body class="bg-obsidian-950 text-slate-100 min-h-screen transition-colors duration-300 antialiased selection:bg-cyan-500 selection:text-white relative">

  <!-- Interactive Dynamic Particle Background -->
  <canvas id="cyber-canvas"></canvas>

  <!-- TOP APP BAR -->
  <header class="sticky top-0 z-40 glass-nav transition-colors duration-300">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
      
      <!-- Brand / Logo with Dynamic Radar Ring -->
      <div class="flex items-center gap-3">
        <div class="relative group cursor-pointer" onclick="scrollToTop()">
          <img src="assets/howard_portrait.jpg" alt="Howard Liao" class="w-10 h-10 rounded-full object-cover ring-2 ring-cyan-500/60 shadow-md">
          <span class="absolute -top-1 -right-1 w-3.5 h-3.5 bg-emerald-500 border-2 border-obsidian-950 rounded-full animate-ping"></span>
          <span class="absolute -top-1 -right-1 w-3.5 h-3.5 bg-emerald-500 border-2 border-obsidian-950 rounded-full"></span>
        </div>
        <div>
          <a href="#hero" class="font-bold text-base sm:text-lg tracking-tight hover:text-cyan-400 transition-colors flex items-center gap-2">
            <span>Howard Liao, Ph.D.</span>
            <span class="text-[10px] px-2 py-0.5 rounded-full bg-cyan-500/10 text-cyan-400 border border-cyan-500/30 font-mono hidden sm:inline-flex items-center gap-1">
              <svg class="w-2.5 h-2.5 animate-spin" viewBox="0 0 24 24" fill="none" stroke="currentColor"><circle cx="12" cy="12" r="10" stroke-width="4" class="opacity-25"></circle><path fill="currentColor" d="M4 12a8 8 0 018-8v8H4z"></path></svg>
              CISO
            </span>
          </a>
        </div>
      </div>

      <!-- Navigation Links (Desktop) -->
      <nav class="hidden lg:flex items-center gap-6 text-sm font-medium text-slate-300">
        <a href="#profile" class="hover:text-cyan-400 transition-colors flex items-center gap-1.5" data-i18n="nav.profile">
          <svg class="w-4 h-4 text-cyan-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"></path></svg>
          Profile
        </a>
        <a href="#radar" class="hover:text-cyan-400 transition-colors flex items-center gap-1.5" data-i18n="nav.radar">
          <svg class="w-4 h-4 text-indigo-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"></path></svg>
          Maturity Radar
        </a>
        <a href="#competencies" class="hover:text-cyan-400 transition-colors flex items-center gap-1.5" data-i18n="nav.competencies">
          <svg class="w-4 h-4 text-amber-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"></path></svg>
          Competencies
        </a>
        <a href="#experience" class="hover:text-cyan-400 transition-colors flex items-center gap-1.5" data-i18n="nav.experience">
          <svg class="w-4 h-4 text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 13.255A23.931 23.931 0 0112 15c-3.183 0-6.22-.62-9-1.745M16 6V4a2 2 0 00-2-2h-4a2 2 0 00-2 2v2m4 6h.01M5 20h14a2 2 0 002-2V8a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path></svg>
          Experience
        </a>
        <a href="#speaking" class="hover:text-cyan-400 transition-colors flex items-center gap-1.5" data-i18n="nav.speaking">
          <svg class="w-4 h-4 text-purple-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11a7 7 0 01-7 7m0 0a7 7 0 01-7-7m7 7v4m0 0H8m4 0h4m-4-8a3 3 0 100-6 3 3 0 000 6z"></path></svg>
          Speaking & Papers
        </a>
      </nav>

      <!-- Action Controls -->
      <div class="flex items-center gap-2 sm:gap-3">
        
        <!-- Language Switcher -->
        <div class="flex items-center bg-obsidian-900 border border-slate-700/60 rounded-lg p-1 text-xs font-semibold">
          <button onclick="setLang('en')" id="btn-lang-en" class="px-2 py-1 rounded transition-all bg-cyan-600 text-white shadow-sm">EN</button>
          <button onclick="setLang('zh')" id="btn-lang-zh" class="px-2 py-1 rounded transition-all text-slate-400 hover:text-white">繁中</button>
          <button onclick="setLang('ja')" id="btn-lang-ja" class="px-2 py-1 rounded transition-all text-slate-400 hover:text-white">日本語</button>
        </div>

        <!-- Cover Letter Button with Dynamic Icon -->
        <button onclick="openCoverLetter()" class="hidden sm:inline-flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs font-semibold bg-indigo-600/20 hover:bg-indigo-600/30 text-indigo-300 border border-indigo-500/30 transition-all shadow-sm group">
          <svg class="w-3.5 h-3.5 text-indigo-400 group-hover:scale-110 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path></svg>
          <span data-i18n="btn.coverLetter">Cover Letter</span>
        </button>

        <!-- Download Word Resume Button -->
        <a href="Howard_Liao_CISO_Resume.docx" download="Howard_Liao_CISO_Resume.docx" class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs font-semibold bg-gradient-to-r from-cyan-600 to-blue-600 hover:from-cyan-500 hover:to-blue-500 text-white shadow-md transition-all hover:scale-105 active:scale-95 group">
          <svg class="w-3.5 h-3.5 text-white group-hover:translate-y-0.5 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"></path></svg>
          <span class="hidden md:inline" data-i18n="btn.downloadResume">Download Word (.docx)</span>
          <span class="md:hidden">.DOCX</span>
        </a>

        <!-- Theme Toggle -->
        <button onclick="toggleTheme()" class="p-2 rounded-lg bg-obsidian-900 border border-slate-700/60 text-slate-300 hover:text-white transition-colors" title="Toggle Theme">
          <span id="theme-icon">🌙</span>
        </button>
      </div>

    </div>
  </header>

  <!-- MAIN CONTENT CONTAINER -->
  <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 sm:py-12 space-y-16 relative z-10">

    <!-- HERO SECTION -->
    <section id="hero" class="relative">
      <div class="glass-card rounded-3xl p-6 sm:p-10 relative overflow-hidden border border-slate-800 shadow-2xl">
        
        <!-- Animated Background Orbs -->
        <div class="absolute -top-24 -right-24 w-96 h-96 bg-cyan-500/15 rounded-full blur-3xl animate-pulse-slow pointer-events-none"></div>
        <div class="absolute -bottom-24 -left-24 w-96 h-96 bg-indigo-500/15 rounded-full blur-3xl animate-pulse-slow pointer-events-none" style="animation-delay: 2s;"></div>

        <div class="flex flex-col lg:flex-row items-center lg:items-start gap-8 sm:gap-12 relative z-10">
          
          <!-- Photo & Status & Interactive Badges -->
          <div class="flex flex-col items-center flex-shrink-0">
            <div class="relative group">
              <!-- Hologram Radar Frame -->
              <div class="absolute -inset-1 rounded-2xl bg-gradient-to-r from-cyan-500 via-indigo-500 to-purple-500 opacity-40 group-hover:opacity-100 blur-sm transition duration-500"></div>
              
              <img src="assets/howard_portrait.jpg" alt="Howard Liao, Ph.D." class="relative w-48 h-64 sm:w-56 sm:h-72 object-cover rounded-2xl ring-2 ring-slate-800 shadow-2xl transition-all duration-300">
              
              <!-- Floating Pulsing Beacon -->
              <div class="absolute -bottom-3 inset-x-0 flex justify-center">
                <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-semibold bg-emerald-950/90 text-emerald-400 border border-emerald-500/30 shadow-lg backdrop-blur-md">
                  <span class="relative flex h-2 w-2">
                    <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75"></span>
                    <span class="relative inline-flex rounded-full h-2 w-2 bg-emerald-500"></span>
                  </span>
                  <span data-i18n="hero.status">Executive Ready</span>
                </span>
              </div>
            </div>

            <!-- Dynamic Micro-Icon Badges -->
            <div class="mt-6 flex flex-col gap-2 w-full max-w-xs text-xs">
              <div class="flex items-center gap-2.5 px-3 py-2 rounded-xl bg-slate-900/80 border border-slate-800 text-slate-300 hover:border-cyan-500/50 transition-colors">
                <div class="w-6 h-6 rounded-lg bg-cyan-500/10 flex items-center justify-center text-cyan-400 flex-shrink-0">
                  <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"></path></svg>
                </div>
                <span data-i18n="hero.badge1">ISO 27001 & 42001 Lead Auditor</span>
              </div>

              <div class="flex items-center gap-2.5 px-3 py-2 rounded-xl bg-slate-900/80 border border-slate-800 text-slate-300 hover:border-indigo-500/50 transition-colors">
                <div class="w-6 h-6 rounded-lg bg-indigo-500/10 flex items-center justify-center text-indigo-400 flex-shrink-0">
                  <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 14l9-5-9-5-9 5 9 5z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 14l6.16-3.422a12.083 12.083 0 01.665 6.479A11.952 11.952 0 0012 20.055a11.952 11.952 0 00-6.824-2.998 12.078 12.078 0 01.665-6.479L12 14z"></path></svg>
                </div>
                <span data-i18n="hero.badge2">Ph.D. in IT Management</span>
              </div>

              <div class="flex items-center gap-2.5 px-3 py-2 rounded-xl bg-slate-900/80 border border-slate-800 text-slate-300 hover:border-amber-500/50 transition-colors">
                <div class="w-6 h-6 rounded-lg bg-amber-500/10 flex items-center justify-center text-amber-400 flex-shrink-0">
                  <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 3v4M3 5h4M6 17v4m-2-2h4m5-16l2.286 6.857L21 12l-5.714 2.143L13 21l-2.286-6.857L5 12l5.714-2.143L13 3z"></path></svg>
                </div>
                <span data-i18n="hero.badge3">PMP & CSM Certified</span>
              </div>
            </div>
          </div>

          <!-- Executive Bio & Title -->
          <div class="flex-1 text-center lg:text-left space-y-4">
            
            <div class="space-y-1.5">
              <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full text-xs font-bold uppercase tracking-wider bg-blue-500/10 text-blue-400 border border-blue-500/20 mb-2" data-i18n="hero.roleTag">
                <span class="w-1.5 h-1.5 rounded-full bg-cyan-400 animate-ping"></span>
                Board-Level Technology & Security Leadership
              </div>
              <h1 class="text-3xl sm:text-5xl font-extrabold tracking-tight text-white">
                <span id="hero-name">Howard Liao, Ph.D.</span>
                <span class="block sm:inline sm:ml-2 text-2xl sm:text-3xl font-semibold text-slate-400" id="hero-name-zh">(廖倫豪 博士)</span>
              </h1>
              <h2 class="text-xl sm:text-2xl font-bold text-gradient" data-i18n="hero.title">
                Group Chief Information Security Officer (CISO)
              </h2>
              <p class="text-base sm:text-lg font-medium text-slate-300" data-i18n="hero.subtitle">
                Global Cybersecurity, Digital Trust & Resilience
              </p>
            </div>

            <!-- Contact & Social Pills with Animated Hover -->
            <div class="flex flex-wrap items-center justify-center lg:justify-start gap-2 sm:gap-3 text-xs sm:text-sm pt-2">
              <span class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-xl bg-slate-800/80 border border-slate-700 text-slate-300 hover:border-cyan-500/50 transition-colors">
                <svg class="w-4 h-4 text-red-400 animate-bounce" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"></path></svg>
                Taiwan (Open to Global Sites)
              </span>
              <a href="tel:+886975323161" class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-xl bg-slate-800/80 border border-slate-700 text-slate-300 hover:text-cyan-400 hover:border-cyan-500/50 transition-all">
                <svg class="w-4 h-4 text-emerald-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"></path></svg>
                +886-975-323161
              </a>
              <a href="mailto:Liao.Howard@gmail.com" class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-xl bg-slate-800/80 border border-slate-700 text-slate-300 hover:text-cyan-400 hover:border-cyan-500/50 transition-all">
                <svg class="w-4 h-4 text-cyan-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path></svg>
                Liao.Howard@gmail.com
              </a>
              <a href="https://linkedin.com/in/howardliao78" target="_blank" rel="noopener" class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-xl bg-blue-900/40 border border-blue-700/60 text-blue-300 hover:bg-blue-800/60 transition-all">
                <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24"><path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/></svg>
                LinkedIn Profile ↗
              </a>
              <a href="https://howardliao.github.io/portfolio/" target="_blank" rel="noopener" class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-xl bg-indigo-900/40 border border-indigo-700/60 text-indigo-300 hover:bg-indigo-800/60 transition-all">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 12a9 9 0 01-9 9m9-9a9 9 0 00-9-9m9 9H3m9 9a9 9 0 01-9-9m9 9c1.657 0 3-4.03 3-9s-1.343-9-3-9m0 18c-1.657 0-3-4.03-3-9s1.343-9 3-9m-9 9a9 9 0 019-9"></path></svg>
                Portfolio ↗
              </a>
            </div>

            <!-- Summary Statement -->
            <p class="text-sm sm:text-base text-slate-300 leading-relaxed pt-2" data-i18n="hero.leadText">
              CISO-level technology executive with 27+ years of enterprise IT leadership, 15+ years of cybersecurity experience, and 10+ years leading cybersecurity strategy, cloud governance, digital resilience, and enterprise transformation across publicly listed, multinational, and regulated business environments.
            </p>

            <!-- Quick Action Buttons -->
            <div class="flex flex-wrap items-center justify-center lg:justify-start gap-3 pt-3">
              <a href="#experience" class="px-5 py-2.5 rounded-xl bg-cyan-600 hover:bg-cyan-500 text-white text-sm font-semibold shadow-lg shadow-cyan-900/30 transition-all hover:scale-105 active:scale-95 flex items-center gap-2" data-i18n="hero.btnExperience">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 14l-7 7m0 0l-7-7m7 7V3"></path></svg>
                Explore Career Milestones
              </a>
              <button onclick="openCoverLetter()" class="px-5 py-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 text-sm font-semibold border border-slate-700 transition-all flex items-center gap-2" data-i18n="hero.btnLetter">
                <svg class="w-4 h-4 text-indigo-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"></path></svg>
                View C-Level Cover Letter
              </button>
              <a href="Howard_Liao_CISO_Resume.docx" download="Howard_Liao_CISO_Resume.docx" class="px-5 py-2.5 rounded-xl bg-blue-600/20 hover:bg-blue-600/30 text-blue-300 border border-blue-500/30 text-sm font-semibold transition-all flex items-center gap-2">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"></path></svg>
                📥 1-Click .DOCX
              </a>
            </div>

          </div>

        </div>
      </div>
    </section>

    <!-- BENTO GRID KPI DASHBOARD (WITH DYNAMIC ANIMATED COUNTERS & GLOWING BORDERS) -->
    <section id="kpi" class="space-y-4">
      <div class="flex items-center justify-between">
        <h2 class="text-xl sm:text-2xl font-bold tracking-tight text-white flex items-center gap-2.5">
          <div class="w-8 h-8 rounded-lg bg-cyan-500/10 flex items-center justify-center text-cyan-400">
            <svg class="w-5 h-5 animate-pulse" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg>
          </div>
          <span data-i18n="kpi.heading">Key Leadership & Resilience Metrics</span>
        </h2>
        <span class="text-xs text-slate-400 font-mono" data-i18n="kpi.subtitle">Live Quantified Metrics</span>
      </div>

      <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-6 gap-3 sm:gap-4">
        
        <!-- KPI 1 -->
        <div class="glass-card rounded-2xl p-4 text-center border border-slate-800 hover:border-cyan-500/60 transition-all group hover:-translate-y-1">
          <div class="w-8 h-8 mx-auto rounded-full bg-cyan-500/10 flex items-center justify-center text-cyan-400 mb-2 group-hover:scale-110 transition-transform">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>
          </div>
          <div class="text-2xl sm:text-3xl font-extrabold text-cyan-400 counter" data-target="100" data-suffix="%">0%</div>
          <div class="text-xs font-bold text-slate-200 mt-1" data-i18n="kpi.kpi1Title">Zero Outage</div>
          <div class="text-[10px] text-slate-400 mt-0.5" data-i18n="kpi.kpi1Sub">GKE Multi-Cloud HA</div>
        </div>

        <!-- KPI 2 -->
        <div class="glass-card rounded-2xl p-4 text-center border border-slate-800 hover:border-blue-500/60 transition-all group hover:-translate-y-1">
          <div class="w-8 h-8 mx-auto rounded-full bg-blue-500/10 flex items-center justify-center text-blue-400 mb-2 group-hover:scale-110 transition-transform">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
          </div>
          <div class="text-2xl sm:text-3xl font-extrabold text-blue-400 counter" data-target="-30" data-prefix="" data-suffix="%">-30%</div>
          <div class="text-xs font-bold text-slate-200 mt-1" data-i18n="kpi.kpi2Title">Cloud FinOps</div>
          <div class="text-[10px] text-slate-400 mt-0.5" data-i18n="kpi.kpi2Sub">Annual TCO Reduction</div>
        </div>

        <!-- KPI 3 -->
        <div class="glass-card rounded-2xl p-4 text-center border border-slate-800 hover:border-emerald-500/60 transition-all group hover:-translate-y-1">
          <div class="w-8 h-8 mx-auto rounded-full bg-emerald-500/10 flex items-center justify-center text-emerald-400 mb-2 group-hover:scale-110 transition-transform">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"></path></svg>
          </div>
          <div class="text-2xl sm:text-3xl font-extrabold text-emerald-400 counter" data-target="-30" data-suffix="%">-30%</div>
          <div class="text-xs font-bold text-slate-200 mt-1" data-i18n="kpi.kpi3Title">Major Incidents</div>
          <div class="text-[10px] text-slate-400 mt-0.5" data-i18n="kpi.kpi3Sub">SOC/SIEM & EDR</div>
        </div>

        <!-- KPI 4 -->
        <div class="glass-card rounded-2xl p-4 text-center border border-slate-800 hover:border-indigo-500/60 transition-all group hover:-translate-y-1">
          <div class="w-8 h-8 mx-auto rounded-full bg-indigo-500/10 flex items-center justify-center text-indigo-400 mb-2 group-hover:scale-110 transition-transform">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
          </div>
          <div class="text-2xl sm:text-3xl font-extrabold text-indigo-400 counter" data-target="-30" data-suffix="%">-30%</div>
          <div class="text-xs font-bold text-slate-200 mt-1" data-i18n="kpi.kpi4Title">MTTR Reduced</div>
          <div class="text-[10px] text-slate-400 mt-0.5" data-i18n="kpi.kpi4Sub">APM & Observability</div>
        </div>

        <!-- KPI 5 -->
        <div class="glass-card rounded-2xl p-4 text-center border border-slate-800 hover:border-amber-500/60 transition-all group hover:-translate-y-1">
          <div class="w-8 h-8 mx-auto rounded-full bg-amber-500/10 flex items-center justify-center text-amber-400 mb-2 group-hover:scale-110 transition-transform">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"></path></svg>
          </div>
          <div class="text-2xl sm:text-3xl font-extrabold text-amber-400 counter" data-target="14" data-prefix="$" data-suffix="M+">$14M+</div>
          <div class="text-xs font-bold text-slate-200 mt-1" data-i18n="kpi.kpi5Title">Budget Scale</div>
          <div class="text-[10px] text-slate-400 mt-0.5" data-i18n="kpi.kpi5Sub">Annual IT & Security</div>
        </div>

        <!-- KPI 6 -->
        <div class="glass-card rounded-2xl p-4 text-center border border-slate-800 hover:border-purple-500/60 transition-all group hover:-translate-y-1">
          <div class="w-8 h-8 mx-auto rounded-full bg-purple-500/10 flex items-center justify-center text-purple-400 mb-2 group-hover:scale-110 transition-transform">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 12a9 9 0 01-9 9m9-9a9 9 0 00-9-9m9 9H3m9 9a9 9 0 01-9-9m9 9c1.657 0 3-4.03 3-9s-1.343-9-3-9m0 18c-1.657 0-3-4.03-3-9s1.343-9 3-9m-9 9a9 9 0 019-9"></path></svg>
          </div>
          <div class="text-2xl sm:text-3xl font-extrabold text-purple-400 counter" data-target="27" data-suffix="+ Y">27+ Y</div>
          <div class="text-xs font-bold text-slate-200 mt-1" data-i18n="kpi.kpi6Title">IT Leadership</div>
          <div class="text-[10px] text-slate-400 mt-0.5" data-i18n="kpi.kpi6Sub">15+ Y Cybersecurity</div>
        </div>

      </div>
    </section>

    <!-- INTERACTIVE SECTION: SECURITY GOVERNANCE RADAR & MATURITY WHEEL -->
    <section id="radar" class="space-y-6">
      <div class="flex flex-col sm:flex-row sm:items-center justify-between border-b border-slate-800 pb-3 gap-2">
        <h2 class="text-2xl font-bold text-white flex items-center gap-2.5">
          <div class="w-8 h-8 rounded-lg bg-indigo-500/10 flex items-center justify-center text-indigo-400">
            <svg class="w-5 h-5 animate-spin-slow" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"></path></svg>
          </div>
          <span data-i18n="radar.heading">Security Maturity & Strategic Governance Radar</span>
        </h2>
        <span class="text-xs text-slate-400 font-mono" data-i18n="radar.subtitle">6-Dimensional CISO Mastery</span>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 items-center">
        
        <!-- Radar Chart Container -->
        <div class="lg:col-span-5 glass-card rounded-3xl p-6 flex flex-col items-center justify-center relative overflow-hidden">
          <div class="w-full max-w-sm h-72 sm:h-80 relative">
            <canvas id="securityRadarCanvas"></canvas>
          </div>
          <div class="text-[11px] text-slate-400 mt-2 font-mono flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-cyan-400"></span>
            <span>Howard Liao Strategic Competency Benchmark</span>
          </div>
        </div>

        <!-- Dynamic Dimension Cards (6 Cards) -->
        <div class="lg:col-span-7 grid grid-cols-1 sm:grid-cols-2 gap-3.5">
          
          <div class="p-4 rounded-2xl bg-slate-900/60 border border-slate-800/80 hover:border-cyan-500/40 transition-all flex items-start gap-3">
            <div class="w-8 h-8 rounded-xl bg-cyan-500/10 flex items-center justify-center text-cyan-400 flex-shrink-0 mt-0.5">
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"></path></svg>
            </div>
            <div>
              <div class="flex items-center justify-between">
                <h4 class="font-bold text-white text-xs sm:text-sm">Zero Trust & IAM</h4>
                <span class="text-[10px] font-mono text-cyan-400 font-bold">98%</span>
              </div>
              <p class="text-[11px] text-slate-400 mt-1">Enterprise SSO, MFA, PAM, Least Privilege, CASB & Micro-segmentation.</p>
            </div>
          </div>

          <div class="p-4 rounded-2xl bg-slate-900/60 border border-slate-800/80 hover:border-blue-500/40 transition-all flex items-start gap-3">
            <div class="w-8 h-8 rounded-xl bg-blue-500/10 flex items-center justify-center text-blue-400 flex-shrink-0 mt-0.5">
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 15a4 4 0 004 4h9a5 5 0 10-.1-9.999 5.002 5.002 0 00-9.78 2.096A4.001 4.001 0 003 15z"></path></svg>
            </div>
            <div>
              <div class="flex items-center justify-between">
                <h4 class="font-bold text-white text-xs sm:text-sm">Multi-Cloud & GKE</h4>
                <span class="text-[10px] font-mono text-blue-400 font-bold">99%</span>
              </div>
              <p class="text-[11px] text-slate-400 mt-1">AWS, Azure, GCP, GKE, Multi-Zone HA, Cross-Region DR, 100% Zero Outage.</p>
            </div>
          </div>

          <div class="p-4 rounded-2xl bg-slate-900/60 border border-slate-800/80 hover:border-purple-500/40 transition-all flex items-start gap-3">
            <div class="w-8 h-8 rounded-xl bg-purple-500/10 flex items-center justify-center text-purple-400 flex-shrink-0 mt-0.5">
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg>
            </div>
            <div>
              <div class="flex items-center justify-between">
                <h4 class="font-bold text-white text-xs sm:text-sm">AI Governance (ISO 42001)</h4>
                <span class="text-[10px] font-mono text-purple-400 font-bold">96%</span>
              </div>
              <p class="text-[11px] text-slate-400 mt-1">Responsible AI, GenAI DLP, Model Risk, Secure RAG & Prompt Safety.</p>
            </div>
          </div>

          <div class="p-4 rounded-2xl bg-slate-900/60 border border-slate-800/80 hover:border-emerald-500/40 transition-all flex items-start gap-3">
            <div class="w-8 h-8 rounded-xl bg-emerald-500/10 flex items-center justify-center text-emerald-400 flex-shrink-0 mt-0.5">
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"></path></svg>
            </div>
            <div>
              <div class="flex items-center justify-between">
                <h4 class="font-bold text-white text-xs sm:text-sm">SOC/SIEM & Incident Ops</h4>
                <span class="text-[10px] font-mono text-emerald-400 font-bold">95%</span>
              </div>
              <p class="text-[11px] text-slate-400 mt-1">Detection Engineering, Threat Intel, Ransomware Defense & -30% MTTR.</p>
            </div>
          </div>

          <div class="p-4 rounded-2xl bg-slate-900/60 border border-slate-800/80 hover:border-amber-500/40 transition-all flex items-start gap-3">
            <div class="w-8 h-8 rounded-xl bg-amber-500/10 flex items-center justify-center text-amber-400 flex-shrink-0 mt-0.5">
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
            </div>
            <div>
              <div class="flex items-center justify-between">
                <h4 class="font-bold text-white text-xs sm:text-sm">FinOps & Cost Governance</h4>
                <span class="text-[10px] font-mono text-amber-400 font-bold">94%</span>
              </div>
              <p class="text-[11px] text-slate-400 mt-1">Multi-cloud TCO -30%, Unit Cost Modeling & ROI/TCO Justification.</p>
            </div>
          </div>

          <div class="p-4 rounded-2xl bg-slate-900/60 border border-slate-800/80 hover:border-rose-500/40 transition-all flex items-start gap-3">
            <div class="w-8 h-8 rounded-xl bg-rose-500/10 flex items-center justify-center text-rose-400 flex-shrink-0 mt-0.5">
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"></path></svg>
            </div>
            <div>
              <div class="flex items-center justify-between">
                <h4 class="font-bold text-white text-xs sm:text-sm">Board Governance & Risk</h4>
                <span class="text-[10px] font-mono text-rose-400 font-bold">97%</span>
              </div>
              <p class="text-[11px] text-slate-400 mt-1">CISO Board Reporting, Audit Readiness, Crisis Leadership & Stakeholder Mgmt.</p>
            </div>
          </div>

        </div>

      </div>
    </section>

    <!-- SECTION: EXECUTIVE PROFILE & VALUE PROPOSITION -->
    <section id="profile" class="space-y-6">
      <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <h2 class="text-2xl font-bold text-white flex items-center gap-2.5">
          <div class="w-8 h-8 rounded-lg bg-cyan-500/10 flex items-center justify-center text-cyan-400">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"></path></svg>
          </div>
          <span data-i18n="profile.heading">Executive Profile & Leadership Value Proposition</span>
        </h2>
      </div>

      <!-- Profile 5 Paragraphs -->
      <div class="glass-card rounded-2xl p-6 sm:p-8 space-y-4 text-sm sm:text-base text-slate-300 leading-relaxed">
        <div id="profile-paragraphs" class="space-y-3">
          <!-- Dynamic injection -->
        </div>
      </div>

      <!-- Leadership Value Proposition (6 Cards with Micro-Icons) -->
      <div>
        <h3 class="text-lg font-bold text-slate-200 mb-4 flex items-center gap-2" data-i18n="value.subheading">
          <svg class="w-5 h-5 text-amber-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg>
          <span>Core Value Pillars for Boards & Enterprises</span>
        </h3>
        <div id="value-cards" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          <!-- Dynamic injection -->
        </div>
      </div>
    </section>

    <!-- SECTION: CORE COMPETENCIES (8 DOMAINS) -->
    <section id="competencies" class="space-y-6">
      <div class="flex flex-col sm:flex-row sm:items-center justify-between border-b border-slate-800 pb-3 gap-2">
        <h2 class="text-2xl font-bold text-white flex items-center gap-2.5">
          <div class="w-8 h-8 rounded-lg bg-amber-500/10 flex items-center justify-center text-amber-400">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"></path></svg>
          </div>
          <span data-i18n="comp.heading">Core Competencies & Technical Governance</span>
        </h2>
        <span class="text-xs text-slate-400 font-mono" data-i18n="comp.subtitle">8 Strategic Security & Architecture Domains</span>
      </div>

      <div id="competency-domains" class="grid grid-cols-1 md:grid-cols-2 gap-6">
        <!-- Dynamic injection -->
      </div>
    </section>

    <!-- SECTION: PROFESSIONAL EXPERIENCE (7 MILESTONES WITH EXPANDABLE SCOPES) -->
    <section id="experience" class="space-y-6">
      <div class="flex flex-col sm:flex-row sm:items-center justify-between border-b border-slate-800 pb-3 gap-2">
        <h2 class="text-2xl font-bold text-white flex items-center gap-2.5">
          <div class="w-8 h-8 rounded-lg bg-blue-500/10 flex items-center justify-center text-blue-400">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"></path></svg>
          </div>
          <span data-i18n="exp.heading">Professional Career & Leadership Experience</span>
        </h2>
        <span class="text-xs text-slate-400 font-mono" data-i18n="exp.subtitle">2002 – Present (27+ Years Leadership)</span>
      </div>

      <!-- Career Timeline List -->
      <div id="experience-list" class="space-y-6">
        <!-- Dynamic injection -->
      </div>
    </section>

    <!-- SECTION: CERTIFICATIONS & EDUCATION -->
    <section id="credentials" class="space-y-6">
      <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <h2 class="text-2xl font-bold text-white flex items-center gap-2.5">
          <div class="w-8 h-8 rounded-lg bg-purple-500/10 flex items-center justify-center text-purple-400">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 14l9-5-9-5-9 5 9 5z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 14l6.16-3.422a12.083 12.083 0 01.665 6.479A11.952 11.952 0 0012 20.055a11.952 11.952 0 00-6.824-2.998 12.078 12.078 0 01.665-6.479L12 14z"></path></svg>
          </div>
          <span data-i18n="cred.heading">Professional Certifications & Academic Degrees</span>
        </h2>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
        
        <!-- Certifications -->
        <div class="glass-card rounded-3xl p-6 space-y-4 border border-slate-800">
          <h3 class="text-lg font-bold text-white flex items-center gap-2" data-i18n="cred.certsTitle">
            <svg class="w-5 h-5 text-cyan-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4M7.835 4.697a3.42 3.42 0 001.946-.806 3.42 3.42 0 014.438 0 3.42 3.42 0 001.946.806 3.42 3.42 0 013.138 3.138 3.42 3.42 0 00.806 1.946 3.42 3.42 0 010 4.438 3.42 3.42 0 00-.806 1.946 3.42 3.42 0 01-3.138 3.138 3.42 3.42 0 00-1.946.806 3.42 3.42 0 01-4.438 0 3.42 3.42 0 00-1.946-.806 3.42 3.42 0 01-3.138-3.138 3.42 3.42 0 00-.806-1.946 3.42 3.42 0 010-4.438 3.42 3.42 0 00.806-1.946 3.42 3.42 0 013.138-3.138z"></path></svg>
            <span>Professional Certifications</span>
          </h3>
          <ul id="cert-list" class="space-y-2.5 text-sm text-slate-300">
            <!-- Dynamic injection -->
          </ul>
        </div>

        <!-- Education -->
        <div class="glass-card rounded-3xl p-6 space-y-4 border border-slate-800">
          <h3 class="text-lg font-bold text-white flex items-center gap-2" data-i18n="cred.eduTitle">
            <svg class="w-5 h-5 text-indigo-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"></path></svg>
            <span>Academic Education</span>
          </h3>
          <div id="edu-list" class="space-y-4">
            <!-- Dynamic injection -->
          </div>
        </div>

      </div>
    </section>

    <!-- SECTION: AWARDS, KEYNOTES, PUBLICATIONS & MEDIA -->
    <section id="speaking" class="space-y-6">
      <div class="flex flex-col sm:flex-row sm:items-center justify-between border-b border-slate-800 pb-3 gap-2">
        <h2 class="text-2xl font-bold text-white flex items-center gap-2.5">
          <div class="w-8 h-8 rounded-lg bg-cyan-500/10 flex items-center justify-center text-cyan-400">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11a7 7 0 01-7 7m0 0a7 7 0 01-7-7m7 7v4m0 0H8m4 0h4m-4-8a3 3 0 100-6 3 3 0 000 6z"></path></svg>
          </div>
          <span data-i18n="speak.heading">Awards, Keynotes, Publications & Speaking</span>
        </h2>
        <span class="text-xs text-slate-400 font-mono" data-i18n="speak.subtitle">Verified Industry & Academic Evidence</span>
      </div>

      <!-- Category Filter Pills -->
      <div class="flex flex-wrap gap-2 text-xs font-semibold">
        <button onclick="filterSpeaking('all')" class="speak-filter-btn px-3.5 py-1.5 rounded-xl bg-cyan-600 text-white flex items-center gap-1.5" data-filter="all">
          <span>⚡</span>
          <span data-i18n="speak.all">All Records</span>
        </button>
        <button onclick="filterSpeaking('keynote')" class="speak-filter-btn px-3.5 py-1.5 rounded-xl bg-slate-800 text-slate-300 hover:text-white flex items-center gap-1.5" data-filter="keynote">
          <span>🎤</span>
          <span data-i18n="speak.keynotes">Keynotes & Speaking</span>
        </button>
        <button onclick="filterSpeaking('paper')" class="speak-filter-btn px-3.5 py-1.5 rounded-xl bg-slate-800 text-slate-300 hover:text-white flex items-center gap-1.5" data-filter="paper">
          <span>📜</span>
          <span data-i18n="speak.papers">Publications & DOI</span>
        </button>
        <button onclick="filterSpeaking('media')" class="speak-filter-btn px-3.5 py-1.5 rounded-xl bg-slate-800 text-slate-300 hover:text-white flex items-center gap-1.5" data-filter="media">
          <span>📰</span>
          <span data-i18n="speak.media">Media & Interviews</span>
        </button>
        <button onclick="filterSpeaking('csr')" class="speak-filter-btn px-3.5 py-1.5 rounded-xl bg-slate-800 text-slate-300 hover:text-white flex items-center gap-1.5" data-filter="csr">
          <span>🏆</span>
          <span data-i18n="speak.csr">Awards & CSR</span>
        </button>
      </div>

      <!-- Speaking Cards Grid -->
      <div id="speaking-grid" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <!-- Dynamic injection -->
      </div>
    </section>

  </main>

  <!-- FOOTER -->
  <footer class="border-t border-slate-800 bg-obsidian-950/90 backdrop-blur-md py-10 mt-20 text-center text-xs text-slate-500 space-y-3 relative z-10">
    <div class="flex flex-wrap justify-center items-center gap-4 text-slate-400">
      <a href="https://howardliao.github.io/portfolio/" target="_blank" class="hover:text-cyan-400 transition-colors flex items-center gap-1">
        <span>🌐</span> Howard Portfolio ↗
      </a>
      <span>•</span>
      <a href="https://linkedin.com/in/howardliao78" target="_blank" class="hover:text-cyan-400 transition-colors flex items-center gap-1">
        <span>🔗</span> LinkedIn ↗
      </a>
      <span>•</span>
      <a href="mailto:Liao.Howard@gmail.com" class="hover:text-cyan-400 transition-colors flex items-center gap-1">
        <span>✉️</span> Liao.Howard@gmail.com
      </a>
      <span>•</span>
      <a href="tel:+886975323161" class="hover:text-cyan-400 transition-colors flex items-center gap-1">
        <span>📱</span> +886-975-323161
      </a>
    </div>
    <p>© 2026 Howard Liao, Ph.D. (廖倫豪 博士). All rights reserved. Progressive Web App (PWA) Enabled (Local Preview Version).</p>
  </footer>

  <!-- LIGHTBOX MODAL -->
  <div id="lightbox-modal" class="fixed inset-0 z-50 bg-black/90 backdrop-blur-md hidden items-center justify-center p-4" onclick="closeLightbox()">
    <div class="relative max-w-4xl w-full max-h-[90vh] flex flex-col items-center" onclick="event.stopPropagation()">
      <button onclick="closeLightbox()" class="absolute -top-12 right-0 text-white text-3xl font-bold hover:text-cyan-400">✕</button>
      <img id="lightbox-img" src="" alt="Enlarged Evidence" class="max-h-[80vh] w-auto max-w-full rounded-xl shadow-2xl object-contain border border-slate-700">
      <p id="lightbox-caption" class="text-slate-300 text-sm mt-3 text-center"></p>
    </div>
  </div>

  <!-- COVER LETTER MODAL -->
  <div id="letter-modal" class="fixed inset-0 z-50 bg-black/80 backdrop-blur-sm hidden items-center justify-center p-4" onclick="closeCoverLetter()">
    <div class="bg-obsidian-900 border border-slate-700 rounded-3xl max-w-3xl w-full max-h-[85vh] flex flex-col shadow-2xl overflow-hidden" onclick="event.stopPropagation()">
      
      <!-- Modal Header -->
      <div class="p-6 border-b border-slate-800 flex items-center justify-between">
        <div class="flex items-center gap-2.5">
          <div class="w-8 h-8 rounded-lg bg-indigo-500/10 flex items-center justify-center text-indigo-400">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path></svg>
          </div>
          <div>
            <h3 class="text-lg font-bold text-white" data-i18n="letter.title">CISO Executive Cover Letter</h3>
            <p class="text-xs text-slate-400" data-i18n="letter.subtitle">Direct Message to Board, CEO & Global CIO</p>
          </div>
        </div>
        <button onclick="closeCoverLetter()" class="text-slate-400 hover:text-white text-2xl font-bold">✕</button>
      </div>

      <!-- Modal Body -->
      <div class="p-6 overflow-y-auto space-y-4 text-sm text-slate-200 leading-relaxed font-sans" id="letter-content">
        <!-- Dynamic injection -->
      </div>

      <!-- Modal Footer -->
      <div class="p-4 border-t border-slate-800 bg-obsidian-950 flex items-center justify-between">
        <span id="copy-toast" class="text-xs font-semibold text-emerald-400 opacity-0 transition-opacity">✓ Copied to clipboard!</span>
        <div class="flex items-center gap-3">
          <button onclick="copyCoverLetter()" class="px-4 py-2 rounded-xl bg-cyan-600 hover:bg-cyan-500 text-white text-xs font-bold shadow-md transition-all flex items-center gap-1.5">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 16H6a2 2 0 01-2-2V6a2 2 0 012-2h8a2 2 0 012 2v2m-6 12h8a2 2 0 002-2v-8a2 2 0 00-2-2h-8a2 2 0 00-2 2v8a2 2 0 002 2z"></path></svg>
            Copy Letter
          </button>
          <button onclick="closeCoverLetter()" class="px-4 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs font-semibold transition-all">
            Close
          </button>
        </div>
      </div>

    </div>
  </div>

  <!-- PWA SCRIPT & APP LOGIC -->
  <script>
    // PWA Service Worker Registration
    if ('serviceWorker' in navigator) {
      window.addEventListener('load', () => {
        navigator.serviceWorker.register('./sw.js')
          .then(reg => console.log('[PWA] Service Worker registered:', reg.scope))
          .catch(err => console.log('[PWA] Service Worker failed:', err));
      });
    }

    // Scroll to Top
    function scrollToTop() {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }

    // Interactive Particle Constellation Canvas
    function initCyberCanvas() {
      const canvas = document.getElementById('cyber-canvas');
      const ctx = canvas.getContext('2d');
      let w = canvas.width = window.innerWidth;
      let h = canvas.height = window.innerHeight;

      const particles = [];
      const count = Math.floor((w * h) / 18000);

      for (let i = 0; i < count; i++) {
        particles.push({
          x: Math.random() * w,
          y: Math.random() * h,
          vx: (Math.random() - 0.5) * 0.4,
          vy: (Math.random() - 0.5) * 0.4,
          radius: Math.random() * 1.5 + 0.8
        });
      }

      function draw() {
        ctx.clearRect(0, 0, w, h);
        
        ctx.fillStyle = 'rgba(56, 189, 248, 0.6)';
        ctx.strokeStyle = 'rgba(56, 189, 248, 0.08)';

        for (let i = 0; i < particles.length; i++) {
          const p = particles[i];
          p.x += p.vx;
          p.y += p.vy;

          if (p.x < 0) p.x = w;
          if (p.x > w) p.x = 0;
          if (p.y < 0) p.y = h;
          if (p.y > h) p.y = 0;

          ctx.beginPath();
          ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
          ctx.fill();

          for (let j = i + 1; j < particles.length; j++) {
            const p2 = particles[j];
            const dist = Math.hypot(p.x - p2.x, p.y - p2.y);
            if (dist < 110) {
              ctx.beginPath();
              ctx.moveTo(p.x, p.y);
              ctx.lineTo(p2.x, p2.y);
              ctx.stroke();
            }
          }
        }
        requestAnimationFrame(draw);
      }

      window.addEventListener('resize', () => {
        w = canvas.width = window.innerWidth;
        h = canvas.height = window.innerHeight;
      });

      draw();
    }

    // Dynamic Chart.js Security Radar Chart
    let radarChart = null;
    function initRadarChart() {
      const ctx = document.getElementById('securityRadarCanvas').getContext('2d');
      
      const labels = currentLang === 'zh' 
        ? ['零信任與IAM', '多雲與GKE', 'AI治理(42001)', 'SOC/SIEM維運', 'FinOps成本管理', '董事會戰略治理']
        : currentLang === 'ja'
        ? ['ゼロトラスト/IAM', 'マルチクラウド/GKE', 'AI統治(42001)', 'SOC/SIEM運用', 'FinOpsコスト統治', '取締役会戦略統制']
        : ['Zero Trust & IAM', 'Multi-Cloud & GKE', 'AI Governance', 'SOC/SIEM Ops', 'FinOps & Cost', 'Board Strategy'];

      if (radarChart) {
        radarChart.destroy();
      }

      radarChart = new Chart(ctx, {
        type: 'radar',
        data: {
          labels: labels,
          datasets: [{
            label: 'Proficiency Score (%)',
            data: [98, 99, 96, 95, 94, 97],
            backgroundColor: 'rgba(56, 189, 248, 0.25)',
            borderColor: '#38bdf8',
            borderWidth: 2.5,
            pointBackgroundColor: '#0284c7',
            pointBorderColor: '#fff',
            pointHoverBackgroundColor: '#fff',
            pointHoverBorderColor: '#38bdf8',
            pointRadius: 4,
            pointHoverRadius: 6
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          scales: {
            r: {
              angleLines: { color: 'rgba(255, 255, 255, 0.1)' },
              grid: { color: 'rgba(255, 255, 255, 0.08)' },
              pointLabels: {
                color: '#94a3b8',
                font: { size: 11, family: 'Plus Jakarta Sans, Noto Sans TC, sans-serif', weight: '600' }
              },
              ticks: {
                display: false,
                min: 80,
                max: 100,
                stepSize: 5
              }
            }
          },
          plugins: {
            legend: { display: false },
            tooltip: {
              backgroundColor: 'rgba(15, 23, 42, 0.95)',
              titleColor: '#38bdf8',
              bodyColor: '#fff',
              borderColor: 'rgba(56, 189, 248, 0.3)',
              borderWidth: 1,
              padding: 10
            }
          }
        }
      });
    }

    // Dynamic Counter Animation
    function animateCounters() {
      const counters = document.querySelectorAll('.counter');
      counters.forEach(c => {
        const target = parseFloat(c.getAttribute('data-target'));
        const prefix = c.getAttribute('data-prefix') || '';
        const suffix = c.getAttribute('data-suffix') || '';
        let start = 0;
        const duration = 1200;
        const stepTime = 20;
        const totalSteps = duration / stepTime;
        const stepValue = target / totalSteps;

        let current = 0;
        const timer = setInterval(() => {
          current += stepValue;
          if ((stepValue > 0 && current >= target) || (stepValue < 0 && current <= target)) {
            c.textContent = `${prefix}${target}${suffix}`;
            clearInterval(timer);
          } else {
            c.textContent = `${prefix}${Math.round(current)}${suffix}`;
          }
        }, stepTime);
      });
    }

    // Theme Management
    function toggleTheme() {
      const html = document.documentElement;
      const isDark = html.classList.contains('dark');
      if (isDark) {
        html.classList.remove('dark');
        html.classList.add('light');
        document.getElementById('theme-icon').textContent = '☀️';
        localStorage.setItem('theme', 'light');
      } else {
        html.classList.remove('light');
        html.classList.add('dark');
        document.getElementById('theme-icon').textContent = '🌙';
        localStorage.setItem('theme', 'dark');
      }
      initRadarChart();
    }

    // Lightbox Helpers
    function openLightbox(src, caption) {
      document.getElementById('lightbox-img').src = src;
      document.getElementById('lightbox-caption').textContent = caption || '';
      const modal = document.getElementById('lightbox-modal');
      modal.classList.remove('hidden');
      modal.classList.add('flex');
    }

    function closeLightbox() {
      const modal = document.getElementById('lightbox-modal');
      modal.classList.add('hidden');
      modal.classList.remove('flex');
    }

    // Cover Letter Helpers
    function openCoverLetter() {
      const modal = document.getElementById('letter-modal');
      modal.classList.remove('hidden');
      modal.classList.add('flex');
    }

    function closeCoverLetter() {
      const modal = document.getElementById('letter-modal');
      modal.classList.add('hidden');
      modal.classList.remove('flex');
    }

    function copyCoverLetter() {
      const text = document.getElementById('letter-content').innerText;
      navigator.clipboard.writeText(text).then(() => {
        const toast = document.getElementById('copy-toast');
        toast.classList.remove('opacity-0');
        setTimeout(() => toast.classList.add('opacity-0'), 2500);
      });
    }

    // DATA STORE (EN, ZH, JA)
"""

# Append the DATA JSON and dynamic renderer logic from before
with open("/Users/howardliao/Desktop/Howard/Howard_CISO/build_index_html.py", "r", encoding="utf-8") as f:
    full_build_code = f.read()

# Extract DATA dictionary and functions
data_idx = full_build_code.find("const DATA = {")
end_idx = full_build_code.rfind("</script>")

data_block = full_build_code[data_idx:end_idx]

html_footer = """
    // Updated setLang with Radar Chart re-render
    const originalSetLang = setLang;
    setLang = function(lang) {
      originalSetLang(lang);
      initRadarChart();
    };

    // Initialize all dynamic elements on DOMContentLoaded
    window.addEventListener('DOMContentLoaded', () => {
      initCyberCanvas();
      const savedTheme = localStorage.getItem('theme') || 'dark';
      if (savedTheme === 'light') {
        toggleTheme();
      }
      setLang('en');
      initRadarChart();
      animateCounters();
    });
  </script>

</body>
</html>
"""

final_html = html_code + data_block + html_footer

with open(target_file, "w", encoding="utf-8") as f:
    f.write(final_html)

print(f"Successfully assembled dynamic PWA at: {target_file}")
