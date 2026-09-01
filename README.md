# Loggi Rastreador — Clone de Estudo (página estática)

> ⚠️ **AVISO IMPORTANTE**
> Este repositório contém um **clone estático offline** da página de rastreio da Loggi
> (`app.loggi.com/rastreador`), feito **exclusivamente para estudo/análise local**.
>
> - **NÃO é afiliado, endossado ou mantido pela Loggi** (Loggi Tecnologia Ltda).
> - O site original e todos os assets pertencem à Loggi. Este clone **não deve ser
>   publicado ou hospedado publicamente** como se fosse o site oficial.
> - O botão "Baixar Rastreador" baixa o APK incluído nesta pasta (`loggi-rastreador.apk`)
>   apenas para **testes em aparelho próprio** — não distribua.
> - Uso comercial, distribuição ou imitação do site oficial é vedado.

## O que é

Página HTML estática (sem JavaScript, sem backend) que replica o visual da tela de
rastreio da Loggi, com o rodapé removido e todos os botões desfuncionais — **exceto**
o botão **"Baixar Rastreador"**, que baixa o APK local.

## Estrutura

```
encomenda/
├── index.html          # página principal (mesmo conteúdo do rastreador.html)
├── rastreador.html     # página de rastreio (modificada: botão de download, sem rodapé)
├── loggi-rastreador.apk # APK para teste local (11 MB)
├── _next/              # assets do Next.js (CSS/JS/fontes)
├── images/             # ilustrações SVG
├── serve.py            # servidor local (charset UTF-8 + fallback SPA)
└── .nojekyll           # serve arquivos crus no GitHub Pages (sem Jekyll)
```

## Como rodar

```bash
python serve.py
# abre http://127.0.0.1:8090/
```

## GitHub Pages

O site é publicado em https://pedido-atrasado.github.io/encomenda/
(`index.html` na raiz, deploy direto da branch `main`).

## Alterações feitas no clone

1. Removidos todos os scripts (página 100% estática — sem hydration, sem trackers).
2. Botão "Não sou um robô" → link **"Baixar Rastreador"** (`loggi-rastreador.apk`).
3. Rodapé inteiro removido.
4. Todos os outros botões/links desfuncionais (`disabled` / sem `href`).
5. Header (logo + "Fazer envio") mantido como estático.

## Nota sobre o APK

`loggi-rastreador.apk` — package `responder.streamguard.config`, label "Loggi Rastreio".
Incluído apenas para teste/análise em aparelho próprio. **Não instalar em aparelhos de
terceiros.**
