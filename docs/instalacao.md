# Instalação

## Uso local

1. Clone ou copie este repositório.
2. Instale/copiei a skill `skills/carrossel-ia/` para o ambiente do agente, se necessário.
3. Crie um cliente em `clientes/[cliente]/`.
4. Preencha `config.md`.
5. Adicione referências visuais em `referencias/`.

## GitHub CLI

Para publicar:

```bash
gh auth login -h github.com
gh repo create carrossel-ia --private --source=. --remote=origin --push
```

Se `gh auth status` mostrar token inválido, refaça o login antes de publicar.

