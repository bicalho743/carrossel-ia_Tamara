---
name: carrossel-ia
description: >
  Cria carrosséis, infográficos e JSONs de imagens para GPT Image 2 a partir de briefing,
  referências visuais, configuração de cliente e feedback. Use sempre que o usuário pedir
  carrossel com IA, infográfico com IA, JSON de imagem, imagem power, GPT Image 2,
  peças visuais em lote, ou transformar conteúdo e referências em prompts/JSONs estruturados.
---

# Carrossel IA

Use esta skill para gerar arquivos `.md` com Briefing + JSONs de imagens. A saída é pensada para alimentar um renderizador visual ou um gerador de imagem como GPT Image 2.

## Antes de criar

1. Identifique o cliente.
2. Leia `clientes/[cliente]/config.md`.
3. Leia a pasta de referências indicada pelo usuário.
4. Se o usuário não indicar referência, procure em:
   - `clientes/[cliente]/referencias/infograficos/`
   - `clientes/[cliente]/referencias/carrosseis/`
   - `clientes/[cliente]/referencias/exemplos-aprovados/`
5. Defina plataforma, formato, quantidade e tema.
6. Se algum dado essencial faltar, use o padrão do cliente e marque a suposição no briefing.

## Saída obrigatória

Sempre gerar um `.md` com esta ordem:

````markdown
# JSONs de Imagens — [Título]

## Briefing

- Cliente:
- Tema:
- Data de criação:
- Mês:
- Semana:
- Plataforma:
- Formato:
- Quantidade:
- Estilo:
- Referências:

## JSONs

### IMAGEM 01 — [Nome]

```json
{
  "dia-metadado": "...",
  "metadata": {},
  "referencias": {},
  "branding": {},
  "layout": {}
}
```

## Sumario de Referencias Por Slide

- Slide 1 =

## Sumario de Estruturas Visuais

- Imagem 1 =
````

## Regras críticas

- Não usar array único para várias imagens.
- Cada imagem tem seu próprio JSON.
- Manter os campos principais: `dia-metadado`, `metadata`, `referencias`, `branding`, `layout`.
- Incluir sempre `metadata.aviso_renderizacao`.
- Em `referencias`, explicar qual arquivo visual inspira a estrutura e como usar sem copiar conteúdo.
- Em `branding`, incluir assinatura, posição de assinatura e paleta.
- Em `layout`, colocar apenas instruções de composição e textos visíveis.
- Não colocar nomes de fontes, tamanhos em px, hex codes, coordenadas ou metadados técnicos como texto visível.

## Referências internas

- Estrutura JSON: `references/estrutura-json.md`
- Como ler referências: `references/workflow-referencias.md`
- Guia visual: `references/guia-visual.md`
- Template de saída: `templates/carrossel-template.md`
- Template de cliente: `templates/cliente-config-template.md`
