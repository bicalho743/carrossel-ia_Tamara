#!/usr/bin/env python3
"""
render_carrossel.py — Tier 3 (execução determinística) do Carrossel IA · Tâmara.

Lê um arquivo .md gerado pela skill (Briefing + um JSON por imagem) e produz
um PNG 1080x1350 por slide, usando a paleta e tipografia oficiais da marca.

Uso:
    python render_carrossel.py <caminho-do-md> [--out PASTA] [--scale N]

Exemplos:
    python render_carrossel.py saidas/semana-25/carrossel-primeira-noite.md
    python render_carrossel.py saidas/semana-25/carrossel.md --out saidas/semana-25/png --scale 2

Requisitos:
    pip install playwright
    python -m playwright install chromium
"""
import argparse
import json
import re
import sys
from pathlib import Path

from slide_template import build_html

try:
    from playwright.sync_api import sync_playwright
except ImportError:
    sys.exit("Falta o Playwright. Rode: pip install playwright && python -m playwright install chromium")

W, H = 1080, 1350
JSON_BLOCK = re.compile(r"```json\s*\n(.*?)\n```", re.DOTALL)
IMG_HEADER = re.compile(r"^###\s*IMAGEM\s*(\d+)\s*[—-]\s*(.+)$", re.MULTILINE)


def extrair_slides(md_text: str):
    """Retorna lista de (numero, nome, dict_json) na ordem do documento."""
    slides = []
    headers = list(IMG_HEADER.finditer(md_text))
    for i, h in enumerate(headers):
        trecho = md_text[h.end(): headers[i + 1].start() if i + 1 < len(headers) else len(md_text)]
        m = JSON_BLOCK.search(trecho)
        if not m:
            print(f"  aviso: IMAGEM {h.group(1)} sem bloco JSON — pulando")
            continue
        try:
            data = json.loads(m.group(1))
        except json.JSONDecodeError as e:
            print(f"  ERRO: JSON inválido na IMAGEM {h.group(1)}: {e}")
            continue
        slides.append((int(h.group(1)), h.group(2).strip(), data))
    return slides


def slug(texto: str) -> str:
    s = re.sub(r"[^a-zA-Z0-9]+", "-", texto.lower()).strip("-")
    return s or "slide"


def main():
    ap = argparse.ArgumentParser(description="Renderiza carrossel da Tâmara (.md → PNGs)")
    ap.add_argument("md", help="caminho do arquivo .md com os JSONs")
    ap.add_argument("--out", help="pasta de saída (padrão: <pasta-do-md>/png)")
    ap.add_argument("--scale", type=int, default=2, help="fator de resolução (2 = 2160x2700, padrão)")
    args = ap.parse_args()

    md_path = Path(args.md)
    if not md_path.exists():
        sys.exit(f"Arquivo não encontrado: {md_path}")

    out_dir = Path(args.out) if args.out else md_path.parent / "png"
    out_dir.mkdir(parents=True, exist_ok=True)

    slides = extrair_slides(md_path.read_text(encoding="utf-8"))
    if not slides:
        sys.exit("Nenhum slide com JSON válido encontrado no arquivo.")

    print(f"Encontrados {len(slides)} slides. Renderizando para {out_dir} (scale {args.scale})...")

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": W, "height": H}, device_scale_factor=args.scale)
        for num, nome, data in slides:
            layout = data.get("layout", {})
            branding = data.get("branding", {})
            html = build_html(layout, branding)
            page.set_content(html, wait_until="networkidle")
            page.wait_for_timeout(400)  # garante carregamento das fontes
            fname = out_dir / f"slide-{num:02d}-{slug(nome)}.png"
            page.screenshot(path=str(fname), clip={"x": 0, "y": 0, "width": W, "height": H})
            print(f"  ✓ {fname.name}")
        browser.close()

    print(f"\nPronto. {len(slides)} imagens em {out_dir}")


if __name__ == "__main__":
    main()
