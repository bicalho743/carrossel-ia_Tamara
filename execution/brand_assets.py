"""
brand_assets.py — sobrepõe logo oficial e padronagem nos slides renderizados.

Roda DEPOIS do Playwright gerar o PNG do slide. Usa Pillow para compor:
- a logo real (colorida em fundo claro, branca em fundo escuro) no rodapé/canto;
- opcionalmente, uma faixa sutil da padronagem oficial em capas/fechos.

Segue o Projeto Executivo de Marca (Marcus Filho): logo nunca distorcida nem
recolorida; padronagem sem alterar cor/escala, apenas com opacidade reduzida
como elemento de apoio (nunca atrás de texto corrido).
"""
from pathlib import Path
from PIL import Image

ASSETS = Path(__file__).parent / "assets"
LOGOS = ASSETS / "logos"
PADRO = ASSETS / "padronagem"

# qual logo para qual fundo
LOGO_CLARO = "logo-cor-horizontal.png"      # símbolo azul + wordmark marrom
LOGO_ESCURO = "logo-branca-horizontal.png"  # negativa


def _load(path):
    try:
        return Image.open(path).convert("RGBA")
    except Exception:
        return None


def apply_brand(slide_png: str, is_dark: bool, slide_type: str = "", scale: int = 2):
    """Compõe logo (e padronagem em capa/cta) sobre o PNG do slide, salvando no lugar."""
    base = Image.open(slide_png).convert("RGBA")
    W, H = base.size

    # --- padronagem sutil em capa e cta (faixa inferior, baixa opacidade) ---
    if slide_type in ("capa", "cta"):
        pat = _load(PADRO / "padronagem-azul-oficial.png")
        if pat:
            band_h = int(H * 0.16)
            ratio = band_h / pat.height
            pat_resized = pat.resize((int(pat.width * ratio), band_h))
            # tile horizontal
            band = Image.new("RGBA", (W, band_h), (0, 0, 0, 0))
            x = 0
            while x < W:
                band.alpha_composite(pat_resized, (x, 0))
                x += pat_resized.width
            # opacidade reduzida
            alpha = band.getchannel("A").point(lambda a: int(a * (0.10 if not is_dark else 0.14)))
            band.putalpha(alpha)
            base.alpha_composite(band, (0, 0))  # faixa no topo
            base.alpha_composite(band, (0, H - band_h))  # e no rodapé

    # --- logo no rodapé direito ---
    logo_file = LOGO_ESCURO if is_dark else LOGO_CLARO
    logo = _load(LOGOS / logo_file)
    if logo:
        target_w = int(W * 0.30)  # ~30% da largura
        ratio = target_w / logo.width
        logo_r = logo.resize((target_w, int(logo.height * ratio)))
        margin = int(W * 0.06)
        pos = (W - logo_r.width - margin, H - logo_r.height - margin)
        base.alpha_composite(logo_r, pos)

    base.convert("RGB").save(slide_png)
