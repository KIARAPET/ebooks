#!/usr/bin/env python3
"""Gera as landing pages (uma pasta por ebook) a partir de products.
Edite PIXEL_ID e os dados abaixo e rode: python3 build.py"""
import os, html

PIXEL_ID = "SEU_PIXEL_ID_AQUI"  # ID do Pixel da Meta (só números)

PRODUCTS = [
 dict(slug="bolachas-biscoitos-natal", art="cookies", c1="#3a0a16", c2="#ff4d6d", c3="#ffc46b", snow=True, name="Bolachas & Biscoitos de Natal", emoji="🍪",
  checkout="https://pay.hotmart.com/D103367264X", price_from="", price="",
  headline="Bolachas e Biscoitos de Natal que encantam na ceia e <em>rendem dinheiro</em> na sua cozinha",
  sub="Receitas passo a passo para você fazer, presentear e vender neste Natal.",
  bullets=["Receitas práticas de bolachas e biscoitos natalinos","Passo a passo simples, mesmo para quem está começando","Ideias para montar kits e vender como presente","Aprenda a aproveitar a alta procura da época"],
  audience=["Quem quer uma renda extra no fim de ano","Quem quer surpreender a família na ceia","Quem já vende doces e quer ampliar o cardápio"]),
 dict(slug="brigadeiros-gourmet", art="brigadeiros", c1="#2a0a3a", c2="#ff4fa3", c3="#ffb86b", snow=False, name="Brigadeiros Gourmets: 40 Receitas para Vender", emoji="🍫",
  checkout="https://pay.hotmart.com/H102991489G", price_from="", price="",
  headline="Transforme brigadeiros em <em>renda todo mês</em>, direto da sua cozinha",
  sub="Mais de 40 receitas organizadas em linhas de sabores, como uma confeitaria profissional. Mesmo começando do zero.",
  bullets=["Mais de 40 receitas de brigadeiros gourmets em 6 linhas de sabores",
           "Módulo especial de Coxinhas Doces, campeãs de venda nas caixinhas gourmet",
           "Módulo bônus com ponto, conservação, preço de venda, kits e embalagens",
           "Trabalhe na sua cozinha, no seu tempo, com sabores que fazem o cliente salivar"],
  lines=[("Linha Tradicional","Brigadeiro, beijinho, casadinho, churros, sensação, M&M, prestígio e outros clássicos que não podem faltar."),
         ("Linha Premium","Belga, ferrero/avelã, pistache, nutella, oreo, cappuccino, café e sabores com cara de vitrine chique."),
         ("Linha Ninho & Recheados","Ninho, ninho brûlée, ninho trufado, ninho com Nutella, ninho com morango e outras combinações super cremosas."),
         ("Linha Frutas","Maracujá, limão siciliano, laranja, maçã, banoffe, surpresa de uva, bicho de pé e coxinha de brigadeiro com morango."),
         ("Linha Crocantes & Castanhas","Paçoca, amendoim, milho verde, abóbora, pé de moça, nozes, ovomaltine crocante e muito mais."),
         ("Linha Adulta (18+)","Brigadeiro de caipirinha e de amarula/licor de café, perfeitos para festas e eventos."),
         ("Módulo Coxinhas Doces","Coxinha de brigadeiro com morango e coxinha de leite ninho com morango, campeãs de vendas nas caixinhas gourmet.")],
  final="Comece hoje a montar o seu cardápio de brigadeiros gourmet.",
  bonus_title="Módulo bônus: aprenda a vender",
  bonus=["Ponto ideal do brigadeiro para enrolar e vender",
         "Validade, conservação e congelamento para não perder produto",
         "Uma forma simples de calcular o preço de venda, sem complicar",
         "Sugestões prontas de kits com 100 unidades por linha: tradicional, kids, premium, ninho, frutas, crocantes e alcoólicos",
         "Ideias de apresentação e embalagens para deixar seus doces com cara de loja"],
  audience=["Quem quer sair do básico e montar um verdadeiro cardápio de confeitaria","Quem quer uma renda todo mês trabalhando em casa, mesmo começando do zero","Quem ama cozinha e quer ouvir: \"meu Deus, que brigadeiro é esse?\""],
  format="Se você quer aumentar seu cardápio e ouvir seus clientes dizendo “meu Deus, que brigadeiro é esse?” e “essa coxinha de morango é perfeita!”, esse e-book foi feito pra você."),
 dict(slug="guirlandas-natal-lucrativas", art="wreath", c1="#06301f", c2="#2ee59d", c3="#ff5a6e", snow=True, name="Guirlandas de Natal Lucrativas", emoji="🎄",
  checkout="https://pay.hotmart.com/B103367409V", price_from="", price="",
  headline="Guirlandas de Natal <em>lucrativas</em>: faça e venda na época mais forte do ano",
  sub="Aprenda a criar guirlandas lindas que todo mundo quer levar para casa.",
  bullets=["Passo a passo para criar guirlandas de Natal","Ideias para diferentes estilos e públicos","Como transformar a produção em renda extra","Conteúdo prático para começar do zero"],
  audience=["Quem quer lucrar no Natal","Quem gosta de trabalhos manuais e decoração","Quem quer um negócio com baixo investimento"]),
 dict(slug="panettones-chocottones", art="panettone", c1="#2b0a1f", c2="#ffc46b", c3="#ff6fa0", snow=True, name="Panettones & Chocottones Trufados", emoji="🍞",
  checkout="https://pay.hotmart.com/Q103366986Y", price_from="", price="",
  headline="Panettones e Chocottones <em>fofinhos, trufados</em> e com cara de confeitaria",
  sub="Massa 100% caseira e recheios simples de preparar: para presentear, enfeitar a ceia ou faturar no fim de ano.",
  bullets=["Massa base de panettone/chocottone feita do zero, sem mistura pronta",
           "Passo a passo de fermentação, descanso e assamento para não murchar",
           "Chocottone trufado de morango",
           "Panettone trufado de doce de leite com nozes",
           "Chocottone trufado de Ninho com Nutella",
           "Sugestões de outros sabores para variar seu cardápio",
           "Dicas de montagem, corte, recheio, cobertura e acabamento",
           "Ideias de embalagem e apresentação para presentear ou vender"],
  audience=["Donas de casa que querem uma mesa linda sem depender de produtos caros de mercado",
            "Iniciantes na confeitaria que querem começar por uma receita campeã de vendas",
            "Empreendedoras da cozinha que desejam incluir panettones e chocottones trufados no cardápio de Natal"],
  format="Você recebe 1 mini e-book digital em PDF, organizado, direto ao ponto e pronto para te acompanhar na cozinha. Comece hoje a produzir panettones e chocottones que encantam no olhar, na primeira fatia… e no bolso. 💛🎄"),
]

