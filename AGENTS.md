# AGENTS.md — Carrossel IA · Tâmara Cavalcante

> Arquivo de instrução do agente. Carregue este arquivo antes de qualquer tarefa neste repositório.
> Vale para qualquer agente de IA (Claude Code, Antigravity, Gemini, etc.). Em caso de conflito entre arquivos, a ordem de autoridade é: este `AGENTS.md` → `config/marca.md` → `skills/carrossel-ia/SKILL.md` → referências.

---

## 1. Quem você está atendendo

Você produz carrosséis e peças visuais para **Tâmara Cavalcante** (@tamaraorganiza) — Personal Organizer de alto padrão (BH / Nova Lima), especialista em mudanças white-glove.

A promessa central da marca é: **Sua casa pronta para ser vivida.** (frase de apoio: *Transformando caos em harmonia.*)

Antes de criar qualquer peça, internalize a marca lendo `config/marca.md`. Tudo o que você gerar deve passar no teste: "Isso reforça a ideia de uma casa pronta para ser vivida?". Se não, está genérico demais — reescreva.

---

## 2. Princípios (inegociáveis)

- Sempre ler `config/marca.md` **antes** de criar qualquer peça.
- Sempre olhar as referências em `referencias/` antes de definir estrutura e estética.
- Tratar referências como **estrutura, estética, tom ou performance** — nunca copiar conteúdo literal, salvo pedido explícito.
- Gerar a saída em `.md`, com **Briefing + um JSON por imagem**. Nunca agrupar todas as imagens num array único.
- JSON técnico é **instrução de renderização**: hex codes, nomes de fonte, coordenadas e tamanhos **nunca** aparecem como texto visível na imagem.
- Zero emojis no design. Zero estética de varejo/promoção.
- Não nomear marcas, produtos ou modelos nas peças.
- Não usar linguagem corretiva ou de julgamento sobre a casa da cliente.

---

## 3. Como você opera (fluxo padrão)

Quando o usuário pedir um carrossel, siga esta ordem sem pular passos:

1. **Ler a marca.** Abra `config/marca.md` e absorva paleta, tipografia, tom, vocabulário aprovado/proibido e a assinatura.
2. **Definir os parâmetros.** Tema, plataforma, formato e quantidade de slides. Se o usuário não informar algo, use o padrão da marca e **registre a suposição no Briefing**.
3. **Consultar referências.** Use as indicadas pelo usuário; se nenhuma, busque em `referencias/carrosseis/`, `referencias/infograficos/`, `referencias/exemplos-aprovados/`.
4. **Definir o arco narrativo.** Para a Tâmara, o arco padrão é uma jornada elegante, não uma aula:
   - Slide 1: capa (eyebrow + título com palavra em itálico dourado).
   - Slides do meio: abertura conceitual → desenvolvimento concreto → virada emocional.
   - Penúltimo: propósito (frase-síntese da marca).
   - Último: CTA suave + assinatura ("Quer transformar o seu espaço?").
5. **Gerar o `.md`** seguindo a Estrutura Obrigatória (seção 4) e a skill em `skills/carrossel-ia/SKILL.md`.
6. **Validar** com o checklist (seção 6) antes de entregar.
7. **Salvar** em `saidas/[semana]/` com nome descritivo (ex: `saidas/semana-25/carrossel-primeira-noite.md`).
8. **Oferecer a legenda** nos 4 movimentos ao final do documento.

---

## 4. Estrutura obrigatória da saída

Sempre gerar um `.md` nesta ordem (detalhes e exemplo de JSON em `skills/carrossel-ia/SKILL.md` e `references/estrutura-json.md`):

1. Título do documento.
2. `## Briefing` (Marca, Tema, Data, Mês, Semana, Plataforma, Formato, Quantidade, Estilo, Pilar, Referências, Suposições).
3. `## JSONs`.
4. Uma seção por imagem: `### IMAGEM 01 — [Nome]` + bloco JSON completo.
5. `## Sumario de Referencias Por Slide`.
6. `## Sumario de Estruturas Visuais`.
7. (Recomendado para a Tâmara) `## Legenda sugerida (4 movimentos)`.

Cada JSON de imagem deve conter os blocos: `metadata`, `referencias`, `branding` (com `palette` e `fontes`) e `layout`. A `palette` e as `fontes` vêm sempre de `config/marca.md` — não invente cores.

---

## 5. Pilares de conteúdo (rotacionar)

Use os pilares da Tâmara para variar os temas e marcar `metadata.pilar`:

- `mudanca_pronta` — primeira noite, caixas essenciais, mudança antes do caminhão.
- `casa_bonita_funcional` — estética vs. rotina, parceria com arquitetura, luxo silencioso.
- `closets_rotina` — closet que acompanha a manhã.
- `cozinha_fluxo` — cozinha e cristaleira por frequência de uso.
- `bastidores_metodo` — como a Tâmara pensa, organização invisível.

---

## 6. Checklist de validação (antes de entregar)

- [ ] Li `config/marca.md` e usei a paleta/fontes oficiais (cream/gold/forest, Cormorant + Jost)?
- [ ] Cada imagem tem um JSON separado (sem array único)?
- [ ] Nenhum hex code, nome de fonte ou coordenada aparece como texto visível?
- [ ] Zero emojis, zero estética de varejo?
- [ ] O tom é elegante e acolhedor, sem julgamento e sem urgência de venda?
- [ ] A peça reforça "uma casa pronta para ser vivida"?
- [ ] Há capa, propósito e CTA suave no arco?
- [ ] Salvei em `saidas/[semana]/` com nome descritivo?

Se qualquer item falhar, corrija antes de entregar.

---

## 7. Caminhos do projeto

- Configuração da marca: `config/marca.md`
- Skill principal: `skills/carrossel-ia/SKILL.md`
- Referências de apoio: `skills/carrossel-ia/references/` (`guia-visual.md`, `estrutura-json.md`, `workflow-referencias.md`)
- Banco de referências visuais: `referencias/` (`carrosseis/`, `infograficos/`, `exemplos-aprovados/`)
- Saídas: `saidas/[semana]/`

---

## 8. Camada de execução (futuro — automação de imagem)

> Esta seção descreve a camada que ainda **não** existe no repositório. Documentada aqui para orientar a construção.

O método de 3 camadas separa:
- **Tier 1 — Orientação:** este `AGENTS.md` + a skill (o que fazer e como).
- **Tier 2 — Conteúdo:** o agente gera o `.md` com Briefing + JSONs (probabilístico).
- **Tier 3 — Execução:** scripts Python determinísticos em `execution/` que leem o `.md`, enviam cada JSON para uma API de geração de imagem e salvam os arquivos. Credenciais e tokens em `.env` (nunca versionados).

Enquanto `execution/` não existe, o passo "JSON → imagem" é manual: o usuário cola cada JSON no gerador de imagem (ex: GPT Image). Quando a camada de execução for construída, este fluxo passa a ser automático.

---

## 9. O que nunca fazer

- Criar pasta nova do zero em vez de operar dentro do repositório existente.
- Inventar paleta, fontes ou medidas que não estejam em `config/marca.md`.
- Agrupar todas as imagens num único JSON.
- Escrever hex/fontes/coordenadas como texto visível do slide.
- Usar tom de coach, urgência, emojis ou "antes/depois de caos extremo".
- Gerar imagens de avatar ou inventar fotos da Tâmara.
