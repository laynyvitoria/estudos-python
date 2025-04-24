# =======================================
##======== VARIAVEIS EM PYTHON ========##
# =======================================

# Criação de variáveis com tipos diferentes
nome = 'Layny'  # String
nome2 = 'Mario'  # String
idade = 25  # Inteiro
altura = 1.8  # Float
estudantes = True  # Booleano
resultado = None  # Similar ao null/nil

# Verificando o tipo de cada variável
print(type(nome))  # <class 'str'>
print(type(idade))  # <class 'int'>
print(type(altura))  # <class 'float'>
print(type(estudantes))  # <class 'bool'>

# Convenções de nomeação de variáveis

# Nomes válidos
variavel = 10
variavel_completa = 20
_variavel_interna = 30
VariavelMaiuscula = 40
variavel2 = 50

# Atribuição múltipla
x, y, z = 10, 20, 30
print("Valores de x, y, z:", x, y, z)

# Troca de valores
var1, var2 = 5, 10
print("Antes da troca:", var1, var2)
var1, var2 = var2, var1
print("Após a troca:", var1, var2)

# Constantes (por convenção, são escritas em maiúsculas)
PI = 3.14159
TAXA_JUROS = 0.05
print("Valor de PI:", PI)
print("Taxa de juros:", TAXA_JUROS)

# Reatribuição dinâmica de tipo
valor = 10
print("Antes da reatribuição:", valor, type(valor))

valor = "dez"
print("Após a reatribuição:", valor, type(valor))

# Exemplo de uso de variáveis em um contexto prático: Cálculo de IMC

nome = "Carlos"
idade = 28
altura = 1.75
peso = 70

# Cálculo do IMC
imc = peso / (altura ** 2)

# Exibição dos resultados
print(f"{nome} tem {idade} anos, altura de {altura} metros e peso de {peso} kg.")
print(f"O IMC de {nome} é: {imc:.2f}")
