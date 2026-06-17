# execution/ — Renderizador de carrossel (Tier 3)

Camada determinística do método: lê o `.md` gerado pela skill (Briefing + JSONs) e produz um PNG por slide, em 1080x1350, com a paleta e tipografia oficiais da Tâmara. Sem IA na imagem — resultado idêntico à marca, toda vez, sem custo.

## Instalação (uma vez)

```bash
pip install -r requirements.txt
python -m playwright install chromium
```

## Uso

```bash
python render_carrossel.py <caminho-do-md>
```

Exemplos:
```bash
python render_carrossel.py ../saidas/semana-25/carrossel-primeira-noite.md
python render_carrossel.py ../saidas/semana-25/carrossel.md --out ../saidas/semana-25/png --scale 2
```

- `--out`  pasta de saída (padrão: `<pasta-do-md>/png`)
- `--scale` fator de resolução (padrão 2 = exporta em 2160x2700, ótimo para Instagram; use 1 para 1080x1350)

As imagens saem nomeadas `slide-01-....png`, `slide-02-....png`, na ordem do documento.

## Como funciona

1. `render_carrossel.py` lê o `.md`, encontra cada `### IMAGEM NN` e o bloco JSON seguinte.
2. Para cada slide, `slide_template.py` monta um HTML com a paleta/fontes do `branding` do JSON (ou a paleta oficial padrão) e o conteúdo do `layout`.
3. O Playwright (Chromium headless) renderiza e fotografa em 1080x1350.

## O que o JSON precisa ter

Cada slide usa `branding.palette`, `branding.fontes` e `branding.assinatura`, e o bloco `layout` com qualquer combinação de: `eyebrow`, `titulo` (+ `destaque_italico_dourado`), `corpo`, `lista`, `divisor`, `cta_visual`, `assinatura_marca`, `numero_ornamental`, `ornamento_canto`, `fundo` ("background" | "surface" | "surface_dark").

Campos técnicos (hex, fontes, coordenadas) são instruções de renderização — nunca viram texto visível.

## Fontes

Carregadas via Google Fonts (Cormorant Garamond + Jost). Requer internet na primeira renderização (o Chromium baixa as fontes). Para uso offline, instale as fontes no sistema e ajuste o `slide_template.py`.
