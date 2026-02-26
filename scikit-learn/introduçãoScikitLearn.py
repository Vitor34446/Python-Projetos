import pandas as pd 
import os 
from sklearn.model_selection import train_test_split

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

df = pd.read_csv("arquivosImportados/Base Financeiro.csv", encoding='utf-8',
                 sep=',')
print(df.head())
# print(os.getcwd())

x = df.drop(columns=['Tipo Pessoa','Municipio'])
y = df['Razao Social']

print(x.head())

print(x.shape)
print(y.shape)