import random
from string import ascii_uppercase

battle_list = []
acc_list = []


class account:
    def get_account_data(ID):
        for acc_data in acc_list:
            if acc_data["id"] == ID:
                return acc_data
    
    def new_acc_id():  # todo Verificar se o ID já existe no server e então retornar ID
        id = random.randrange(100000, 999999)
        idd = 100 #! DEBUG
        return idd
    
    def add_new_character(ID, character_id): #todo REWORK POST SERVER
        acc_data = account.get_account_data(ID)
        char_list = acc_data["characters"]
        
        new_character_data = obj.character
        new_character_data.update({"id":character_id})
        
        char_list.append(new_character_data)
        acc_data.update({"characters":char_list})

class obj:
    player_account = {
        "name":str,
        "password":str,
        "id":account.new_acc_id(),
        "history_progress":0,
        "currency":{
            "coins":0,
            "souls":0,
            "crystal":0
            },
        "inventory":[],
        "account_lvl":0,
        "account_xp":0,
        "characters":[]}
    
    battle_obj = {
        "id":"null",
        "entity_list":"null",
        "turn_code":0,
        "turn":0,
        "effect_list":[]}
    
    character = {
        "id":int,
        "lvl":0,
        "skill_lvl":0}
    
    effect = {"enity_id":"null",
              "effect_id":"null",
              "duration":0}

class cards:
    class id:
        list = {
        0: {'name': 'testCard Attack',  # Define o nome da carta
        'desc':'Carta de testes Attack', #descrição da carta
        'type':'attack', #define o tipo da carte entre: attack, heal, enchance, defense
        'dmg':1, #dano base da carta
        'crit':1.5, #multiplicador de dano em caso de critico
        'lvl_mult':1.1, #multplicador de Dano dependendo do nivel da carta
        'max_lvl':10}, #nivel máximo da carta
        
        1: {'name':'testCard Heal',
        'desc':'Carta de testes Heal',
        'type':'heal',
        'heal':2,
        'crit':2,
        'lvl_mult':1.1,
        'max_lvl':10},
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
        0:{'type':'testObj', #tipo da entidade deve ser entre normal, elite, boss ou testObj para testes.
        'name':'ADM Doll',  #nome da entidade
        'desc': 'a boneca de testes do ademir', #descrição da entidade que pode ser lida dentro do jogo
        'max_hp':1000, #hp máximo da entidade para inpedir que ela possa curar mais do que o máximo de vida.
        'card_list': [0, 1, 2, 3]}  # lista contendo as cartas dessa entidade, essa lista deve possuir 20 cartas
        }

class characters:
    class id:
        list = {
            0:{'name':'Hiro', #Nome do personagem
            'desc':'Heroi falso', #Descrição acessivel dentro do jogo
            'type':'attack', #Classe do personagem entre attack, sup e berserker
            'hp': 10, #hp máximo do personagem
            'ult_charge':100, #valor de consumo de energia da suprema
            'card_list':[0,1,2,3], #lista de cartas do personagens
            'max_lvl':'10', #nivel máximo do personagem
            'lvl_mult':1.5 #multiplicador de estatus por nível
            }
        }

class battle:
    def battle_code():
        code = ''.join(random.choice(ascii_uppercase) for x in range(4))
        
        return "DERE-00" #! DEBUG
        
        return code + "-" +str(random.randrange(10, 99))
    
    def turn_action(match_id, action):
        def player_card(battle): #TODO função a ser executada caso o jogador use uma carta
            print('attack')
            return
        
        def player_opt(battle): #retorna as cartas que o jogador pode usar
            entity_in_charge = battle["entity_list"][battle["turn"]]
            if 'c' in entity_in_charge: #retorna os dados do personagem caso seja o turno dele
                character_id = int(entity_in_charge.replace('c',''))
                print(characters.id.list[character_id])
            if 'e' in entity_in_charge: #retorna os dados da entidade caso seja o turno delas
                enemy_id = int(entity_in_charge.replace('e',''))
                print(entity.id.list[enemy_id])
            return
        
        action_list = { #dict com todas as ações que podem ser passadas pela api
            "player_card":player_card,
            "player_opt":player_opt
        }
        
        for battle in battle_list:
            if battle["id"] == match_id:
                action_list[action](battle) #executa a função passada pela api
        return
    
    def create(characters_list, enemy_list): #! REWORK?
        battle_order = []
        for idx in range(0, max(len(characters_list), len(enemy_list))):
            try:
                battle_order.append(characters_list[idx])
                battle_order.append(enemy_list[idx])
            except:
                try:
                    battle_order.append(enemy_list[idx])
                    battle_order.append(characters_list[idx])
                except:
                    break
                
        match_data = obj.battle_obj
        match_data.update({"id":battle.battle_code(),
                           "entity_list": battle_order})
                
        return match_data
    
    def next_turn(match_id): #! IMPROVE passa para o próximo turno
        for battle in battle_list:
            if battle["id"] == match_id:
                entity_value = len(battle["entity_list"])-1
                if (battle["turn_code"] +1) <= entity_value: #muda o valor o turno e impede que esse valor seja maior que a quantade de entdidades na batalha
                    battle["turn_code"] += 1
                else:
                    battle["turn_code"] = 0
                battle["turn"] += 1
        return



battle_list.append(battle.create(['c0'], ['e0']))
battle.next_turn('DERE-00')
battle.next_turn('DERE-00')
battle.next_turn('DERE-00')
#battle.turn_action('DERE-00', "player_opt")

acc = obj.player_account
acc.update({"name":"Dere","password":"dere123"})
acc_list.append(acc)
account.add_new_character(100,0)
print(account.get_account_data(100))

print("\n\n",battle_list)