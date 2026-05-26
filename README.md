# Python Aula 04 - Listas e Dicionários

## Exercícios de Listas e Dicionários

### 1. Lista de números ao quadrado

```python
# Criando uma lista de números de 1 a 10
numeros: list = list(range(1, 11))
for numero in numeros:
    print(numero ** 2)
```

### 2. Modificar lista de linguagens

```python
# Criando uma lista de linguagens de programação
linguagem: list = ["Python", "Java", "C++", "JavaScript"]
# Imprimindo a lista original
print("A lista original é:", linguagem)
linguagem.append("SQL") # Adiciona "SQL" à lista
linguagem.remove("Java") # Remove "Java" da lista
# Imprime a lista modificada
print("A lista modificada é:", linguagem)
```

### 3. Informações de um livro

```python
livro: dict = {
    "titulo": "O Senhor dos Anéis",
    "autor": "J.R.R. Tolkien",
    "ano_publicacao": 1954,
    "genero": "Fantasia"
}
for chave, valor in livro.items():
    # Imprime o valor de "chave" e "valor"
    print(f"{chave} : {valor}")
```

### 4. Contar ocorrências de caracteres

```python
# Solicita ao usuário que digite uma frase
frase: str = input("Digite uma frase: ")
def contagem(frase) -> dict:
    # Cria um dicionário vazio para armazenar a frequência dos caracteres
    contagem_dict: dict = {}
    for char in frase: # Itera sobre cada caractere na frase
        contagem_dict[char] = contagem_dict.get(char, 0) + 1 # Incrementa a contagem do caractere
    return contagem_dict
# Imprime a contagem dos caracteres na frase
print("Segue a contagem dos caracteres na frase:", contagem(frase))
```

### 5. Preço total da lista de compras

```python
produtos: list = [
    {"nome": "Arroz", "preco": 5.50},
    {"nome": "Feijão", "preco": 7.30},
    {"nome": "Macarrão", "preco": 3.20}
]
# Calcula o preço total dos produtos
total: float = sum(produto["preco"] for produto in produtos)
# Imprime o preço total formatado
print(f"O preço total da lista de compras é: R${total:.2f}")
```

## Exercícios intermediários e mais avançados

### 6. Eliminação de Duplicatas

##### **Objetivo:** Dada uma lista de emails, remover todos os duplicados.

```python
emails: list = [
    "user1@example.com",
    "user2@example.com",
    "user1@example.com",
    "user3@example.com"
]
# Converte a lista para um conjunto, elimina duplicatas e depois de volta para lista
emails_unicos: list = list(set(emails))
# Imprime a lista de emails sem duplicatas
print("Lista de emails sem duplicatas:", emails_unicos)
```

#### 7. Filtragem de Dados

##### **Objetivo:** Dada uma lista de idades, filtrar apenas aquelas que são maiores ou iguais a 18.

```python
# Cria uma lista de idades
idades: list = [15, 22, 17, 30, 18, 12]
# Usa list comprehension para filtrar idades maiores ou iguais a 18
idades_adultas: list = [idade for idade in idades if idade >= 18]
# Imprime as idades filtradas
print("Idades maiores ou iguais a 18:", idades_adultas)
```

#### 8. Ordenação Personalizada

##### **Objetivo:** Dada uma lista de dicionários representando pessoas, ordená-las pelo nome.

```python
pessoas: list = [
    {"nome": "Marcelo", "idade": 38},
    {"nome": "Janaina", "idade": 34},
    {"nome": "Marcelly", "idade": 12}
]
# Ordena a lista de pessoas pelo nome usando a função "sorted" e a função "lambda"
pessoas_ordenadas: list = sorted(pessoas, key=lambda pessoa: pessoa["nome"])
# Imprime a lista de pessoas ordenada por nome
print("Pessoas ordenadas por nome:", pessoas_ordenadas)
```

#### 9. Agregação de Dados

##### **Objetivo:** Dado um conjunto de números, calcular a média.

```python
# Solicita ao usuário para digitar um conjunto de números separados por vírgula
numeros_input: str = input("Digite um conjunto de números separados por vírgula: ")
# Converte a "string" de entrada em uma lista de números, remove espaços e converte para "float"
numeros_list: list = [float(num.strip()) for num in numeros_input.split(",")]
# Calcula a média dos números
media: float = sum(numeros_list) / len(numeros_list)
# Imprime a média formatada
print(f"A média dos números é: {media:.2f}")
```

