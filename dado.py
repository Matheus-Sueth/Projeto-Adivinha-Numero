from random import randint
print('Jogo do Dado')
jogo = False
tent = 1
while True:
    r = input('Você gostaria de adivinhar o número do dado? ')
    if r.lower() == 'sim':
        dado = randint(1,6)
        jogo = True
        break
    elif r.lower() == 'nao':
        print('vai embora merda')
        break
    else:
        print('Erro!!!')

while jogo:
  try:
    num = int(input('Digite um número entre 1 e 6: '))
    if num == dado:
      print('Parabéns vc acertou o número do dado')
      break
    else:
      if tent == 3:
        print(f'Você errou pela {tent}ª vez. Game over!')
        break
      print(f'Você errou pela {tent}ª vez. Tente de novo!')
      tent+=1
  except:
      print('Essa resposta é inválida')
