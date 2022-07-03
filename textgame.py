answer_yes = ["Yes", "Y", "yes", "y"]
answer_no = ["No", "N", "no", "n"]

print("""
WELCOME! LET'S START THE ADVENTURE

You are going home in your car when you see a woman in dirty clothes running towards you and asking for a ride home.

Will you give her a ride home. (Yes / No)
""")
ans1 = input(">>")

if ans1 in answer_yes:
    print("\nAfter 5 minutes,you are stopped at a checkpoint and police asks you if you seen a suspicious woman. Will you say (Yes / No)\n")

    ans2 = input(">>")

    if ans2 in answer_yes:
        print("\nYou are an honest person. She was a murderer & You won the Game")

    elif ans2 in answer_no:
        print("\nYou helped a murderer. Now, go to Jail. GAME OVER")

    else:
        print("\nYou typed the wrong input. GOODBYE!")




















elif ans1 in answer_no:
    print("\nNow, She is trying to kill you. Will, you knock her down? (Yes / No)\n")

    ans3 = input(">>")

    if ans3 in answer_yes:
        print("\nCongrats! She was a murderer & You helped the police to catch her with your bravery.")

    elif ans3 in answer_no:
        print("\nSorry! You are dead. She was a murderer & She killed you. GAME OVER")

    else:
        print("\nYou typed the wrong input. GOODBYE!")


















else:
    print("\nYou typed the wrong input. GOODBYE!")
