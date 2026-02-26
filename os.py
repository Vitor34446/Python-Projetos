import os
os.chdir('C:\\Teste')
print(f'o diretório atual:{os.getcwd()}')

padrao_nome= input('Qual o padrao preferivel a se usar(não é necessario extensao)?')

for contador, arq in enumerate(os.listdir(),+1):

    if os.path.isfile(arq) :
        nome_arq, exten_arq = os.path.splitext(arq)
        nome_arq = padrao_nome + ' ' + str(contador)

        nome_novo = f'{nome_arq}{exten_arq}'
        os.rename(arq,nome_novo)

print('n/Arquivos renomeados')