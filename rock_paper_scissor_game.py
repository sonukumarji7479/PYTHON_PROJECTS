import random

item_list = ["rock", "paper", "scissor"]

while True:
    user_choice = input("Enter your move (rock, paper, scissor) or 'quit' to exit: ").lower()
    
    if user_choice == "quit":
        print("Game exited. Thanks for playing!")
        break

    if user_choice not in item_list:
        print("Invalid choice! Please choose rock, paper, or scissor.")
        continue

    comp_choice = random.choice(item_list)
    print(f"User choice = {user_choice}, Computer choice = {comp_choice}")

    if user_choice == comp_choice:
        print("Both choices are same = Match tie")

    elif user_choice == "rock":
        if comp_choice == "paper":
            print("Paper covers rock = Computer wins")
        else:
            print("Rock smashes scissor = You win")

    elif user_choice == "paper":
        if comp_choice == "scissor":
            print("Scissor cuts paper = Computer wins")
        else:
            print("Paper covers rock = You win")

    elif user_choice == "scissor":
        if comp_choice == "paper":
            print("Scissor cuts paper = You win")
        else:
            print("Rock smashes scissor = Computer wins")

    print("\n--- Next Round ---\n")
