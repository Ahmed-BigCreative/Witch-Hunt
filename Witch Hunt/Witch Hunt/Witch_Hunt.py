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
print(""" 
   -=-
(\  _  /)
( \( )/ )
(       )
 `>   <'
 /     \  
 `-._.-'

 """)
sprint("You watch in awe as she glides into the air, floating towards a runelike contstruct.")
sleep(2)
sprint('"Wh- Who are you?" you ask, confused with the situation')

sprint('"Me?" she says, "My name is Helia Young one, I have been tasked with leading you onto the right path for this new adventure of yours."\n')
PlayerName = input('"What is your name Player"\n')
print(PlayerName)

print('"',PlayerName,'huh, how peculiar"')
sprint('"You share the same name as him, but can you live up to his will? We shall witness your fate.."')

sprint("Suddenly she stops, as she lands onto the shrine, the only construct in the vast white space above the clouds, you can finally see it in its true beauty")

sprint("It appeared to be old, however its age did not cease its modernised look.")
sprint("The bricks looked strong, impregnable even, and radiated with a holy aura that threatened to erase any tresspassers.")

sprint("Somehow or someway, it seemed sentient, capable of discerning who was free to use its raw power or not.")
sleep(1)
sprint("Slowly its doors opened up to allow the dainty looking angle in")
print("""
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

sprint('"By using the power of thine shrine, the heavens allow to to grant you Hero rank abilities to aid you in your journey"') 







