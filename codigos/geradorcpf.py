# Módulo criador de cpfs aleatórios válidos
import random
import sys

def gerarcpf():

    nove_digitos = ''

    for i in range(9):          # Gera os 9 primeiros digitos do CPF
        nove_digitos += str(random.randint(0,9))


    # Lógica de calculo do governo para o primeiro digito final
    contador_regressivo1 = 10 
    result_digito1 = 0

    for numero in nove_digitos:     
        result_digito1 += int(numero) * contador_regressivo1
        contador_regressivo1 -= 1

    digito1 = (result_digito1 * 10) % 11
    digito1 = digito1 if digito1 <= 9 else 0

    # Lógica de calculo do governo para o segundo digito final
    dez_digitos = nove_digitos + str(digito1)
    contador_regressivo2 = 11
    result_digito2 = 0

    for numero in dez_digitos:
        result_digito2 += int(numero) * contador_regressivo2
        contador_regressivo2 -= 1

    digito2 = (result_digito2 * 10) % 11
    digito2 = digito2 if digito2 <= 9 else 0

    # Resultado da lógica - CPF válido gerado aleatoriamente
    cpf_gerado = nove_digitos + str(digito1) + str(digito2)
    
    return cpf_gerado
    
def validarcpf(numcpf):

    nove_digitos = numcpf[:9]

    # Lógica de calculo do governo para o primeiro digito final
    contador_regressivo1 = 10 
    result_digito1 = 0

    for numero in nove_digitos:     
        result_digito1 += int(numero) * contador_regressivo1
        contador_regressivo1 -= 1

    digito1 = (result_digito1 * 10) % 11
    digito1 = digito1 if digito1 <= 9 else 0

    # Lógica de calculo do governo para o segundo digito final
    dez_digitos = nove_digitos + str(digito1)
    contador_regressivo2 = 11
    result_digito2 = 0

    for numero in dez_digitos:
        result_digito2 += int(numero) * contador_regressivo2
        contador_regressivo2 -= 1

    digito2 = (result_digito2 * 10) % 11
    digito2 = digito2 if digito2 <= 9 else 0

    cpf_gerado = nove_digitos + str(digito1) + str(digito2)

    if cpf_gerado == numcpf:
        return ("CPF Válido")
    else:
        return ("CPF Inválido")