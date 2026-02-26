import numpy as np 
# minha_lista = [1,2,3,4,5,6]

# minha_lista = minha_lista * 2 

# print(minha_lista)

# array = np.array([1,2,3,4,5,6])

# array =  array * 2
# print(array)

array = np.array([[['A','B','C'],['D','E','F']],
                 [['G','H','I'],['J','k',' ']]])
# print(array.ndim)
# print(array.shape)

palavra = array[0,0,0] + array[0,1,0] + array[1,0,0]  
print(palavra)