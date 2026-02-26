from math import sqrt

# class NumeroNegativoError(Exception):
#     def __init__(self):
#         pass


if __name__=='__main__':
    while True:
        try:
            num =  int(input('Digite um numero positivo: '))
            if num<0:
                raise ArithmeticError
            break
        except ArithmeticError:
            print(f'voce colocou um numero negativo')
        except:
            print(f'algo deu errado')
    try:
        r=sqrt(num)
    except:
        print(f'algum erro ocorreu')

    else:
        print(f'A raiz quadrada de {num} é {sqrt(num)}')  
    finally:
        print('fim do calculo')  


# if __name__=='__main__':
#     try:
#          num =  int(input('Digite um numero positivo: '))
#          if num<0:
#             raise ArithmeticError
#     except ArithmeticError:
#         print(f'voce colocou um numero negativo')
#     else:
#         print(f'A raiz quadrada de {num} é {sqrt(num)}')  
#     finally:
#         print('fim do calculo')  

