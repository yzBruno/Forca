import random


def escolher_personagem():
    """
    Função para escolher um personagem aleatório de um anime, também atribui a variável global "anime" o respectivo
    anime do personagem escolhido
    :return: personagem escolhido
    """
    personagens = {
        'Dragon Ball': ['goku', 'vegeta', 'piccolo', 'bulma', 'kuririn', 'gohan', 'trunks', 'freeza', 'cell',
                        'majinbuu'],
        'One Piece': ['luffy', 'zoro', 'nami', 'sanji', 'chopper', 'robin', 'franky', 'brook', 'usopp', 'jinbe'],
        'Naruto': ['naruto', 'sasuke', 'sakura', 'kakashi', 'gaara', 'hinata', 'shikamaru', 'neji', 'rocklee',
                   'tsunade'],
        'Hunter x Hunter': ['gon', 'killua', 'kurapika', 'leorio', 'hisoka', 'illumi', 'chrollo', 'meruem', 'netero',
                            'neferpitou']
    }
    global anime
    anime = random.choice(list(personagens.keys()))
    return random.choice(personagens[anime])


def exibir_forca(personagem_oculto, tentativas_restantes):
    """
    Função para exibir a forca e a palavra oculta, tal como as tentativas restantes
    :param personagem_oculto:
    :param tentativas_restantes:
    :return:
    """
    print('Personagem: ' + personagem_oculto)
    print('Tentativas Restantes:', tentativas_restantes)


def forca():
    """
    Função principal da Forca
    :return:
    """
    personagem_oculto = escolher_personagem()
    personagem_letras = '_' * len(personagem_oculto)
    tentativas_restantes = 6
    letras_erradas = []

    print(' Jogo da Forca! '.center(40, '—'))
    print('Se diz fã de anime? Vamos lá provar!')
    print(f'O personagem da vez é do anime {anime}.')
    exibir_forca(personagem_letras, tentativas_restantes)

    while tentativas_restantes > 0 and '_' in personagem_letras:
        tentativa = input("Digite uma letra: ").lower()

        if len(tentativa) != 1 or not tentativa.isalpha():
            print('Por favor, insira uma única letra.')
            continue

        if tentativa in personagem_oculto:
            for i in range(len(personagem_oculto)):
                if personagem_oculto[i] == tentativa:
                    personagem_letras = personagem_letras[:i] + tentativa + personagem_letras[i+1:]
        else:
            letras_erradas.append(tentativa)
            tentativas_restantes -= 1

        exibir_forca(personagem_letras, tentativas_restantes)
        print('Letras erradas:', letras_erradas)
        print('—' * 40)

    if '_' not in personagem_letras:
        print(f'Parabéns! {personagem_oculto} era o/a personagem, e parece que temos um verdadeiro otaku aqui!')
        if anime == 'Dragon Ball':
            print('Você pode destruir mil planetas, galáxias, ou universos, mas não é capaz de destruir este Saiyajin.'
                  '~ Goku')
        if anime == 'One Piece':
            print('Os anjos nos deram a comida; os demônios, o tempero. ~ Sanji')
        if anime == 'Naruto':
            print('Desista de me fazer desistir! ~ Naruto')
        if anime == 'Hunter x Hunter':
            print('Amigos podem seguir caminhos diferentes, mas não deixam de ser amigos. ~ Gon')
    else:
        print('Você perdeu! O personagem era:', personagem_oculto)
