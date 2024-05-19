import random

def play():
    print("Choose: 'r' for Rock, 'p' for Paper, 's' for Scissors")
    move = ['r', 'p', 's']
    computer = random.choice(move)
    user = input("Enter your choice: ")
    user = user.lower()

    print(f"User choice : {user}")
    print(f"Computer choice : {computer}")
    
    if user not in move:
        print("Invalid Choice")

    if computer == user:
        print("Its a Draw")

    if user == 'r':
        if computer == 'p':
            print("You Lose!")
        if computer == 's':
            print("You Win!")
    if user == 'p':
        if computer == 's':
            print("You Lose!")
        if computer == 'r':
            print("You Win!")
    if user == 's':
        if computer == 'r':
            print("You Lose!")
        if computer == 'p':
            print("You Win!")
            
choose = input("Wanna Play rock, paper, scissors [Y/n]: \n ") 
choose = choose.lower()

while choose == 'y':
    play()
    choose = input("Play Again [Y/n]: \n ") 
    choose = choose.lower()
    if choose == 'n':
        print("Bye bye!!")
        break