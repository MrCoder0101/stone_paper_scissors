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

game_images = [rock, paper, scissors]
game_count = int(input("How many time do you want to play?:"))
while True:
    if game_count > 0:
        computer_choice = random.randint(0, 2)
        user_choice = int(input("Which do you prefer ?\nType 0 for Rock,\nType 1 for Paper,\nType 2 for "
                                "Scissors.\nResponse:"))
        if user_choice > 2 or user_choice < 0:
            print("Invalid response,Try again please")
            continue
        else:
            if computer_choice == 2 and user_choice == 0:
                print(game_images[user_choice]+' '+game_images[computer_choice])
                print(computer_choice)
                print("you win")
            elif computer_choice == 0 and user_choice == 2:
                print(game_images[user_choice]+' '+game_images[computer_choice])
                print(computer_choice)
                print("computer win")
            elif computer_choice > user_choice:
                print(game_images[user_choice]+' '+game_images[computer_choice])
                print(computer_choice)
                print("computer win")
            elif computer_choice < user_choice:
                print(game_images[user_choice]+' '+game_images[computer_choice])
                print(computer_choice)
                print("you win")
            elif computer_choice == user_choice:
                print(game_images[user_choice]+' '+game_images[computer_choice])
                print(computer_choice)
                print("ıt is a draw")
    else:
        print("How you want ,Good Day")
        break
