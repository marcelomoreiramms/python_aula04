# Python Aula 04 - Listas e Dicionários

## Exercícios de Listas e Dicionários

### 1. Lista de números ao quadrado

# ```python
# numeros: list = list(range(1, 11)) # Criando uma lista de números de 1 a 10
# for numero in numeros:
#     print(numero ** 2)
# ```

### 2. Modificar lista de linguagens

# ```python
# linguagem: list = ["Python", "Java", "C++", "JavaScript"] # Criando uma lista de linguagens de programação
# print("A lista original é:", linguagem) # Imprimindo a lista original
# linguagem.append("SQL") # Adicionando "SQL" à lista
# linguagem.remove("Java") # Removendo "Java" da lista
# print("A lista modificada é:", linguagem) # Imprimindo a lista modificada
# ```

### 3. Informações de um livro

# ```python
# livro: dict = {
#     "titulo": "O Senhor dos Anéis",
#     "autor": "J.R.R. Tolkien",
#     "ano_publicacao": 1954,
#     "genero": "Fantasia"
# }
# for chave, valor in livro.items():
#     print(f"{chave} : {valor}")
# ```

### 4. Contar ocorrências de caracteres

frase: str = input("Digite uma frase: ") # Solicitando ao usuário que digite uma frase
def contagem(frase) -> dict:
    caractere: dict = {} # Criando um dicionário vazio para armazenar a frequência dos caracteres
    for caractere in frase: # Iterando sobre cada caractere na frase
       contagem[caractere] = contagem.get(caractere, 0) + 1 # Incrementando a contagem do caractere
    return caractere
print(contagem(frase)) # Imprimindo a contagem dos caracteres na frase

### 5. Preço total da lista de compras


## Exercícios intermediários e mais avançados

### 6. Eliminação de Duplicatas

##### **Objetivo:** Dada uma lista de emails, remover todos os duplicados.


#### 7. Filtragem de Dados

##### **Objetivo:** Dada uma lista de idades, filtrar apenas aquelas que são maiores ou iguais a 18.


#### 8. Ordenação Personalizada

##### **Objetivo:** Dada uma lista de dicionários representando pessoas, ordená-las pelo nome.


#### 9. Agregação de Dados

##### **Objetivo:** Dado um conjunto de números, calcular a média.


#### 10. Divisão de Dados em Grupos

##### **Objetivo:** Dada uma lista de valores, dividir em duas listas: uma para valores pares e outra para ímpares.


### Exercícios com Dicionários

#### 11. Atualização de Dados

##### **Objetivo:** Dada uma lista de dicionários representando produtos, atualizar o preço de um produto específico.


#### 12. Fusão de Dicionários

##### **Objetivo:** Dados dois dicionários, fundi-los em um único dicionário.


#### 13. Filtragem de Dados em Dicionário

##### **Objetivo:** Dado um dicionário de estoque de produtos, filtrar aqueles com quantidade maior que 0.


#### 14. Extração de Chaves e Valores

##### **Objetivo:** Dado um dicionário, criar listas separadas para suas chaves e valores.


#### 15. Contagem de Frequência de Itens

##### **Objetivo:** Dada uma string, contar a frequência de cada caractere usando um dicionário.

