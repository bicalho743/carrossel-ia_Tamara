# COMO EXECUTAR — gerar as imagens do carrossel

> Instruções para o agente (Antigravity) executar o renderizador. O usuário pede em português; o agente roda os comandos.

## Pré-requisito — instalar uma única vez

Antes da primeira execução, instale as dependências (só precisa fazer uma vez por máquina/ambiente):

```bash
pip install -r execution/requirements.txt
python -m playwright install chromium
```

Se `pip` falhar por permissão, tente `pip install -r execution/requirements.txt --user`.
Se faltar dependência de sistema para o Chromium, rode `python -m playwright install-deps chromium` (Linux) antes do `install chromium`.

## Fluxo completo (do tema às imagens)

1. **Gerar o conteúdo.** Seguindo o `AGENTS.md` da raiz, gerar o `.md` com Briefing + um JSON por imagem e salvar em `saidas/[semana]/`. Exemplo de caminho: `saidas/semana-25/carrossel-primeira-noite.md`.

2. **Renderizar as imagens.** Rodar:

```bash
python execution/render_carrossel.py saidas/semana-25/carrossel-primeira-noite.md
```

   Troque o caminho pelo arquivo `.md` real que foi gerado.

3. **Entregar.** Os PNGs saem em `saidas/semana-25/png/`, nomeados `slide-01-....png`, `slide-02-....png`, na ordem dos slides. Informe ao usuário onde ficaram.

## Opções do comando

- `--out PASTA` — muda a pasta de saída (padrão: `<pasta-do-md>/png`).
- `--scale N` — resolução. Padrão `2` (exporta 2160x2700, ótimo para Instagram). Use `1` para 1080x1350 exato.

Exemplo com opções:
```bash
python execution/render_carrossel.py saidas/semana-25/carrossel.md --out saidas/semana-25/png --scale 2
```

## Verificação de sucesso

- O comando imprime `✓ slide-NN-...png` para cada slide e termina com `Pronto. N imagens em ...`.
- Confira que o número de PNGs bate com o número de slides do `.md`.
- Se aparecer `JSON inválido` para algum slide, o `.md` tem erro de formatação naquele bloco — corrija o JSON e rode de novo.

## Observações

- O renderizador usa fontes do sistema (Helvetica/Arial) — funciona offline.
- Não há geração por IA aqui: as imagens são montadas de forma determinística a partir do HTML/CSS com a paleta e fontes oficiais da Tâmara. O resultado é idêntico à marca toda vez.
- Não edite os `.py` para mudar cores ou textos de um carrossel específico — isso vem do `.md`/JSON. Os `.py` só mudam se for preciso criar um novo tipo de layout.
