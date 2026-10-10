#!/usr/bin/env python3
"""Gera as landing pages (uma pasta por ebook) a partir de products.
Edite PIXEL_ID e os dados abaixo e rode: python3 build.py"""
import os, html

PIXEL_ID = "SEU_PIXEL_ID_AQUI"  # ID do Pixel da Meta (só números)

PRODUCTS = [
 dict(slug="bolachas-biscoitos-natal", name="Bolachas & Biscoitos de Natal", emoji="🍪",
  checkout="https://pay.hotmart.com/D103367264X", price_from="", price="",
  headline="Bolachas e Biscoitos de Natal que encantam na ceia e <em>rendem dinheiro</em> na sua cozinha",
  sub="Receitas passo a passo para você fazer, presentear e vender neste Natal.",
  bullets=["Receitas práticas de bolachas e biscoitos natalinos","Passo a passo simples, mesmo para quem está começando","Ideias para montar kits e vender como presente","Aprenda a aproveitar a alta procura da época"],
  audience=["Quem quer uma renda extra no fim de ano","Quem quer surpreender a família na ceia","Quem já vende doces e quer ampliar o cardápio"]),
 dict(slug="brigadeiros-gourmet", name="Brigadeiros Gourmets: 40 Receitas para Vender", emoji="🍫",
  checkout="https://pay.hotmart.com/H102991489G", price_from="", price="",
  headline="40 receitas de <em>Brigadeiros Gourmets</em> para você fazer e vender",
  sub="Sabores que se destacam, fáceis de fazer e com ótima margem de lucro.",
  bullets=["40 receitas de brigadeiros gourmets","Sabores sofisticados com ingredientes acessíveis","Passo a passo para iniciantes","Ideal para vender em casa, em encomendas e eventos"],
  audience=["Quem quer começar a vender doces","Confeiteiras que querem novos sabores","Quem busca renda extra trabalhando de casa"]),
 dict(slug="guirlandas-natal-lucrativas", name="Guirlandas de Natal Lucrativas", emoji="🎄",
  checkout="https://pay.hotmart.com/B103367409V", price_from="", price="",
  headline="Guirlandas de Natal <em>lucrativas</em>: faça e venda na época mais forte do ano",
  sub="Aprenda a criar guirlandas lindas que todo mundo quer levar para casa.",
  bullets=["Passo a passo para criar guirlandas de Natal","Ideias para diferentes estilos e públicos","Como transformar a produção em renda extra","Conteúdo prático para começar do zero"],
  audience=["Quem quer lucrar no Natal","Quem gosta de trabalhos manuais e decoração","Quem quer um negócio com baixo investimento"]),
 dict(slug="panettones-chocottones", name="Panettones & Chocottones Trufados", emoji="🍞",
  checkout="https://pay.hotmart.com/Q103366986Y", price_from="", price="",
  headline="Panettones e Chocottones <em>Trufados</em>: o Natal lucrativo da sua cozinha",
  sub="Receitas irresistíveis para vender muito no fim de ano.",
  bullets=["Receitas de panettones e chocottones trufados","Passo a passo detalhado","Recheios e coberturas que valorizam o produto","Ideal para encomendas de Natal"],
  audience=["Quem quer faturar no Natal","Quem já faz doces e quer um produto de alto valor","Quem quer presentear com algo especial"]),
]

FAQ = [
 ("Como recebo o ebook?","Logo após a confirmação do pagamento você recebe o acesso por e-mail, direto pela Hotmart."),
 ("Preciso ter experiência?","Não. O conteúdo é explicado passo a passo, do jeito mais simples possível."),
 ("Posso vender o que aprender?","Sim, o objetivo do material é ajudar você a produzir e vender."),
 ("E se eu não gostar?","Você tem garantia de 7 dias: se não gostar, pedimos o reembolso direto na Hotmart."),
]

def esc(s): return html.escape(s, quote=True)

def page(p):
    lis = "".join(f"<li>{esc(b)}</li>" for b in p["bullets"])
    aud = "".join(f"<li>{esc(b)}</li>" for b in p["audience"])
    faq = "".join(f"<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>" for q,a in FAQ)
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
<link rel="stylesheet" href="../assets/style.css">
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
<body>
<header class="hero">
 <div class="wrap">
  <div class="emoji" aria-hidden="true">{p["emoji"]}</div>
  <h1>{p["headline"]}</h1>
  <p class="sub">{esc(p["sub"])}</p>
  {price}
  <a class="cta" href="{p["checkout"]}" data-cta>Quero meu ebook agora</a>
  <p class="safe">🔒 Compra segura pela Hotmart · Acesso imediato</p>
 </div>
</header>
<main class="wrap">
 <section><h2>O que você vai encontrar</h2><ul class="check">{lis}</ul></section>
 <section class="alt"><h2>Para quem é</h2><ul class="check">{aud}</ul>
  <a class="cta" href="{p["checkout"]}" data-cta>Quero começar agora</a></section>
 <section class="guarantee"><h2>Garantia de 7 dias</h2>
  <p>Você tem 7 dias para conferir o material. Se não ficar satisfeita(o), é só pedir o reembolso.</p></section>
 <section><h2>Perguntas frequentes</h2>{faq}</section>
 <section class="final"><h2>Garanta o seu agora</h2>
  <a class="cta" href="{p["checkout"]}" data-cta>Quero meu ebook agora</a></section>
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
idx = "".join(f'<li><a href="{p["slug"]}/">{p["emoji"]} {esc(p["name"])}</a></li>' for p in PRODUCTS)
open(os.path.join(root, "index.html"), "w", encoding="utf-8").write(
 f'<!doctype html><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex"><title>Ebooks</title><link rel="stylesheet" href="assets/style.css"><div class="wrap" style="padding:40px 20px"><h1>Landing pages</h1><ul>{idx}</ul></div>')
print("ok")
