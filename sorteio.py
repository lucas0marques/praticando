from random import choice
nomes = []
for x in range(1,4):
   adic = str(input('Informe o nome do {} participantes do sorteio : '.format(x)))
   nomes.append(adic)

#print(nomes)
sort = choice(nomes)
print('O ganhador foi:', sort)






