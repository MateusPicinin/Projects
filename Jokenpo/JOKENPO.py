2
import random

PlacarJogador1 = 0
PlacarJogador2 = 0
PlacarMaquina = 0


print('Bem vindo ao JOKENPÔ')
print('-----------------------------------------------------------------------------------------------------')
print('\nHUMANO X HUMANO | Digite 1 ')
print('HUMANO X ROBÔ | Digite 2 ')
print('ROBÔ X ROBÔ | Digite 3 \n')
print('-----------------------------------------------------------------------------------------------------')


escolha = int(input('Qual modo você quer jogar?'))

while True:
    if escolha == 1:
        print('teste')
        print('Voce escolheu HUMANO X HUMANO\n')
        print('Para jogar escolha uma opção\n')
        print('------------------------------------------------------------------------------------------------------')
        print('Pedra | Digite 1 ')
        print('Papel | Digite 2 ')
        print('Tesoura | Digite 3 ')
        print('------------------------------------------------------------------------------------------------------')
        Jogador1 = int(input('Jogador 1, escolha uma opção: '))
        print('\n' * 10)
        if Jogador1 < 1 or Jogador1 > 3:
            print('Número inválido!')
            break

        print('Para jogar escolha uma opção')
        print('')
        print('------------------------------------------------------------------------------------------------------')
        print('Pedra | Digite 1 ')
        print('Papel | Digite 2 ')
        print('Tesoura | Digite 3 ')
        print('------------------------------------------------------------------------------------------------------')
        Jogador2 = int(input('Jogador 2, escolha uma opção: '))
        print('\n' * 10)
        if Jogador2 < 1 or Jogador2 > 3:
            print('Número inválido!')
            break

        if Jogador1 == 1 and Jogador2 == 1 or Jogador1 == 2 and Jogador2 == 2 or Jogador1 == 3 and Jogador2 == 3:

            print('\nA rodada empatou🫠\n')
            print(' Escolha uma opção \n')
            print(
                '------------------------------------------------------------------------------------------------------')
            print('Continuar | 1')
            print('Sair | 2 \n')
            print(
                '------------------------------------------------------------------------------------------------------\n')
            Final1 = int(input('Digite aqui: '))
            if Final1 < 1 or Final1 > 2:
                print('Número inválido!')
                break
            PlacarJogador1 += 1
            PlacarJogador2 += 1
            if Final1 == 1:
                print('Recomeçando jogo')
            elif Final1 == 2:
                print(f"Placar final: {PlacarJogador1} x {PlacarJogador2}")
                print('\nObrigado por jogar nosso JOKENPÔ! 🎮')
                print('Esperamos que você tenha se divertido e volte para jogar novamente! 😄\n')
                print('Jogo desenvolvido por:')
                print('Mateus Augusto Picinin')
                print('Eduardo Henrique Fernandes Pereira')
                print('Vitor Skrypec Donini')
                break



        elif Jogador1 == 1 and Jogador2 == 3 or Jogador1 == 2 and Jogador2 == 1 or Jogador1 == 3 and Jogador2 == 2:
            print('\nO Jogador 1 Venceu🥳\n')
            print(' Escolha uma opção \n')
            print('-----------------------------------------------------------------------------------------------\n')
            print('Continuar | 1')
            print('Sair | 2 \n')
            print('-----------------------------------------------------------------------------------------------\n')
            Final1 = int(input('Digite aqui: '))
            if Final1 < 1 or Final1 > 2:
                print('Número inválido!')
                break
            PlacarJogador1 += 1
            if Final1 == 1:
                print('Recomeçando jogo')
            elif Final1 == 2:
                print(f"Placar final: {PlacarJogador1} x {PlacarJogador2}")
                print('\nObrigado por jogar nosso JOKENPÔ! 🎮')
                print('Esperamos que você tenha se divertido e volte para jogar novamente! 😄\n')
                print('Jogo desenvolvido por:')
                print('Mateus Augusto Picinin')
                print('Eduardo Henrique Fernandes Pereira')
                print('Vitor Skrypec Donini')
                break


        elif Jogador2 == 1 and Jogador1 == 3 or Jogador2 == 2 and Jogador1 == 1 or Jogador2 == 3 and Jogador1 == 2:
            print('\nO Jogador 2 Venceu🥳\n')
            print(' Escolha uma opção \n')
            print('------------------------------------------------------------------------------------------------\n')
            print('Continuar | 1')
            print('Sair | 2 \n')
            print('------------------------------------------------------------------------------------------------\n')
            Final1 = int(input('Digite aqui: '))
            if Final1 < 1 or Final1 > 2:
                print('Número inválido!')
                break
            PlacarJogador2 += 1
            if Final1 == 1:
                print('Recomeçando jogo')
            elif Final1 == 2:
                print(f"Placar final: {PlacarJogador1} x {PlacarJogador2}")
                print('\nObrigado por jogar nosso JOKENPÔ! 🎮')
                print('Esperamos que você tenha se divertido e volte para jogar novamente! 😄\n')
                print('Jogo desenvolvido por:')
                print('Mateus Augusto Picinin')
                print('Eduardo Henrique Fernandes Pereira')
                print('Vitor Skrypec Donini')


                break

                # Opção 2

    if escolha == 2:
        print('voce escolheu HUMANO X ROBO')
        Jogador1 = int(input('escolha uma opcao \n 1. Pedra \n 2. Tesoura \n 3. Papel\n'))

        if Jogador1 < 1 or Jogador1 > 3:
            print('Número inválido!')
            break

        maquina = random.randint(1, 3)
        if maquina == 1:
            escolha_maquina = "Pedra"
        elif maquina == 2:
            escolha_maquina = "Tesoura"
        elif maquina == 3:
            escolha_maquina = "Papel"
        if Jogador1 == 1:
            escolha_jogador = "Pedra"
        elif Jogador1 == 2:
            escolha_jogador = "Tesoura"
        elif Jogador1 == 3:
            escolha_jogador = "Papel"

        if Jogador1 == 1 and maquina == 1 or Jogador1 == 2 and maquina == 2 or maquina == 3 and Jogador1 == 3:
            print(f'jogador:{escolha_jogador} X maquina:{escolha_maquina}')
            print('A rodada empatou🫠')

        elif Jogador1 == 1 and maquina == 2 or Jogador1 == 2 and maquina == 3 or Jogador1 == 3 and maquina == 1:
            print(f'jogador:{escolha_jogador} X maquina:{escolha_maquina}')
            print('O Jogador Venceu🥳')

        elif maquina == 1 and Jogador1 == 2 or maquina == 2 and Jogador1 == 3 or maquina == 3 and Jogador1 == 1:
            print(f'jogador:{escolha_jogador} X maquina:{escolha_maquina}')
            print('A maquina Venceu🥳')


        if maquina == Jogador1:
            PlacarJogador1 += 1
            PlacarMaquina += 1

        elif maquina == 1 and Jogador1 == 3 or maquina == 2 and Jogador1 == 1 or maquina == 3 and Jogador1 == 2:
            PlacarJogador1 += 1

        else:
            PlacarMaquina += 1

        print(f'Placar geral: {PlacarJogador1} x {PlacarMaquina}\n')
        print('Escolha uma opção\n')
        print('---------------------------------------------------------------------------------------------------\n')
        print('Continuar | 1')
        print('Sair | 2\n')
        print('---------------------------------------------------------------------------------------------------\n')

        Final2 = int(input('Digite sua opção: '))
        if Final2 < 1 or Final2 > 2:
            print('Número inválido!')
            break

        if Final2 == 1:
            print('Recomeçando jogo\n')

        elif Final2 == 2:
            print(f"Placar final: {PlacarJogador1} x {PlacarMaquina}")
            print('\nObrigado por jogar nosso JOKENPÔ! 🎮')
            print('Esperamos que você tenha se divertido e volte para jogar novamente! 😄\n')
            print('Jogo desenvolvido por:')
            print('Mateus Augusto Picinin')
            print('Eduardo Henrique Fernandes Pereira')
            print('Vitor Skrypec Donini')

            break


        # Opção 3

    if escolha == 3:
        print('Voce escolheu ROBO X ROBO\n')

        maquina1 = random.randint(1, 3)
        maquina2 = random.randint(1, 3)

        if maquina1 == 1:
            escolha_maquina1 = "Pedra"
        elif maquina1 == 2:
            escolha_maquina1 = "Papel"
        elif maquina1 == 3:
            escolha_maquina1 = "Tesoura"

        if maquina2 == 1:
            escolha_maquina2 = "Pedra"
        elif maquina2 == 2:
            escolha_maquina2 = "Papel"
        elif maquina2 == 3:
            escolha_maquina2 = "Tesoura"

        print(f'Robo 1: {escolha_maquina1} X Robo 2: {escolha_maquina2}\n')

        if maquina1 == maquina2:
            print('A rodada empatou🫠\n')
            PlacarJogador1 += 1
            PlacarJogador2 += 1

        elif maquina1 == 1 and maquina2 == 3 or maquina1 == 2 and maquina2 == 1 or maquina1 == 3 and maquina2 == 2:
            print('O Robo 1 venceu🥳\n')
            PlacarJogador1 += 1

        else:
            print('O Robo 2 venceu🥳\n')
            PlacarJogador2 += 1

        print(f'Placar geral: {PlacarJogador1} x {PlacarJogador2}\n')
        print('Escolha uma opção\n')
        print('--------------------------------------------------------------------------------------------------\n')
        print('Continuar | 1')
        print('Sair | 2\n')
        print('--------------------------------------------------------------------------------------------------\n')

        Final1 = int(input('Digite aqui: '))
        if Final1 < 1 or Final1 > 2:
            print('Número inválido!')
            break

        if Final1 == 1:
            print('Recomeçando jogo\n')


        elif Final1 == 2:
            print(f"Placar final: {PlacarJogador1} x {PlacarJogador2}")
            print('\nObrigado por jogar nosso JOKENPÔ! 🎮')
            print('Esperamos que você tenha se divertido e volte para jogar novamente! 😄\n')
            print('Jogo desenvolvido por:')
            print('Mateus Augusto Picinin')
            break