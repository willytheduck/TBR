from ui import say, rule

ENDING={
    "genocide": {
        "title": "THE LONELY ENDING",
        "text": ("Papyrus is gone.. His scarf lies on the golden tiles. The corridor is silent... "
                 "and somewhere behind you a skeleton in a blue jacket stops making jokes. "
                 "You stand at the barrier, but there's nobody left to say goodbye... (how evil...)"),
    },
    "pacifist": {
        "title": "THE FRIENDSHIP ENDING",
        "text": ("Papyrus grins. 'SEE, HUMAN? EVERYONE DESERVES A SECOND CHANCE! NYEH HEH HEH' "
                 "One by one, monsters from every corner of the Underground gather to see you off: "
                 "a goat woman, a fish captain, a robot star. Together you walk to the barrier, "
                 "and it shatters in golden light."),
    },
    "neutral": {
        "title": "THE HEAVY ENDING",
        "text": ("Papyrus lets you pass, but there's sadness in his eyes. "
                 "You leave the Underground behind, carrying the weight of the monsters "
                 "you couldn't save..."),
    },
}


def pick_ending(player):
    if getattr(player, "last_boss", "killed") == "killed":
        return "genocide"
    return "pacifist" if player.kills == 0 else "neutral"

def ending(player):
    key = pick_ending(player)
    rule("=")
    say(ENDING[key]["title"], slow=True)
    say(ENDING[key]["text"], slow=True)
    rule("=")
    say(f"Final stats   |   STR {player.strength}   |   Max HP {player.max_hp}  |"
        f"Kills {player.kills}  |   Spared {player.spares}")
    say("\nTHE END. Thanks for playing!")