numero_base_decimal = eval(input("Digite um numero inteiro positivo: "))
numero_base_binaria = "{0:b}".format(numero_base_decimal)
print(f'Numero na base decimal: {numero_base_decimal}')
print(f'Numero na base binária: {numero_base_binaria}')

### Exemplo 1 ###
print("## Exemplo 1 - Usando While")

#Inicializando variáveis
numero = numero_base_decimal
binario = ""

#Realiza divisões por base 2
while numero > 0:
    if(numero % 2) > 0:
        binario = binario + '1'
    else:
        binario = binario + '0'
    numero = int(numero / 2)

binario = binario[(len(binario))::-1] #Inverte a leitura da string
print(f'Base becimal: {numero_base_decimal}')
print(f'Binario: {binario}')

### Exemplo 2 ###
print('## Exemplo 2 - Usando uma função')

#Inicializando variáveis
numero = numero_base_decimal

def converBinario(numero):
    binario = ""
    while numero > 0:
        if (numero % 2) > 0:
            binario = binario + '1'
        else:
            binario = binario + '0'
        numero = int(numero / 2)
    return binario[(len(binario))::-1]

print(f'Base becimal: {numero_base_decimal}')
print(f'Binario: {converBinario(numero)}')