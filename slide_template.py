"""
slide_template.py — monta o HTML de um slide a partir do JSON de layout.

O HTML usa a paleta e tipografia oficiais da Tâmara. Cada slide é renderizado
em 1080x1350 (Instagram 4:5). Hex codes, fontes e coordenadas NUNCA aparecem
como texto visível — só os campos de conteúdo (titulo, corpo, lista, eyebrow, cta).
"""

# Paleta oficial (fallback caso o JSON não traga o branding.palette)
PALETTE_DEFAULT = {
    "background": "#FAF7F2",
    "surface": "#F5F1EA",
    "surface_dark": "#2C3B2D",
    "primary": "#1E1E1E",
    "accent": "#B8955A",
    "accent_light": "#D4AF7A",
    "muted": "#7A7267",
    "border": "rgba(184,149,90,0.25)",
}

FONTS_LINK = (
    '<link href="https://fonts.googleapis.com/css2?'
    'family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;1,300;1,400&'
    'family=Jost:wght@300;400;500&display=swap" rel="stylesheet">'
)


def _italic_highlight(titulo: str, destaque: str, accent: str) -> str:
    """Envolve a palavra-chave em itálico dourado dentro do título."""
    if destaque and destaque in titulo:
        span = f'<em style="font-style:italic;color:{accent};">{destaque}</em>'
        return titulo.replace(destaque, span, 1)
    return titulo


def build_html(layout: dict, branding: dict) -> str:
    pal = {**PALETTE_DEFAULT, **(branding.get("palette") or {})}
    fundo_key = layout.get("fundo", "background")
    fundo = pal.get(fundo_key, pal["background"])
    is_dark = fundo_key == "surface_dark"

    # cores de texto conforme fundo claro/escuro
    titulo_cor = pal["accent_light"] if is_dark else pal["surface_dark"]
    corpo_cor = pal["background"] if is_dark else pal["muted"]
    eyebrow_cor = pal["accent_light"] if is_dark else pal["accent"]
    accent = pal["accent_light"] if is_dark else pal["accent"]

    parts = []

    # eyebrow (label superior com traço)
    eb = layout.get("eyebrow")
    if eb:
        parts.append(
            f'<div class="eyebrow" style="color:{eyebrow_cor};">'
            f'<span class="dash" style="background:{eyebrow_cor};"></span>'
            f'{eb.get("texto","")}</div>'
        )

    # titulo (com destaque em itálico dourado)
    t = layout.get("titulo")
    if t:
        texto = _italic_highlight(t.get("texto", ""), t.get("destaque_italico_dourado", ""), accent)
        parts.append(f'<h1 style="color:{titulo_cor};">{texto}</h1>')

    # divisor dourado
    if layout.get("divisor"):
        parts.append(f'<div class="divider" style="background:{accent};"></div>')

    # corpo
    c = layout.get("corpo")
    if c:
        op = c.get("opacidade", 1)
        parts.append(f'<p class="corpo" style="color:{corpo_cor};opacity:{op};">{c.get("texto","")}</p>')

    # lista elegante
    li = layout.get("lista")
    if li:
        itens = "".join(
            f'<li style="border-color:{pal["border"]};color:{pal["primary"] if not is_dark else pal["background"]};">{x}</li>'
            for x in li.get("itens", [])
        )
        parts.append(f'<ul class="lista">{itens}</ul>')

    # cta visual (caixa com borda dourada)
    cta = layout.get("cta_visual")
    if cta:
        parts.append(
            f'<div class="cta" style="color:{pal["accent_light"]};border-color:{accent};">'
            f'{cta.get("texto","")}</div>'
        )

    # assinatura da marca (frase-síntese)
    if layout.get("assinatura_marca"):
        parts.append(
            f'<div class="assinatura-marca" style="color:{accent};">{layout["assinatura_marca"]}</div>'
        )

    # número ornamental
    num = layout.get("numero_ornamental")
    num_html = ""
    if num:
        num_html = (
            f'<div class="ornamento-num" style="color:{accent};opacity:{num.get("opacidade",0.45)};">'
            f'{num.get("texto","")}</div>'
        )

    # ornamento de canto (borda dupla)
    corner = ""
    if layout.get("ornamento_canto"):
        corner = f'<div class="corner" style="border-color:{accent};"></div>'

    # assinatura @ (rodapé)
    handle = branding.get("assinatura", "")
    handle_html = (
        f'<div class="handle" style="color:{pal["muted"] if not is_dark else pal["accent_light"]};">{handle}</div>'
        if handle else ""
    )

    body = "\n".join(parts)

    return f"""<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8">{FONTS_LINK}
<style>
  * {{ margin:0; padding:0; box-sizing:border-box; }}
  html,body {{ width:1080px; height:1350px; }}
  body {{
    background:{fundo};
    font-family:'Jost',sans-serif; font-weight:300;
    padding:110px 96px; position:relative; overflow:hidden;
    display:flex; flex-direction:column; justify-content:center;
  }}
  .eyebrow {{
    font-family:'Jost',sans-serif; font-size:24px; font-weight:400;
    letter-spacing:0.22em; text-transform:uppercase;
    display:flex; align-items:center; gap:18px; margin-bottom:40px;
  }}
  .eyebrow .dash {{ display:block; width:48px; height:1px; }}
  h1 {{
    font-family:'Cormorant Garamond',serif; font-weight:300;
    font-size:88px; line-height:1.1; margin-bottom:18px;
  }}
  .divider {{ width:64px; height:1px; margin:36px 0; }}
  .corpo {{
    font-family:'Jost',sans-serif; font-weight:300;
    font-size:34px; line-height:1.6; max-width:760px; margin-top:12px;
  }}
  .lista {{ list-style:none; margin-top:30px; }}
  .lista li {{
    font-family:'Jost',sans-serif; font-weight:300; font-size:36px;
    padding:26px 0; border-bottom:1px solid;
  }}
  .cta {{
    display:inline-block; align-self:flex-start; margin-top:48px;
    font-family:'Jost',sans-serif; font-size:26px; letter-spacing:0.16em;
    text-transform:uppercase; padding:22px 44px; border:1px solid;
  }}
  .assinatura-marca {{
    font-family:'Cormorant Garamond',serif; font-style:italic;
    font-size:40px; margin-top:40px;
  }}
  .ornamento-num {{
    position:absolute; bottom:80px; left:96px;
    font-family:'Cormorant Garamond',serif; font-weight:300; font-size:150px;
  }}
  .corner {{
    position:absolute; bottom:64px; right:64px; width:96px; height:96px;
    border-right:2px solid; border-bottom:2px solid;
  }}
  .handle {{
    position:absolute; bottom:80px; right:96px;
    font-family:'Jost',sans-serif; font-size:24px; letter-spacing:0.14em;
  }}
</style></head>
<body>
{num_html}
{body}
{corner}
{handle_html}
</body></html>"""
