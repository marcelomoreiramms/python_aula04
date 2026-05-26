# Python Aula 04 - Funções

# Solicita ao usuário digitar uma lista de números
numeros: str = input("Digite uma lista de numeros separados por virgulas:")

# Converte a variável de entrada em uma lista de números e remove os espaços
lista: list = [int(num.strip()) for num in numeros.split(",")]

# Cria uma função personalizada para ordenar por seleção
def numeros_ordenados(lista: list) -> list:
    nova_lista = lista.copy()
    for i in range(len(nova_lista)):
        for j in range(i+1, len(nova_lista)):
            if nova_lista[i] > nova_lista[j]:
                nova_lista[i], nova_lista[j] = nova_lista[j], nova_lista[i]
    return nova_lista

# Ordenando a lista
nova_lista = numeros_ordenados(lista)
print("Segue a lista ordenada com função personalizada:", nova_lista)