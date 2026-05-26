# Python Aula 04 - Listas e Dicionários

## Exercícios de Listas e Dicionários

### 1. Lista de números ao quadrado

numeros: list = list(range(1, 11)) # Criando uma lista de números de 1 a 10
for numero in numeros:
    print(numero ** 2)

### 2. Modificar lista de linguagens

linguagem: list = ["Python", "Java", "C++", "JavaScript"] # Criando uma lista de linguagens de programação
print("A lista original é:", linguagem) # Imprimindo a lista original
linguagem.append("SQL") # Adicionando "SQL" à lista
linguagem.remove("Java") # Removendo "Java" da lista
print("A lista modificada é:", linguagem) # Imprimindo a lista modificada

### 3. Informações de um livro

livro: dict = {
    "titulo": "O Senhor dos Anéis",
    "autor": "J.R.R. Tolkien",
    "ano_publicacao": 1954,
    "genero": "Fantasia"
}
for chave, valor in livro.items():
    print(f"{chave} : {valor}")

### 4. Contar ocorrências de caracteres

frase: str = input("Digite uma frase: ") # Solicitando ao usuário que digite uma frase
def contagem(frase) -> dict:
    contagem_dict: dict = {} # Criando um dicionário vazio para armazenar a frequência dos caracteres
    for char in frase: # Iterando sobre cada caractere na frase
        contagem_dict[char] = contagem_dict.get(char, 0) + 1 # Incrementando a contagem do caractere
    return contagem_dict
print("Segue a contagem dos caracteres na frase:", contagem(frase)) # Imprimindo a contagem dos caracteres na frase

### 5. Preço total da lista de compras

produtos: list = [
    {"nome": "Arroz", "preco": 5.50},
    {"nome": "Feijão", "preco": 7.30},
    {"nome": "Macarrão", "preco": 3.20}
]
total: float = sum(produto["preco"] for produto in produtos) # Calculando o preço total dos produtos
print(f"O preço total da lista de compras é: R${total:.2f}") # Imprimindo o preço total formatado

## Exercícios intermediários e mais avançados

### 6. Eliminação de Duplicatas

##### **Objetivo:** Dada uma lista de emails, remover todos os duplicados.

emails: list = [
    "user1@example.com",
    "user2@example.com",
    "user1@example.com",
    "user3@example.com"
]
emails_unicos: list = list(set(emails)) # Convertendo a lista para um conjunto para eliminar duplicatas e depois de volta para lista
print("Lista de emails sem duplicatas:", emails_unicos) # Imprimindo a lista de emails sem duplicatas

#### 7. Filtragem de Dados

##### **Objetivo:** Dada uma lista de idades, filtrar apenas aquelas que são maiores ou iguais a 18.

idades: list = [15, 22, 17, 30, 18, 12] # Criando uma lista de idades
idades_adultas: list = [idade for idade in idades if idade >= 18] # Usando list comprehension para filtrar idades maiores ou iguais a 18
print("Idades maiores ou iguais a 18:", idades_adultas) # Imprimindo as idades filtradas

#### 8. Ordenação Personalizada

##### **Objetivo:** Dada uma lista de dicionários representando pessoas, ordená-las pelo nome.

pessoas: list = [
    {"nome": "Marcelo", "idade": 38},
    {"nome": "Janaina", "idade": 34},
    {"nome": "Marcelly", "idade": 12}
]
pessoas_ordenadas: list = sorted(pessoas, key=lambda pessoa: pessoa["nome"]) # Ordenando a lista de pessoas pelo nome usando a função sorted e uma função lambda
print("Pessoas ordenadas por nome:", pessoas_ordenadas) # Imprimindo a lista de pessoas ordenada por nome

#### 9. Agregação de Dados

##### **Objetivo:** Dado um conjunto de números, calcular a média.

