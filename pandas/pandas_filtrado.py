import pandas as pd

arq = pd.read_csv('c:/Python-Projetos/Compra_Dos_Clientes_Revissado.csv',sep=',')

# print(arq.head())
# print(arq['Nome'].unique())
# print(arq['Nome'] =='Gina')
# print(arq.sort_values(by='Nome'))

seleção= arq['Nome'] =='Wyatt'
print(arq[seleção])
# print(arq.loc[seleção])    # faz a mesma coisa que o codigo de cima 


       # metodo query

# arq.query('Nome=="Wyatt"')
query = arq.query('Nome=="Wyatt"')

# print(type(seleção))
# print(seleção.shape)
print(arq[seleção].reset_index())
print(query.reset_index())     # o codigo dessa linha faz a mesma coisa que o de cima
print(query.reset_index(drop=True))    # a variavel query nao teve os indexs mudados
query.reset_index(drop=True, inplace= True)    # a variavel query teve os indexs mudados
print(query)


       # fazer a mesma coisa que em cima, porem de uma forma mais utilizada

query = arq.query('Nome=="Wyatt"').reset_index(drop=True)


