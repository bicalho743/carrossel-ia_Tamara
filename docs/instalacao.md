# Instalação

## Uso local

1. Clone ou copie este repositório.
2. Instale/copiei a skill `skills/carrossel-ia/` para o ambiente do agente, se necessário.
3. Preencha `config/marca.md` com sua marca.
4. Adicione referências visuais em `referencias/`.
5. Gere suas saídas em `saidas/semana-XX/`.

## GitHub CLI

Para publicar:

```bash
gh auth login -h github.com
gh repo create carrossel-ia --public --source=. --remote=origin --push
```

Se `gh auth status` mostrar token inválido, refaça o login antes de publicar.
