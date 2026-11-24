# Mini Compactador de Arquivos de Texto

## Sobre o projeto

O **Mini Compactador de Arquivos de Texto** é um sistema desenvolvido em Python com o objetivo de compactar e descompactar arquivos de texto utilizando uma técnica baseada na contagem de caracteres consecutivos (Run-Length Encoding – RLE).

O programa permite comparar o tamanho do arquivo original com o arquivo compactado, verificando a diferença em quantidade de caracteres e bytes, além de calcular a porcentagem de redução do tamanho.

## Funcionalidades

O sistema possui um menu interativo com as seguintes opções:

- **Ler arquivo:** permite visualizar o conteúdo do arquivo compactado ou descompactado.
- **Compactar:** realiza a compactação do arquivo original (`arquivo.txt`), gerando o arquivo `compactado.txt`.
- **Descompactar:** recupera o conteúdo do arquivo compactado, gerando `descompactado.txt`.
- **Comparar:** compara os tamanhos dos arquivos original e compactado, apresentando a quantidade de caracteres, bytes e a porcentagem de redução.
- **Sair:** encerra o sistema ou retorna ao menu principal.

## Tecnologias utilizadas

- **Python:** linguagem utilizada no desenvolvimento.
- **Módulo `time`:** utilizado para adicionar pequenos intervalos durante a navegação do sistema.
- **Módulo `os`:** utilizado para consultar o tamanho dos arquivos em bytes.

## Técnica de compactação

O projeto utiliza uma técnica chamada **Run-Length Encoding (RLE)**.

Seu funcionamento consiste em identificar caracteres consecutivos iguais e substituir suas repetições pela quantidade de vezes que aparecem, seguida do próprio caractere.

Exemplo:

**Texto original:**
```text
AAAAABBBCCDDDD
```

**Texto compactado:**
```text
5A3B2C4D
```

Dessa forma, sequências de caracteres repetidos podem ocupar menos espaço no arquivo.

## Arquivos utilizados

O sistema trabalha com três arquivos de texto:

| Arquivo | Finalidade |
|---|---|
| `arquivo.txt` | Armazena o conteúdo original. |
| `compactado.txt` | Armazena o conteúdo após a compactação. |
| `descompactado.txt` | Armazena o conteúdo recuperado. |

**Observação:** o arquivo `arquivo.txt` deve existir antes de executar as opções de compactação e comparação.

## Como executar

1. Instale o Python em sua máquina.
2. Clone ou baixe este repositório.
3. Coloque o arquivo `arquivo.txt` na mesma pasta do programa.
4. Execute o arquivo Python:

```bash
python main.py
```

5. Utilize o menu interativo para acessar as funcionalidades.

## Objetivo acadêmico

Este projeto tem como finalidade aplicar conceitos fundamentais de programação em Python, incluindo:

- Manipulação de arquivos (`open`, `read` e `write`).
- Estruturas condicionais (`if`, `elif`, `else` e `match/case`).
- Estruturas de repetição (`while` e `for`).
- Tratamento de exceções (`try` e `except`).
- Manipulação de strings.
- Utilização de módulos e bibliotecas.
- Cálculos matemáticos e comparação de dados.

## Considerações finais

O Mini Compactador permite compreender, na prática, como funciona uma técnica básica de compressão de dados, além de desenvolver habilidades relacionadas à manipulação de arquivos e à lógica de programação utilizando Python.