FAQ = [
 ("Como recebo o ebook?","Logo após a confirmação do pagamento você recebe o acesso por e-mail, direto pela Hotmart."),
 ("Preciso ter experiência?","Não. O conteúdo é explicado passo a passo, do jeito mais simples possível."),
 ("Posso vender o que aprender?","Sim, o objetivo do material é ajudar você a produzir e vender."),
 ("E se eu não gostar?","Você tem garantia de 7 dias: se não gostar, pedimos o reembolso direto na Hotmart."),
]
STEPS = [("Faça a compra","Pagamento seguro pela Hotmart."),("Receba por e-mail","O acesso chega logo após a confirmação."),("Coloque a mão na massa","Siga o passo a passo e comece a produzir.")]

ART = {
"cookies": '''<circle cx="70" cy="76" r="44" fill="#d9a066"/><circle cx="70" cy="76" r="34" fill="none" stroke="#fff" stroke-width="5" stroke-dasharray="3 9" stroke-linecap="round"/><circle cx="70" cy="76" r="9" fill="#c8283c"/>
<polygon points="140,90 150,118 180,118 156,136 165,164 140,147 115,164 124,136 100,118 130,118" fill="#e8b878"/><polygon points="140,104 145,118 160,118 148,127 153,141 140,132 127,141 132,127 120,118 135,118" fill="#fff"/>
<polygon points="60,112 90,150 74,150 100,184 20,184 46,150 30,150" fill="#d9a066" transform="translate(10 -4) scale(.9)"/><polygon points="68,134 82,150 72,150 86,170 44,170 58,150 50,150" fill="#2f8f5b" transform="translate(10 -4) scale(.9)" opacity=".9"/><circle cx="64" cy="140" r="3" fill="#fff"/><circle cx="58" cy="156" r="3" fill="#e0a43a"/>''',
"brigadeiros": '''<g><path d="M20 130 L36 188 H84 L100 130Z" fill="#b8860b" opacity=".35"/><circle cx="60" cy="112" r="34" fill="#4a2a1a"/><g fill="#fff"><rect x="42" y="96" width="8" height="3" rx="1.5" transform="rotate(30 46 97)"/><rect x="62" y="88" width="8" height="3" rx="1.5" transform="rotate(-20 66 89)"/><rect x="70" y="110" width="8" height="3" rx="1.5" transform="rotate(60 74 111)"/><rect x="48" y="118" width="8" height="3" rx="1.5" transform="rotate(-50 52 119)"/></g></g>
<g><path d="M104 140 L116 190 H164 L176 140Z" fill="#b8860b" opacity=".35"/><circle cx="140" cy="122" r="32" fill="#e58fa5"/><g fill="#fff"><circle cx="128" cy="112" r="3"/><circle cx="148" cy="108" r="3"/><circle cx="150" cy="130" r="3"/><circle cx="130" cy="132" r="3"/></g></g>
<g><circle cx="100" cy="60" r="30" fill="#f6eee3"/><g fill="#d9c7ad"><circle cx="90" cy="52" r="3"/><circle cx="108" cy="50" r="3"/><circle cx="100" cy="68" r="3"/><circle cx="116" cy="66" r="3"/><circle cx="84" cy="68" r="3"/></g></g>''',
"wreath": '''<circle cx="100" cy="100" r="58" fill="none" stroke="#1f6b45" stroke-width="30"/><circle cx="100" cy="100" r="58" fill="none" stroke="#2f8f5b" stroke-width="16" stroke-dasharray="10 6"/>
<g fill="#d1344a"><circle cx="52" cy="78" r="6"/><circle cx="148" cy="70" r="6"/><circle cx="150" cy="130" r="6"/><circle cx="60" cy="140" r="6"/><circle cx="100" cy="44" r="6"/></g><g fill="#fff"><circle cx="76" cy="52" r="3"/><circle cx="130" cy="150" r="3"/><circle cx="44" cy="110" r="3"/></g>
<path d="M100 150 L74 176 L92 158Z M100 150 L126 176 L108 158Z" fill="#a31d33"/><circle cx="100" cy="152" r="9" fill="#d1344a"/>''',
"panettone": '''<path d="M44 190 V110 C44 52 156 52 156 110 V190Z" fill="#d9a066"/><path d="M50 106 C50 62 150 62 150 106 C130 96 120 112 100 100 C80 112 70 96 50 106Z" fill="#fff" opacity=".95"/><path d="M44 190 V150 H156 V190Z" fill="#a31d33"/><path d="M44 150 H156" stroke="#e0a43a" stroke-width="5"/>
<g fill="#e0a43a"><circle cx="100" cy="84" r="4"/><circle cx="78" cy="94" r="3"/><circle cx="122" cy="94" r="3"/></g><g fill="#5a1830"><circle cx="70" cy="126" r="4"/><circle cx="104" cy="122" r="4"/><circle cx="130" cy="132" r="4"/></g>''',
}
GALLERY = {
 "panettones-chocottones": [("Chocottone trufado de morango","#f7c6cf"),("Panettone trufado de doce de leite com nozes","#f0c98a"),("Chocottone trufado de Ninho com Nutella","#e9dcc8")],
 "brigadeiros-gourmet": [("Sabores variados","#f2d3c4"),("Caixas para presentear e vender","#e6c3cf"),("Cores e texturas","#ead9bf"),("Acabamento de confeitaria","#f0c9d6")],
 "bolachas-biscoitos-natal": [("Biscoitos natalinos","#f3d9b5"),("Kits para presente","#f1c9c9"),("Venda na época forte","#e5d3b8")],
 "guirlandas-natal-lucrativas": [("Guirlandas de Natal","#cfe6d4"),("Estilos para cada público","#f3d2d6"),("Renda extra","#dbead9")],
}
CHECK = '<svg viewBox="0 0 20 20" width="20" height="20" aria-hidden="true"><circle cx="10" cy="10" r="10" fill="currentColor" opacity=".15"/><path d="M5.5 10.5l3 3 6-7" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>'

