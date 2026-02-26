# funçoes 
# modularizaçao, reuso de codigo, facilita a leitura do codigo 

# def mensagem():
#     print('eu gosto de cavalos')
#     print('eu vou bater todos os recordes')
# mensagem()

# função com argumentos 

# def soma(a,b):
#     print(a+b)

# soma(2,2)

# def mult(x,y):
#     return x * y
# a = 4
# b = 6
# c = mult(a,b)
# print(c)

# def porc(k,j):
#       return ((k-j)/j)* 100

# if __name__ == '__main__':
#      a = float(input('digite um numero: '))
#      b = float(input('digite outro numero: '))
# if b == 0:
#      print('o segundo valor não pode ser zero')
# else:

#      r = porc(a,b)
#      print(f' {a} com relação à {b} é {r:.2f} % ')


# def div(k,j):
#     return k / j

# if __name__ == '__main__':
#     a = int(input('digite um numero: '))
#     b = int(input('digite outro numero: '))
# if b == 0:
#     print('o denominador não pode ser zero')
# else:
#     r = div(a,b)
#     print(f'{a} dividido por {b} é {r}')

# def quadrado(val):
#     quadrados = []
#     for x in val:
#         quadrados.append(x**2)
#     return quadrados 

# if __name__ == '__main__':
#     valores = [12,23,4567]
#     resultados = quadrado(valores)
#     for g in resultados:
#         print(g)

# def contar(num=10, caractere = '+'):
#     for i in range(1,num):
#         print(caractere)

# if __name__== '__main__':
#     contar(num=5, caractere= 'penis')


x = 3
y = 5
z = 8

def soma_mult(a,b,c='0'):
    if c=='0':
        return a * b
    else:
        return a + b + int(c) 
    
if __name__== '__main__':
    res = soma_mult(x,y)
    print(res)


def nossa_soma(linha):
    return linha.sum()


