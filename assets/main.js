(function () {
  var cfg = window.LP || {};
  document.getElementById('y').textContent = new Date().getFullYear();
  var track = function (ev, data) { if (window.fbq) fbq('track', ev, data || {}); };
  var info = { content_name: cfg.name, content_type: 'product', currency: cfg.currency || 'BRL' };

  // ViewContent after 3s on the page (filters low quality traffic)
  setTimeout(function () { track('ViewContent', info); }, 3000);

  // CTA click: InitiateCheckout, then pass UTMs/fbclid on to the Hotmart checkout
  document.querySelectorAll('[data-cta]').forEach(function (a) {
    a.addEventListener('click', function () {
      track('InitiateCheckout', info);
      try {
        var u = new URL(a.href), q = new URLSearchParams(location.search);
        q.forEach(function (v, k) { if (/^(utm_|fbclid|src|sck)/.test(k)) u.searchParams.set(k, v); });
        a.href = u.toString();
      } catch (_) {}
    });
  });
})();
