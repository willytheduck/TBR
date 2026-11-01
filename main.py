from ui import say, talk, rule, pause, menu, hp_bar
from player import Player
from items import FOOD
from inv import inv_menu
from enemy import ENEMY_DATA, make_enemy
from atk import enemy_turn, hit_dmg
from battle import battle
from gym import gym

def title_sc():
    rule("=")
    print("   U N D E R T A L E - I N S P I R E D   R P G")
    rule("=")
    say("A fan-made terminal game :D", slow=True)
    name = input("Name your fallen human (Enter for 'Frisk'): ").strip()
    return name[:12] if name else "Frisk"


def show_e(key):
    e = make_enemy(key)
    rule()
    say(f"{e.name.upper()}{'    [BOSS]' if e.boss else ''}")
    say(e.intro)
    say(
        f"HP {e.hp} ATK {e.atk} DEF {e.defense} attacks/turn {e.volleys} types {e.kinds}"
    )
    for name, (txt, mercy) in e.acts.items():
        say(f"  ACT {name}: +{mercy} mercy -> {txt}")
    rule()


def main():
    player = Player("Tester")
    state = {}
    keys = list(ENEMY_DATA. keys())

    while True:
        say(f"\nHP {hp_bar(player.hp, player.max_hp)}   STR {player.strength}   ATK {player.atk}")
        pick = menu("Test manu:", ["Train", "Fight", "Heal", "Status", "Inv", "Quit"])
        if pick == 0:
            gym(player, "Test Gym", state)
        elif pick == 1:
            names = [ENEMY_DATA[k]["name"] for k in keys] + ["Back"]
            i = menu("Which", names)
            if i < len(keys):
                result = battle(player, make_enemy(keys[i]))
                say(f"\nResult: {result}")
                if result == "dead":
                    player.hp = player.max_hp
        elif pick == 2:
            player.hp = player.max_hp
        elif pick == 3:
            player.status()
        elif pick ==4:
            inv_menu(player)
        else:
            break
    say("\nWORK")

if __name__ == "__main__":
    main()
