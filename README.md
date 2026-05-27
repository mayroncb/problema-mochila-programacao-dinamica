# Problema da Mochila 0/1 – Programação Dinâmica

Este projeto apresenta uma solução para o **problema da Mochila Inteira 0/1** utilizando **programação dinâmica**. A implementação foi desenvolvida como parte da disciplina de Algoritmos Complexos e Estruturas de Dados de um curso de mestrado em informática.

O problema consiste em selecionar um subconjunto de itens com pesos e valores dados de forma a maximizar o valor total sem exceder uma capacidade máxima da mochila. Cada item pode ser escolhido no máximo uma vez (versão 0/1).

## Estrutura do repositório

```text
┌── instancias/          # Arquivos de entrada com as instâncias do problema
│   ├── mochila01.txt    # Instância pequena de exemplo
│   ├── mochila02.txt    # Outra instância pequena
│   ├── mochila1000.txt  # Instância com 1 000 itens
│   ├── mochila2500.txt  # Instância com 2 500 itens
│   └── mochila5000.txt  # Instância com 5 000 itens
├── mochila_dp.py        # Script que resolve o problema de cada instância
├── resultados_mochila.txt  # Resultado das instâncias no formato texto
├── resultados_mochila.csv  # Resultado das instâncias no formato CSV
├── requirements.txt     # Dependências (apenas Python 3 puro é necessário)
├── .gitignore           # Arquivos/ pastas ignorados pelo Git
└── LICENSE              # Licença do projeto (MIT)
```

## Como executar

Certifique‑se de ter **Python 3.8** ou superior instalado. Este projeto não depende de bibliotecas externas além da biblioteca padrão.

Clone o repositório ou faça download dos arquivos e navegue até a pasta raiz. Em seguida, você pode executar:

```bash
python mochila_dp.py
```

Sem argumentos, o script irá processar todas as instâncias da pasta `instancias/` e gerar dois arquivos de saída: `resultados_mochila.txt` e `resultados_mochila.csv`. Os resultados também serão impressos no terminal.

Para processar uma instância específica, forneça o caminho para o arquivo como argumento:

```bash
python mochila_dp.py instancias/mochila1000.txt
```

## Exemplos de resultado

Os seguintes resultados foram obtidos ao executar o script nas instâncias fornecidas (valores calculados previamente):

| Instância        | n    | Capacidade | Valor ótimo | Peso usado | Qtd. itens |
|------------------|------:|-----------:|------------:|-----------:|-----------:|
| mochila01.txt    | 7    | 23         | 107         | 23         | 4          |
| mochila02.txt    | 5    | 10         | 130         | 9          | 2          |
| mochila1000.txt  | 1000 | 12811      | 4135        | 12735      | 86         |
| mochila2500.txt  | 2500 | 31896      | 37138       | 31896      | 1102       |
| mochila5000.txt  | 5000 | 62862      | 71811       | 62862      | 2138       |

## Licença

Este projeto é distribuído sob a licença [MIT](LICENSE). Você é livre para usar, copiar, modificar e distribuir este código, desde que preserve o aviso de direitos autorais e a licença.
