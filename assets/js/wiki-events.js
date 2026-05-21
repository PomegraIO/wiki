/* Pomegra Wiki — custom Umami analytics events.
 *
 * Mirrors the Docusaurus client module that /learn ships (books/_shared/
 * umami-events.js), adapted to a static Hugo site: no router lifecycle,
 * just one page = one session = one finalize on pagehide.
 *
 * Events emitted (see https://docs.umami.is/docs/tracker-functions):
 *   scroll-depth          — {depth, path} at 25/50/75/90/100%
 *   heartbeat             — {activeSeconds, scroll, path} every 15s while engaged
 *   engagement-summary    — {reason, activeSeconds, totalSeconds, maxScroll, depths, readingComplete}
 *   page-idle / page-resume
 *   tab-hidden / tab-visible
 *   reading-complete      — when <article> bottom enters viewport
 *   external-link-click   — {href, host, text} (off-site links)
 *   internal-link-click   — {href, text} (within /wiki/ — useful for cross-link graph)
 *   cross-property-click  — {to: 'learn'|'home'} (anchors with data-umami-event="cross-property-click")
 *   anchor-click          — {anchor}
 *   download-click        — {href, file}
 *   text-copy / text-select — {length}
 *   theme-toggle          — {from, to}
 *   page-print
 *   search-open           — fired on first focus of the search input
 *   search-query          — {q} debounced (1s after last keystroke, if any results)
 *   search-result-click   — {q, to}
 *   random-article        — {to}
 */
