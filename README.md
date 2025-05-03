# 🖼️ Ditherização de Imagens com Floyd-Steinberg

Este projeto aplica o algoritmo de ditherização de Floyd-Steinberg em imagens, suportando tanto imagens em escala de cinza quanto imagens coloridas.

## 📌 Funcionalidades

- Quantização de pixels para preto e branco
- Cálculo e difusão de erro (Floyd-Steinberg)
- Suporte a imagens coloridas e em escala de cinza
- Opção de usar o método de ditherização embutido da biblioteca Pillow (PIL) para comparação
- Interface de linha de comando para seleção de modo entre colorido e em escala de cinza

## 🛠️ Instalação

Clone o repositório:

```bash
git clone https://github.com/JuliaSilvass/comp-aplicadaV.git
cd comp-aplicadaV
```

Instale as dependências:
```bash
pip install -r requirements.txt
```

## ▶️ Execução

Para executar o código da Ditherização manual no terminal, execute o script principal:

```bash
cd Ditherizacao
python index.py
```
Siga as instruções interativas para escolher entre imagem colorida ou em cinza.

Para executar o código de comparação da ditherização usando a biblioteca PIL, vá até a pasta

Colorida:
```bash
cd Ditherizacao_direta
python dither_direta_colorida.py
```

ou 

Em escala de cinza:
```bash
cd Ditherizacao_direta
python dither_direta.py
```

## 📁 Estrutura do Projeto

comp-aplicadaV/
├── Ditherizacao/
│   ├── index.py                           # Script principal 
│   ├── ditherizacao.py                    # Lógica de ditherização manual
├── Ditherizacao_direta/                   # Contém os codigo da ditherização (usando PIL) para comparação
|   ├── dither_direta_colorida.py          # Ditherização usando pil para resultado colorido
|   ├── dither_direta.py                   # Ditherização usando pil para resultado em escada de cinza
│   ├── canais/                            # Pasta com imagens separadas por canal
├── Img/                                   # Pasta onde armazena a imagem para ser ditherizada
│   └── nicolas_cage.jpeg                  # Imagem de exemplo
├── ImgDitherizada/                        # Pasta onde armazena as imagems ditherizada (colorida e cinza)
├── ImgDitherizadaDireta/                  # Pasta onde armazena as imagems ditherizada usando o pil (colorida e cinza)
├── README.md
└── requirements.txt

## 📷 Resultado
As imagens ditherizadas são salvas automaticamente na pasta de saída com nomes descritivos.

## 📌 Requisitos

Python 3.10 ou superior
OpenCV
Pillow
NumPy

## ✍️ Autora
Julia Silva – Estudante de Análise e Desenvolvimento de Sistemas no IFSul