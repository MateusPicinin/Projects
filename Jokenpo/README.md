- Descrição do Projeto

Este projeto consiste no desenvolvimento de um jogo de Jokenpô (Pedra, Papel e Tesoura) utilizando a linguagem Python, executado diretamente no terminal.

O objetivo da atividade foi aplicar conceitos fundamentais de programação, como variáveis, estruturas condicionais, laços de repetição e geração de números aleatórios.

O sistema permite três modos de jogo:

Humano x Humano
Humano x Robô
Robô x Robô

- Regras do Jogo

Cada jogador escolhe uma opção:

1 → Pedra
2 → Papel
3 → Tesoura

As regras são simples:

Pedra vence Tesoura
Tesoura vence Papel
Papel vence Pedra
Escolhas iguais resultam em empate

- Tecnologias Utilizadas
Python 3
Biblioteca padrão:
import random

A biblioteca random foi utilizada para gerar jogadas aleatórias da máquina.

- Como Executar o Projeto
 Requisitos:
Ter o Python 3 instalado no computador

- Execução
Salve o código em um arquivo chamado main.py
Execute no terminal:
python main.py
⚙️ Funcionalidades do Sistema
🎯 Menu Inicial com 3 Modos de Jogo
print('HUMANO X HUMANO | Digite 1 ')
print('HUMANO X ROBÔ | Digite 2 ')
print('ROBÔ X ROBÔ | Digite 3 ')

O usuário escolhe como deseja jogar.

- Modo Humano x Humano

Dois jogadores fazem suas escolhas manualmente:

Jogador1 = int(input('Jogador 1, escolha uma opção: '))
Jogador2 = int(input('Jogador 2, escolha uma opção: '))

O sistema compara as jogadas e informa o vencedor.

- Modo Humano x Robô

A máquina escolhe automaticamente:

maquina = random.randint(1, 3)

Depois o sistema compara jogador e robô.

- Modo Robô x Robô

Duas jogadas aleatórias são geradas:

maquina1 = random.randint(1, 3)
maquina2 = random.randint(1, 3)

Ideal para simulações automáticas.

- Sistema de Placar

O código registra vitórias em variáveis:

PlacarJogador1 = 0
PlacarJogador2 = 0
PlacarMaquina = 0

Ao final de cada rodada:

print(f'Placar geral: {PlacarJogador1} x {PlacarMaquina}')

- Exemplo de Interação
Bem vindo ao JOKENPÔ

HUMANO X HUMANO | Digite 1
HUMANO X ROBÔ   | Digite 2
ROBÔ X ROBÔ     | Digite 3

Qual modo você quer jogar? 2

Você escolheu HUMANO X ROBÔ

Escolha uma opção:
1. Pedra
2. Tesoura
3. Papel

Jogador: Pedra X Máquina: Tesoura

O Jogador venceu 🥳

Placar geral: 1 x 0

- Estrutura do Código

O sistema foi desenvolvido utilizando while True, mantendo o jogo em execução até o usuário sair:

while True:

As decisões do jogo são controladas com:

if escolha == 1:
elif escolha == 2:
elif escolha == 3:
Verificação de Empate
if Jogador1 == maquina:
    print('A rodada empatou')
Verificação de Vitória
elif Jogador1 == 1 and maquina == 2:
    print('O Jogador venceu')
    
- Possíveis Melhorias Futuras
Interface gráfica com Tkinter
Organização do código em funções
Sistema de ranking
Salvamento de partidas
Multiplayer online
Sons e efeitos visuais
Inteligência artificial avançada

- Autor
Mateus Augusto Picinin

- Informações Acadêmicas

Trabalho desenvolvido para disciplina de Raciocínio Algorítmico da Pontifícia Universidade Católica do Paraná (PUCPR).

Projeto voltado à prática dos conceitos introdutórios de programação em Python.