def esc(s): return html.escape(s, quote=True)

def cover(p, big=True):
    # Capa real: se existir assets/img/<slug>.webp|jpg|png, ela substitui a ilustracao.
    for ext in ("webp", "jpg", "png"):
        if os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "img", f'{p["slug"]}.{ext}')):
            return f'<div class="cover photo"><img src="../assets/img/{p["slug"]}.{ext}" alt="Capa do ebook {esc(p["name"])}"></div>'
    # Troque pela capa real: salve assets/img/<slug>.jpg (ou .png) e rode build.py de novo.
    return f'''<div class="cover" role="img" aria-label="Capa do ebook {esc(p["name"])}">
<div class="book"><div class="spine"></div><div class="face"><span class="tag">E-BOOK</span>
<svg viewBox="0 0 200 200" class="art" aria-hidden="true">{ART[p["art"]]}</svg>
<strong>{esc(p["name"])}</strong></div></div>
<img class="real" src="../assets/img/{p["slug"]}.jpg" alt="" onerror="this.remove()"></div>'''

def gallery(p):
    tiles = ""
    root = os.path.dirname(os.path.abspath(__file__))
    for i,(label,bg) in enumerate(GALLERY[p["slug"]], 1):
        photo = next((f'../assets/img/{p["slug"]}-{i}.{e}' for e in ("jpg","webp","png")
                      if os.path.exists(os.path.join(root,"assets","img",f'{p["slug"]}-{i}.{e}'))), None)
        inner = (f'<img src="{photo}" alt="{esc(label)}" loading="lazy">' if photo else
                 f'<svg viewBox="0 0 200 200" aria-hidden="true" style="transform:rotate({(-6,5,-3,4)[i-1]}deg) scale({(1,1.08,.96,1.02)[i-1]})">{ART[p["art"]]}</svg>')
        tiles += f'<figure class="tile" style="--bg-t:{bg}"><div class="tile-img">{inner}</div><figcaption>{esc(label)}</figcaption></figure>'
    return f'<section class="wrap"><h2>Uma prévia do que você vai criar</h2><div class="gallery n{len(GALLERY[p["slug"]])}">{tiles}</div></section>'

