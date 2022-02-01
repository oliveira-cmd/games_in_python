from random import randint
print('-=-' * 20)
jogar = str(input('Vou pensar em um numero entre 0 e 5, Quer tentar adivinhar?  '))
print('-=-' * 20)
if jogar == 'S':
    jogador_placar = 0
    computador_placar = 0
    while True:
        computador = randint(0, 5)  # faz a maquina sortear um numero entre 0 e 5
        jogador = int(input('Em que numero eu pensei?   '))
        if jogador == computador:
            print('Parabens, você ganhou, nós dois pensamos no numero {}'.format(computador))
            jogador_placar = jogador_placar + 1
            print('Agora o jogo está:\n')
            print('Computador : {} e Jogador: {}'.format(computador_placar, jogador_placar))
            jogar = input('Quer Continuar? S/N  ')
            if jogar == 'N':
                if jogador_placar > computador_placar:
                    print('Parabens Genio, você ganhou')
                    print('Placar Final Computador: {}  e Jogador  {} '.format(computador_placar, jogador_placar))
                else:
                    if computador_placar > jogador_placar:
                        print('Melhor parar antes de perder o caminho de casa')
                        print('Placar Final Computador: {}  e Jogador  {} '.format(computador_placar, jogador_placar))
                    else:
                        print('Foi um bom jogo, acabamos empatados')
                        print('Placar Final Computador: {}  e Jogador  {} '.format(computador_placar, jogador_placar))
                break
        else:
            print('Errou, eu pensei no numero {} e não no numero {}'.format(computador, jogador))
            computador_placar = computador_placar + 1
            print('Agora o jogo está:\n')
            print('Computador : {} e Jogador: {}'.format(computador_placar, jogador_placar))
            jogar = input('Quer Continuar? S/N  ')
            if jogar == 'N':
                if jogador_placar > computador_placar:
                    print('Parabens Genio, você ganhou')
                    print('Placar Final Computador: {}  e Jogador  {} '.format(computador_placar, jogador_placar))
                else:
                    if computador_placar > jogador_placar:
                        print('Melhor parar antes de perder o caminho de casa')
                        print('Placar Final Computador: {}  e Jogador  {} '.format(computador_placar, jogador_placar))
                    else:
                        print('Foi um bom jogo, acabamos empatados')
                        print('Placar Final Computador: {}  e Jogador  {} '.format(computador_placar, jogador_placar))
                break
else:
    print('Medroso')
