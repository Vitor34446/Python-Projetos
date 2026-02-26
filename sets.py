# set 

# ratos = {'ratazana', 'ratinho', 'rato cinza','ratão'}
# print(ratos, end=' ')

# ratos = ['ratazana', 'ratinho', 'rato cinza','ratão','ratinho']
# print(type(ratos),end=' ')
# print(ratos,end=' ')
# ratos_set = set(ratos)
# print(type(ratos_set))
# print(ratos_set)

ratos1 = {'ratazana', 'ratinho', 'rato cinza','ratão','ratinho'}
ratos2 = {'ratazana', 'ratinho', 'rato cinza','ratão','ratinho','ratasso'}
print(ratos1 != ratos2)
print(ratos1 | ratos2)
print(ratos1.union(ratos2))

print(ratos1 &ratos2)
print(ratos1.intersection(ratos2))

print(len(ratos1 ^ ratos2))
print(ratos1.symmetric_difference(ratos2))

ratos1.pop()
print(ratos1)
ratos1.clear()







