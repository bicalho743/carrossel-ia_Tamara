# Agent Instructions — Carrossel IA

Este repositório empacota um sistema de produção de carrosséis e imagens com IA.

## Princípios

- Sempre ler `clientes/[cliente]/config.md` antes de criar qualquer peça.
- Sempre olhar as referências disponíveis em `clientes/[cliente]/referencias/`.
- Tratar referências como estrutura, estética, tom ou performance. Não copiar conteúdo literal salvo quando o usuário pedir explicitamente.
- Gerar a saída em `.md`, com Briefing + JSONs de imagens.
- Cada imagem deve ter um JSON separado. Não usar um array único para agrupar todas as imagens.
- JSON técnico é instrução de renderização. Metadados, hex codes, fonte, coordenadas e tamanhos nunca devem aparecer como texto visível na imagem.

## Estrutura obrigatória da saída

1. Título do documento.
2. Briefing.
3. Seção `## JSONs`.
4. Uma seção por imagem:
   - `### IMAGEM 01 — [Nome]`
   - bloco JSON completo.
5. `## Sumario de Referencias Por Slide`.
6. `## Sumario de Estruturas Visuais`.

## Caminhos

- Configuração do cliente: `clientes/[cliente]/config.md`
- Referências: `clientes/[cliente]/referencias/`
- Saídas: `clientes/[cliente]/carrosseis/[semana]/`
- Skill: `skills/carrossel-ia/SKILL.md`

