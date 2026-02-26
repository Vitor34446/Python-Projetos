# numeros = [1,2,46,8,8]

# quadrados = [num**2 for num in numeros]
# print(quadrados)

# criar uma lista de numeros pares ate dez

# pares = [num for num in range(19) if num %2 ==0]
# print(pares)

# frase = 'a logica é legal'
# vogais = ['a','e','i','o','u','á','é','í','ó','ú']

# lista_vogais = [f for f in frase if f in vogais]
# print(f'A lista possui {len(lista_vogais)} vogais')
# print(lista_vogais)

# distributiva de valores entre duas listas


distributiva = [x * y for x in [23,345,54] for y in [4,545,89]]
print(distributiva)