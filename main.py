numero = int(input())
if numero > 2:
    if numero % 2 == 0:
        print('Não primo')
    if numero % 2 != 0:
        print('Primo')
elif numero == 1:
    print('Não Primo')
elif numero == 2:
    print('Primo')
