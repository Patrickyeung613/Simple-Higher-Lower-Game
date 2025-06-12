import random
import art
from game_data import data

data_list = data

def check_list():
    if len(data_list) < 2:
        return 2
    
def compare():
    if check_list() == 2:
        return 2
    data_A = random.choice(data_list)
    print(f"Compare A: {data_A['name']}, {data_A['description']}, from {data_A['country']}.")
    data_list.remove(data_A)

    print(art.vs)

    data_B = random.choice(data_list)
    print(f"Compare B: {data_B['name']}, {data_B['description']}, from {data_B['country']}.")
    data_list.remove(data_B)

    choice = input("Who has more follower? Type 'A' or 'B':").upper()
    if (choice == "A" and data_A['follower_count'] > data_B['follower_count']) or (choice == "B" and data_B['follower_count'] > data_A['follower_count']):
        return 1
    else:
        return 0
    
def play_game(): 
    result = -1
    score = 0
    print(art.logo)

    while result != 0:
      result = compare()
      if result == 1:
          score += 1
          print("\n" * 20)
          print(art.logo)
          print(f"You are right! Current score: {score}")
      elif result == 2:
          print(f"No more data to compare, You win! Final score: {score}")
          return 
      else:
          print(f"Sorry, that's wrong. Final score: {score}")
          return


play_game()
