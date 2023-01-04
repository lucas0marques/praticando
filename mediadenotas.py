n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2)/2
if (media >= 7):
    print('Você foi aprovado')

elif(media >= 4 and media <= 7):
    print('Você está de recuperação')

else:
    print('Você foi reprovado')
