n = int(input())
if n <= 0:
    print('Número inválido')
if n == 1:
    print('Não primo')
if n == 2:
    print('Primo')
if n > 2:
    for i in range (2,n):
        if n % i == 0:
            print('Não primo')
            break
    else:
        print('Primo')
