# frase = 'Eu gosto de sorvete'                   
# palavras = frase.split()                    # split: transforma string em lista
# print(palavras[1])
# for palavra in palavras:
#     print(palavra)

# print(frase[5:9])

# email = input('digite o seu email:\n')
# arroba = email.find('@')
# print(arroba)
# usuario = email[0:arroba]
# dominio = email[arroba+1:]
# print(usuario)
# print(dominio)

# produtos = 'farinha com lama e um pouco de carne de porco'
# print('carne de porco' in produtos)
# print('farinha' in produtos)
# print('sabonete' in produtos)

# item = 'esponja'
# letras = item.find('esp')
# print(letras)
# letras1 = item.find('nja')
# print(letras1)
# letras2 = item.find('fer')
# print(letras2)

# planeta = 'La Vaca SaTurno Saturnita'
# print(planeta.lower())
# print(planeta.capitalize())
# print(planeta.upper())
# print(planeta.title())

# suplemento = 'cloreto de magnesio'
# n_suplemento = suplemento.replace('magnesio','zinco')
# print(n_suplemento)

# frase = '        Presidentes do Brasil     '
# print(frase.lstrip())
# print(frase.rstrip())
# print(frase.strip())

# fruta = 'abacate'
# print(fruta.rjust(20, '-'))
# print(fruta.center(20, '-'))
# print(fruta.ljust(20, '-'))

# p = 'eu sou lindo'
# print(p.startswith('eu'))
# print(p.endswith('o'))

# docstrings

texto = '''
Docstring é uma especie de documentação, eu nao vou escrever exatamente
o que o cara do video esta escrevendo, mas eu vou sim escrever umas coisas
aqui, olha como Deus é maravilhoso
'''
print(texto)