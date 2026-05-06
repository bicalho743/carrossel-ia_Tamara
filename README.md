# Carrossel IA

Sistema de criação de carrosséis, infográficos e peças visuais com IA a partir de:

- briefing editorial;
- referências visuais em pastas;
- configuração da sua marca;
- JSONs estruturados por imagem;
- feedback acumulado.

O objetivo é entregar uma estrutura inteligente para o usuário final cadastrar seus estilos, colocar referências e gerar arquivos `.md` com Briefing + JSONs prontos para renderização.

## Estrutura

```text
carrossel-ia/
├── AGENTS.md
├── README.md
├── skills/
│   └── carrossel-ia/
│       ├── SKILL.md
│       ├── references/
│       │   ├── estrutura-json.md
│       │   ├── guia-visual.md
│       │   └── workflow-referencias.md
│       └── templates/
│           ├── carrossel-template.md
│           └── marca-config-template.md
├── config/
│   └── marca.md
├── referencias/
│   ├── infograficos/
│   ├── carrosseis/
│   ├── prints/
│   ├── identidade-visual/
│   └── exemplos-aprovados/
├── saidas/
│   └── semana-01/
│       └── exemplo-jsons-imagens.md
├── docs/
│   ├── como-configurar-sua-marca.md
│   ├── fluxo-operacional.md
│   └── instalacao.md
└── examples/
    └── exemplo-jsons-imagens.md
```

## Fluxo rápido

1. Preencha `config/marca.md` com sua marca, estilos, paleta e assinatura.
2. Coloque referências visuais nas pastas de `referencias/`.
3. Peça ao agente: "crie 3 infográficos 4:5 sobre [tema], usando as referências da pasta X".
4. O agente gera um `.md` em `saidas/[semana]/`.
5. O arquivo vem com Briefing + JSONs separados por imagem.
6. Cada imagem deve ter um JSON próprio, separado por seção.

## Regra central

Não usar array único para várias imagens. Cada imagem precisa ter seu próprio bloco:

````markdown
### IMAGEM 01 — [Nome]

```json
{ ... }
```

### IMAGEM 02 — [Nome]

```json
{ ... }
```
````

O padrão completo está em `skills/carrossel-ia/references/estrutura-json.md`.
