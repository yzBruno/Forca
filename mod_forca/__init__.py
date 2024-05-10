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
        'Hunter x Hunter': ['gon', 'killua', 'kurapika', 'leorio', 'hisoka', 'illumi', 'chrollo', 'meruem', 'netero',
                            'neferpitou'],
        'One Piece': ['luffy', 'zoro', 'nami', 'sanji', 'chopper', 'robin', 'franky', 'brook', 'usopp', 'jinbe'],
        'Naruto': ['naruto', 'sasuke', 'sakura', 'kakashi', 'gaara', 'hinata', 'shikamaru', 'neji', 'rocklee',
                   'tsunade']
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


def escolher_frase():
    """
    Função para escolher uma frase aleatória do anime escolhido, atruibuindo a variável "frase" a respectiva frase
    do anime escolhido
    :return:
    """
    frases = {
        'Dragon Ball': ['É mais de oito mil! ~Vegeta', 'Meu coração é puro... pura maldade! ~Vegeta',
                        'Os limites só existem se você os deixar existir. ~Goku', 'Você pode destruir mil planetas, '
                        'galáxias, ou universos, mas não é capaz de destruir este Saiyajin. ~Goku'],
        'Hunter x Hunter': ['Gon, você é luz. Mas às vezes você brilha tanto que devo desviar o olhar... Mesmo assim, '
                            'tudo bem se eu ficar ao seu lado?” ~Killua',
                            'e você estiver mentindo, será fácil para mim. Não terei que mostrar nenhuma misericórdia. '
                            'Posso derrotá-lo sem hesitação. ~Gon'
                            'Os enigmas dos ceifadores não precisam de ninguém para responder ~Hisoka',
                            'Se eu conseguir que meu alvo se mova como eu quero, eu tive sucesso como Caçador. ~Ging'],
        'One Piece': ['Os anjos nos deram a comida; os demônios, o tempero. ~Sanji',
                      'Eles se perderam novamente, bando de idiotas! ~Zoro',
                      'Eu não quero conquistar nada, só acho que a pessoa com mais liberdade do mundo é o rei dos '
                      'piratas! ~Luffy', 'Você sabe o que os heróis fazem? Vou dar o exemplo de um pedaço de carne, '
                      'tudo bem? Piratas irão ter um banquete e comê-la, mas os heróis irão dividir com outras pessoas.'
                      ' Eu quero comer toda a carne! ~Luffy'],
        'Naruto': ['Trabalho duro é inútil para aqueles que não acreditam em si mesmos. ~Naruto',
                   'Aqueles que não entendem a verdadeira dor nunca vão entender a verdadeira paz. ~Pain',
                   'O conceito de esperança não é mais do que desistir. Uma palavra que não contém qualquer '
                   'significado. ~Madara',
                   'Às vezes eu gostaria de ser apenas uma nuvem, flutuando. ~Shikamaru']
    }
    return random.choice(frases[anime])


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
        print('Parabéns! Você acertou, é o/a: ', end='')
        print(f'{personagem_oculto}'.capitalize())
        print(f'\nFica uma frase do anime: {escolher_frase()}')
    else:
        print('Você perdeu! Era o/a: ', end='')
        print(f'{personagem_oculto}'.capitalize())
