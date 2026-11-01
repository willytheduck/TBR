from dataclasses import dataclass


def S(txt):
    return {"kind": "story", "text": txt}


def F(enemy, pre=""):
    return {"kind": "fight", "enemy": enemy, "text": pre}


def B(enemy, pre=""):
    return {"kind": "boss", "enemy": enemy, "text": pre}


def L(kind, key, txt=""):
    return {"kind": "loot", "loot": kind, "key": key, "text": txt}


def G(name, txt=""):
    return {"kind": "gym", "name": name, "text": txt}


@dataclass
class Route:
    title: str
    intro: str
    rooms: list
    outro: str


ROUTES = [
    Route(
        title="THE RUINS",
        intro=(
            "Long ago, humans and monsters shared the Earth. The humans, afraid of the one "
            "thing that could hurt them, attacked. The monsters lost, and seven great "
            "magicians sealed them beneath Mount Ebott. \n"
            "They say anyone who climbs the mountain never comes back. A child climbed it "
            "anyway. And fell."
        ),
        rooms=[
            S(
                "You land on a bed of golden flowers. They broke your fall. Somewhere in the "
                "dark a small flower with a face smiles at you. 'Howdy! You're new to the "
                "Underground, aren't ya?' He teaches you how things work here. Something in his "
                "smile feels wrong."
            ),
            L(
                "food",
                "monster_candy",
                "A candy dish sits on a stone table. Someone is looking after this place.",
            ),
            G(
                "Ruins - Stone Block Room",
                "Giant stone blocks sit in a puzzle room, scuffed from years of pushing. You could use them as weights.",
            ),
            F(
                "froggit",
                "Something hops in the dark. It doesn't look dangerous. It doesn't look confident, either.",
            ),
            L(
                "weapon",
                "toy_knife",
                "A plastic knife lies in a corner, left behind by a child who came here before you.",
            ),
            L(
                "armor",
                "ribbon",
                "A faded ribbon, tied to a dead vine. It belonged to the same child, you think.",
            ),
            S(
                "A shelf of old books. One tells how, after the war, the monsters walked deep "
                "into the earth until they reached the end of the cavern and called it 'Home.' "
                "It smells like cinnamon here."
            ),
            L(
                "hpup",
                4,
                "A golden glow pulses above a small pedestal. You feel more determined.",
            ),
            F(
                "whimsun",
                "A tiny moth-like monster flutters toward you, already apologizing.",
            ),
            F("moldsmal", "A mound of gelatin wobbles out of the shadows."),
            B(
                "toriel",
                "A tall goat-like woman steps out of the hallway. She once ruled the Underground beside the king. She left when he decided that every human who fell here must die. She's been waiting at the exit ever since.",
            ),
        ],
        outro=(
            "The Ruins' door opens. A cold wind blows snowflakes in. Far behind you, "
            "a flower watches you go."
        ),
    ),
    Route(
        title="SNOWDIN",
        intro=(
            "Snow crunches under your feet. A tall, loud silhouette waves from the trees. "
            "A short one in a blue jacket stands a little further away, hands in his pockets."
        ),
        rooms=[
            S(
                "A broken sentry station. A skeleton named Sans sits behind it, 'working.' "
                "His brother Papyrus keeps setting puzzles for you, because he dreams of "
                "capturing a human and joining the Royal Guard."
            ),
            L("armor", "bandage", "A first aid kit sticks out of a snow drift."),
            F(
                "snowdrake",
                "A bird-shaped silhouette swoops overhead, laughing at its own joke.",
            ),
            G(
                "Snowdin - Papyrus's Cool Dude Gym",
                "Papyrus has set up weights in the snow. 'THIS IS FOR SPECIAL TRAINING!' says his hand-painted sign. 'FOR BECOMING A GREAT GUARDSMAN!'",
            ),
            F("icecap", "A pointed hat glints in the white."),
            L(
                "armor",
                "bandanna",
                "A sweat-wicking bandanna is draped over a snowman.",
            ),
            L(
                "food",
                "nice_cream",
                "A friendly vendor offers you a frozen treat. It's enormously kind.",
            ),
            S(
                "A small town of lights and snow. A library holds a worn book: after a long "
                "time in Home, the monsters crossed cold, swamp and fire to build a new capital, "
                "New Home. They stopped fearing the humans, and stopped hoping, too."
            ),
            F("doggo", "Something squints in the snow. It can oly see what moves."),
            L(
                "hpup",
                4,
                "A snowball glows in a drift. You decide to take it with you.",
            ),
            B(
                "greater_dog",
                "The ground shakes. A suit of armor the size of a house gallops toward you, tail wagging so hard it knocks trees over.",
            ),
        ],
        outro=(
            "Behind you, Papyrus waves goodbye. Somewhere far above, a skeleton in a blue "
            "jacket is watching, as if he already knows how this ends. Water drips ahead."
        ),
    ),
    Route(
        title="WATERFALL",
        intro=(
            "Blue crystals glow on the cave walls like a night sky. Echo flowers whisper "
            "back whatever was said near them. Old glyphs cover the stone, carved by "
            "someone long ago."
        ),
        rooms=[
            S(
                "The glyphs tell what monsters remember about the war: a monster who held a "
                "human SOUL would be a horrible, powerful thing, so the humans struck first, "
                "without mercy. Every monster's SOUL combined barely matches one human's"
            ),
            L(
                "food",
                "spider_donut",
                "A cobweb stand sits in the corner. A coin goes in the jar and a donut comes out.",
            ),
            F(
                "woshua",
                "A tiny monster scrubs its way toward you, determined to clean this whole cave.",
            ),
            G(
                "Waterfall - Dripping Weights",
                "Weights tied to ropes hang in a shallow pool. Someone trains here in secret, away from the Royal Guard's eyes.",
            ),
            F("aaron", "A heavily flexed shape blocks the path. It winks. It flexes."),
            L(
                "weapon",
                "ballet_shoes",
                "A pair of pink ballet shoes dangle from a bush. They're worn through at the toes.",
            ),
            L(
                "armor",
                "tutu",
                "A torn tutu lies in the tall grass nearby. you get the feeling the monsters tried to hunt a human here.",
            ),
            S(
                "An old turtle polishes a counter. He fought in the war and survived. He doesn't "
                "say much about it. he only looks at the stars on the ceiling and says they "
                "were a lot brighter once."
            ),
            L("hpup", 5, "A star-shaped rock hums in your hand."),
            B(
                "undyne",
                "A spear slams into the ground. Heavy armor, glowing eyes: the captain of the Royal Guard has found you.",
            ),
        ],
        outro=(
            "The caverns warm. Heat rises from somewhere deep. Hotland is near, and with it, "
            "the Core."
        ),
    ),
    Route(
        title="HOTLAND",
        intro=(
            "Rivers of lava glow in the dark. A strange pink spotlight sweeps across the "
            "stone. Machines of every size hum in the distance."
        ),
        rooms=[
            S(
                "A lab full of dusty monitors. The royal scientist Alphys studied SOULs here, "
                "searching for a gentler way to break the barrier, and discovered "
                "DETERMINATION, the thing that lets a human SOUL linger after death. "
                "She also built a robot body for a ghost who wanted to be a star."
            ),
            L(
                "food",
                "hot_dog",
                "A hot dog cart rolls by with nobody pushing it. You grab one.",
            ),
            F("vulkin", "A little volcano toddles toward you, beaming."),
            G(
                "Hotland - Lab treadmill",
                "A convenyor belt in the lab runs endlessly. It makes a great treadmill.",
            ),
            F("pyrope", "A burning rope bounces into view, grinning."),
            L(
                "weapon",
                "burnt_pan",
                "A scorched frying pan hangs on a hook. Whoever cooked here had more heart than skill.",
            ),
            L(
                "weapon",
                "empty_gun",
                "A toy gun sits in a case. There's no ammo, but it looks intimidating.",
            ),
            L(
                "armor",
                "glasses",
                "A pair of cloudy glasses sits on a torn notebook. ('Urmm... AKSUALLY')",
            ),
            S(
                "A glittering hotel lobby, The elevator hums, taking visitors to the Core "
                "and to New Home. The staff keep their eyes down. A trophy on the wall has "
                "the name of a ghost-turned-robot star."
            ),
            F(
                "tsunderplane",
                "A little plane buzzes by, trying hard not to look at you.",
            ),
            L("hpup", 5, "A warm light pulses from a vent. You feel it in your SOUL."),
            B(
                "mettaton",
                "The lights flare. A robotic voice shouts your name into the dark, and the cameras all turn to you.",
            ),
        ],
        outro=(
            "The show is over. The elevator opens. Beyond it lies New Home, the last city "
            "the monsters ever built."
        ),
    ),
    Route(
        title="NEW HOME & THE LAST CORRIDOR",
        intro=(
            "New Home is quiet. The houses all look the same and nobody is outside. At the "
            "end of the city stands the king's castle. Six human SOULs wait inside it, "
            "and with a seventh, the barrier would break."
        ),
        rooms=[
            S(
                "A house like Toriel's, but with two small bedrooms side by side. The king's "
                "children lived here: Asriel, and the first human to fall, who he called "
                "his sibling. When they died, everything came after began: the "
                "decree that every fallen human must die, and Toriel leaving."
            ),
            L(
                "weapon",
                "worn_dagger",
                "A rusty gardening tool lies in the golden flowers. It belongs to someone who has stopped tending the garden.",
            ),
            L(
                "food",
                "legendary_hero",
                "A hero-shaped sandwich is left on a bench. You take it, feeling a bit guilty.",
            ),
            G(
                "New Home - Empty Courtyard",
                "A courtyard with old training dummies. Nobody has swung at them in years.",
            ),
            S(
                "The king's throne room. A garden of golden flowers, a pair of empty chairs, "
                "and a king who clearly doesn't want to be what he's become. He admits he "
                "doesn't have the heart to fight a child."
            ),
            L(
                "hpup",
                5,
                "A glowing flower grows beside the throne. You feel stronger.",
            ),
            S(
                "A long golden corridor lit by tall windows. Stories of the war and the old "
                "kingdom are painted in the glass. At its end, a skeleton in a blue jacket "
                "leans against a pillar and says it's a nice day for judging."
            ),
            L(
                "weapon",
                "real_knife",
                "A real knife lies on the floor. It's old and well kept, as if someone kept hoping to use it.",
            ),
            S(
                "The last quiet hall before the barrier. Someone is waiting just ahead, "
                "wearing homemade armor and the biggest smile you've ever seen. He's been "
                "preparing for this moment his entire life."
            ),
            B(
                "papyrus",
                "THE GREAT PAPYRUS, newly promoted Royal Guard, blocks the last door. 'HUMAN! I HAVE COME TO CAPTURE YOU! NYEH HEH HEH!'",
            ),
        ],
        outro="",
    ),
]
