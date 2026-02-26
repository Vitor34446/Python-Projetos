# formula geral para o fatorial:
# fatorial(num): = 1, se num = 0 ou se num = 1.'caso-base'
# fatorial(num): num * (num-1), para num >1.'caso-recursivo'
# 4! 4 * fatorial(3)= 4 * 3 * fatorial(2)=...

def fatorial(numero):
    if numero == 0 or numero ==1:
        return 1
    else:
        return numero * fatorial(numero-1)


# if __name__=='__main__':
#     x = int(input('digite um numero inteiro positivo para fatorial: '))
#     try:
#         res = fatorial(x)
#     except RecursionError:
#         print(f'número muito grande ou número negativo')
#     else:
#         print(f'a resposta do fatorial é {res}')
#     finally:
#         print(f'fim da conta')


if __name__=='__main__':
    x = int(input('digite um numero inteiro positivo para fatorial: '))
    try:
            res = fatorial(x)
    except RecursionError:
            print(f'número muito grande ou número negativo')
    else:
            print(f'a resposta de {x} é {res}')
    finally:
            print(f'fim da conta')


    


 
