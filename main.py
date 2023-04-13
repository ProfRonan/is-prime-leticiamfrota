numero = int(input())

if numero <= 0:
    print('Número inválido')
else:
    if numero % 2 == 0 and numero != 2:
            print('Não primo')
    if numero % 2 != 0 or numero == 2:
            print('Primo')