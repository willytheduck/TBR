import copy
from dataclasses import dataclass, field


@dataclass
class Enemy:
    key: str
    name: str
    hp: int
    atk: int
    defense: int
    intro: str
    flavor: list  # random lines
    acts: dict
    volleys: tuple = (1, 2)  # attacks/enemy turn (min,max)
    seq_len: tuple = (2, 3)  # arrows/dodge atk (min,max)
    kinds: list = field(default_factory=lambda: ["dodge"])  # dodge/blue/orange
    spare_txt: str = "You spared them. Good job! They can live another day!"
    die_txt: str = "They crumble to dust... why..."
    boss: bool = False
    taunts: list = field(default_factory=list)  # (hp fraction, line) showed once
    block_spare: str = ""#"They just doesn't want to listen anymore. What did you do??"
    max_hp: int = 0
    mercy: int = 0

    def __post_init__(self):
        self.max_hp = self.hp


ENEMY_DATA = {
    # --RUINS--
    "froggit": dict(
        name="Froggit",
        hp=30,
        atk=4,
        defense=5,
        intro="Froggit hopped close!",
        flavor=[
            "Froggit doesn't seem to know why it's here.",
            "Froggit hops to and fro.",
            "The battlefield is filled with the smell of mustard seed.",
            "You are intimidated by Froggit's raw strength. Only kidding.",
        ],
        acts={
            "Compliment": (
                "Froggit didn't understand what you said, but was flattered anyway.",
                50,
            ),
            "Threaten": (
                "Froggit didn't understand what you said, but was scared anyway.",
                25,
            ),
        },
    ),
    "whimsun": dict(
        name="Whimsun",
        hp=10,
        atk=5,
        defense=0,
        intro="Whimsun approached meekly!",
        flavor=[
            "Whimsun continues to mutter apologies.",
            "Whimsun avoids eye contact.",
            "Whimsun is fluttering.",
            "It's starting to smell like lavender and mothballs.",
        ],
        acts={
            "Console": (
                "Halfway through your first word, Whimsun bursts into tears and runs away.",
                60,
            ),
            "Terrorize": (
                "You raise your arms and wiggle your fingers. Whimsun freaks out!",
                100,
            ),
        },
    ),
    "moldsmal": dict(
        name="Moldsmal",
        hp=50,
        atk=6,
        defense=0,
        intro="Moldsmal blocked the way!",
        flavor=[
            "Moldsmal waits pensively.",
            "Moldsmal burbles quietly.",
            "Moldsmal is ruminating.",
            "The aroma of lime gelatin wafts through.",
        ],
        acts={
            "Flirt": (
                "You wiggle your hips. Moldsmal wiggles back. What a meaningful conversation!",
                60,
            ),
            "Imitate": (
                "You lie immobile with Moldsmal. You feel like you understand the world a little better.",
                50,
            ),
        },
    ),
    "toriel": dict(
        name="Toriel",
        hp=440,
        atk=80,
        defense=80,
        boss=True,
        volleys=(2, 2),
        intro="Toriel blocks the way! ",
        flavor=[
            "Toriel looks through you.",
            "Toriel prepares a magical attack.",
            "Toriel takes a deep breath.",
            "Toriel is acting aloof.",
        ],
        acts={
            "Talk": ("You say you just want to go home. Toriel flinches", 30),
            "Hug": ("You step into the flames and hug her", 45),
            "Stay": (
                "You stand still. She can't bring herself to attack you (Stay with me Mayonaka no doa o tataki :P)",
                40,
            ),
        },
        spare_txt="Toriel decided to let you go.. 'Ah.. go on then, my child.'",
        die_txt="Toriel's flames fade away... 'Be.. good, won't you...? M y c h i l d.",
        taunts=[(0.5, "Toriel: 'Plase, just turn back, my child.'")],
    ),
    # --Snowdin--
    "snowdrake": dict(
        name="Snowdrake",
        hp=74,
        atk=12,
        defense=7,
        intro="Snowdrake flutters forth!",
        flavor=[
            "Snowdrake is assessing the crowd.",
            "Snowdrake is practicing its next pun.",
            "Snowdrake is smiling at its own bad joke.",
            "It smells like a wet pillow.",
        ],
        acts={
            "Heckle": ("You boo the Snowdrake", 50),
            "Joke": ("You make a bad ice pun.", 70),
        },
    ),
    "icecap": dict(
        name="Ice Cap",
        hp=48,
        atk=11,
        defense=4,
        intro="Icecap struts into view.",
        flavor=[
            "It's snowing dandruff.",
            "Ice Cap also wants a hat for its nose.",
            "Ice Cap makes sure its hat is still there.",
            "Ice Cap is thinking about a certain article of clothing.",
            "Here comes that new clothes smell.",
        ],
        acts={
            "Ignore": ("You manage to tear your eyes away from Ice Cap's hat.", 30),
            "Steal": (
                "You tried to steal Ice Cap's hat... And succeeded! (It melts in your hands...)",
                60,
            ),
        },
    ),
    "doggo": dict(
        name="Doggo",
        hp=70,
        atk=13,
        defense=7,
        intro="Doggo blocks the way!",
        flavor=[
            "Doggo is too suspicious of your movements.",
            "Doggo can't seem to find anything.",
        ],
        kinds=["dodge", "blue"],
        acts={
            "Pet": ("You pet Doggo.", 100),
            "Stick": (
                "You threw the stick and the dog ran to get it. You played fetch for a while.",
                60,
            ),
        },
    ),
    "greater_dog": dict(
        name="Greater Dog",
        hp=105,
        atk=15,
        defense=8,
        intro="It's the Greater Dog.",
        flavor=[
            "Greater Dog is watching you intently.",
            "Greater Dog is waiting for your command.",
            "It smells like freshly-squeezed puppy juice.",
            "Greater Dog is seeking affection.",
        ],
        acts={
            "Pet": (
                "Greater Dog is too far away to pet. You just pet the air. But.. atleast you tried",
                45,
            ),
            "Beckon": (
                "You call the Greater Dog. It bounds towards you, flecking slobber into your face.",
                60,
            ),
        },
        spare_txt="Greater Dog is contented.",
        die_txt="The armor clatters to the ground. How evil!",
    ),
    # lazy to do papyrus
    # --Waterfall--
    "woshua": dict(
        name="Woshua",
        hp=70,
        atk=18,
        defense=5,
        intro="Woshua shuffles up.",
        flavor=[
            "Woshua wonders if tears are sanitary.",
            "Woshua is friends with a little bird.",
            "Woshua is rinsing off a pizza.",
            "Woshua is looking for some good clean fun.",
            "Smells like detergent.",
        ],
        acts={
            "Clean": ("You ask Woshua to clean you. It hops around excitedly.", 70),
            "Joke": ("NO. THAT JOKE'S TOO... DIRTY", 40),
        },
    ),
    "aaron": dict(
        name="Aaron",
        hp=98,
        atk=24,
        defense=12,
        intro="Aaron flexes in!",
        flavor=[
            "Aaron is sweating bullets. Literally.",
            "Aaron is admiring his own muscles.",
            "Smells like an underwater barnyard.",
            "Smells like a mussel farm.",
        ],
        acts={
            "Flex": (
                "You flex harder. Aaron flexes thrice as hard. ATTACK increases for you two.",
                100,
            ),
            "Flirt": ("You wink. Aaron wiggles out of range, blushing.", 40),
        },
    ),
    "undyne": dict(
        name="Undyne",
        hp=1500,
        atk=50,
        defense=20,
        boss=True,
        volleys=(2, 3),
        seq_len=(3, 4),
        kinds=["dodge", "blue", "orange"],
        intro="Undyne attacks!",
        flavor=[
            "Undyne points heroically towards the sky.",
            "Undyne flashes a menacing smile.",
            "Undyne holds her fist in front of her and shakes her head.",
            "Undyne thinks of her friends and pounds the ground with her fists.",
        ],
        acts={
            "Plead": (
                "You told Undyne you just want to be friends. She remembers someone...",
                25,
            ),
            "Challenge": (
                "You tell UNDYNE her attacks are too easy. She doesn't care.",
                25,
            ),
            "Fake attack": ("You pretend to swing at UNDYNE with all your might.", 20),
        },
        spare_txt="Undyne drops her spear, laughing. (NGAHHH!!). 'You're... annoying. Fine.'",
        die_txt="In the name of everybody's hopes and dreams... I WILL DEFEAT YOU SOMEDAY!",
        taunts=[
            (0.6, "Undyne: 'Is that really all you've got?!'"),
            (0.25, "Undyne: 'I'm not done yet!'"),
        ],
    ),
    # --Hotland--
    "vulkin": dict(
        name="Vulkin",
        hp=20,
        atk=25,
        defense=0,
        intro="Vulkin strolls in.",
        flavor=[
            "Vulkin parades around the room.",
            "Vulkin is making coffee in its crater.",
            "Vulkin is wiggling its weird rump.",
            "Vulkin makes a smoke hoop and jumps through it.",
            "Smells like a lava lamp.",
        ],
        acts={
            "Criticize": ("Vulkin stands in the corner.", 40),
            "Encourage": (
                "You tell Vulkin it's doing a great job. Its attacks become extreme...",
                70,
            ),
        },
    ),
    "pyrope": dict(
        name="Pyrope",
        hp=110,
        atk=29,
        defense=14,
        intro="Pyrope bounds towards you!",
        flavor=[
            "Pyrope is protected by its winsome smile.",
            "Pyrope is pretending to pull the fire alarm.",
            "Pyrope is chuckling through its teeth.",
            "Pyrope is pretending to be a candle.",
            "Smells like rope burn.",
        ],
        kinds=["dodge", "orange"],
        acts={
            "Invite": ("You invite Pyrope to hang out.", 60),
            "Heat": ("You crank up the thermostat. It's SOOOO hot!", 60),
        },
    ),
    "tsunderplane": dict(
        name="Tsunderplane",
        hp=80,
        atk=25,
        defense=26,
        intro="Tsunderplane gets in the way! Not on purpose or anything.",
        flavor=[
            "Tsunderplane looks over, then turns up its nose.",
            "Tsunderplane shakes its nose dimissively at you.",
            "Tsunderplane 'accidentally' bumps you with its wing.",
            "Tsunderplane gives you a condescending barrel roll.",
            "Smells like an airport perfume counter.",
        ],
        acts={
            "Fllirt": (
                "You tell Tsunderplane that you like its taste in movies and books.",
                70,
            ),
            "Approach": ("You get close to Tsunderplane. But not too close.", 20),
        },
    ),
    "mettaton": dict(
        name="Mettaton",
        hp=9999,
        atk=30,
        defense=255,
        boss=True,
        volleys=(2,3),
        seq_len=(3, 4),
        kinds=["dodge", "blue"],
        intro="A spotlight snaps on. 'LADIES AND GENTLEMONSTERS!' Mettaton rolls out.",
        flavor=["The quiz show continues.", "Mettaton."],
        acts={
            "Pose": ("You strike a pose. The audience loves it.", 30),
            "Applaud": ("You clap for him. Mettaton is touched.", 35),
            "Heckle": ("You boo. Mettaton gets angry, ratings drop.", 5),
        },
        spare_txt="I'LL BE ALRIGHT. KNOCK 'EM DEAD, DARLING. AND EVERYONE... THANK YOU. YOU'VE BEEN A GREAT AUDIENCE!",
        die_txt="I still got to perform for a human, didn't I? So, thank you, darling... You've been a great audience!",
        taunts=[(0.5, "Mettaton: 'The ratings! Keep the show going!")],
    ),
}


def make_enemy(key, player=None):
    # fresh copy of an enemy (dmg never carries over)
    return Enemy(key=key, **copy.deepcopy(ENEMY_DATA[key]))
