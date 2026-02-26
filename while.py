# num = 1
# while(num <= 10):
#     print(num)
#     num += 1
# print('laço encerrado')

nome = None
while True:
    print('digite seu nome, ou x para parar:')
    nome = input()
    if nome == 'x' or nome == 'X':
        break
    print(f'bem vindo {nome}') 
print('adeus!!')