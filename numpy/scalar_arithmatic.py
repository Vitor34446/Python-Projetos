import numpy as np


# aritmetica escalar 

array1 = np.array([1,2,3,4])
array2 = np.array([4,6,7,9])

print(array1 + array2)
print(array1 - array2)
print(array1 * array2)
print(array1 / array2)
print(array1 ** array2)

# print(array + 2 )
# print(array * 2 )
# print(array - 2 )
# print(array / 2 )
# print(array ** 8 )


# print(np.sqrt(array))
# print(np.round(array))
# print(np.pi)


# circonferencia dos valores de array

# print(np.pi * array **2 )

# operadores de comparação 

scores = np.array([22,34,67,89,12])
print(scores >= 60)

scores[scores <60] = 0 
print(scores)
