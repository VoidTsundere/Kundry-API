val = 1

class obj:
    player_account = {
        "name": str,
        "password": str,
        "id": str,
        "history_progress": {
            "arkandia":0},
        "currency": {
            "coins": 0,
            "souls": 0,
            "crystal": 0},
        "inventory": [],
        "account_lvl": 0,
        "account_xp": 0,
        "characters": [],
        "weekly_tasks":{},
        "gacha_data":{
            "base_pool":[0,0], #1° é garantido T4 e 2° é garantido T5
            "rotation_pool":[0,0],
            "especial_pool":[0,0]},
        "battles":[]}

    battle_obj = {
        "id": "null",
        "entity_list": "null",
        "entity_stats":[],
        "turn_code": 0,
        "turn": 0,
        "effect_list": []}

    character = {
        "id": int,
        "lvl": 0,
        "skill_lvl": [0,0,0],
        "copy":0}

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
            "C-0": {'name': 'Hiro',  # Nome do personagem
                'desc': 'Heroi falso',  # Descrição acessivel dentro do jogo
                "title":"Boneco de testes",
                'type': 'attack',  # Classe do personagem entre attack, sup e berserker
                "elemnt":"Unknow", #Elemnto do personagem entre fire, earth, air, water, etc
                'hp': 10,  # hp máximo do personagem
                'ult_charge': 100,  # valor de consumo de energia da suprema
                'card_list': [0, 1, 2, 3],  # lista de cartas do personagens
                'max_lvl': '10',  # nivel máximo do personagem
                'lvl_mult': 1.5,  # multiplicador de estatus por nível
                'rank':'t4'
                },
            
            "C-1": {'name': 'Fenyx Shiracc',
                'desc': 'Após acordar do experimento feito nele e em outros hibridos, Fenyx aprimorou sua habilidades e se concentrou apenas na sua magia de fogo.',  # Descrição acessivel dentro do jogo
                "title": "Hell Flare",
                'type': 'attack',
                'elemnt':'fire',
                'hp': 115,  # hp máximo do personagem
                'ult_charge': 45,  # valor de consumo de energia da suprema
                'card_list': [0, 1, 2, 3],  # lista de cartas do personagens
                'max_lvl': 100,  # nivel máximo do personagem
                'lvl_mult': 1.25,  # multiplicador de estatus por nível
                'rank':'t4'
                },
            
            "C-2": {'name': 'N° 19',
                    'desc': '',
                    "title": '',
                    'type': 'attack',
                    'elemnt': 'water',
                    'hp': 105,  # hp máximo do personagem
                    'ult_charge': 90,  # valor de consumo de energia da suprema
                    'card_list': [0, 1, 2, 3], # lista de cartas do personagens
                    'max_lvl': 100,  # nivel máximo do personagem
                    'lvl_mult': 1.20,  # multiplicador de estatus por nível
                    'rank': 't4'
                    },
            
            "C-3": {'name': 'Eliza',
                    'desc': '',
                    "title": '',
                    'type': 'attack',
                    'elemnt': 'earth',
                    'hp': 125,  # hp máximo do personagem
                    'ult_charge': 65,  # valor de consumo de energia da suprema
                    'card_list': [0, 1, 2, 3],
                    'max_lvl': 100,  # nivel máximo do personagem
                    'lvl_mult': 1.20,  # multiplicador de estatus por nível
                    'rank': 't5'
                    }
            }
        
class itens:
    list = {
        "I-0":{
            "name":"Test Item",
            "desc": "Teste Item desc",
            "rarity":6
            },
        "I-1":{"name":"DogTag militar",
               "desc":"Deixada por soldados, muitos sentimentos se esvaem junto com essa etiqueta.",
               "rarity":3
            },
        "I-2":{"name":"Livro de encantamento",
               "desc":"Está todo empoeirado, esse livro de encantamento deve ser bem antigo e de uma qualidade duvidosa.",
               "rarity":3
            },
        "I-3":{"name":"Pena de fogo",
               "desc":"Uma pena que alguma ave qualquer de fogo deixou cair, ainda sim sua mana é extremamente útil.",
               "rarity":3
            },
        "I-4":{"name":"Cantil com água mágica",
               "desc":"Pega de um lago em uma região de mana forte, muito útil para encantamentos",
               "rarity":3
            },
        "I-5":{"name":"Cristal da natureza",
               "desc":"Encontrados em regiões de mana forte, usados originalmente para fabricação de algumas runas",
               "rarity":3
            },
        "I-6":{"name":"Amuleto de Girard",
               "desc":"Um amuleto simples feito de madeira comum",
               "rarity":3
            },
        "I-7":{"name":"Talismã simples",
               "desc":"Usado em magiias simples e capaz de armazenar mana com propriiedades.",
               "rarity":1
            }
    }

class gacha:
    class pools:
        pool_list = {
            "pool-0":{
                "T5":["C-3"],
                "T4":["C-1","C-2"],
                "T3": ["I-1", "I-2", "I-3", "I-4", "I-5", "I-6"],
                "pool_type":"base_pool"
                }
        }
