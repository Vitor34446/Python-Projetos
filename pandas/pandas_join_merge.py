import pandas as pd 


arq_final1 = pd.read_csv('c:/Python-Projetos/Compra_Dos_Clientes_Revissado_Final.csv')
arq_final2 = pd.read_csv('c:/Python-Projetos/Base Financeiro.csv')
# print(arq_final1)
# print(arq_final2)

         # função concat com DadaBases que nao combinam 

print(pd.concat([arq_final1,arq_final2], axis=0))
print(pd.concat([arq_final1,arq_final2], axis=1))
print(pd.concat([arq_final1,arq_final2]))

          # outra coisa nao relacionada 
        
# df = pd.read_excel("Base Financeiro.xlsx")
# df.to_csv("Base Financeiro.csv", index=False, encoding="utf-8-sig")


          # função join 

left = arq_final1
right = arq_final2

print(left.join(right))
print(left.join(right, lsuffix='_A', rsuffix='_B'))


          # metodo merge

datas_combinados = arq_final1.merge(arq_final2)
print(datas_combinados)