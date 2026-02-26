# funçoes lamba ou funçoes anonimas 
# suntaxe 
# lambda argumentos: expressao 

# quadrados = lambda x :(x**2)

# for i in range(1,11):
#     print(quadrados(i))

# par = lambda x: x %2 == 0
# print(par(8))

# f_c = lambda f: (f - 32) * 5/9
# print(round(f_c(6),2))





# função map()
# sintaxe
# map( função, iteravel)





# num = [1,2,3,4,5,6,7]
# dobro = list(map(lambda x: x * 2, num))
# print(dobro)

# palavras = ['eu','gosto','de','carros']
# maiusculas = list(map(str.upper, palavras))
# print(maiusculas)



# função filter()
# sintaxe
# filter (função, sequencia)



# def num_pares(n):
#     return n %2== 0
# numeros = [233,23,33,344,3,4,45,45667]
# num_par = list(filter(num_pares, numeros))
# print(num_par)

# num_impar = list(filter(lambda x: x %2!=0, numeros))
# print(num_impar)



# função reduce()

from functools import reduce

# def mult(x,y):
#     return x * y
# lista = [1,2,3,3,4,5,9]

# total = reduce(mult,lista)
# print(total)


# soma cumulativa dos quadrados de valores, usando expressao lambda

numero = [1,2,3,4,5,6,7,8,9,10]

# total = reduce(lambda x,y: x**2 + y**2, numero)
# print(total)

# total = reduce(lambda x,y,z: x/y*z, numero)
# print(total)

x,y,z = numero[:3]
total = (x/y) *  z
print(total)

import pandas as pa

