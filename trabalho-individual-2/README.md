# Projeto Trabalho Individual 2

Este projeto implementa o algoritmo de seleção simultânea do maior e menor elemento (MaxMin Select) utilizando a abordagem de divisão e conquista em Python.

---

## Algoritmo MaxMin Select

O algoritmo `maxmin_select` busca simultaneamente o maior e o menor valor de uma sequência de números inteiros usando recursão e divisão do problema em subproblemas menores.

* Caso base: Se o array tem tamanho 1, retorna o único elemento como máximo e mínimo.
* Caso geral: Divide o array ao meio, resolve recursivamente para as duas metades, e combina os resultados escolhendo os valores máximos e mínimos entre as metades.

---

## Como executar o projeto

1. Instale o Python em [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Salve o código acima em um arquivo chamado `main.py`
3. Abra o terminal ou prompt de comando
4. Navegue até o diretório onde `main.py` está salvo
5. Execute o comando:

   ```bash
   python main.py
   ```
6. Insira a quantidade de números e os valores conforme solicitado

---

## Versão do Python

Este projeto foi desenvolvido e testado na versão 3.13.3 do Python.

---

## Complexidade Assintótica

**Temporal:**

* Melhor caso: O(n) — ocorre quando o array tem apenas um elemento.
* Caso médio e pior caso: O(n) — o algoritmo percorre o array dividindo e comparando em cada nível da recursão.

**Espacial:**

* Caso médio e pior caso: O(log n) — devido à profundidade da recursão que divide o array ao meio a cada chamada.

---

## Complexidade Ciclomática

Analisando o código da função `maxmin_select` considerando que cada linha que atribui valor não nulo para uma variável conta como um nó, temos:

| Nó | Descrição                            |
| -- | ------------------------------------ |
| 1  | Início da função                     |
| 2  | Atribuição `n = len(arr)`            |
| 3  | Teste `if n == 1`                    |
| 4  | Retorno no caso base                 |
| 5  | Atribuição `mid = n // 2`            |
| 6  | Chamada recursiva `max1, min1 = ...` |
| 7  | Chamada recursiva `max2, min2 = ...` |
| 8  | Teste `if max1 > max2`               |
| 9  | Atribuição `maximum = max1`          |
| 10 | Atribuição `maximum = max2`          |
| 11 | Teste `if min1 < min2`               |
| 12 | Atribuição `minimum = min1`          |
| 13 | Atribuição `minimum = min2`          |
| 14 | Retorno `return maximum, minimum`    |

**Total de nós (N): 14**

**Total de arestas (E): 16** (arestas que conectam cada passo e decisões)

**Componentes conexos (P): 1**

---

### Cálculo:

$$
M = E - N + 2P = 16 - 14 + 2 \times 1 = 4
$$

---

### Interpretação:

A complexidade ciclomática é **4**, indicando que o fluxo do código possui 4 caminhos independentes:

1. Caso base: `n == 1`
2. Caso recursivo: `max1 > max2` e `min1 < min2`
3. Caso recursivo: `max1 > max2` e `min1 >= min2`
4. Caso recursivo: `max1 <= max2` (ambos casos de `min1 < min2` ou `min1 >= min2`)
<!-- COMENTÁRIO TESTE-->

