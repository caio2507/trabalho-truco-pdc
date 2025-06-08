import random

naipes = ['Ouro', 'Espada', 'Copas', 'Paus']
valores = ['4', '5', '6', '7', 'Q', 'J', 'K', 'A', '2', '3']

emoji_naipes = {
    'Ouro': '♦️',
    'Espada': '♠️',
    'Copas': '♥️',
    'Paus': '♣️'
}

ordem_forca = {
    '4': 1, '5': 2, '6': 3, '7': 4, 'Q': 5, 'J': 6, 'K': 7, 'A': 8, '2': 9, '3': 10
}

pedidos_ordem = [1, 3, 6, 9, 12]
 
def criar_baralho():
    return [f'{v} de {n}' for n in naipes for v in valores]

def carta_com_emoji(carta):
    valor, _, naipe = carta.partition(' de ')
    return f'{valor}{emoji_naipes[naipe]}'

def distribuir_cartas(baralho):
    random.shuffle(baralho)
    mao_jogador1 = [baralho.pop() for _ in range(3)]
    mao_jogador2 = [baralho.pop() for _ in range(3)]
    return mao_jogador1, mao_jogador2

def valor_carta(carta):
    return carta.split()[0]

def calcular_manilha_carta_virada(carta_virada):
    valor_virado = valor_carta(carta_virada)
    idx = valores.index(valor_virado)
    manilha_idx = (idx + 1) % len(valores)
    return valores[manilha_idx]

def comparar_cartas(carta1, carta2, manilha):
    v1 = valor_carta(carta1)
    v2 = valor_carta(carta2)

    if v1 == manilha and v2 != manilha:
        return 1
    if v2 == manilha and v1 != manilha:
        return 2

    ordem_naipe_manilha = {'Paus': 4, 'Copas': 3, 'Espada': 2, 'Ouro': 1}
    if v1 == manilha and v2 == manilha:
        naipe1 = carta1.split(' de ')[1]
        naipe2 = carta2.split(' de ')[1]
        if ordem_naipe_manilha[naipe1] > ordem_naipe_manilha[naipe2]:
            return 1
        elif ordem_naipe_manilha[naipe2] > ordem_naipe_manilha[naipe1]:
            return 2
        else:
            return 0

    if ordem_forca[v1] > ordem_forca[v2]:
        return 1
    elif ordem_forca[v2] > ordem_forca[v1]:
        return 2
    else:
        return 0

def escolher_carta(mao, jogador):
    print(f"\nJogador {jogador}, suas cartas são:")
    for i, carta in enumerate(mao):
        print(f"{i + 1}: {carta_com_emoji(carta)}")
    while True:
        escolha = input(f"Escolha a carta para jogar (1-{len(mao)}): ")
        if escolha.isdigit():
            escolha = int(escolha)
            if 1 <= escolha <= len(mao):
                return mao.pop(escolha - 1)
        print("Escolha inválida, tente novamente.")

def pedir_aumento(jogador, aposta_atual):
    pedidos_ordem = [1, 3, 6, 9, 12]
    index_atual = pedidos_ordem.index(aposta_atual)
    if index_atual == len(pedidos_ordem) - 1:
        return False, aposta_atual

    prox_aposta = pedidos_ordem[index_atual + 1]
    while True:
        resposta = input(f"Jogador {jogador}, quer aumentar para {prox_aposta} pontos? (s/n): ").lower()
        if resposta == 's':
            return True, prox_aposta
        elif resposta == 'n':
            return False, aposta_atual
        else:
            print("Resposta inválida, digite 's' para sim ou 'n' para não.")

def responder_aumento(jogador, pontos_rodada):
    while True:
        resposta = input(f"Jogador {jogador}, aceita aumentar para {pontos_rodada} pontos? (s/n): ").lower()
        if resposta == 's':
            print(f"Jogador {jogador} aceitou o aumento para {pontos_rodada} pontos.")
            return True, pontos_rodada
        elif resposta == 'n':
            print(f"Jogador {jogador} recusou o aumento.")
            return False, pontos_rodada
        else:
            print("Resposta inválida, digite 's' para sim ou 'n' para não.")

def jogar_truco():
    pontos_jogador1 = 0
    pontos_jogador2 = 0

    while pontos_jogador1 < 12 and pontos_jogador2 < 12:
        print("\n--- Nova mão! ---")
        baralho = criar_baralho()
        mao1, mao2 = distribuir_cartas(baralho)

        # Carta que virou (define manilha)
        carta_virada = baralho.pop()
        manilha = calcular_manilha_carta_virada(carta_virada)

        print(f"\nCarta que virou: {carta_com_emoji(carta_virada)} ({carta_virada})")
        print(f"Manilha dessa rodada: {manilha}")
