# exceçao é um erro no processo de execuçao do programa 
# blocos try ... except 

def div(j,k):
    return round(j/k,2)

if __name__=='__main__':
    while True:
        try:
            n1 = int(input('digite um numero: '))
            n2 = int(input('digite outro numero: '))
            break
        except ValueError:
            print(f'ocorreu um erro de digitação, try again.')
        except ZeroDivisionError:
            print(f'tenta de novo, puta')

    try:
        r = div(n1,n2)
    except  ZeroDivisionError:

        print(f'infelizmente nao é possivel dividir por zero')

    except:
        print('Algo deu errado, tente novamente')
    else:
        print(f'resultado: {r}')
    finally:
        print('fim do calculo')

# try:
#     r = round(n1 / n2, 2) 
# except ZeroDivisionError:
#     print(f'infelizmente nao é possivel dividir por zero')
# else:
#     print(f'resultado: {r}')