(function () {
  if (typeof window === 'undefined') return;

  var SCROLL_THRESHOLDS = [25, 50, 75, 90, 100];
  var HEARTBEAT_MS = 15000;
  var IDLE_MS = 60000;
  var TEXT_SELECT_MIN_CHARS = 20;
  var TEXT_SELECT_THROTTLE_MS = 2000;
  var SEARCH_DEBOUNCE_MS = 1000;

  var state = freshState();
  var queue = [];
  var heartbeatTimer = null;
  var themeObserver = null;
  var searchTimer = null;

  function freshState() {
    return {
      path: location.pathname,
      startTime: Date.now(),
      activeMs: 0,
      lastTickAt: Date.now(),
      lastActivityAt: Date.now(),
      idle: false,
      maxScrollPct: 0,
      scrollThresholdsFired: {},
      readingComplete: false,
      selectFiredAt: 0,
      finalized: false,
      searchOpened: false
    };
  }

  function flushQueue() {
    if (!window.umami) return;
    while (queue.length) {
      var pair = queue.shift();
      try {
        if (pair[1] !== undefined) window.umami.track(pair[0], pair[1]);
        else window.umami.track(pair[0]);
      } catch (_) { /* drop */ }
    }
  }

  function track(name, data) {
    var u = window.umami;
    if (!u || typeof u.track !== 'function') {
      queue.push([name, data]);
      if (queue.length > 50) queue.shift();
      return;
    }
    flushQueue();
    try {
      if (data !== undefined) u.track(name, data);
      else u.track(name);
    } catch (_) { /* drop */ }
  }

  function scrollPct() {
    var doc = document.documentElement;
    var h = doc.scrollHeight - doc.clientHeight;
    if (h <= 0) return 100;
    var pct = (window.scrollY / h) * 100;
    return Math.max(0, Math.min(100, Math.round(pct)));
  }

  function markActive() {
    var now = Date.now();
    state.lastActivityAt = now;
    if (state.idle) {
      state.idle = false;
      track('page-resume', { path: state.path });
      state.lastTickAt = now;
    }
  }

  function onScroll() {
    if (state.finalized) return;
    markActive();
    var pct = scrollPct();
    if (pct > state.maxScrollPct) state.maxScrollPct = pct;
    for (var i = 0; i < SCROLL_THRESHOLDS.length; i++) {
      var t = SCROLL_THRESHOLDS[i];
      if (pct >= t && !state.scrollThresholdsFired[t]) {
        state.scrollThresholdsFired[t] = 1;
        track('scroll-depth', { depth: t, path: state.path });
      }
    }
    if (!state.readingComplete) {
      var article = document.querySelector('article');
      var done = false;
      if (article) {
        var rect = article.getBoundingClientRect();
        done = rect.bottom <= window.innerHeight + 200;
      } else {
        done = pct >= 95;
      }
      if (done) {
        state.readingComplete = true;
        track('reading-complete', {
          path: state.path,
          seconds: Math.round((Date.now() - state.startTime) / 1000)
        });
      }
    }
  }

  function tickHeartbeat() {
    if (!state || state.finalized) return;
    var now = Date.now();
    var dt = now - state.lastTickAt;
    state.lastTickAt = now;
    var sinceActivity = now - state.lastActivityAt;
    var visible = document.visibilityState === 'visible';
    if (!state.idle && sinceActivity > IDLE_MS) {
      state.idle = true;
      track('page-idle', {
        path: state.path,
        activeSeconds: Math.round(state.activeMs / 1000)
      });
    }
    if (visible && !state.idle) {
      state.activeMs += dt;
      track('heartbeat', {
        path: state.path,
        activeSeconds: Math.round(state.activeMs / 1000),
        scroll: state.maxScrollPct
      });
    }
  }

  function finalize(reason) {
    if (!state || state.finalized) return;
    state.finalized = true;
    var now = Date.now();
    if (document.visibilityState === 'visible' && !state.idle) {
      state.activeMs += now - state.lastTickAt;
    }
    var depths = [];
    for (var k in state.scrollThresholdsFired) depths.push(k);
    depths.sort(function (a, b) { return a - b; });
    track('engagement-summary', {
      path: state.path,
      reason: reason,
      activeSeconds: Math.round(state.activeMs / 1000),
      totalSeconds: Math.round((now - state.startTime) / 1000),
      maxScroll: state.maxScrollPct,
      depths: depths.join(','),
      readingComplete: state.readingComplete
    });
  }

  function onVisibility() {
    if (document.visibilityState === 'hidden') {
      track('tab-hidden', { path: state.path });
      finalize('tab-hidden');
    } else {
      track('tab-visible', { path: state.path });
      if (state.finalized) {
        state = freshState();
        if (heartbeatTimer) clearInterval(heartbeatTimer);
        heartbeatTimer = setInterval(tickHeartbeat, HEARTBEAT_MS);
      }
    }
  }

  function onClick(e) {
    markActive();
    var link = e.target && e.target.closest ? e.target.closest('a[href]') : null;
    if (!link) return;
    var href = link.getAttribute('href') || '';
    if (!href) return;

    // declarative cross-property clicks (Pomegra.io / Learn nav)
    var crossTo = link.getAttribute('data-umami-event-to');
    if (link.getAttribute('data-umami-event') === 'cross-property-click' && crossTo) {
      track('cross-property-click', { to: crossTo, href: href, path: state.path });
      return;
    }

    if (href.charAt(0) === '#') {
      track('anchor-click', { anchor: href, path: state.path });
      return;
    }
    var url;
    try { url = new URL(href, location.href); } catch (_) { return; }
    var isDownload = link.hasAttribute('download') ||
      /\.(pdf|zip|csv|xlsx?|docx?|pptx?|epub)$/i.test(url.pathname);
    if (isDownload) {
      track('download-click', {
        href: url.href,
        file: url.pathname.split('/').pop(),
        path: state.path
      });
      return;
    }
    if (url.origin !== location.origin) {
      track('external-link-click', {
        href: url.href,
        host: url.host,
        text: (link.textContent || '').trim().slice(0, 80),
        path: state.path
      });
    } else if (link.closest('.wiki-prose')) {
      // Internal cross-link inside an article body. Sampled (10%) to keep
      // payload small at 10k entries — full graph still recoverable.
      if (Math.random() < 0.1) {
        track('internal-link-click', {
          href: url.pathname,
          text: (link.textContent || '').trim().slice(0, 80),
          path: state.path
        });
      }
    } else if (link.closest('.wiki-search-results')) {
      var sin = document.getElementById('pom-search-input');
      track('search-result-click', {
        q: sin ? sin.value.slice(0, 80) : '',
        to: url.pathname,
        path: state.path
      });
    }
  }

  function onCopy() {
    markActive();
    var sel = window.getSelection && window.getSelection();
    if (!sel) return;
    var text = sel.toString();
    if (!text) return;
    track('text-copy', { length: text.length, path: state.path });
  }

  function onSelectionChange() {
    var now = Date.now();
    if (now - state.selectFiredAt < TEXT_SELECT_THROTTLE_MS) return;
    var sel = window.getSelection && window.getSelection();
    if (!sel) return;
    var text = sel.toString();
    if (text && text.length >= TEXT_SELECT_MIN_CHARS) {
      state.selectFiredAt = now;
      track('text-select', { length: text.length, path: state.path });
    }
  }

  function onKey() { markActive(); }
  function onMouse() { markActive(); }
  function onPrint() { track('page-print', { path: state.path }); }

  function watchThemeToggle() {
    if (themeObserver) return;
    var last = document.documentElement.getAttribute('data-theme') || 'light';
    themeObserver = new MutationObserver(function () {
      var now = document.documentElement.getAttribute('data-theme') || 'light';
      if (now !== last) {
        track('theme-toggle', { from: last, to: now, path: state.path });
        last = now;
      }
    });
    themeObserver.observe(document.documentElement, {
      attributes: true,
      attributeFilter: ['data-theme']
    });
  }

  function attachSearchEvents() {
    var input = document.getElementById('pom-search-input');
    if (!input) return;
    input.addEventListener('focus', function () {
      if (!state.searchOpened) {
        state.searchOpened = true;
        track('search-open', { path: state.path });
      }
    });
    input.addEventListener('input', function () {
      if (searchTimer) clearTimeout(searchTimer);
      searchTimer = setTimeout(function () {
        var q = input.value.trim();
        if (!q) return;
        var box = document.getElementById('pom-search-results');
        var hits = box ? box.querySelectorAll('.wiki-search-result').length : 0;
        track('search-query', { q: q.slice(0, 80), hits: hits, path: state.path });
      }, SEARCH_DEBOUNCE_MS);
    });
  }

  function start() {
    window.addEventListener('scroll', onScroll, { passive: true });
    window.addEventListener('click', onClick, true);
    window.addEventListener('keydown', onKey, true);
    window.addEventListener('mousemove', onMouse, { passive: true });
    window.addEventListener('touchstart', onMouse, { passive: true });
    document.addEventListener('visibilitychange', onVisibility);
    document.addEventListener('copy', onCopy);
    document.addEventListener('selectionchange', onSelectionChange);
    window.addEventListener('beforeprint', onPrint);
    window.addEventListener('pagehide', function () { finalize('pagehide'); });
    window.addEventListener('beforeunload', function () { finalize('beforeunload'); });
    watchThemeToggle();
    attachSearchEvents();
    if (heartbeatTimer) clearInterval(heartbeatTimer);
    heartbeatTimer = setInterval(tickHeartbeat, HEARTBEAT_MS);
    onScroll(); // seed scroll bookkeeping for deep-linked landings
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', start);
  } else {
    start();
  }
})();
