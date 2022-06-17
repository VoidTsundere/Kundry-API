val = 1

class obj:
    player_account = {
        "name": str,
        "password": str,
        "id": str,
        "history_progress": 0,
        "currency": {
            "coins": 0,
            "souls": 0,
            "crystal": 0
        },
        "inventory": [],
        "account_lvl": 0,
        "account_xp": 0,
        "characters": []}

    battle_obj = {
        "id": "null",
        "entity_list": "null",
        "turn_code": 0,
        "turn": 0,
        "effect_list": []}

    character = {
        "id": int,
        "lvl": 0,
        "skill_lvl": 0}

    effect = {"enity_id": "null",
              "effect_id": "null",
              "duration": 0}


class cards:
    class id:
        list = {
            0: {'name': 'testCard Attack',  # Define o nome da carta
                'desc': 'Carta de testes Attack',  # descrição da carta
                'type': 'attack',  # define o tipo da carte entre: attack, heal, enchance, defense
                'dmg': 1,  # dano base da carta
                'crit': 1.5,  # multiplicador de dano em caso de critico
                'lvl_mult': 1.1,  # multplicador de Dano dependendo do nivel da carta
                'max_lvl': 10},  # nivel máximo da carta

            1: {'name': 'testCard Heal',
                'desc': 'Carta de testes Heal',
                'type': 'heal',
                'heal': 2,
                'crit': 2,
                'lvl_mult': 1.1,
                'max_lvl': 10},
            2: {'name': 'testCard enchance',
                'desc': 'Carta de testes Enchance',
                'type': 'enchance',
                'enchance': 3,
                'crit': 1.5,
                'lvl_mult': 1.2,
                'max_lvl': 10},
            3: {'name': 'testCard defense',
                'desc': 'Carta de testes Defense',
                'type': 'defense',
                'def': 2,
                'crit': 2,
                'lvl_mult': 1.2,
                'max_lvl': 10}
        }


class entity:
    class id:
        list = {
            0: {'type': 'testObj',  # tipo da entidade deve ser entre normal, elite, boss ou testObj para testes.
                'name': 'ADM Doll',  # nome da entidade
                'desc': 'a boneca de testes do ademir', # descrição da entidade que pode ser lida dentro do jogo
                'max_hp': 1000, # hp máximo da entidade para inpedir que ela possa curar mais do que o máximo de vida.
                'card_list': [0, 1, 2, 3]}  # lista contendo as cartas dessa entidade, essa lista deve possuir 20 cartas
        }


class characters:
    class id:
        list = {
            0: {'name': 'Hiro',  # Nome do personagem
                'desc': 'Heroi falso',  # Descrição acessivel dentro do jogo
                'type': 'attack',  # Classe do personagem entre attack, sup e berserker
                'hp': 10,  # hp máximo do personagem
                'ult_charge': 100,  # valor de consumo de energia da suprema
                'card_list': [0, 1, 2, 3],  # lista de cartas do personagens
                'max_lvl': '10',  # nivel máximo do personagem
                'lvl_mult': 1.5  # multiplicador de estatus por nível
                }
        }
