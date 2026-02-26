import pandas as pd


arq = pd.read_csv('c:/Python-Projetos/Compra_Dos_Clientes_Revissado.csv',sep=',')
# print(arq['ID_Loja'].unique())
print(arq)
# print(arq['ID_Loja'] == 1)
# print(arq['Preco_Unit'] > 400)
# filtro = (arq['ID_Loja'] == 1) & (arq['Preco_Unit'] > 400)
# Met_query = arq.query('ID_Loja == "1" or Preco_Unit > 400')
# print(filtro)
# print(Met_query)


         # mesma coisa de cima, porem mais eficiente 


# selec_1= arq['ID_Loja'] == 1
# loja_f =arq[selec_1]
# print(loja_f)
# preço_f = loja_f['Preco_Unit'] > 400
# filtro = loja_f[preço_f]                # putala merda, eu consegui essa porra!!!!!!!!
# print(filtro)

                        # mais de duas perguntas sobre a base de dados 

# fiutro = (arq['ID_Loja']== 1) | (arq['ID_Loja'] == 4 )
# preço = (arq['Preco_Unit'] > 400)
# var_3 = (arq['Custo_Unit'] < 500)
# seleção_final = fiutro & preço & var_3
# data_filtrado = arq[seleção_final]

# filtro = (arq['ID_Loja']== 1) | (arq['ID_Loja'] == 4 )
# vari_1= (arq[filtro])
# vari_2 = (vari_1['Preco_Unit'] > 400)
# vari_3 = (vari_1[vari_2])
# vari_4 = (vari_3['Custo_Unit'] < 500)
# print(vari_4)                         # Esse aqui é pra rever 
# vari_5 = vari_3[vari_4]
# print(vari_5)



# print(fiutro)
# print(arq[fiutro])
# filtros = ((arq['ID_Loja']== 1) | (arq['ID_Loja'] == 4 )) & (arq['Preco_Unit'] > 400)
# print(arqarq[ID_Loja].unique())
# print(data_filtrado)
# print(data_filtrado['ID_Loja'].unique())





             # metodo com listas 


lista_ID_lojas = [1,4,7]
var1 = arq['ID_Loja'].isin (lista_ID_lojas) 
var2 = arq[var1]
print(var2)
 

        # metodo query


# print(arq.query('ID_Loja in @lista_ID_lojas'))

       # outra parada


for index, row in arq.head(10).iterrows():
    print(f'indice{index} ==> {row['Nome']}')

