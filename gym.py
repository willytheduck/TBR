import random

from ui import say, pause, menu
from player import XP_P_STRENGTH

SETS = 3
REPS = 5
MAX_STR = 30
STRAIN_DMG = 3


def success_ch(player, weight):
    return max(30, min(95, 95 - weight * 14 + player.strength * 1.5))


def gym(player, name, state):
    sets_left = state.setdefault("gym", {}).setdefault(name, SETS)
    say(f"\n== {name} == (sets left: {sets_left})")
    while True:
        if sets_left <= 0:
            say("Your arms are like a jelly now. No more lifting here bro.")
            return
        opts = [
            "Light weight (safe, but little progress)",
            "Medium weight (balanced)",
            "Heavy weight (high risk high reward)",
            "Leave",
        ]
        pick = menu("CHOOSE YOUR WEIGHT:", opts)
        if pick == 3:
            return
        weight = pick + 1
        chance = success_ch(player, weight)
        say(f"{REPS} reps. Success chance per rep ~{int(chance)}%.")
        reps_ok = 0
        fails = 0
        for rep in range(1, REPS + 1):
            pause(f"Rep {rep}: PUSH! (Enter)")
            if random.random() * 100 < chance:
                reps_ok += 1
                say(f"  Rep {rep}: smooth.. like butter (+)")
            else:
                fails += 1
                say(f"  Rep {rep}: you wobble... (x)")

        sets_left -= 1
        state["gym"][name] = sets_left
        gaind = weight * reps_ok
        player.muscle += gaind
        say(f"Set done: {reps_ok}/{REPS} reps -> +{gaind} muscle.")

        while player.muscle >= XP_P_STRENGTH and player.strength < MAX_STR:
            player.muscle -= XP_P_STRENGTH
            player.strength += 1
            say(f"STRENGTH UP! You've gotten stronger.. ({player.strength})")
        if fails >= 3:
            strain = min(STRAIN_DMG, player.hp - 1)
            if strain > 0:
                player.hp -= strain
                say(f"You strained something. -{strain} HP welp.")
        say(f"(sets left: {sets_left})")