numeros_input: str = input("Digite um conjunto de números separados por vírgula: ") # Armazenando a entrada do usuário em uma variável
numeros_list: list = [float(num.strip()) for num in numeros_input.split(",")] # Convertendo a string de entrada em uma lista de números, removendo espaços e convertendo para float
media: float = sum(numeros_list) / len(numeros_list) # Calculando a média dos números
print(f"A média dos números é: {media:.2f}") # Imprimindo a média formatada

#### 10. Divisão de Dados em Grupos

##### **Objetivo:** Dada uma lista de valores, dividir em duas listas: uma para valores pares e outra para ímpares.

numeros_input: str = input("Digite um conjunto de números por vírgula: ") # Armazenando a entrada do usuário em uma variável
numeros_list: list = [float(num.strip()) for num in numeros_input.split(",")] # Convertendo a string de entrada em uma lista de números, removendo espaços e convertendo para float
pares: list = [num for num in numeros_list if num % 2 == 0] # Criando uma lista de números pares usando list comprehension
impares: list = [num for num in numeros_list if num % 2 != 0] # Criando uma lista de números ímpares usando list comprehension
print(f"Números pares: {pares}") # Imprimindo a lista de números pares
print(f"Números ímpares: {impares}") # Imprimindo a lista de números ímpares

### Exercícios com Dicionários

#### 11. Atualização de Dados

##### **Objetivo:** Dada uma lista de dicionários representando produtos, atualizar o preço de um produto específico.

produtos: list = [
    {"nome": "Arroz", "preco": 8.50},
    {"nome": "Feijão", "preco": 7.50},
    {"nome": "Macarrão", "preco": 3.20},
    {"nome": "Açúcar", "preco": 4.00},
    {"nome": "Sal", "preco": 2.50}
]
produto_para_atualizar: str = input("Digite o nome do produto para atualizar o preço: ") # Solicitando ao usuário que digite o nome do produto a ser atualizado
novo_preco: float = float(input("Digite o novo preço do produto: ")) # Solicitando ao usuário que digite o novo preço do produto

for produto in produtos: # Iterando sobre a lista de produtos
    if produto["nome"].lower() == produto_para_atualizar.lower(): # Verificando se o nome do produto corresponde ao nome fornecido pelo usuário (ignorando maiúsculas/minúsculas)
        produto["preco"] = novo_preco # Atualizando o preço do produto
        print(f"O preço do produto '{produto['nome']}' foi atualizado para R${novo_preco:.2f}") # Imprimindo uma mensagem de confirmação da atualização
        break # Saindo do loop após atualizar o produto
else:
    print(f"Produto '{produto_para_atualizar}' não encontrado na lista.") # Imprimindo uma mensagem caso o produto não seja encontrado
print("Segue a lista de produtos atualizada:", produtos) # Imprimindo a lista de produtos atualizada

#### 12. Fusão de Dicionários

##### **Objetivo:** Dados dois dicionários, fundi-los em um único dicionário.

dicio1: dict = {"a": 1, "b": 2}
dicio2: dict = {"c": 3, "d": 4}
dicio_fundido: dict = {**dicio1, **dicio2}
print(f"Dicionário fundido: {dicio_fundido}")

#### 13. Filtragem de Dados em Dicionário

##### **Objetivo:** Dado um dicionário de estoque de produtos, filtrar aqueles com quantidade maior que 0.

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

#### 14. Extração de Chaves e Valores

##### **Objetivo:** Dado um dicionário, criar listas separadas para suas chaves e valores.

dicionario: dict = {
    "nome": "Marcelo",
    "idade": 38,
    "cidade": "Cotia"
}
chaves: list = list(dicionario.keys())
valores: list = list(dicionario.values())
print(f"Chaves: {chaves}")
print(f"Valores: {valores}")

#### 15. Contagem de Frequência de Itens

##### **Objetivo:** Dada uma string, contar a frequência de cada caractere usando um dicionário.

frase: str = input("Digite uma frase: ")
frequencia: dict = {}
for caractere in frase:
    if caractere in frequencia:
        frequencia[caractere] += 1
    else:
        frequencia[caractere] = 1
print(f"Frequência de caracteres: {frequencia}")
