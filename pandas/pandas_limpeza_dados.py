import pandas as pd


def nossa_soma(linha):
    return linha.sum()
# arq = pd.read_csv('c:/Python-Projetos/Compra_Dos_Clientes_Revissado.csv',sep=',')
# print(arq.head())

# print(arq.info())
# arq_pre = arq.copy()

# arq_pre['Data_venda'] = pd.to_datetime(arq_pre['Data_Venda'], yearfirst=True)

# arq_pre.drop(columns=['Data_Venda'], inplace=True)

# arq_pre.rename(columns={'Data_venda': 'Data_Venda'}, inplace=True)

# print(arq_pre.info())

# for atributo in ['Nome','ID_Loja']:
#     arq_pre[atributo] = pd.to_numeric(arq_pre[atributo], errors='coerce')    # exemplo

# mask = arq_pre['Data_Venda'].isnull()
# print(mask)
# print(arq_pre[mask])       # no meu dataFrame nao tem valores nulos 

# arq_pre_fill = arq_pre.fillna(0)
# print(arq_pre_fill)

# data_pre_fill = arq_pre.fillna(value={
#     'PREÇO MÉDIO DISTRIBUIÇÃO': 10,
#     'DESVIO PADRÃO DISTRIBUIÇÃO': 20,
#     'PREÇO MÍNIMO DISTRIBUIÇÃO': 30,
#     'PREÇO MÁXIMO DISTRIBUIÇÃO': 'vazio'
# })
# arq_pre_fill

# arq_pre.dropna(inplace=True)   # ao invez de substi os val nulos por outras coisas, as exclui

# print(arq_pre)

# arq_pre.to_csv('c:/Python-Projetos/Compra_Dos_Clientes_Revissado_Final.csv', index=False)

arq_final = pd.read_csv('c:/Python-Projetos/Compra_Dos_Clientes_Revissado_Final.csv')

                # estatistica descritiva
print(arq_final)

stats = arq_final.describe()
print(stats[['Preco_Unit','Custo_Venda','Custo_Unit','Receita_Venda']])

         # mesma coisa de cima, so que mais rapido para o computador

# print(arq_final[['Preco_Unit','Custo_Venda','Custo_Unit','Receita_Venda']].describe())

print(stats.loc[['min','max','mean'],['Custo_Venda','Custo_Unit']])
min = arq_final['Custo_Venda'].min()
max = arq_final['Custo_Venda'].max()
mean = arq_final['Custo_Venda'].mean()
std = arq_final['Custo_Venda'].std()
print(f'A media do custo de venda é de {mean:.2f} +- {std:.2f}')
# print(sorted(arq_final['Nome'].unique()))

print(arq_final['Nome'].value_counts())
frequencia = arq_final['Nome'].value_counts().to_frame  # converte series para dataframe

df = pd.DataFrame({
    'col1':[1,2,3],
    'col2':[10,20,30],
    'col3':[100,200,300]
}, index=['Linha1','Linha2','Linha3'])


print(df.applymap(lambda x: x ** 2))


df['SOMA(A),(B),(C)'] = df.apply(nossa_soma,axis=1)
df.loc['Linha5'] = df.apply(nossa_soma,axis=0)
print(df)
# print(df[['col1','col2','col3']].apply(lambda series: series.mean(), axis=1))
df['Media'] = df[['col1','col2','col3']].apply(lambda series: series.mean(), axis=1)
print(df)

df['col3 * 2'] = df['col3'].apply(lambda x: x * 2)
print(df)