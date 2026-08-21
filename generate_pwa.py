import json
import os

target_dir = "/Users/howardliao/Desktop/Howard/Howard_CISO"

# 1. manifest.json
manifest = {
    "name": "Howard Liao, Ph.D. | Group CISO Portfolio",
    "short_name": "Howard CISO",
    "description": "Group Chief Information Security Officer (CISO) | Global Cybersecurity, Digital Trust & Resilience",
    "start_url": "./index.html",
    "display": "standalone",
    "background_color": "#020617",
    "theme_color": "#0f172a",
    "orientation": "portrait-primary",
    "icons": [
        {
            "src": "assets/icon-192.png",
            "sizes": "192x192",
            "type": "image/png",
            "purpose": "any maskable"
        },
        {
            "src": "assets/icon-512.png",
            "sizes": "512x512",
            "type": "image/png",
            "purpose": "any maskable"
        }
    ]
}

with open(os.path.join(target_dir, "manifest.json"), "w", encoding="utf-8") as f:
    json.dump(manifest, f, indent=2, ensure_ascii=False)
print("Created manifest.json")

# 2. sw.js
sw_js = """// Service Worker for Howard Liao CISO Portfolio PWA
const CACHE_NAME = 'howard-ciso-pwa-v1.0.0';
const ASSETS_TO_CACHE = [
  './',
  './index.html',
  './manifest.json',
  './Howard_Liao_CISO_Resume.docx',
  './assets/howard_portrait.jpg',
  './assets/icon-192.png',
  './assets/icon-512.png',
  './assets/2024_MongoDB02.jpg',
  './assets/問題比答案重要.png',
  './assets/e等公務園__洞見機遇-雲端管理與實務01.png',
  './assets/2024_CIO報導.png',
  './assets/IThome_MangoDB.png',
  './assets/20260712_韓系證照.png',
  './assets/Oracle_認照01.png'
];

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      console.log('[Service Worker] Caching all app shell assets');
      return cache.addAll(ASSETS_TO_CACHE).catch(err => console.warn('Cache partial failure', err));
    })
  );
  self.skipWaiting();
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((keyList) => {
      return Promise.all(
        keyList.map((key) => {
          if (key !== CACHE_NAME) {
            console.log('[Service Worker] Removing old cache', key);
            return caches.delete(key);
          }
        })
      );
    })
  );
  self.clients.claim();
});

self.addEventListener('fetch', (event) => {
  if (event.request.method !== 'GET') return;
  event.respondWith(
    caches.match(event.request).then((cachedResponse) => {
      if (cachedResponse) {
        return cachedResponse;
      }
      return fetch(event.request).then((networkResponse) => {
        if (!networkResponse || networkResponse.status !== 200 || networkResponse.type !== 'basic') {
          return networkResponse;
        }
        const responseToCache = networkResponse.clone();
        caches.open(CACHE_NAME).then((cache) => {
          cache.put(event.request, responseToCache);
        });
        return networkResponse;
      }).catch(() => {
        // Fallback for offline if not found
        if (event.request.headers.get('accept').includes('text/html')) {
          return caches.match('./index.html');
        }
      });
    })
  );
});
"""

with open(os.path.join(target_dir, "sw.js"), "w", encoding="utf-8") as f:
    f.write(sw_js)
print("Created sw.js")
