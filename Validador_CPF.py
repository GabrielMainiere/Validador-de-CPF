"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
"""
import sys

cpf_enviado_usuario = input('Digite seu CPF:').replace('.','').replace('-','')
nove_digitos = cpf_enviado_usuario[:9]
contagem_1 = 10
soma_1 = 0 

#verificando se o usuário enviou dados repetidos
entrada_repetida = cpf_enviado_usuario == cpf_enviado_usuario[0] *len(cpf_enviado_usuario)
if entrada_repetida:
    print('Você enviou dados sequenciais.')
    sys.exit()

#Algorítmo para encontrar o primeiro dígito de um CPF
for digito_1 in nove_digitos:
    multiplicacao_1 = int(digito_1) * contagem_1
    contagem_1 -= 1
    soma_1 +=multiplicacao_1

resultado_1 = (soma_1 *10) %11
if resultado_1 > 9:
    primeiro_digito = 0
else:
    primeiro_digito = resultado_1

#Algorítmo para encontrar o segundo dígito de um CPF
soma_2 = 0

dez_digitos = nove_digitos + str(primeiro_digito)
contagem_2 = 11
for digito_2 in dez_digitos:
    multiplicacao_2 = int(digito_2) * contagem_2
    contagem_2 -=1
    soma_2 += multiplicacao_2

resultado_2 = (soma_2 *10) % 11
if resultado_2 > 9:
    segundo_digito = 0
else:
    segundo_digito = resultado_2

#Validando o CPF
cpf_gerado = f'{nove_digitos}{primeiro_digito}{segundo_digito}'
if cpf_enviado_usuario == cpf_gerado:
    print('CPF válido.')
else:
    print('CPF inválido, verifique se digitou corretamente.')
