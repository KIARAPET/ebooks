(function () {
  var cfg = window.LP || {};
  document.getElementById('y').textContent = new Date().getFullYear();
  var track = function (ev, data) { if (window.fbq) fbq('track', ev, data || {}); };
  var info = { content_name: cfg.name, content_type: 'product', currency: cfg.currency || 'BRL' };

  // ViewContent depois de 3s na página (filtra tráfego de baixa qualidade)
  setTimeout(function () { track('ViewContent', info); }, 3000);

  // Clique no botão -> InitiateCheckout (e leva ao checkout da Hotmart)
  document.querySelectorAll('[data-cta]').forEach(function (a) {
    a.addEventListener('click', function (e) {
      track('InitiateCheckout', info);
      // repassa UTMs/fbclid para o checkout da Hotmart (atribuição)
      try {
        var u = new URL(a.href), q = new URLSearchParams(location.search);
        q.forEach(function (v, k) { if (/^(utm_|fbclid|src|sck)/.test(k)) u.searchParams.set(k, v); });
        a.href = u.toString();
      } catch (_) {}
    });
  });
})();
