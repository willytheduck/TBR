from enemy import Enemy

KILLS_NO_MERCY = 5


def make_papyrus(player=None):
    kills = player.kills if player else 0

    base = dict(
        key="papyrus",
        name="Papyrus",
        hp=2040,
        atk=40,
        defense=60,
        boss=True,
        volleys=(2, 3),
        seq_len=(3, 4),
        kinds=["dodge", "blue", "orange"],
        intro="IT IS I, THE GREAT PAPYRUS, BLOCKING THE LAST DOOR, NYEH HEH HEH.",
        flavor=[
            "Papyrus prepares a non-bone attack then spends a minute fixing his mistake.",
            "Papyrus remembered a bad joke Sans told and is frowning.",
            "Papyrus is rattling his bones.",
            "Papyrus whispers 'Nyeh heh heh!'",
        ],
        spare_txt=(
            "Papyrus is sparing you. 'NYEH HEH HEH... I KNEW YOU WERE A GOOD HUMAN. '"
            "I SHALL LET YOU THROUGH. BUT YOU MUST PROMISE TO BE MY FRIEND!"
        ),
        die_txt=(
            "W-WELL, THAT'S NOT WHAT I EXPECTED... BUT... ST... STILL! I BELIEVE IN YOU!"
        ),
    )
    if kills >= KILLS_NO_MERCY:
        base.update(
            intro="Papyrus stands there, silent... For once, he isn't the 'Nyeh heh heh'..",
            acts={
                "Plead": (
                    "You beg for another chance. He doesn't respond (what's the point)",
                    0,
                ),
                "Talk": ("There's nothing to say...", 0),
            },
            block_spare=(
                "Papyrus: 'WHAT'S THE POINT OF SPARING. "
                "AFTER WHAT YOU DID TO EVERYONE...'"
            ),
            taunts=[
                (0.7, "Papyrus: 'EVERYONE YOU KILLED... THEY HAD FRIENDS, HUMAN.'"),
                (
                    0.3,
                    "Papyrus: 'I WON'T GIVE UP ON YOU. ...BUT I CAN'T LET YOU PASS...'",
                ),
            ],
        )
    else:
        base.update(
            acts={
                "Compliment": (
                    "You say his cooking looks amazing. He weeps with joy.",
                    25,
                ),
                "Spaghetti": (
                    "You offer to cook spaghetti together. His eyes sparkle.",
                    30,
                ),
                "Talk": ("You say you don't want to fight. 'NYEH?'", 20),
                "Hug": (
                    "You hug Papyrus. He doesn't know what to do with his arms.",
                    35,
                ),
            },
            taunts=[
                (0.7, "Papyrus: 'HUMAN, YOU'RE DAM STRONGER THAN YOU LOOK! WOW!"),
                (0.3, "Papyrus: 'I WON'T GIVE UP ON YOU!'"),
            ],
        )
    return Enemy(**base)
