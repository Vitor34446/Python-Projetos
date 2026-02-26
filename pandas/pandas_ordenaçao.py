import pandas as pd 


arq_final = pd.read_csv('c:/Python-Projetos/Compra_Dos_Clientes_Revissado_Final.csv')


notas = pd.DataFrame({
    'nome': ['João', 'Maria', 'José', 'Alice'],
    'idade': [20, 21, 19, 20],
    'nota_final': [5.0, 10.0, 6.0, 10.0]
})
print(notas)

print(notas.sort_values(by='nota_final',ascending=False))
print(notas.sort_values(by=['nota_final','nome'],ascending=[False,True]).reset_index(drop=True))
notas.sort_values(by=['nota_final','nome'],ascending=[False,True], inplace=True)
notas.reset_index(drop=True, inplace=True)
print(notas)
