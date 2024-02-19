import random

type_win = {
    "fire water": "water",
    "fire earth": "earth",
    "fire wind": "fire",

    "water fire": "water",
    "water earth": "water",
    "water wind": "wind ",

    "earth fire": "earth",
    "earth water": "water",
    "earth wind": "earth",

    "wind fire": "fire",
    "wind water": "wind",
    "wind earth": "earth",
}
class Pokemon:
    def __init__(self, name, level, strength, speed, type, life, player_id):
        self.name = name
        self.level = level
        self.strength = strength
        self.speed = speed
        self.type = type
        self.life = life
        self.player_id = player_id

    def __str__(self):
        return f"Pokemon(name='{self.name}', strength='{self.strength}', speed='{self.speed}', type='{self.type}', life='{self.life}')"
class Player:
    def __init__(self, id, numOfPok):
        self.id = id
        self.numOfPok = numOfPok
        self.pokemons = []

    def add(self, pokemon):
        self.pokemons.append(pokemon)
def welcome_fun():
    print("Player 1 has  " + str(player1.numOfPok) + "  " + "Pokemons")
    print("Player 2 has  " + str(player2.numOfPok) + "  " + "Pokemons")
    random_player1 = random.randint(0, player1.numOfPok - 1)
    random_player2 = random.randint(0, player2.numOfPok - 1)
    return player1.pokemons[random_player1], player2.pokemons[random_player2]
def choose_starter(pokemon1, pokemon2):
    pokemon2.speed += random.randint(1, 20)
    pokemon1.speed += random.randint(1, 20)
    if pokemon1.speed > pokemon2.speed:
        return 1
    elif pokemon1.speed < pokemon2.speed:
        return 2
    return 0
def cal_modifier(pok1, pok2):
    key = f"{pok1.type} {pok2.type}"
    print(f"the winner between {pok1.type} and {pok2.type} is {type_win.get(key)} ")
    if type_win.get(key) is None:  return 1,1
    elif pok1.type == type_win.get(key): return 2,1
    else:return 1,2
def damage(pok,mod):
    return (mod*random.randint(1,20)+pok.strength)
def battle(player1,player2,pok1,pok2,start,mod1,mod2):
  while pok1.life>0 and pok2.life>0:
      print("Life of Pokemon 1 : " + str(pok1.life))
      print("Life of Pokemon 2 : " + str(pok2.life))
      dmg1to2=damage(pok1,mod1)
      dmg2to1 = damage(pok2, mod2)

      pok1.life -= dmg2to1
      pok2.life -= dmg1to2
      if start == 1 and pok2.life <=0:
          pok1.life += dmg2to1
      if start == 2 and pok1.life <=0:
          pok2.life += dmg1to2
      print("dmg1to2 is "+str(dmg1to2))
      print("dmg2to1 is " + str(dmg2to1))

      if pok1.life <=0 and pok2.life <=0:
         print("pok1 died, pok2 died, no winner")
         player1.numOfPok -= 1
         player2.numOfPok -= 1
         player1.pokemons.remove(pok1)
         player2.pokemons.remove(pok2)
         return
      elif pok2.life <= 0:
          print("pok2 died, pok1 win")
          player2.numOfPok -= 1
          player2.pokemons.remove(pok2)
          return
      elif pok1.life <= 0:
          print("pok1 died, pok2 win")
          player1.numOfPok -= 1
          player1.pokemons.remove(pok1)
          return

if __name__ == "__main__":
    names = ["pok1", "pok2", "pok3", "pok4", "pok5", "pok6", "pok7", "pok8", "pok9", "pok10"]
    types = ["fire", "water", "wind", "earth"]
    player1 = Player(1, 3)
    player2 = Player(2, 3)
    players = [player1, player2]
    for i in range(3):
        name = random.choice(names)
        names.remove(name)
        index = random.randint(0, 3)
        player1.add(Pokemon(name, 1, random.randint(1, 10), random.randint(1, 5), types[index], 50, 1))
        name = random.choice(names)
        names.remove(name)
        player2.add(Pokemon(name, 1, random.randint(1, 10), random.randint(1, 5), types[index], 50, 2))
    while player2.numOfPok > 0 and player1.numOfPok > 0:
        pok1, pok2 = welcome_fun()
        print(pok1.name + " has joined the fight (player1) ")
        print(pok2.name + " has joined the fight (player2) ")
        start=choose_starter(pok1, pok2)
        mod1,mod2=cal_modifier(pok1,pok2)
        battle(player1,player2,pok1,pok2,start,mod1,mod2)
    if player2.numOfPok > 0:print("player 2 win the game")
    else: print("player 1 win the game")