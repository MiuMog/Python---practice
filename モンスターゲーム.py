import random
def choice_monster(monsters: list)->str:
    stop = 0
    user_monster = ""
    user_monster_id = 0
    while stop == 0:
        for monster in monsters:
            print(f"「{monster.get("name")}」")

        user_choice_monster= input("上記のモンスターの中から、あなたの相棒になるモンスターを選んでください。(例: 火ネズミ): ")
        found = 0
        for serch in range(len(monsters)):
            if monsters[serch].get("name") == user_choice_monster:
                    user_monster_id = monsters[serch].get("ID")
                    print(f"--選択したモンスターが見つかりました！おめでとうございます。{user_choice_monster}はあなたの相棒になりました！--")
                    user_monster = user_choice_monster
                    found = 1
                    stop = 1
                    break
        if found == 0:
            print("--選択したモンスターがいないようです…もう一度確認してください‥--")
    return user_monster, user_monster_id


def choice_monsters_dura(monsters_info: list, user_monster_id: int):
    monster_dura= "" 
    for dura in monsters_info:
        if dura.get("type") == user_monster_id:
          monster_dura= (dura.get("dura"))
    return monster_dura

def choice_monsters_type(monsters_type: list, user_monster_id: int):
    monster_type= ""
    for type_dict in monsters_type:
        if type_dict.get(user_monster_id):
            monster_type= type_dict.get(user_monster_id)
    return monster_type
    
class Monster_fight:
    def __init__(self, name: str, id: int, dura: int, type: str):
        self.name= name
        self.id= id
        self.dura= dura
        self.type= type
        self.hp= 100

    def info(self, user: str):
        print(f"「{user}のモンスター:{self.name},体力:{self.hp},属性:{self.type},ダメージ軽減率:{self.dura}」")

    def manage(self):
        display= {1: "攻撃", 2:"回復",3:"逃げる"}
        print(display)
        user_choice_action= input("何をする？（例: 1): ")

    

l_monsters= [
    {"name":"火ネズミ", "ID":1},
    {"name":"水ガメ", "ID":2},
    {"name":"土モグラ", "ID":3},
    {"name":"風ワシ", "ID":4}
]

l_monsters_info=[
    {"type":1, "dura":5},
    {"type":2, "dura":7},
    {"type":3, "dura":3},
    {"type":4, "dura":2}
]

l_monsters_type=[
    {1:"火"},
    {2:"水"},
    {3:"土"},
    {4:"風"}
]


user_choice_monster, user_choice_monster_id= choice_monster(l_monsters)

cpu_choice= random.choice(l_monsters)
cpu_choice_monster= cpu_choice["name"]
cpu_choice_monster_id= cpu_choice["ID"]

user_choice_monster_dura= choice_monsters_dura(l_monsters_info, user_choice_monster_id)
cpu_choice_monster_dura= choice_monsters_dura(l_monsters_info, cpu_choice_monster_id)

user_choice_monster_type= choice_monsters_type(l_monsters_type, user_choice_monster_id)
cpu_choice_monster_type= choice_monsters_type(l_monsters_type, cpu_choice_monster_id)

#print(f"ユーザーの選択モンスター:{user_choice_monster}　ID:{user_choice_monster_id} dura:{user_choice_monster_dura} type:{user_choice_monster_type}")
#print(f"CPUの選択モンスター:{cpu_choice_monster}　ID:{cpu_choice_monster_id} dura:{cpu_choice_monster_dura} type:{cpu_choice_monster_type}")


p1= Monster_fight(user_choice_monster, user_choice_monster_id, user_choice_monster_dura, user_choice_monster_type)
p2= Monster_fight(cpu_choice_monster, cpu_choice_monster_id, cpu_choice_monster_dura, cpu_choice_monster_type)

p1.info("あなた")
p2.info("相手")

print("バトルを開始します。")

