from random import randint
print('Jogo da Adivinhacao')
jogo = False
tent = 1
while True:
    r = input('Você gostaria de adivinhar o número adivinhado ? Lembrando que voce possui 3 tentativas ')
    if r.lower() == 'sim':
        dado = randint(1,2)
        jogo = True
        break
    elif r.lower() == 'nao':
        print('Jogo nao inicializado')
        break
    else:
        print('Erro!!!')

while jogo:
  try:
    num = int(input('Digite um número entre 1 e 6: '))
    if num == dado:
      print('Parabéns vc acertou o número adivinhado')
      break
    else:
      if tent == 3:
        print(f'Você errou pela {tent}ª vez. Game over!')
        break
      print(f'Você errou pela {tent}ª vez. Tente de novo!')
      tent+=1
  except:
      print('Essa resposta é inválida')
