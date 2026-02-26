# viado = input('você dá a bunda?')

# if viado == 'sim':    print('fã do Carlinhos')

# elif viado == 'não':    print('você não bebeu porra o suficiente')

# else:    print('responda a pergunta, pequeno sangue')
# import random 

# for i in range(3):
#     n = random.random()
#     print(f'valores gerados: {round(n * 100, 2)}')


# bebidas = []
# for i in range(5):
#     print('digite sua bebida favorita:')
#     bebida = input()
#     bebidas.append(bebida)

# bebidas.sort()

# print(f'\nsuas bebidas escolhidas foram:')
# for bebida in bebidas:
#     print(bebida)
# print(f'saude!!!')

bebidas = []
for i in range(5):
     print('digite sua bebida favorita:')
    
     bebidas.append(input())


bebidas.sort()
print(f'suas bebidas escolhidas foram:\n')
for bebida in bebidas:
     print(bebida)
print('\nsaúde!!!!')