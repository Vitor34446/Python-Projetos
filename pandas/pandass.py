import pandas as pd

arquivo = pd.read_csv('compra dos clientes.csv',sep=',')
arq = pd.read_csv('c:/Python-Projetos/Compra_Dos_Clientes_Revissado.csv',sep=',')
# print(arquivo.head(10))

# arquivo.shape

# print(f'Possui {arquivo.shape[0]} linhas e {arquivo.shape[1]} colunas')

# frutas = pd.DataFrame({
#     'maças': ['verdes','vermelhas','suculentas'],
#     'quantidade': [30,103,88],
#     'peso_unitario':[0.30,0.56,0.67],
#     'madura':[False,True,True]
# })

# print(frutas)

# infor = frutas.info

# frutas.columns
# tipo_colunas = type(frutas.columns)

# colunas_lista = list(frutas.columns)
# print(tipo_colunas)
# print(infor)
# print(colunas_lista)

# frutas_renomeadas = frutas.rename(columns={
#     'maças': 'Maças',
#     'quantidade':'Quantidade'
# }
# )

# frutas.rename(columns={
#     'maças': 'Maças',
#     'quantidade':'Quantidade'
# },inplace=True)

# print(frutas_renomeadas)

# frutas.columns=['bosta','merda','mijo','reto']

# print

# arquivo.head

# nome = arquivo['Nome']

# print(nome)

# arquivo.Nome     # so funciona se nao tiver nenhum espaço, nenhuma porra assim 

linha = (arquivo.iloc[300])
print(linha)


# serie = pd.Series([3.4,5.5,7.6],
#                   index=['Prova1','Prova2','Prova3'],
#                   name='Bosta liquida')
# print(serie)

# nomes = ['Ana','jefrey','Bob Odenkirk']
# idades = [12,34,55]
# dados = list(zip(nomes,idades))
# print(dados)

# df = pd.DataFrame(dados)
# print(df)

# nome_view = arquivo['Nome']
# nome_copia = arquivo['Nome'].copy()

# print(arquivo.head())

# nrows, ncols = arquivo.shape


# novo_pedido = [f'Pedidos{i + 1}' for i in range (nrows) ]
# print(novo_pedido)

# arquivo['ID_Pedido'] = novo_pedido
# print(arquivo.head())

# arquivo['Walter Branco'] = 'Branco'
# arquivo['Numeros'] = range(arquivo.shape[0])
# arquivo['Preço_Unit reais'] = arquivo['Preco_Unit'] * 6


# print(arquivo.head())


# print(arquivo.index)

# print(arquivo.iloc[[1,5,10,15]])
# print(arquivo.iloc[[5,1,15,10]])
# print(arquivo.iloc[2,10])
# print(arquivo.iloc[:3])


# satisfação = pd.DataFrame({
#     'bom':[100,90,80],
#     'medio':[70,60,50],
#     'ruim':[40,30,20]
# },index=['Bobson','Marlon','Cleiton'])
# print(satisfação)
# print(satisfação.iloc[0,2])
# print(satisfação.loc['Bobson'])
# print(satisfação.loc['Bobson','ruim'])
# print(satisfação.loc['Bobson','bom'])
# print(satisfação.loc[['Bobson','Marlon'],'ruim'])
# print(satisfação.loc[['Bobson','Marlon']])
# print(satisfação.loc[:,['bom','ruim']])
# print(satisfação.iloc[0,1],satisfação.iloc[1,2])
# print(satisfação.loc[1])

# print(arquivo.head())
# del arquivo['Walter Branco']
# del arquivo['Numeros']
# del arquivo['Preço_Unit reais']
# print(arquivo)
arquivo.to_csv('c:/Python-Projetos/Compra_Dos_Clientes_Revissado.csv', index=False, sep=',')

print(arq.head())