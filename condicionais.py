# simples, composto, encadeado

n1 = n2 = 0.0
media = 0.0
n1 = float (input('digite a primeira nota: '))
n2 = float (input('digite a segunda nota: '))

# calcular a media aritmetica das notas

media = (n1 + n2) / 2
if  (media >= 6):
    print("passou, seu lindo")
    print("parabéns")
elif (media >= 5):
    print("óia óia, foi quase")
elif (media >= 8):
    print("já tá querendo se achar")
else:
    print("que burrinho kkk")

print('sua media é {} ' .format(media))