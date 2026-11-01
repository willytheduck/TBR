import copy
import sys
from ui import say, rule, menu
from player import Player
from story import ROUTES
from explore import run_route
from end import ending
import atk
import battle as battle_mod

DEBUG = "--debug" in sys.argv

# hit_divisor, player_dmg_mult
# big divisor = enemy hits softer, big mult = you hit harder
DIFF = {
    "Easy": (4, 4),
    "Normal": (2, 3),
    "TRUE": (2, 2),
}


def set_diff(name):
    div, mult = DIFF[name]
    for module, attr, value in (
        (atk, "HIT_D", div),
        (battle_mod, "PLAYER_DMG_MULT", mult),
    ):
        if hasattr(module, attr):
            setattr(module, attr, value)
        else:
            say(
                f"(warning: couldn't find {attr} in {module.__name__}.py), "
                f"difficulty won't change it)"
            )


def title_sc():
    rule("=")
    print(" U N D E R T A L E - I N S P I R E D  R P G")
    rule("=")
    say("A fan-made terminal game :D")
    say("Tip: you can REST once per route in a quiet room. Gyms raise your STRENGTH.")
    print()
    name = input("Name your fallen human (Enter for 'Frisk'): ").strip()
    return name[:12] if name else "Frisk"


def play_once():
    player = Player(title_sc())
    set_diff(list(DIFF)[menu("\nChoose difficulty:", list(DIFF))])

    start = 0
    if DEBUG:
        start = menu("Start route? (debug)", [r.title for r in ROUTES])
        if start > 0 or menu("Boost?", ["No", "Yes"]) == 1:
            player.strength = 8 + 4 * start
            player.max_hp = player.hp = 30 + 6 * start
            player.weapon = "toy_knife" if start == 0 else "burnt_pan"
            player.wpns_owned.append(player.weapon)

    for idx in range(start, len(ROUTES)):
        snapshort = copy.deepcopy(player)  # checkpoint at the start
        while True:
            result = run_route(player, ROUTES[idx], idx)
            if result == "cleared":
                break
            rule("#")
            say(
                "You fell down... but you are filled with D E T E R M I N A T I O N.",
                slow=True,
            )
            rule("#")
            if menu("Continue?", ["Retry this route", "Give up"]) == 1:
                say("Game over. Thanks for playing. :D")
                return
            player = copy.deepcopy(snapshort)

    ending(player)


def main():
    while True:
        play_once()
        if menu("\nPlay again?", ["Yes", "No"]) == 1:
            say("See you in the Underground!")
            return


if __name__ == "__main__":
    main()
