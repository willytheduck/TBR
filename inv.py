from items import WEAPON, ARMOR, FOOD
from ui import say,menu

def food_lbl(key):
    f = FOOD[key]
    return f"{f.name} (+{'ALL' if f.heal == 999 else f.heal})"

def inv_menu(player, in_battle=False):
    #open the inv
    while True:
        #battle only can eat (equipping armor takes forever u know)
        opts = ["Eat food", "Back"] if in_battle else ["Eat food", "Equip weapon", "Equip armor", "Back"]
        choice = opts[menu("-- INVENTORY --", opts)]

        if choice == "Back":
            return False
        if choice == "Eat food":
            if not player.items:
                say("hm... You have nothing...")
                continue
            names = [food_lbl(k) for k in player.items] + ["Cancel"]
            pick = menu("What you gonna eat?", names)
            if pick == len(player.items):
                continue
            player.eat(pick)
            if in_battle:
                return True
        elif choice == "Equip weapon":
            names = [f"{WEAPON[w].name} (+{WEAPON[w].dmg})" + (" [equipped]" if w == player.weapon else "") for w in player.wpns_owned] + ["Cancel"]
            pick = menu("Which weapon?", names)
            if pick < len(player.wpns_owned):
                player.wpns_owned = player.wpns_owned[pick]
                say(f"You equipped {WEAPON[player.weapon].name}.")
        elif choice == "Equip armor":
            if not player.arms_owned:
                say("hm... You have no armor.")
                continue
            names = [f"{ARMOR[a].name} (DEF {ARMOR[a].defense})" + (" [equipped]" if a == player.armor else "") for a in player.arms_owned] + ["Cancel"]
            pick = menu("Which armor?", names)
            if pick < len(player.arms_owned):
                player.armor = player.arms_owned[pick]
                say(f"You equipped {ARMOR[player.armor].name}.")        