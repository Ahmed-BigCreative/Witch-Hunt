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
sprint('"Recently,the dark apostle, Herbia, has been deemed as an enemy of the holy kingdoms."')
sleep(1)
sprint('"Disgustingly,her name is unfortunately very similar to mine"')
print("\n")
sprint("You flinch as her attitude immediately changes at the mention of this evil witch")
print("\n")
sleep(1)
sprint('"We, the ACTUAL holy ones cannot intervene, so we have called you over in order to vanquish her"')     
sprint("It seems this matter is of great importance to Miss Helia you think to yourself\n")

sprint('"Is Herbia really that bad?...I mean, I still havent really heard of what she has done"')


WillYouTakeOnThisMission = input('"Will you take on this mission Player? Yes or No "\n')
if WillYouTakeOnThisMission == 'Yes':
    sprint('"I must thank you hero, there will certainly be a multitiude of rewards and benefits for you after you complete your mission,... maybe even me.."')
elif WillYouTakeOnThisMission == 'No':
    sleep(1)
    sprint('"Then may death grasp your soul"')
    sprint('"Foolish Mortal....."ZWAP')
    print("fu23*&£YUR{@}{@y2")
    print(R"""
    ⣴⠀⣀⣤⣴⣶⣾⣿⣿⣿⣿⣿⣿⣷⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢾⣷⣿⣿⣿⣿⣿⠿⠟⠛⠉⠉⠉⠉⠉⠙⠳⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠘⢿⡏⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠸⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡴⠒⠒⠒⠒⢢⣤⠀⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀
⠀⠀⢿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠉⠀⠀⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀
⠀⠀⠘⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣷⣿⡆⠀⠀
⠀⠀⠀⢻⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀
⠀⠀⠀⠘⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣤⣤⣤⣄⣠⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀
⠀⠀⠀⠀⣿⣶⡄⠀⠀⠀⠀⠀⠀⠀⢀⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀
⠀⠀⠀⠀⠻⣿⣿⣄⠀⠀⠀⠀⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀
⠀⠀⠀⠀⠀⢹⡌⢻⣿⣦⣄⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡼⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀
⠀⠀⠀⠀⠀⠘⣧⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠁⢹⣿⡇⢿⣿⣿⣿⣿⣿⣿⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢹⣄⣀⣀⠈⠛⢻⣿⣿⣿⣿⡏⠀⠀⠀⣿⣿⠀⣿⣿⣿⣿⣿⣿⡇⠀⠀
⠀⠀⠀⠀⠀⠀⠈⣯⠉⠀⠀⠀⢸⣿⣿⣿⣿⣆⠀⠀⠀⢿⣿⡇⠸⣿⣿⣿⣿⣿⣿⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢹⡆⠀⠀⠀⢸⣿⣿⣿⣿⣿⣧⠀⠀⠘⣿⡇⠀⢹⣿⣿⣿⣿⣿⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⣷⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⡇⠀⠀⢹⣧⡀⠀⣿⣿⣿⣿⡿⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢹⡆⠀⠀⢸⣿⣿⣿⣿⣿⣿⣧⠀⠀⣿⣿⣷⣄⢹⣿⣿⣿⡇⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣷⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⡄⠀⢿⣿⢿⡻⢝⣿⣿⣿⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡆⠀⢸⣿⣿⣿⣿⣿⣿⣿⣷⠀⠐⠈⠁⠁⠀⣿⣿⣿⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣷⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⢸⣿⡟⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠘⣿⠃⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠏⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠿⠟⠛⠛⠿⠿⠿⠿⠿⣿⣿⣿⣿⠿⠿⠿⢿⠿⠟⠛⠛⠃
    """)
    sleep(2)
    print("beep")
    sprint("You have made the wrong choice")
    sprint("You have died..")
    sprint("You start to see, and witness a pool of darkness below you")
    sleep(1)
    sprint("Slowly, your senses return")
    sprint("And with it excruitiating pain")
    sprint("In the midst of agony, you feel")
    sprint("However you do not feel")
    sprint("You are a living being no longer, In the realm of the dead all being are equal")
    sprint("Before the king of the underworld and his messenger, the reaper, suffering is beauty")
    HowDoYouFeel = input("How do you feel\n")
    sprint("It does not matter, your feelings are not important")
    DoYouHarbourRegretOrVengeanceInYourHeart = input("Do you harbour regret or vengeance in your heart. Yes or No\n")
    if DoYouHarbourRegretOrVengeanceInYourHeart == 'Yes':
        sleep(2)
        sprint("Through the darkness of the abyss, an even darker aura emerges")
        sprint("Torrents of deathly mana rush through the space")
        sprint("A tear, rips through reality and finally,... a voice speaks to you")
        sprint('"We have heard your pleas,..Player"',PlayerName)
        sprint('"Your heart has the place for desire, it glows with hatred for the being who caused unjust"')
    

