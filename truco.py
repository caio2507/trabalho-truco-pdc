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