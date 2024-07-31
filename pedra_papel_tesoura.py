import random

pontos_usuario = 0
pontos_computador = 0

opcoes = ["r", "t", "p"]

while True:
    escolha_usuario = input("Escolha R(Pedra)/T(Tesoura)/P(Papel) ou Q para sair: ").lower()

    if escolha_usuario == 'q':
        break

    if escolha_usuario not in opcoes:
        continue

    escolha_computador = random.randint(0, 2)
    # 0 : R, 1 : T, 2 : P
    opcao_computador = opcoes[escolha_computador]

    print("O computador escolheu " + opcao_computador)

    if escolha_usuario == opcao_computador:
        print("Empate!")

    elif escolha_usuario == "r" and opcao_computador == "t":
        print("Você ganhou!")
        pontos_usuario = pontos_usuario + 1

    elif escolha_usuario == "p" and opcao_computador == "r":
        print("Você ganhou!")
        pontos_usuario = pontos_usuario + 1

    elif escolha_usuario == "t" and opcao_computador == "p":
        print("Você ganhou!")
        pontos_usuario = pontos_usuario + 1

    else:
        print("Você perdeu!")
        pontos_computador = pontos_computador + 1

print("Sua pontuação: " + str(pontos_usuario))
print("Pontuação do Computador: " + str(pontos_computador))

if pontos_computador > pontos_usuario:
    print("Derrota!!!!")
elif pontos_computador == pontos_usuario:
    print("Empate")
else:
    print("Vitória!!")
