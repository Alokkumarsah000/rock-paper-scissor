
import random

rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")


paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

scissor = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

# paper win against rock
# scissor win against paper
# rock win against scissor


game_image = [rock,paper,scissor]
user_choose = int(input("what do you choose? Type 0 for rock, 1 for paper and 2 for scissor \n" ))
while user_choose >=3 or user_choose < 0 :
    user_choose = int(input("invalid choice, please choose again \n"))

print(game_image[user_choose])
print("computer_choose:")
computer_choose = random.randint(0,2)

print(game_image[computer_choose])

if user_choose == computer_choose:
    print("It's a draw")

elif user_choose == 0 and computer_choose == 2:
    print("you win")

elif computer_choose == 0 and user_choose == 2:
    print("you loose")

elif user_choose > computer_choose:
    print("you win")

elif computer_choose > user_choose:
    print("you loose")
                        





