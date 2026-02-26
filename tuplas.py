# sao imutaveis

pedras = ('pedra','diamante','rubi','esmeralda','jadi',)
drogas = ('maconha','craque','metanfetamina','anfetamina')
t1 = (1,23,43,6,87,3,4,76,23,1,123,5,6)
natureza = pedras + drogas
print(natureza)
# for pedra in pedras:
print(len(natureza))
print(sum(t1))

# operaçoes nao disponiveis em tuplas: sort(), append(), reverse(), pop()...

# for natu in natureza:
#     print(f'coisas da natureza: {natu}')

# grupo = list(pedras)
# grupo[4] = 3
# print(grupo)

cores = ['vermelho','verde','azul','amarelo','rosa']
print(type(cores))
grupo1 = tuple(cores)
print(type(grupo1))
print(sorted(grupo1))
# print(grupo1.sort()) esse esta errado



