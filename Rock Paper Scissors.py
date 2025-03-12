rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
art=(rock, paper, scissors)
import random
computer= random.randint(1,3)
person = int(input("1 for Rock, 2 For Paper, 3 for Scissors:\n"))
print("Computer chose\n"+ art[computer-1] )

if 0<person<4:
    print("You chose\n"+art[person-1])
else:
    print("Invalid Input")
    exit()

if computer==person: print("draw")
elif (person==1 and computer==3)or(person==2 and computer==1)or(person==3 and computer==2):
    print("You win")
else: print("You lose")
