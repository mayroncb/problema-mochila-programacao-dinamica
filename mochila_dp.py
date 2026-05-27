#!/usr/bin/env python3
"""Solução do problema da Mochila Inteira 0/1 usando Programação Dinâmica.

Este módulo lê instâncias do problema no formato especificado pelo enunciado da
disciplina e calcula o valor máximo obtido, o peso total utilizado e a
quantidade de itens selecionados. A instância deve ser fornecida em um
arquivo de texto com o seguinte formato:

```
n M
peso_1 valor_1
peso_2 valor_2
...
peso_n valor_n
```

Onde ``n`` é o número de itens, ``M`` é a capacidade máxima da mochila,
``peso_i`` é o peso do i‑ésimo item e ``valor_i`` é o valor correspondente.

O programa recebe como argumento o caminho para o arquivo da instância e
escreve o resultado no terminal. Para calcular as soluções de todas as
instâncias na pasta ``instancias``, execute este script sem argumentos.

"""
from __future__ import annotations

import os
import csv
import sys
from dataclasses import dataclass


@dataclass
class Resultado:
    """Representa o resultado de uma instância da mochila."""
    nome: str
    n: int
    capacidade: int
    valor_otimo: int
    peso_usado: int
    quantidade_itens: int

    def to_row(self) -> list[str | int]:
        return [
            self.nome,
            str(self.n),
            str(self.capacidade),
            str(self.valor_otimo),
            str(self.peso_usado),
            str(self.quantidade_itens),
        ]


def ler_instancia(caminho: str) -> tuple[list[int], list[int], int]:
    """Lê uma instância da mochila no formato especificado.

    Args:
        caminho: Caminho para o arquivo da instância.

    Returns:
        Uma tupla (pesos, valores, capacidade).
    """
    with open(caminho, "r", encoding="utf-8") as f:
        primeira = f.readline().strip().split()
        n = int(primeira[0])
        capacidade = int(primeira[1])
        pesos: list[int] = []
        valores: list[int] = []
        for linha in f:
            linha = linha.strip()
            if not linha:
                continue
            p, v = map(int, linha.split())
            pesos.append(p)
            valores.append(v)
        if len(pesos) != n:
            raise ValueError(
                f"Instância {caminho!r} inválida: número de itens não confere ({len(pesos)} != {n})"
            )
    return pesos, valores, capacidade


def resolver_mochila(pesos: list[int], valores: list[int], capacidade: int) -> tuple[int, int, int]:
    """Resolve uma instância da mochila usando programação dinâmica.

    A função implementa a versão otimizada em espaço para o problema 0/1,
    acompanhando não apenas o valor máximo mas também o peso total e a
    quantidade de itens necessária para reconstruir a solução. Em caso de
    empates de valor, prefere soluções com peso menor e, em seguida, com
    menor quantidade de itens.

    Args:
        pesos: Lista de pesos dos itens.
        valores: Lista de valores dos itens.
        capacidade: Capacidade máxima da mochila.

    Returns:
        Uma tupla (valor_otimo, peso_usado, quantidade_itens).
    """
    # Estruturas para armazenar o melhor valor, peso e quantidade de itens
    dp_valor = [0] * (capacidade + 1)
    dp_peso = [0] * (capacidade + 1)
    dp_count = [0] * (capacidade + 1)

    for peso_item, valor_item in zip(pesos, valores):
        # Atualiza as células da direita para a esquerda para preservar a semântica 0/1
        for c in range(capacidade, peso_item - 1, -1):
            candidato_valor = dp_valor[c - peso_item] + valor_item
            candidato_peso = dp_peso[c - peso_item] + peso_item
            candidato_count = dp_count[c - peso_item] + 1

            # Atualiza se o valor for maior ou se empatar com melhor peso/quantidade
            if (
                candidato_valor > dp_valor[c]
                or (candidato_valor == dp_valor[c] and candidato_peso < dp_peso[c])
                or (
                    candidato_valor == dp_valor[c]
                    and candidato_peso == dp_peso[c]
                    and candidato_count < dp_count[c]
                )
            ):
                dp_valor[c] = candidato_valor
                dp_peso[c] = candidato_peso
                dp_count[c] = candidato_count

    return dp_valor[capacidade], dp_peso[capacidade], dp_count[capacidade]


def processar_instancia(caminho: str) -> Resultado:
    """Processa uma instância, retornando um objeto Resultado."""
    nome = os.path.basename(caminho)
    pesos, valores, capacidade = ler_instancia(caminho)
    valor_otimo, peso_usado, quantidade = resolver_mochila(pesos, valores, capacidade)
    return Resultado(nome, len(pesos), capacidade, valor_otimo, peso_usado, quantidade)


def main(argv: list[str]) -> None:
    """Ponto de entrada do script.

    Se um argumento de caminho for passado, processa apenas essa instância.
    Caso contrário, processa todas as instâncias na pasta ``instancias`` do
    diretório atual e grava os resultados em arquivos ``resultados_mochila.txt``
    e ``resultados_mochila.csv``.
    """
    if len(argv) > 1:
        caminho = argv[1]
        resultado = processar_instancia(caminho)
        print(
            f"Instância: {resultado.nome}\n"
            f"n: {resultado.n}\n"
            f"Capacidade: {resultado.capacidade}\n"
            f"Valor ótimo: {resultado.valor_otimo}\n"
            f"Peso usado: {resultado.peso_usado}\n"
            f"Quantidade de itens: {resultado.quantidade_itens}"
        )
        return

    # Processa todas as instâncias na pasta "instancias"
    pasta_instancias = os.path.join(os.path.dirname(__file__), "instancias")
    entradas = [
        os.path.join(pasta_instancias, nome)
        for nome in sorted(os.listdir(pasta_instancias))
        if nome.lower().endswith(".txt")
    ]
    resultados: list[Resultado] = []
    for caminho in entradas:
        resultados.append(processar_instancia(caminho))

    # Grava resultado em TXT
    with open(os.path.join(os.path.dirname(__file__), "resultados_mochila.txt"), "w", encoding="utf-8") as f:
        for r in resultados:
            f.write(
                f"Instância: {r.nome}\n"
                f"n: {r.n}\n"
                f"Capacidade: {r.capacidade}\n"
                f"Valor ótimo: {r.valor_otimo}\n"
                f"Peso usado: {r.peso_usado}\n"
                f"Quantidade de itens: {r.quantidade_itens}\n\n"
            )

    # Grava resultado em CSV
    with open(os.path.join(os.path.dirname(__file__), "resultados_mochila.csv"), "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            "instancia",
            "n",
            "capacidade",
            "valor_otimo",
            "peso_usado",
            "quantidade_itens",
        ])
        for r in resultados:
            writer.writerow(r.to_row())

    for r in resultados:
        print(
            f"{r.nome}: valor={r.valor_otimo}, peso={r.peso_usado}, itens={r.quantidade_itens}"
        )


if __name__ == "__main__":
    main(sys.argv)
