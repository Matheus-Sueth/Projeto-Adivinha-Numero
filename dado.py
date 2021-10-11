from random import randint
print('Jogo do Dado')
while True:
    r = input('Você gostaria de adivinhar o número do dado? ')
    if r.lower() == 'sim':
        dado = randint(1,6)
        break
    elif r.lower() == 'nao':
        print('vai embora merda')
        break
    else:
        print('Erro!!!')
        
num = int(input('Digite um número entre 1 e 6: '))

