# manipulação arquivos de texto

# manipulador = open('arquivo.txt','r', encoding='utf-8')

# print(f'metodo read():\n')
# print(manipulador.read())

# print(f'metodo readline():\n')
# print(manipulador.readline())
# print(manipulador.readline())

# print(f'metodo readlines():\n')
# print(manipulador.readlines())

# texto = input('qual termo deseja procurar no arquivo?')
# encontrado = False
# try:
#     manipulador = open('arquivo.txt','r', encoding='utf-8')
#     for linha in manipulador:
#         linha= linha.rstrip()
#         if texto in linha:
#             print(f'O termo foi encontrado')
#             print(linha)
#             encontrado = True

#     if not encontrado:
#         print(f'O termo não foi encontrado')
# except IOError:
#     print(f'Não foi possivel abrir o arquivo')
# else:
#     manipulador.close()



# texto = input('qual termo deseja procurar no arquivo?')
# encontrado = False
# try:
#     manipulador = open('arquivo.txt','r', encoding='utf-8')
#     for linha in manipulador:
#         linha= linha.rstrip()
#         if texto in linha:
#             if not encontrado:
#                 print(f'O termo foi encontrado')
#                 print(linha)
#                 encontrado = True

#     if not encontrado:
#         print(f'O termo não foi encontrado')
# except IOError:
#     print(f'Não foi possivel abrir o arquivo')
# else:
#     manipulador.close()
import os 


# texto = '\nGet away from me, please'
# try:
#     manipulador = open('arquivo.txt','a', encoding='utf-8')
#     manipulador.write(texto)
# except IOError:
#     print(f'Não foi possivel abrir o arquivo')
# else:
#     manipulador.close()


# criar e gravar arquivo
frutas= ['morango\n','pera\n','laranja\n','banana\n']

try:
    manipulador = open('frutas.txt','w', encoding='utf-8')
    manipulador.writelines(frutas)
except IOError:
    print(f'Não foi possivel abrir o arquivo')
else:
    manipulador.close()

# ler o arquivo criado

try:
    manipulador = open('frutas.txt','r', encoding='utf-8')
    print(manipulador.read())
except IOError:
    print(f'Não foi possivel abrir o arquivo')
else:
    manipulador.close()
