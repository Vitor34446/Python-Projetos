import numpy as np


idades = np.array([[15,56,23,12,78,9],
                   [34,45,32,17,67,13]])

# adolescentes = idades [idades < 18]
# adultos = idades[(idades >= 18) & (idades <65)]
# velhos = idades[idades >=65]
# redondos = idades[idades % 2 ==0]
# Nredondos = idades[idades % 2 !=0]
# print(adolescentes)
# print(adultos)
# print(velhos)
# print(redondos)
# print(Nredondos)

adultos = np.where(idades >=18,idades,0)

print(adultos)