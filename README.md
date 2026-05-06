# Carrossel IA

Sistema de criação de carrosséis, infográficos e peças visuais com IA a partir de:

- briefing editorial;
- referências visuais em pastas;
- configuração do cliente;
- JSONs estruturados por imagem;
- feedback acumulado.

O objetivo é transformar a lógica de produção visual em um repositório reutilizável por cliente. O usuário configura a marca, coloca referências em pastas e pede ao agente para gerar um `.md` com Briefing + JSONs prontos para renderização.

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
│           └── cliente-config-template.md
├── clientes/
│   └── exemplo-cliente/
│       ├── config.md
│       ├── referencias/
│       │   ├── infograficos/
│       │   ├── carrosseis/
│       │   ├── prints-cliente/
│       │   ├── identidade-visual/
│       │   └── exemplos-aprovados/
│       └── carrosseis/
│           └── semana-01/
│               └── exemplo-jsons-imagens.md
├── docs/
│   ├── como-configurar-cliente.md
│   ├── fluxo-operacional.md
│   └── instalacao.md
└── examples/
    └── exemplo-jsons-imagens.md
```

## Fluxo rápido

1. Copie `clientes/exemplo-cliente/` para criar um novo cliente.
2. Preencha `config.md`.
3. Coloque referências visuais nas pastas de `referencias/`.
4. Peça ao agente: "crie 3 infográficos 4:5 para [cliente] sobre [tema], usando as referências da pasta X".
5. O agente gera um `.md` em `clientes/[cliente]/carrosseis/[semana]/`.
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
