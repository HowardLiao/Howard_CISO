// Service Worker for Howard Liao CISO Portfolio PWA
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
