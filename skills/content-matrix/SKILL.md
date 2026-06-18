---
name: content-matrix
description: >
  Gera dezenas de ideias de conteúdo cruzando os 5 pilares da Tâmara com 8 formatos.
  Use quando o usuário perguntar "o que postar essa semana", "me dá ideias de conteúdo",
  "preciso de pauta", "matriz de conteúdo" ou quando faltar tema para post, carrossel,
  Reels ou story. Resolve o "página em branco" transformando pilares fixos em pauta.
---

# Content Matrix — Tâmara Cavalcante

Cruza os 5 pilares de conteúdo da Tâmara com 8 formatos para gerar uma matriz de 40 ideias, cada uma já no tom da marca. Inspirado no estilo Justin Welsh / Charlie Hills, adaptado à voz da Tâmara.

## Antes de gerar

1. Leia a marca (`config/marca.md` no repo do carrossel). Toda ideia deve passar no teste: **"Isso reforça uma casa pronta para ser vivida?"**.
2. Use o tom: elegante, acolhedor, sem julgamento, sem urgência de venda, sem emojis nos títulos.
3. Respeite o vocabulário: "closet" (não armário), "cristaleira" (não louceiro), "caos/desordem" (não bagunça).
4. Palavras proibidas: corre, não perca, oferta imperdível, tô chocada, bagunça, mágico, perfeito, incrível, transformador, "muda sua vida", top, hacks, DIY, escaninho.

## Os 5 pilares

| ID | Pilar | Descrição | Distribuição |
|---|---|---|---|
| `mudanca_pronta` | Mudança pronta para ser vivida | Primeira noite, caixas essenciais, mudança antes do caminhão, casa nova funcionando nos primeiros dias. | 40% |
| `casa_bonita_funcional` | Casa bonita que funciona | Estética vs. rotina, parceria com arquitetura, beleza com praticidade, luxo silencioso. | 25% |
| `closets_rotina` | Closets e rotina da manhã | Closet que acompanha a manhã, visualização, manutenção. | 15% |
| `cozinha_fluxo` | Cozinha, cristaleira e fluxo | Cozinha de uso real, cristaleira, organização por frequência, receber em casa. | 10% |
| `bastidores_metodo` | Bastidores do método | Como a Tâmara pensa, o que observa, organização invisível, detalhes que evitam retrabalho. | 10% |

## Os 8 formatos

| # | Formato | Descrição | Melhor canal |
|---|---|---|---|
| 1 | Verdade que ressoa | Uma frase-insight curta. | X, capa de carrossel |
| 2 | Lista elegante | "X coisas que..." sem virar dica barata. | Carrossel |
| 3 | Antes do método / depois do método | Contraste de sensação, nunca "caos chocante". | Carrossel, Reels |
| 4 | Bastidor | Cena real de um projeto, o que ninguém vê. | Reels, story |
| 5 | Mito x realidade | Desfaz uma crença comum com delicadeza, nunca corretivo. | Carrossel, post |
| 6 | Pergunta que identifica | Provoca reconhecimento ("você já sentiu..."). | Story, post |
| 7 | Cena da rotina | Um momento concreto do dia da cliente (manhã, café, chegada). | Reels, story |
| 8 | Princípio da marca | Uma crença da Tâmara desenvolvida. | Carrossel, post (autoridade) |

## Como gerar

1. Para cada combinação **pilar × formato**, escreva:
   - **Ângulo** (1 linha): o conteúdo da ideia.
   - **Gancho sugerido**: a primeira frase na voz da Tâmara.
2. Marque o pilar e o formato para facilitar o agendamento.
3. Priorize os pilares pela distribuição da marca: mudança 40%, casa funcional 25%, closets 15%, cozinha 10%, bastidores 10%.
4. Toda ideia deve soar como algo que a Tâmara diria — elegante, acolhedora, confiante, poética sem ser floreada.
5. Evite tom de influencer popular, urgência artificial, linguagem de "salvação do caos".

## Saída obrigatória

```markdown
# Matriz de Conteúdo — Tâmara Cavalcante

> [semana/mês] · [quantidade] ideias · Pilares × Formatos

## Pilar 1 — [Nome do pilar]

| # | Formato | Ângulo | Gancho sugerido |
|---|---|---|---|
| 1 | [formato] | [ângulo] | "[gancho]" |

[... repetir para os 5 pilares ...]

## Sugestão para esta semana

- **Terça (Reels):** #N — [descrição]
- **Quarta (Carrossel):** #N — [descrição]
- **Domingo (post/story):** #N — [descrição]
```

## Regras críticas

- Mínimo 1 ideia por célula relevante da matriz (até 40 combinações).
- Ao final, **sempre** sugerir 3–5 ideias para a semana, alinhadas aos melhores dias (terça, quarta, domingo) e formatos de maior alcance (Reels).
- Rotacionar os pilares ao longo das semanas seguindo a distribuição da marca.
- Se o usuário pedir tema específico, filtrar a matriz por pilar ou formato.
- Se o usuário pedir "ideias para Reels", filtrar pelos formatos 3, 4 e 7.
- Se o usuário pedir "ideias de carrossel", filtrar pelos formatos 2, 3, 5 e 8.

## Referências

- Matriz preenchida de referência: `examples/matriz-tamara.md`
- Configuração da marca: `config/marca.md`
- Estilo inspirado em: Justin Welsh (Content Matrix), Charlie Hills (pilar × formato)
