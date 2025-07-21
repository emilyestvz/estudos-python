# Estruturas de Listas em Python

## O que são listas em Python?
- **Lista** é uma estrutura de dados que armazena uma sequência de valores de qualquer tipo (números, strings, booleanos e até outras listas).
- São **mutáveis**, ou seja, você pode alterar seus elementos ou o tamanho da lista.

## Como criar uma lista?
```python
minha_lista = [1, 2, 3, "Python", True]
lista_vazia = []
```

## Dicas 

### 1. Listas são mutáveis
- Você pode alterar, adicionar ou remover elementos a qualquer momento.
- Para adicionar, use `append()` (adiciona ao final) ou `insert()` (adiciona em uma posição específica).
- Para remover, utilize `remove()` (remove pelo valor), `pop()` (remove pelo índice) ou `del`.

### 2. Indexação e Fatiamento
- Acesse qualquer elemento pelo índice: `minha_lista`
- Índices negativos permitem acessar do fim para o começo: `minha_lista[-1]`
- Para obter sublistas, use o fatiamento: `minha_lista[1:3]` retorna o segundo e o terceiro elementos.

### 3. Métodos úteis de lista
- `append(x)`: adiciona `x` ao final da lista.
- `insert(i, x)`: adiciona `x` na posição `i`.
- `remove(x)`: remove a primeira ocorrência do valor `x`.
- `pop([i])`: remove e retorna o elemento na posição `i` (ou o último, se não especificar).
- `sort()`: ordena a lista em ordem crescente.
- `reverse()`: inverte a ordem da lista.
- `count(x)`: conta quantas vezes `x` aparece na lista.
- `index(x)`: retorna o índice da primeira ocorrência de `x`.

### 4. Compreensão de listas: código mais elegante
- Crie listas a partir de expressões compactas:
```python
quadrados = [x**2 for x in range(10)]
```
- Permite incluir condições:
```python
pares = [x for x in range(10) if x % 2 == 0]
```

### 5. Listas aninhadas (listas dentro de listas)
- Úteis para representar tabelas ou matrizes.
- Acesse elementos internos: `matriz[1]` (linha 0, coluna 1).

### 6. Atenção aos índices!
- Índices fora do intervalo geram o erro `IndexError`.
- Use `len(lista)` para saber o tamanho e evitar acessos inválidos.

### 7. Listas versus tuplas
- Listas: mutáveis, sintaxe com colchetes `[ ]`.
- Tuplas: imutáveis, sintaxe com parênteses `( )`.

## Práticas recomendadas

- Evite misturar tipos de dados na mesma lista (mantenha consistência sempre que possível).
- Prefira **compreensão de listas** para manipulação elegante e eficiente de dados.
- Para grandes volumes ou processamento numérico avançado, conheça arrays do NumPy[2].

## Problemas comuns e como evitar

- Erro de índices: sempre verifique o tamanho antes de acessar um elemento.
- Remover elementos durante iteração pode causar saltos indesejados; prefira criar uma nova lista quando necessário filtrar/limpar dados.

Aqui está um resumo com dicas valiosas sobre **tuplas em Python**, baseado no conteúdo do link indicado e nas principais fontes confiáveis:

<br><br>

## Tuplas em Python

### O que são tuplas?
- **Tuplas** são coleções ordenadas e **imutáveis** de elementos, ou seja, uma vez criadas, seus valores **não podem ser alterados, adicionados ou removidos**.
- São definidas por elementos separados por vírgulas, geralmente entre parênteses:  
  ```python
  minha_tupla = (1, 2, 3)
  ```
- Podem conter diversos tipos de dados juntos (heterogêneas), incluindo números, strings e até outras tuplas.

### Como criar tuplas

| Tipo de tupla           | Exemplo                     | Observações                               |
|------------------------|-----------------------------|------------------------------------------|
| Tupla vazia            | `tupla_vazia = ()`           | Necessário para criar tuplas sem elementos |
| Tupla com um elemento  | `tupla_um = (42,)`           | **Importante:** a vírgula depois do elemento é obrigatória para Python entender que é uma tupla e não um valor simples |
| Tupla com múltiplos elementos | `tupla_multi = (1, "dois", 3.0)` | Elementos separados por vírgulas       |

### Propriedades principais
- **Imutabilidade:** não permite alterar os elementos após a criação; isso previne modificações acidentais.
- **Ordenada:** os itens mantêm a ordem e podem ser acessados pelo índice, como listas (ex.: `minha_tupla`).
- Podem conter **objetos mutáveis**, como listas, mas alterar os objetos internos não altera a imutabilidade da tupla em si.
- São mais eficientes em performance e uso de memória que listas, especialmente para dados que não precisam mudar.

### Operações comuns com tuplas
- Acesso por índice: `minha_tupla`
- Desempacotamento:
  ```python
  a, b, c = (1, 2, 3)
  ```
- Concatenar cria uma nova tupla:
  ```python
  t1 = (1, 2)
  t2 = (3,)
  t3 = t1 + t2  # (1, 2, 3)
  ```
- Métodos limitados, exemplos:
  - `count(x)` conta quantas vezes aparece `x`
  - `index(x)` retorna o índice da primeira ocorrência de `x`

### Diferenças importantes entre tuplas e listas

| Característica      | Listas                  | Tuplas                      |
|---------------------|-------------------------|-----------------------------|
| Mutabilidade        | Mutáveis (podem ser alteradas) | Imutáveis (não podem ser alteradas) |
| Sintaxe             | Colchetes `[ ]`         | Parênteses `( )` ou só vírgulas para tuplas simples |
| Usos comuns         | Coleções que mudam, listas dinâmicas | Dados fixos, protegidos e constantes |
| Performance         | Um pouco mais lentas    | Um pouco mais rápidas, menos uso de memória |

### Dicas 

- Use tuplas para **dados que não devem mudar**, como coordenadas geográficas, configurações ou registros que precisam ser protegidos contra alterações acidentais.
- Ao criar tuplas com um único elemento, **não esqueça a vírgula** para evitar erros inesperados.
- Aproveite o fato de que tuplas podem armazenar objetos mutáveis para casos especiais, mas tome cuidado para não modificar os dados "indiretamente".
- Use o desempacotamento de tuplas para deixar o código mais limpo e legível.
- Para agrupar dados heterogêneos que representam um registro fixo, prefira tuplas, pois expressam a intenção de imutabilidade.

<br><br>

