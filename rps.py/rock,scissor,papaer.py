import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK  = 1
    PAPPER = 2
    SCISSORS = 3


print("")
playerchoice =input("Enter ....\n1 for Rock, \n2 for Paper or \n3 fpr Scissors:\n\n")

player = int(playerchoice)#makes sure that the input is integer


if player < 1 or player > 3:
    sys.exit("You enter unvalid key. So, Please enter 1, 2 or 3.")

computerchoice =random.choice("123") #make the computer to choose random number 1 2 or 3

computer =int(computerchoice)

print("")
print("You choose " + str(RPS(player)).replace('RPS.', '') +".")
print("Computer choose " + str(RPS(computer)).replace('RPS.', '') + '.')
print("")

if player ==1 and computer==3:
    print("🎉🎉🎉You win!")
elif  player ==2 and computer==1:
    print("🎉🎉🎉You win!")
elif player ==3 and computer==2:
    print("🎉🎉🎉You win!")
elif player==computer:
    print("😒😒😒Tie Game!")
else:
    print("😡😡😡Computer wins!")    