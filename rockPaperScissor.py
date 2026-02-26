import random

options = ["rock","scissors","paper"]
userpoint = 0
comPoint = 0

while True :
    user = input("Enter (rock or paper or scissors) : ").lower()
    com_choice = random.choice(options)

    print(f"The computer's choice is {com_choice}")
    print(f"You choose {user}")

    if user not in options:
        print("Invalid choice")
        print("Enter rock or paper or scissors only!")
        continue
    if(user == com_choice):
        print("It's a tie")
    elif((user == "rock" and com_choice == "scissors") or
         (user == "paper" and com_choice == "rock") or
         (user == "scissors" and com_choice == "paper")):
        print("You Win")
        userpoint += 1
        comPoint = (comPoint - 1) if comPoint > 0 else 0
    else:
        print("You Lost")
        userpoint = userpoint - 1 if userpoint>0 else 0
        comPoint += 1
    want_to_play = input("Do you want to play again (yes or no) : ")
    if(want_to_play != "yes"):
        print("Exiting..")
        break;

print(f"computer points {comPoint}")
print(f"user points is {userpoint}")
