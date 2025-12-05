# 📘 Geração de Envelope P–T–x/y Interativo (UNIQUAC)

## 🧩 Descrição do Projeto

Este repositório contém o código, dados e arquivos interativos utilizados para gerar o **diagrama 3D P–T–x/y** de um sistema binário (metanol + acetato), calculado a partir de modelos termodinâmicos no **Aspen Plus** e visualizado em **Plotly**.

O resultado é um **gráfico tridimensional interativo**, exibido diretamente no navegador, mostrando as superfícies de **bolha** e **orvalho** como funções de **pressão, temperatura e composição**.

O gráfico é hospedado via **GitHub Pages**, permitindo compartilhamento público e acesso sem necessidade de software adicional.

---

# 🔧 1. Geração dos Dados no Aspen Plus

## Passo 1 — Binary Analysis

No Aspen:

- Acesse **Analysis → Binary**
- Escolha o cálculo **Txy**
- Configure:
  - x_1 variando de **0 a 1** (20 intervalos)
  - P variando de **1 a 6 atm** (10 valores)

O Aspen gera uma tabela contendo diversos dados, mas os importantes para esse gráfico são: **P x1 T y1 K1 K2 Gamma1 Gamma2****

---

## Passo 2 — Exportar no Excel

No Excel:

- Ajustar cabeçalhos para **P x1 T y1 K1 K2 Gamma1 Gamma2**
- Remover linhas vazias
- Garantir que decimais estejam com **ponto**
- Salvar como: **dados_PTxy.txt**
  - **Obs:** Delimitado por TAB (modelo .csv)

---

# 🐍 2. Plotagem em Python (Plotly)

## Instalar Python

Baixar em:  
https://www.python.org/

## Instalar IDE

Recomendado: **PyCharm**  
Também funciona com VS Code, Spyder ou Jupyter Notebook.

## Instalar pacotes necessários

No terminal:

```
pip install pandas numpy scipy plotly kaleido
```

## Executar script:

Rodar o arquivo com a rotina ```sup_inter_PTxy.py```

Irá ser gerado um arquivo .html 

# 🌐 3. Publicação via GitHub Pages

## Renomear arquivo
Mude o nome do arquivo .html para **index.html**

## Criar repositório

Suba no GitHub:

- index.html
- plot_PTxy.py
- dados_PTxy.txt
- README.md

## Ativar GitHub Pages

No repositório:

Vá em Settings → Pages

Configure:

- Source: Deploy from a branch
- Branch: main
- Folder: /(root)

O GitHub publicará seu site em: ```https://<seu-usuario>.github.io/<nome-do-repo>/```

Se index.html estiver na raiz, o gráfico abrirá automaticamente.

**Por Gabriel Rodrigues Favero**




