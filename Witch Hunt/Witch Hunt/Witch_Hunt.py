﻿print(R""" 
         __________________ _______                               _       _________
|\     /|\__   __/\__   __/(  ____ \|\     /|  |\     /||\     /|( (    /|\__   __/
| )   ( |   ) (      ) (   | (    \/| )   ( |  | )   ( || )   ( ||  \  ( |   ) (   
| | _ | |   | |      | |   | |      | (___) |  | (___) || |   | ||   \ | |   | |   
| |( )| |   | |      | |   | |      |  ___  |  |  ___  || |   | || (\ \) |   | |   
| || || |   | |      | |   | |      | (   ) |  | (   ) || |   | || | \   |   | |   
| () () |___) (___   | |   | (____/\| )   ( |  | )   ( || (___) || )  \  |   | |   
(_______)\_______/   )_(   (_______/|/     \|  |/     \|(_______)|/    )_)   )_(   
""")

from ctypes.wintypes import ULONG
from time import sleep


skip = False
import sys,time
from tkinter import N

def sprint(str):
   for c in str + '\n':
     sys.stdout.write(c)
     sys.stdout.flush()
     time.sleep(1./90)

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
PlayerChosenClass = input('"Which path will you choose"\n') # useless inout since shrine will fail anyways
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
sprint('"We, the ACTUAL holy ones cannot intervene, so we have called for you in order to vanquish her"')     
sprint("'It seems this matter is of great importance to Miss Helia you think to yourself'\n")

IsHerbiaReallyThatBad = input(""" 
What would you like to responde with
1 for "Do i really have to??...I mean, I dont know what she has done and this isnt even my own world"
2 for "What has she done to recieve that treatment"
3 for "I understand"
                             \n""") #makes your choice of pathway 1 or 2
if IsHerbiaReallyThatBad == '1': # ur dead (become stuffed doll)
    sprint('"You dare disrespect the heavens wishes like this?"')
    sleep(1)
    sprint('"Foolish mortal, I shall erase you before you decide to taint the air with your blasphemous prescence"')
    print("\n")
    print("You feel her powering up")
    sleep(1)
    sprint('"No wait, I didnt mean to disrespect you like that" you plead,')
    sleep(1)
    print("but it is already too late")
    print("\n")
    sleep(2)
    sprint("You wake up.. but you are stiff")
    sleep(1)
    sprint("You are stuck, and paralysed.... as a doll made out of a living human soul")
    sleep(1)
    sprint("You shall live for the rest of existence as so,... ")
    sleep(1)
    sprint("and not even the udnerworld can save you")
    print("\n")
    print("\n")
    sleep(2)
    print("You have made the wrong choice.")
    sleep(2)
    sprint("Before you embark on your long journey of silence, degradation, silence, boredom, silence, paralysation and silence you lament yourself")
    sleep(1)
    sprint('"Ah, I wish I had made the right decisions"')
    sleep(2)
    print("\n")
    print("You are a failure.")
    sleep(1)
    sprint("An entity that can literally one tap  you expressed her hate on her opps however you still decide to question her")
    sleep(1)
    sprint("you are a being of ignorance, one that needed to be removed in order for this world to progress")
    sleep(3)
    print("\n")
    print("\n")
    print("\n")
    sprint("Intelligence is chasing you... however you have always been faster")
    sleep(2)
    sprint("better luck next time,.. dumbass")
    exit()
elif IsHerbiaReallyThatBad == '2': # pathway 1
    sprint("The angel glares at you")
    IsHerbiaReallyThatBadContinuation = input ("""
    1 for "Sorry if i offended you, I am just curious Miss"
    2 for "So,.. are you going to answer"
    \n""")
    if IsHerbiaReallyThatBadContinuation == '1':
        sleep(1)
        sprint('"It is fine" the angel remarks')
        sleep(1)
        sprint('"She spreads chaos and terror across the realm"')
        sleep(1)
        print("\n")
        sprint('"And worst of all, she dares to rival us higher beings,"')
        sleep(1)
        sprint("'That sounds kind of petty', you think to yourself")
        sleep(1)
        sprint('"That you for informing me" you reply')
    
    
    elif IsHerbiaReallyThatBadContinuation == '2': # u die
        sleep(1)
        sprint('"How arrogant"')
        sleep(1)
        sprint('"A mere human, with not even an ounce of power in his hands"')
        sleep(1)
        sprint('"DARES TO RESPOND IN SUCH ARROGANCE TO ME?"')
        sleep(1)
        sprint('"A being of such an opulence of stupidity will not make it far regardless....Natural selection would have taken you down anyways"')
        sleep(1)
        sprint('"Your stupidity has lead to this"')
        sleep(3)
        print("\n")
        print("\n")
        print("You have made the wrong choice.")
        sleep(2)
        print("\n")
        print("You are a failure.")
        sleep(1)
        sprint("You would respond to an angel with such arrogance and remarks?, It seems some of us have yet to evolve. ")
        sleep(1)
        sprint("Stupidity has taken ahold of you. If you had been taught some manners maybe you would have survived today.")
        sleep(3)
        print("\n")
        print("\n")
        print("\n")
        sprint("Intelligence is chasing you... however you have always been faster")
        sleep(2)
        sprint("better luck next time,... rude ahh")
        exit()
elif IsHerbiaReallyThatBad == '3':
    sprint('"good"')
    sleep(1)