def page(p):
    lis = "".join(f'<li>{CHECK}<span>{esc(b)}</span></li>' for b in p["bullets"])
    aud = "".join(f'<li>{CHECK}<span>{esc(b)}</span></li>' for b in p["audience"])
    faq = "".join(f"<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>" for q,a in FAQ)
    steps = "".join(f'<li><b>{i+1}</b><div><strong>{esc(t)}</strong><span>{esc(d)}</span></div></li>' for i,(t,d) in enumerate(STEPS))
    snow = '<canvas id="snow" aria-hidden="true"></canvas>' if p.get("snow") else ""
    lines_html = ""
    if p.get("lines"):
        cards = "".join(f'<div class="line"><h3>{esc(t)}</h3><p>{esc(d)}</p></div>' for t,d in p["lines"])
        lines_html = f'<section class="wrap"><h2>Linhas de sabores</h2><div class="lines">{cards}</div></section>'
    bonus_html = ""
    if p.get("bonus"):
        bl = "".join(f'<li>{CHECK}<span>{esc(b)}</span></li>' for b in p["bonus"])
        bonus_html = f'<section class="wrap"><h2>{esc(p["bonus_title"])}</h2><ul class="list grid">{bl}</ul></section>'
    fmt = f'<p class="fmt">{esc(p["format"])}</p>' if p.get("format") else ""
    price = ""
    if p["price"]:
        old = f'<s>De {esc(p["price_from"])}</s>' if p["price_from"] else ""
        price = f'<div class="price">{old}<strong>por apenas {esc(p["price"])}</strong></div>'
    return f"""<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(p["name"])}</title>
<meta name="description" content="{esc(p["sub"])}">
<meta property="og:title" content="{esc(p["name"])}">
<meta property="og:description" content="{esc(p["sub"])}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&family=Sora:wght@600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../assets/style.css">
<script>document.documentElement.className="js"</script>
<!-- Meta Pixel Code -->
<script>
!function(f,b,e,v,n,t,s){{if(f.fbq)return;n=f.fbq=function(){{n.callMethod?
n.callMethod.apply(n,arguments):n.queue.push(arguments)}};if(!f._fbq)f._fbq=n;
n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;
t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}}(window,
document,'script','https://connect.facebook.net/en_US/fbevents.js');
fbq('init', '{PIXEL_ID}');
fbq('track', 'PageView');
</script>
<noscript><img height="1" width="1" style="display:none" src="https://www.facebook.com/tr?id={PIXEL_ID}&ev=PageView&noscript=1"/></noscript>
<!-- End Meta Pixel Code -->
<script>window.LP={{name:{p["name"]!r},checkout:"{p["checkout"]}",value:0,currency:"BRL"}};</script>
</head>
<body style="--c1:{p["c1"]};--c2:{p["c2"]};--c3:{p["c3"]}">
<div class="topbar">{"Especial de Natal · " if p.get("snow") else ""}Receitas para presentear e vender</div>
<header class="hero">{snow}<i class="orb o1"></i><i class="orb o2"></i><div class="wrap hero-grid">
 <div class="hero-text">
  <h1>{p["headline"]}</h1>
  <p class="sub">{esc(p["sub"])}</p>
  {price}
  <a class="cta" href="{p["checkout"]}" data-cta>Quero meu ebook agora</a>
  <ul class="trust"><li>Compra segura</li><li>Acesso imediato</li><li>Garantia de 7 dias</li></ul>
 </div>
 <div class="hero-art">{cover(p)}</div>
</div></header>
<main>
 <section class="wrap"><h2>O que você vai encontrar</h2><ul class="list grid">{lis}</ul>{fmt}</section>
 {lines_html}
 {gallery(p)}
 {bonus_html}
 <section class="band"><div class="wrap"><h2>Para quem é</h2><ul class="list">{aud}</ul>
  <a class="cta" href="{p["checkout"]}" data-cta>Quero começar agora</a></div></section>
 <section class="wrap"><h2>Como funciona</h2><ol class="steps">{steps}</ol></section>
 <section class="wrap"><div class="guarantee"><div class="seal">7<small>dias</small></div><div><h2>Garantia incondicional</h2>
  <p>Você tem 7 dias para conferir o material. Se não gostar, é só pedir o reembolso pela Hotmart.</p></div></div></section>
 <section class="wrap narrow"><h2>Perguntas frequentes</h2>{faq}</section>
 <section class="final"><div class="wrap"><h2>Garanta o seu agora</h2><p>{esc(p.get("final","Comece hoje e deixe o seu Natal mais doce."))}</p>
  <a class="cta" href="{p["checkout"]}" data-cta>Quero meu ebook agora</a></div></section>
</main>
<footer><div class="wrap"><p>© <span id="y"></span> · {esc(p["name"])}. Produto digital, entrega por e-mail via Hotmart. Os resultados dependem da dedicação de cada pessoa.</p></div></footer>
<div class="sticky"><a class="cta" href="{p["checkout"]}" data-cta>Quero meu ebook</a></div>
<script src="../assets/main.js"></script>
</body>
</html>
"""

root = os.path.dirname(os.path.abspath(__file__))
for p in PRODUCTS:
    d = os.path.join(root, p["slug"]); os.makedirs(d, exist_ok=True)
    open(os.path.join(d, "index.html"), "w", encoding="utf-8").write(page(p))
idx = "".join(f'<li><a href="{p["slug"]}/">{esc(p["name"])}</a></li>' for p in PRODUCTS)
open(os.path.join(root, "index.html"), "w", encoding="utf-8").write(
 f'<!doctype html><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex"><title>Ebooks</title><div style="max-width:560px;margin:40px auto;padding:0 20px;font-family:system-ui"><h1>Landing pages</h1><ul>{idx}</ul></div>')
print("ok")
