import random
from string import ascii_uppercase
import objects
import pymongo

bd_pass = "iDn4HavIPEKnOAJl"
VERSION = "Gliphnyr Live Alpha 0.0.2"

battle_list = []
acc_list = []

T5_CHANCE = 1.75
T4_CHANCE = 7.5

class account:
    def gacha_pull(ID, gacha_code, rolls):
        acc_data = account.get_account_data(ID)
        pool = objects.gacha.pools.pool_list[gacha_code]
        garantee = acc_data["gacha_data"][pool["pool_type"]]
        
        
        def final():
            new_data = acc_data
            new_data["currency"]["souls"] -= rolls*5
            new_data["gacha_data"][pool["pool_type"]] = garantee
            update_data = {"$set": {"gacha_data": new_data["gacha_data"]},"$set":{"currency": new_data["currency"]}}
            ACCOUNTS.update_one({"id": ID}, update_data)
        
        def pull_result(result):
            return (pool[result][random.randrange(0, len(pool[result]))])
        
        if acc_data["currency"]["souls"] >= rolls*5:
            for x in range(rolls):
                roll = random.randrange(0, 1000)/10
                
                if garantee[0]+1 == 10:
                    garantee[0] = 0
                    garantee[1] += 1
                    roll_result = pull_result("T4")
                    
                elif garantee[1]+1 == 80:
                    garantee[1] = 0
                    garantee[1] += 1
                    roll_result = pull_result("T5")
                    
                else:
                    garantee[0] += 1
                    garantee[1] += 1
                    
                    if roll <= T5_CHANCE:
                        garantee[1] = 0
                        roll_result = pull_result("T5")
                        
                    elif roll <= T4_CHANCE:
                        garantee[0] = 0
                        roll_result =  pull_result("T4")
                        
                    else:
                        roll_result =  pull_result("T3")
                    
                if "C" in roll_result:
                        print(objects.characters.id.list[roll_result]["name"], garantee)
                        
                if "I" in roll_result:
                        print(objects.itens.list[roll_result]["name"], garantee)
                        
            final()
        else:
            print("Not enough souls")
                    
    def create_account(name, password):
        new_acc_data = objects.obj.player_account
        new_acc_data.update({"name": name, "password": password, "id": account.new_acc_id()})
        return new_acc_data
        
    def get_account_data(ID):
        try:
            search = ACCOUNTS.find_one({"id": ID})
            return search
        except:
            return None
    
    def new_acc_id():
        while True:
            gen_id = random.randrange(100000000, 999999999)
            search = ACCOUNTS.find_one({"id": gen_id})
            if type(search) != dict:
                return gen_id
                break
    
    def add_new_character(ID, character_id): #! REWORK 
        acc_data = account.get_account_data(ID)
        char_list = acc_data["characters"]
        
        def update():
            update_data = {"$set": {"characters": char_list}}
            ACCOUNTS.update_one({"id": ID}, update_data)
        
        for nums, dicts in enumerate(char_list):
            if character_id == dicts["id"]:
                if char_list[nums]["copy"] +1 == 11:
                    print("Copy limit")
                    return #! here
                char_list[nums]["copy"] += 1
                update()
                return #! here
                
        character_obj = objects.obj.character
        character_obj.update({"id": character_id})
        char_list.append(character_obj)
                
        acc_data.update({"characters":char_list})
        update()
        return #! here

    def add_currency(ID, currency, ammount):
        acc_data = account.get_account_data(ID)
        
        new_ammount = acc_data["currency"][currency]+ammount
        acc_data["currency"][currency] = new_ammount
            
        update_data = {"$set":{"currency":acc_data["currency"]}}
        ACCOUNTS.update_one({"id": ID}, update_data)

    def level_up_character(ID, character_id): #! pos-inventory
        acc_data = account.get_account_data(ID)
        
        for char in acc_data["characters"]:
            if char["id"] == character_id:
                char_element = objects.characters.id.list[char["id"]]["elemnt"]
                
                if char["lvl"] >= 10:
                    print("lvl >= 10")
                    
                else:
                    upgrade_materials = objects.level.character_list[char_element]["level_up_materials_basic"]
                    upgrade_cost = int(char["lvl"]*upgrade_materials[1])
                    print(upgrade_cost)
        return

    def add_to_inv():
        return
    
    def remove_from_inv():
        return
    
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
    
    def create(characters_list, enemy_list, ID): #! REWORK?
        acc_data = account.get_account_data(ID)
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
        match_data.update({"id":battle.battle_code(),"entity_list": battle_order})
        
        for num, entity in enumerate(match_data["entity_list"]):
            stats = dict(objects.obj.entity_stats_obj)
            stats["id"] = entity
            
            for character in acc_data["characters"]:
                if character["id"] in characters_list:
                    print(character, characters_list)
            compute_atk = ()
            
            stats["computed_atk"]
            
            match_data["entity_stats"].append(stats)
        
        
        battle_list.append(match_data)
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


if __name__ == "__main__":
    db_client = pymongo.MongoClient("mongodb+srv://kurony:iDn4HavIPEKnOAJl@kundryapi.zauacf5.mongodb.net/?retryWrites=true&w=majority")
    db = db_client.kundryDB
    ACCOUNTS = db.ACCOUNTS
    BATTLES = db.BATTLES
    
    battle.create(["C-1"], ["E-0"], 916072406)

    
    
    #ACCOUNTS.insert_one(account.create_account("dere", "dere123"))
    #BATTLES.insert_one(battle.create(['c0'],['e1']))
    
    #account.gacha_pull(875495425, "pool-0", 10) 
    
    #account.add_new_character(916072406, "C-1")
    #account.add_currency(875495425, "souls", 5)
    #account.level_up_character(875495425, "C-1")
    
    #print("\n\n", ACCOUNTS.find_one({"id": 200545478}))
