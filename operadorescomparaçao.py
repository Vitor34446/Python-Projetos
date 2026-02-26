w = x = y = z = False
n1 = n2 = 0

print("digite um numero:")
n1 = int(input())
n2 = int(input('digite outro numero: '))

x = n1 == n2 

print('sao iguais? ', x, '\n')

z = n1 > n2

print(n1, 'é maior que', n2, '?', z, '\n' )

y = n1 != n2 

# print('esses numeros sao diferentes?',n1,n2,y,'\n' )


print('sao numeros diferentes ?'+ str(y))

w = n1 >= n2 


print( 'o primeiro é maior ou igual que o segundo ?', w)