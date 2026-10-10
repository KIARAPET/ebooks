(function () {
  var cfg = window.LP || {};
  var reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
  document.getElementById('y').textContent = new Date().getFullYear();

  /* ---------- Meta Pixel ---------- */
  var track = function (ev, data) { if (window.fbq) fbq('track', ev, data || {}); };
  var info = { content_name: cfg.name, content_type: 'product', currency: cfg.currency || 'BRL' };
  setTimeout(function () { track('ViewContent', info); }, 3000);
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

  /* ---------- Reveal on scroll ---------- */
  var els = document.querySelectorAll('section h2, .line, .list li, .steps li, .tile, .guarantee, details, .fmt, .final p, .band .cta');
  els.forEach(function (el, i) { el.classList.add('reveal'); el.style.setProperty('--d', (i % 4) * 0.08 + 's'); });
  if ('IntersectionObserver' in window && !reduce) {
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
    }, { threshold: 0.12 });
    els.forEach(function (el) { io.observe(el); });
    setTimeout(function () { els.forEach(function (el) { el.classList.add('in'); }); }, 6000);
  } else { els.forEach(function (el) { el.classList.add('in'); }); }

  /* ---------- Cover tilt (mouse) ---------- */
  var cover = document.querySelector('.cover');
  if (cover && !reduce && matchMedia('(pointer: fine)').matches) {
    var hero = document.querySelector('.hero');
    hero.addEventListener('mousemove', function (e) {
      var r = cover.getBoundingClientRect();
      var x = (e.clientX - (r.left + r.width / 2)) / r.width, y = (e.clientY - (r.top + r.height / 2)) / r.height;
      cover.style.transform = 'perspective(900px) rotateY(' + (x * 14) + 'deg) rotateX(' + (-y * 12) + 'deg)';
    });
    hero.addEventListener('mouseleave', function () { cover.style.transform = ''; });
  }

  /* ---------- Snow ---------- */
  var cv = document.getElementById('snow');
  if (cv && !reduce) {
    var ctx = cv.getContext('2d'), W, H, flakes = [];
    var size = function () { W = cv.width = cv.offsetWidth; H = cv.height = cv.offsetHeight; };
    size(); window.addEventListener('resize', size);
    var n = W < 600 ? 30 : 60;
    for (var i = 0; i < n; i++) flakes.push({ x: Math.random() * W, y: Math.random() * H, r: Math.random() * 2.2 + .6, s: Math.random() * .7 + .25, d: Math.random() * 6 });
    var t = 0;
    (function frame() {
      ctx.clearRect(0, 0, W, H); t += .01;
      ctx.fillStyle = 'rgba(255,255,255,.75)';
      flakes.forEach(function (f) {
        f.y += f.s; f.x += Math.sin(t + f.d) * .4;
        if (f.y > H) { f.y = -4; f.x = Math.random() * W; }
        ctx.beginPath(); ctx.arc(f.x, f.y, f.r, 0, 6.283); ctx.fill();
      });
      requestAnimationFrame(frame);
    })();
  }
})();