print("\n")
print("\n")
sprint("The conversation ceases, however you start to think")
sleep(1)
sprint("As you do, you feel a certain aura enveloping your surroudings")
sleep(1)
sprint("It seemed as if someone was there...however, there was no one")
sleep(1)
sprint('"Young one...Not everything is as it seems"')
sleep(1)
sprint('"Who are you"you whisper back in fear as wicked energy surrounds you')
sprint('"And where is miss Helia"')
sleep(1)
print("\n")
sprint('"We are seperated for a while. Player, she is tricking you, do not fall for her manipulative poisonous words coated in honey.."the unknown voice says')
WouldYouLikeToFollowMeInstead = input ("""
"Would you like to follow me instead"
1 for "yes"
2 for "Who are you... and why do you want "
3 for "no"
""")
if WouldYouLikeToFollowMeInstead == '1'or "yes".lower() :
    sprint('"ugh" she says')
    sprint("...\n")
    sprint("so you're one of those huh... disgusting")
    sprint('"what did i do?" you respond confused\n')
    sleep(1)
    sprint('"Your kind of people, switching sides with one sentence..."')
    sprint('"I cannot take in traitors, for you will betray me in the same way you have just betrayed that filthy angel"')
    sprint('"No variables must be left alive... good riddance"')
    sleep(3)
    print("\n")
    print("\n")
    print("You have made the wrong choice.")
    sleep(2)
    print("\n")
    print("You are simply stupid.")
    sleep(1)
    sprint("Really switched sides faster than michael jackson huh?")
    sleep(1)
    sprint("you flithy snake, someone who backstabs others every chance they get should be removed anyways.")
    sprint('"good riddance" indeed')
    sleep(3)
    print("\n")
    print("\n")
    print("\n")
    sprint("Intelligence is chasing you... however you have always been faster")
    sleep(2)
    sprint("better luck next time,... traitor..")
    exit()
elif WouldYouLikeToFollowMeInstead == '2':
    sprint('"I am the great witch Herbia, ')
    sprint('"')

elif WouldYouLikeToFollowMeInstead == '3':
    sprint('"You refuse???...I guess i cant force you" she says')
    sleep(1)
    sprint('"Very well then"')
    sprint(R'"I shall let you go... to HELL 😈"')
    sleep(1)
    sprint('"No variables must be left.. so you shall not be allowed to exist"')
    



    WillYouTakeOnThisMission = input('"Will you formally take on this mission Player? Yes or No "\n') #decides pathway 1 or 3
    if WillYouTakeOnThisMission == 'Yes': #you will go on pathway 1
        sprint('"I must thank you hero, there will certainly be a multitiude of rewards and benefits for you after you complete your mission,... maybe even me.."')
    elif WillYouTakeOnThisMission == 'No': #test your luck in pathway 3
        sleep(1)
        sprint('"Then may death grasp your soul"')
        sleep(1)
        sprint('"Foolish Mortal....."ZWAP')
        print("fu23*&£YUR{@}{@y2")
        sleep(1)
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
        print("beep") # now in underworld 
        sprint("You have made the wrong choice")
        sprint("You have died..")
        sprint("You start to see, and witness a pool of darkness below you")
        sleep(1)
        sprint("Slowly, your senses return")
        sprint("And with it excruitiating pain")
        sleep(2)
        sprint("In the midst of agony, you feel")
        sprint("However you do not feel")
        sleep(1)
        sprint("You are a living being no longer, In the realm of the dead all beings are equal")
        sleep(1)
        sprint("Before the king of the underworld and his messenger, the reaper, suffering is beauty")
        sleep(1)
        HowDoYouFeel = input("How do you feel\n") # useless input
        sleep(2)
        sprint("It does not matter, your feelings are not important")
        DoYouHarbourRegretOrVengeanceInYourHeart = input("Do you harbour regret or vengeance in your heart. Yes or No\n") 
        if DoYouHarbourRegretOrVengeanceInYourHeart == 'Yes': # MAIN SCANERIO 3 you said you have regrets when underworld ruler asked (will lead you to pathway 3)
            sleep(2)
            sprint("Through the darkness of the abyss, an even darker aura emerges")
            sleep(1)
            sprint("Torrents of deathly mana rush through the space")
            sprint("A tear, rips through reality and finally,... a voice speaks to you")
            sleep(1)
            sprint('"We have heard your pleas,..Player"',PlayerName)
            sprint('"Your heart has the place for desire, it glows with hatred for the being who caused unjust"')
            sleep(1)
            print("\n")
            print("\n")
            print("Pathway 'Three' unlocked")
        elif DoYouHarbourRegretOrVengeanceInYourHeart == 'No': #you said you have no regrets when underworld ruler asked (will kill you)
            sleep(2)
            print("You have made the wrong choice.")
            sleep(1)
            sprint('"Return.."')
            print("\n")
            sprint("You feel yourself losing something")
            sleep(1)
            sprint("Something deep inside of you,... Something..profound")
            sleep(1)
            sprint("A trail of essense exits your consciousness")
            sleep(1)
            sprint("In your final moments of sentience, you come to a realisation")
            sleep(1)
            sprint('"Ah, I wish I had made the right decisions"')
            sleep(2)
            print("\n")
            print("You are a failure.")
            sprint("You have been given a chance after the next, however your ignorance continues to shine")
            sleep(3)
            print("\n")
            print("\n")
            print("\n")
            sprint("Intelligence is chasing you... however you have always been faster")
            sleep(2)
            sprint("better luck next time, if there is one...")
            exit()
            #dead from pathway 3 after saying u have no regrets

    

