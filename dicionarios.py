# dicionario 
pessoas = {
    'altura': 1.78,
    'idade': 38,
    'genero': 'm',
    'trabalho':'administrador'
}

print(f'a altura dessa pessoa é: {pessoas['altura']}')
print(f'o dicionarrio possui {len(pessoas)} informações')


# atualizar 
pessoas['altura'] = 1.88
pessoas['peso'] = '300kg'
print(pessoas)

# exclusao itens dicionario 

# del pessoas ['peso'] 
# print(pessoas)

# pessoas.clear()
# print(pessoas)

# del pessoas 
# print(pessoas)

print(pessoas.items())
for i in pessoas.items():
    print(i)
print(pessoas.keys())
for i in pessoas.keys():
    print(i)
print(pessoas.values())
for i in pessoas.values():
    print(i)

for i, j in pessoas.items():
    print(f'{i}:{j}')


    