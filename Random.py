import random 

# print('gerar 5 numeros aleatorios entre 1 e 50: \n')
# for i in range(5):
#     n = random.randint(1,50)
#     print(f'numero gerado:{n}')

# valor = random.random()
# print(f'o valor gerado foi:\n {round(valor * 10, 2)}')

# valor = random.uniform(1, 100)
# print(f'numero gerado:\n {valor}')

L = [1,223,4,43,54,65,67,7]
# n = random.choice(L)
# print(f'numero obtido: {n}')

# n = random.sample(L,3)
# print(f'numeros obtidos: {n}')

# embaralhar 

print(f'exibir a lista original: {L}')
print(f'embaralhar a lista:')
n = random.shuffle(L)
print(L)




