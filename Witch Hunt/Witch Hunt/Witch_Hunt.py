def start_game():
    print("Welcome to The Witch's Pursuit!")
    print("The year is 1692, and the village of Eldridge is gripped by fear and paranoia.")
    print("Rumors of witchcraft have spread, and it's your task to investigate.")
    print("Are you ready to begin?")

    choice = input("Type 'yes' to accept the task or 'no' to refuse: ").strip().lower()

    if choice == 'yes':
        chapter_one()
    elif choice == 'no':
        print("You decided not to get involved. The village continues to suffer from fear and suspicion.")
    else:
        print("Please choose a valid option.")
        start_game()

def chapter_one():
    print("\nYou are summoned by Magistrate Thornton to investigate the witchcraft accusations.")
    print("The magistrate provides you with a list of names and sends you out into the village.")
    print("Your first stop is the village inn.")

    choice = input("Do you want to (1) Interview the innkeeper, (2) Seek out the traveling merchant, or (3) Investigate the inn? ").strip()

    if choice == '1':
        interview_innkeeper()
    elif choice == '2':
        seek_merchant()
    elif choice == '3':
        investigate_inn()
    else:
        print("Please choose a valid option.")
        chapter_one()

def interview_innkeeper():
    print("\nThe innkeeper, Martha, tells you about a peculiar visitor who stayed last week.")
    print("She mentions that the visitor paid with strange coins and was in a hurry.")

    choice = input("Do you want to (1) Ask Martha more about the visitor, (2) Examine the strange coins, or (3) Leave and visit the merchant? ").strip()

    if choice == '1':
        print("Martha describes the visitor as a woman who seemed agitated and had a mysterious aura.")
        print("This could be a significant lead.")
        chapter_two()
    elif choice == '2':
        print("Martha no longer has the coins, but you note that this could be a clue for later.")
        chapter_two()
    elif choice == '3':
        seek_merchant()
    else:
        print("Please choose a valid option.")
        interview_innkeeper()

def seek_merchant():
    print("\nThe traveling merchant seems nervous when you approach.")
    print("He mentions a peculiar woman who paid with strange coins and left hastily.")

    choice = input("Do you want to (1) Ask the merchant more about the woman, (2) Examine the coins, or (3) Investigate further on your own? ").strip()

    if choice == '1':
        print("The merchant provides you with a description of the woman, which matches Martha's account.")
        print("You now have more information about the mysterious visitor.")
        chapter_two()
    elif choice == '2':
        print("The merchant does not have the coins anymore, but you note this detail.")
        chapter_two()
    elif choice == '3':
        print("You decide to explore other leads on your own.")
        chapter_two()
    else:
        print("Please choose a valid option.")
        seek_merchant()

def investigate_inn():
    print("\nYou search the inn for any evidence but find nothing unusual.")
    print("However, you decide to return to the merchant for more information.")

    seek_merchant()

def chapter_two():
    print("\nWith your new information, you need to decide your next course of action.")
    print("You have a description of the peculiar woman and know about the strange coins.")

    choice = input("Do you want to (1) Investigate the woman's whereabouts, (2) Look into the strange coins, or (3) Talk to other villagers? ").strip()

    if choice == '1':
        print("You investigate and find that the woman was seen in the forest, which leads to more clues.")
        print("You are getting closer to uncovering the truth.")
    elif choice == '2':
        print("You follow up on the coins and find that they are from a foreign land, possibly linked to dark magic.")
        print("This might be important for your investigation.")
    elif choice == '3':
        print("You talk to other villagers and gather more information about the witchcraft rumors.")
        print("Each conversation adds pieces to the puzzle.")
    else:
        print("Please choose a valid option.")
        chapter_two()

def main():
    start_game()

if __name__ == "__main__":
    main()`