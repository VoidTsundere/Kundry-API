import random
from string import ascii_uppercase
import objects

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
        
        new_character_data = objects.obj.character
        new_character_data.update({"id":character_id})
        
        char_list.append(new_character_data)
        acc_data.update({"characters":char_list})



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
            entity_in_charge = battle["entity_list"][battle["turn_code"]]
            if 'c' in entity_in_charge: #retorna os dados do personagem caso seja o turno dele
                character_id = int(entity_in_charge.replace('c',''))
                #print(objects.characters.id.list[character_id])
            if 'e' in entity_in_charge: #retorna os dados da entidade caso seja o turno delas
                enemy_id = int(entity_in_charge.replace('e',''))
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
                
        match_data = objects.obj.battle_obj
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
#battle.next_turn('DERE-00')
# battle.next_turn('DERE-00')
# battle.next_turn('DERE-00')
battle.turn_action('DERE-00', "player_opt")

acc = objects.obj.player_account
acc.update({"name":"Dere","password":"dere123","id":account.new_acc_id()})
acc_list.append(acc)
account.add_new_character(100,0)
print(account.get_account_data(100))

print("\n\n",battle_list)