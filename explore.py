from ui import say, rule, pause, menu, hp_bar
from items import WEAPON, ARMOR, FOOD
from inv import inv_menu
from gym import gym
from battle import battle
from enemy import make_enemy

INV_LIMIT = 8

def give_loot(player, room):
    kind,key = room["loot"], room["key"]
    if room["text"]:
            say(room["text"], slow=True)
    if kind == "weapon":
          w = WEAPON[key]
          say(f"You found: {w.name} (+{w.dmg})! {w.desc}")
    