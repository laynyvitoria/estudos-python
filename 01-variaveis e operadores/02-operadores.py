# =======================================
# OPERADORES ARITMÉTICOS E LÓGICOS EM PYTHON
# =======================================

# -------- OPERADORES ARITMÉTICOS --------
# Usados para realizar operações matemáticas com números

a = 10
b = 3

# Soma: adiciona dois valores
soma = a + b  # Resultado: 13

# Subtração: subtrai o segundo valor do primeiro
subtracao = a - b  # Resultado: 7

# Multiplicação: multiplica os dois valores
multiplicacao = a * b  # Resultado: 30

# Divisão: retorna um número float (mesmo que a divisão seja exata)
divisao = a / b  # Resultado: 3.333...

# Divisão inteira: descarta os decimais
divisao_inteira = a // b  # Resultado: 3

# Módulo: retorna o resto da divisão
modulo = a % b  # Resultado: 1

# Exponenciação: eleva o primeiro número à potência do segundo
potencia = a ** b  # Resultado: 1000


# Exemplo prático:
# Calcular o total a pagar em uma compra
preco_unitario = 49.90
quantidade = 3
total_compra = preco_unitario * quantidade  # Resultado: 149.7


# -------- OPERADORES LÓGICOS --------
# Utilizados para comparar valores booleanos (True ou False)

x = True
y = False

# AND: retorna True se ambos forem True
resultado_and = x and y  # Resultado: False

# OR: retorna True se pelo menos um for True
resultado_or = x or y  # Resultado: True

# NOT: inverte o valor lógico
resultado_not = not x  # Resultado: False


# Exemplo prático 1:
# Verificar se uma pessoa pode dirigir
idade = 20
tem_carteira = True
pode_dirigir = idade >= 18 and tem_carteira  # Resultado: True

# Exemplo prático 2:
# Entrada em evento: permitido se tiver convite ou estiver na lista VIP
tem_convite = False
esta_na_lista_vip = True
entrada_liberada = tem_convite or esta_na_lista_vip  # Resultado: True

# Exemplo prático 3:
# Negar acesso se a senha estiver errada
senha_correta = False
acesso_negado = not senha_correta  # Resultado: True

# -------- COMBINAÇÃO DE LÓGICOS E ARITMÉTICOS --------

# Situação: desconto só se a compra for acima de 100 reais e o cliente for VIP
valor_compra = 120
cliente_vip = True
tem_desconto = valor_compra > 100 and cliente_vip  # Resultado: True

# Situação: exibir alerta se a temperatura for menor que 15 ou maior que 35
temperatura = 12
alerta = temperatura < 15 or temperatura > 35  # Resultado: True

# Situação: só aceitar números pares positivos
numero = 8
validacao = numero > 0 and numero % 2 == 0  # Resultado: True
