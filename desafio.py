## Desafio: Criar um programa que solicite ao usuário que digite:
## o seu nome, o valor do seu salário e o valor do bônus recebido.

## Integrar na solução um fluxo de While
## que repita o fluxo até que o usuário insira as
## informações corretas

## Refatorar nosso código usando Dicionário, Type Hint e Funcões.

# Declaração de variáveis com tipagem

nome_valido: bool = False
salario_valido: bool = False
bonus_valido: bool = False

while nome_valido is False:
    try:
        # Solicita ao usuário que digite seu nome
        nome = input("Digite o nome do vendedor: ")
        # Verifica se o nome está vazio
        if len(nome) == 0:
            raise ValueError("O nome não pode estar vazio.")
        # Verifica se há números no nome
        elif any(char.isdigit() for char in nome):
            raise ValueError("O nome não deve conter números.")
        # Verifica se há apenas espaços no nome
        elif nome.isspace():
            raise ValueError("O nome não pode conter apenas espaços.")
        elif len(nome.strip()) == 0:
            raise ValueError("O nome não pode estar vazio.")
        else:
            print("Nome válido:", nome.title())
            nome_valido = True
    except ValueError as e:
        print(e)

# Solicita ao usuário que digite o valor do seu salário e converte para float
while salario_valido is False:
    try:
        salario = float(input("Digite o valor do salário: "))
        # Verifica se o salario é negativo
        if salario < 0:
            raise ValueError("O salário não pode ser negativo.")
        # Verifica se o salario está vazio
        if len(str(salario)) == 0:
            raise ValueError("O salário não pode estar vazio.")
        # Se o salário for válido, imprime a mensagem de sucesso e define a variável de controle para True
        else:
            print(f"Salário válido: R${salario:.2f}")
            salario_valido = True
    except ValueError as e:
        print(e)

# Solicita ao usuário que digite o valor do bônus recebido e converte para float
while bonus_valido is False:
    try:
        bonus = float(input("Digite a porcentagem do bônus: "))
        # Verifica se o bônus é negativo
        if bonus < 0:
            raise ValueError("O bônus não pode ser negativo.")
        # Verifica se o bônus está vazio
        if len(str(bonus)) == 0:
            raise ValueError("O bônus não pode estar vazio.")
        # Se o bônus for válido, imprime a mensagem de sucesso e define a variável de controle para True
        else:
            print(f"Bônus válido: {bonus:.2f}%")
        bonus_valido = True
    except ValueError as e:
        print(e)

# Calcula os valores de KPI do bônus recebido
bunus_recebido: float = salario * (bonus / 100)

# Cria um dicionário com o nome, salário e porcentagem de bonus
cadastro_vendedor: dict = {
    "Nome": f"{nome.title()}",
    "Salário": f"{salario:.2f}",
    "Bônus": f"{bonus}%",
    "Bônus recebido": f"{(1000 + bunus_recebido):.2f}",
    "Salário + bônus": f"{(salario + 1000 + bunus_recebido):.2f}",
}
# Imprime as informações ao usuário, separando os valores
print()
print(cadastro_vendedor)
