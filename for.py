# lista = [2,3,6,7,43,56]
# palavra = 'sexo'
# for letra in palavra:
#     print(letra)
# 
# nome = input('digite seu nome: ')
# for x in range (10):
#     print(f'{x+1} {nome}')
# range (valor_inicial, valor_final, incremento)

# for x in range(20,1, -2):
#     print(x)
pedras = ('rubi','esmeralda','diamante','jade')
for pedra in pedras:
    if pedra == 'jade':
        continue
    print(pedra)