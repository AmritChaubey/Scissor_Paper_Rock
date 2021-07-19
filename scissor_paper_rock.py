import random
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
possible_moves = [rock,paper,scissors]

user_input = input('Make a choice\n0 for rock\n1 for paper\n2 for scissors\n')
comp = random.randint(0,2)
if user_input[0].isalpha():
  print("you had one job\n input the number.")
elif user_input[0].isdigit():
  user = int(user_input)
  if ((user == 0) and (comp == 2))or((user == 1) and (comp == 0))or((user == 2) and (comp == 1)):
    print(possible_moves[user])
    print(f"computer choose:\n{possible_moves[comp]}")
    print("You Win")
  elif(user == comp):
    print(possible_moves[user])
    print(f"computer choose:\n{possible_moves[comp]}")
    print("it's a draw")
  elif(user > 2 or user < 0):
    print("it's invalid u dumby\n look at the options")
  else:
    print(possible_moves[user])
    print(f"computer choose:\n{possible_moves[comp]}")
    print("You Lose")
else:
  print("you had one job\n input the number.")