#### 10. Divisão de Dados em Grupos

##### **Objetivo:** Dada uma lista de valores, dividir em duas listas: uma para valores pares e outra para ímpares.

```python
# Solicita ao usuário para digitar um conjunto de números separados por vírgula
numeros_input: str = input("Digite um conjunto de números por vírgula: ")
# Converte a "string" de entrada em uma lista de números, remove espaços e converte para "float"
numeros_list: list = [float(num.strip()) for num in numeros_input.split(",")]
# Cria uma lista de números pares usando "list comprehension"
pares: list = [num for num in numeros_list if num % 2 == 0]
# Cria uma lista de números ímpares usando "list comprehension"
impares: list = [num for num in numeros_list if num % 2 != 0]
# Imprime a lista de números pares e a lista de números ímpares
print(f"Números pares: {pares}")
print(f"Números ímpares: {impares}")
```

### Exercícios com Dicionários

#### 11. Atualização de Dados

##### **Objetivo:** Dada uma lista de dicionários representando produtos, atualizar o preço de um produto específico.

```python
produtos: list = [
    {"nome": "Arroz", "preco": 8.50},
    {"nome": "Feijão", "preco": 7.50},
    {"nome": "Macarrão", "preco": 3.20},
    {"nome": "Açúcar", "preco": 4.00},
    {"nome": "Sal", "preco": 2.50}
]
# Solicita ao usuário que digite o nome do produto a ser atualizado
produto_para_atualizar: str = input("Digite o nome do produto para atualizar o preço: ")
# Solicita ao usuário que digite o novo preço do produto
novo_preco: float = float(input("Digite o novo preço do produto: "))
# Iterando sobre a lista de produtos
for produto in produtos: 
    # Verifica se o nome do produto corresponde ao nome fornecido pelo usuário (ignorando maiúsculas/minúsculas)
    if produto["nome"].lower() == produto_para_atualizar.lower():
        # Atualiza o preço do produto
        produto["preco"] = novo_preco
        # Imprime uma mensagem de confirmação da atualização
        print(f"O preço do produto '{produto['nome']}' foi atualizado para R${novo_preco:.2f}")
        break # Saída do loop após atualizar o produto
else:
    # Imprime uma mensagem caso o produto não seja encontrado
    print(f"Produto '{produto_para_atualizar}' não encontrado na lista.")
# Imprime a lista de produtos atualizada
print("Segue a lista de produtos atualizada:", produtos)
```

#### 12. Fusão de Dicionários

##### **Objetivo:** Dados dois dicionários, fundi-los em um único dicionário.

```python
dicio1: dict = {"a": 1, "b": 2}
dicio2: dict = {"c": 3, "d": 4}
dicio_fundido: dict = {**dicio1, **dicio2}
print(f"Dicionário fundido: {dicio_fundido}")
```

#### 13. Filtragem de Dados em Dicionário

##### **Objetivo:** Dado um dicionário de estoque de produtos, filtrar aqueles com quantidade maior que 0.

```python
estoque: dict = {
    "Arroz": 10,
    "Feijão": 0,
    "Macarrão": 5,
    "Açúcar": 0,
    "Sal": 20
}
produtos_disponiveis: dict = {produto: quantidade for produto, quantidade in estoque.items() if quantidade > 0}
produtos_indisponiveis: dict = {produto: quantidade for produto, quantidade in estoque.items() if quantidade == 0}
print("Produtos disponíveis em estoque:", produtos_disponiveis)
print("Produtos indisponíveis em estoque:", produtos_indisponiveis)
```

#### 14. Extração de Chaves e Valores

##### **Objetivo:** Dado um dicionário, criar listas separadas para suas chaves e valores.

```python
dicionario: dict = {
    "nome": "Marcelo",
    "idade": 38,
    "cidade": "Cotia"
}
chaves: list = list(dicionario.keys())
valores: list = list(dicionario.values())
print(f"Chaves: {chaves}")
print(f"Valores: {valores}")
```

#### 15. Contagem de Frequência de Itens

##### **Objetivo:** Dada uma string, contar a frequência de cada caractere usando um dicionário.

```python
frase: str = input("Digite uma frase: ")
frequencia: dict = {}
for caractere in frase:
    if caractere in frequencia:
        frequencia[caractere] += 1
    else:
        frequencia[caractere] = 1
print(f"Frequência de caracteres: {frequencia}")
```
