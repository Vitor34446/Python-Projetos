# trocar valores entre duas variaveis 

var1 = 33
var2 = 23
# var1, var2 = var2, var1 

# print(f'var1:{var1}, var2:{var2}')

# operador condicional Ternario 


# maior = var1 if var1 > var2 else var2
# print(f'Maior valor: {maior}')
# print(f'Maior valor: {(var1, var2)[var2>var1]}')


# generators


# valores = [1,2,35,6,78,9,5]
# for num in valores:
#     quadra = (num ** 2)
#     print(quadra)
# quadrados = (itens **2 for itens in valores)
# print(quadrados)
# for valor in quadrados:
#     print(valor)


# função enumerate()

# bebidas = ['suco', 'coca-cola','Pepsi','leite']
# for i, item in enumerate(bebidas):
#     print(f'indice: {i + 1}  Item:{item}')


temperatura = [-2,43,5,7,-12]
total = 0

# for i, t in enumerate(temperatura):
#     if t < 0:
#         total +=1

# print(f'temos {total} temperaturas negativas')

# for i, t in enumerate(temperatura):
#     if t < 0:
#         print(f'no local {i +1 } é negativo, com {t} graus')



# gerenciamento de contexto com with

with open('frutas.txt','r',encoding='utf-8')as a:
    for linha in a:
        print(linha, end = ' ')

