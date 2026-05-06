# Estrutura JSON Obrigatória

O arquivo final é um `.md`, não um `.json` isolado. Ele contém briefing e múltiplos blocos JSON.

## Campos obrigatórios por imagem

```json
{
  "dia-metadado": "YYYY-MM-DD — [tipo] — imagem 01",
  "metadata": {
    "template": "[nome da referência ou estrutura]",
    "formato": "4:5",
    "dimensions": "1080x1350",
    "cliente": "[cliente]",
    "semana": 1,
    "dia": "YYYY-MM-DD",
    "data_criacao": "YYYY-MM-DD",
    "tema": "[tema]",
    "post": "[slug-do-post]",
    "aviso_renderizacao": "PROIBIDO exibir como texto visível: nomes de fontes, tamanhos em px, códigos hex, coordenadas, pesos tipográficos ou qualquer metadado técnico. Esses dados são instruções de renderização, não conteúdo."
  },
  "referencias": {
    "estrutura": "Infograficos/30.jpeg",
    "uso_estrutura": "descrever a lógica visual que será reaproveitada",
    "instrucao_referencia": "Copiar a estrutura visual da referência, não o conteúdo. Adaptar para o tema atual."
  },
  "branding": {
    "assinatura": "[nome]",
    "assinatura_posicao": "top_left",
    "palette": {
      "background": "#FFFFFF",
      "surface": "#F7F3EE",
      "primary": "#111111",
      "accent": "#E8632A",
      "muted": "#555555"
    }
  },
  "layout": {
    "estilo": "[direção visual]",
    "headline": "[texto visível principal]",
    "subheadline": "[texto visível secundário]",
    "estrutura_visual": "[descrição da composição]",
    "footer": "[assinatura visível, se aplicável]"
  }
}
```

## Variações comuns em `layout`

Use campos específicos conforme a estrutura:

- Fluxo: `entrada`, `centro`, `saida`
- Funil: `etapas`, `callout`
- Comparação: `comparacao`, `conclusao`
- Carrossel educativo: `slides`, `narrativa`
- Checklist: `itens`, `alerta`, `conclusao`

## Proibições

- Não agrupar imagens em `"images": []`.
- Não misturar várias imagens em um único JSON.
- Não usar texto técnico de renderização como conteúdo visível.
- Não copiar conteúdo literal da referência visual.

