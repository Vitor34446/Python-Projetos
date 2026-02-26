import pandas as pd


arq_final = pd.read_csv('c:/Python-Projetos/Compra_Dos_Clientes_Revissado_Final.csv')

# print(arq_final)

# grupos = arq_final.groupby('ID_Loja')
# print(grupos)

# print(grupos.groups)

# print(grupos.get_group(1))
# print(grupos.describe())
# print(grupos.max())

grupos = arq_final.groupby(['ID_Loja','ID_Produto'])
# print(grupos.groups)
# print(grupos.max())
# print(grupos['Preco_Unit'].mean())
print(grupos['Preco_Unit'].describe())


# grupo = arq_final.groupby(['ID_Loja'])
# print(grupo['Preco_Unit'].agg([min, max]))