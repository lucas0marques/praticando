valor = float(input('Informe o valor do produto: R$'))
desc = float(input('Qual é o valor do desconto a ser aplicado? '))
n = (valor * desc)/100
print('O produto vai custar R${} com desconto de {}% '.format(valor - n, desc))

