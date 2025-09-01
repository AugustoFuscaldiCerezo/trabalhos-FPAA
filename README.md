# Projeto Trabalho Individual 1

O Trabalho Individual 1 é um projeto desenvolvido para implementar e demonstrar o algoritmo de multiplicação rápida de Karatsuba, que permite multiplicar grandes números inteiros de forma mais eficiente do que a multiplicação tradicional.

## Algoritmo de Karatsuba

O algoritmo de Karatsuba é uma técnica de multiplicação recursiva que reduz o número de multiplicações necessárias ao dividir os números em partes menores e combinar os resultados usando uma fórmula matemática específica:

```(ac * 10^(2m)) + ((ab+cd - ac - bd) * 10^m) + bd```

Esse método é especialmente útil para multiplicar números grandes, onde a multiplicação tradicional é muito lenta.

## Como executar o projeto

1. Fazer o download do Python em https://www.python.org/downloads/
2. Fazer a instalação do Python
3. Configurar as variáveis de ambiente
4. Baixar o projeto em sua pasta de escolha
6. Abrir o CMD do windows
7. Digitar o caminho até a pasta onde se encontra o main.py
```cd exemplo\de\caminho\do\projeto```
9. Executar o comando ```main.py``` ou ```python main.py``` no cmd dentro da pasta onde se encontra o arquivo main.py

Exemplo do funcionamento:

- Digite o primeiro número inteiro: 12345 <- input
- Digite o segundo número inteiro: 12345 <- input
- Usando Karatsuba(x,y) = 152399025 <- resultado do algorítmo
- Prova usando x * y = 152399025 <- prova

## Versão do Python
Este projeto foi desenvolvido na versão 3.13.3 do Python.

## Complexidade Assintótica

**Temporal:**
- Melhor caso: O(n)
- Caso médio: O(n^(log(2)3)
- Pior caso: O(n^(log(2)3)

**Espacial:**
- Melhor caso: O(1)
- Caso médio: O(log(n))
- Pior caso: O(log(n))

## Complexidade Ciclomática

Análise do código:

**Nós:**

N1 -	Início da função karatsuba

N2 -	Teste da condição if x < 10 or y < 10

N3 -	Retorno return x * y

N4 -	Cálculo de m

N5 -	Cálculo de a, b, c, d

N6 -	Chamada recursiva bd = karatsuba(b, d)

N7 -	Chamada recursiva ab_vezes_cd = karatsuba(a + b, c + d)

N8 -	Chamada recursiva ac = karatsuba(a, c)

N9 -	Retorno final com a expressão da fórmula de Karatsuba

- Total de nós: 9

**Arestas:**

N1 -	N2	Entrando na função, vai para o if

N2 -	N3	Se x < 10 or y < 10 for verdadeiro

N2 -	N4	Se x >= 10 e y >= 10 (condição falsa)

N4 -	N5	cálculo de a, b, c, d

N5 -	N6	chamada karatsuba(b, d)

N6 -	N7	chamada karatsuba(a + b, c + d)

N7 -	N8	chamada karatsuba(a, c)

N8 -	N9	calcula o resultado final

N3 -	fim	Retorno do caso base

N9 -	fim	Retorno do caso geral

- Total de arestas: 10

**Calculo:**
- M = 10 - 9 + 2(1)
- M = 3 (O número de caminhos possíveis depende do tamanho dos números por conta da recursividade, mas no geral serão 3 caminhos)

