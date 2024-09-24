print(R""" 
         __________________ _______                               _       _________
|\     /|\__   __/\__   __/(  ____ \|\     /|  |\     /||\     /|( (    /|\__   __/
| )   ( |   ) (      ) (   | (    \/| )   ( |  | )   ( || )   ( ||  \  ( |   ) (   
| | _ | |   | |      | |   | |      | (___) |  | (___) || |   | ||   \ | |   | |   
| |( )| |   | |      | |   | |      |  ___  |  |  ___  || |   | || (\ \) |   | |   
| || || |   | |      | |   | |      | (   ) |  | (   ) || |   | || | \   |   | |   
| () () |___) (___   | |   | (____/\| )   ( |  | )   ( || (___) || )  \  |   | |   
(_______)\_______/   )_(   (_______/|/     \|  |/     \|(_______)|/    )_)   )_(   
""")

from time import sleep

import sys,time
from tkinter import N

def sprint(str):
   for c in str + '\n':
     sys.stdout.write(c)
     sys.stdout.flush()
     time.sleep(4./90)

sprint("You awaken...")
sleep(1)
sprint('"Where am I?" you look around you, but you stop arubtply when something catches your eyes')
sprint("\n")
sprint("A being of light draped in holy white clothes emerges before you")
sleep(1)
print(R""" 
   -=-
(\  _  /)
( \( )/ )
(       )
 `>   <'
 /     \  
 `-._.-'

 """)
sleep(2)
sprint("You watch in awe as she glides into the air, floating towards a runelike contstruct.")
sleep(2)
sprint('"Wh- Who are you?" you ask, confused with the situation')
print("\n")
sprint('"Me?" she says, "My name is Helia Young one, I have been tasked with leading you onto the right path for this new adventure of yours."\n')
PlayerName = input('"What is your name Player"\n')
print(PlayerName)
print("\n")
print('"',PlayerName,'huh, how peculiar"')
print("\n")
sprint('"You share the same name as him, but can you live up to his will? "')
sprint('"We shall witness your fate.."')
print("\n")

sprint("Suddenly she stops, as she lands onto the shrine, the only construct in the vast white space above the clouds, you can finally see it in its true beauty")
print("\n")
sprint("It appeared to be old, however its age did not cease its modernised look.")
sprint("The bricks looked strong, impregnable even, and radiated with a holy aura that threatened to erase any tresspassers.")
print("\n")
sprint("Somehow or someway, it seemed sentient, capable of discerning who was free to use its raw power or not.")
sleep(1)
sprint("Slowly its doors opened up to allow the dainty looking angel in")
sleep(1)
print("\n")
print(R"""
              )\          _._._._  _._._._           /(
                \`--.___,'=================`.___,--'/
                 \`--._.__                 __._,--'/
                   \  ,. l`~~~~~~~~~~~~~~~'l ,.  /
       __            \||(_)!_!_!_.-._!_!_!(_)||/            __
       \\`-.__        ||_|____!!_|;|_!!____|_||        __,-'//
        \\    `==---='-----------'='-----------`=---=='    //
        | `--.                                         ,--' |
         \  ,.`~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~',.  /
           \||  ____,-------._,-------._,-------.____  ||/
            ||\|___!`======="!`======="!`======="!___|/||
            || |---||--------||-| | |-!!--------||---| ||
  __O_____O_ll_lO_____O_____O|| |'|'| ||O_____O_____Ol_ll_O_____O__
  o H o o H o o H o o H o o |-----------| o o H o o H o o H o o H o
 ___H_____H_____H_____H____O =========== O____H_____H_____H_____H___
                          /|=============|\
()______()______()______() '==== +-+ ====' ()______()______()______()
||{_}{_}||{_}{_}||{_}{_}/| ===== |_| ===== |\{_}{_}||{_}{_}||{_}{_}||
||      ||      ||     / |==== s(   )s ====| \     ||      ||      ||
======================()  =================  ()======================
----------------------/| ------------------- |\----------------------
                     / |---------------------| \
-'--'--'           ()  '---------------------'  ()
                   /| ------------------------- |\    --'--'--'
       --'--'     / |---------------------------| \    '--'
                ()  |___________________________|  ()           '--'-
  --'-          /| _______________________________  |\
 --'           / |__________________________________| \
""")

sleep(1)
sprint('"By using the power of this holy shrine, the heavens allow to to grant you high rank abilities to aid you in your journey"') 
sleep(1)
sprint('"Which class intrests you the most young one"')
print("\n")
print("""
There are many classes, but these are the base ones:
Warrior
Archer
Mage
Alchemist
Rogue
Tamer
Dancer
Dragoon
""")
print("\n")
sprint('"These are all the base starting classes, after your class evolution you would be able to choose to evolve into a better version of your class for example:"')
sprint('"A Warrior would be able to become a berserker. Other than that, Summoner, Lich, Ranger, Assassain, Necromancer, Jester, Enchanter, Dark Mage and Wizard are all just some of your Class opportunities"')
print("\n")
PlayerChosenClass = input('"Which path will you choose"\n')
sleep(1)
print('"',PlayerChosenClass,'...? Very well then, I shall do as you wish"')
sprint('"Let us get on with the ritual"')
sleep(2)
print("\n")
sprint('"While we wait for the Shrine to finish processing its power, I must inform you of your mission"')
print("\n") 
sleep(1)
sprint('"Lately, a dark witch has ravaged the holy kingdoms."')
sleep(1)
sprint('"Disgustingly, her name is Herbia. Which is unfortunately very similar to mine"')
print("\n")
sprint("You flinch as her attitude immediately changes at the mention of this evil witch")
print("\n")
sprint('"We, ACTUAL holy ones cannot intervene, so we have called you over in order to vanquish her"')