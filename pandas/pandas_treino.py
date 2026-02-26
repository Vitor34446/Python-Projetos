import pandas as pd


arq_final = pd.read_csv('c:/Python-Projetos/Compra_Dos_Clientes_Revissado_Final.csv')
print(arq_final)

      # quantos pedidos Julio fez?

julio = arq_final['Nome'] == 'Julio'
print(arq_final[julio])
    
        # Mostre os produtos de cada loja
     # metodo groupby

# categorias = arq_final.groupby(['ID_Loja','ID_Produto'])
# print(categorias.value_counts())
# print(categorias['ID_Produto'].value_counts())

#        # o de cima eu fiz sozinho 

# grupos = arq_final.groupby(['ID_Loja'])
# print(grupos['ID_Produto'].value_counts())

      # ID_Produto = 1 e 6, Preco_Unit > 300, Custo_Unit < 300  filtrar 

var1 = (arq_final['ID_Produto'] == 3) | (arq_final['ID_Produto'] == 6)
var2 = arq_final[var1]
var3 = var2['Preco_Unit'] > 300
var4 = var2[var3]
var5 = var4['Custo_Unit'] < 300
var6 = var4[var5]
print(var6)
print(var6.describe())

      #   comparação entre os dois produtos 


print(var6.groupby('ID_Produto')['Preco_Unit'].describe())





