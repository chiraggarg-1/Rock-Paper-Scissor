import random

user_input = int(input("User Please choose one from Rock(0),Paper(1) and Scissor(2)"))
if user_input == 0:
    print("you have Choose Rock")
elif user_input == 1:
    print("you have Choose Paper")
elif user_input == 2:
    print("you have choose Scissor")
else:
    print("Please select the valid input")

computer_choose = random.randint(0,2)
if computer_choose == 0:
    print("Computer Chooses Rock")
elif computer_choose == 1:
    print("Computer Chooses Paper")
elif computer_choose == 2:
    print("Computer Chooses Scissor")
else:
    print("INVALID")

if user_input > computer_choose and user_input-computer_choose != 2:
    print("YOU WON!!😉")
elif computer_choose > user_input and computer_choose-user_input != 2:
    print("YOU LOOSE!!😕")
elif  user_input<computer_choose and computer_choose-user_input == 2:
    print("YOU WINS!!🤩")
elif  user_input>computer_choose and user_input-computer_choose == 2:
    print("YOU LOOSE!!🥺")
elif computer_choose == user_input:
    print("DRAW!!🤪")
else:
    print("NO RESULT")
print("PLAY AGAIN!!🤡")


