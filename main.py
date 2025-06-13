import random
import art
from game_data import data

data_list = data

def check_list():
    if len(data_list) == 0:
        return False
    
def compare(data_A):
    if check_list() == False:
        return 2
    print(f"Compare A: {data_A['name']}, {data_A['description']}, from {data_A['country']}.")

    print(art.vs)

    data_B = random.choice(data_list)
    print(f"Against B: {data_B['name']}, {data_B['description']}, from {data_B['country']}.")

    choice = input("Who has more follower? Type 'A' or 'B':").upper()
    if choice == "A" and (data_A['follower_count'] > data_B['follower_count'] or data_A['follower_count'] == data_B['follower_count']):
        try:
            data_list.remove(data_B)
        except ValueError:
            pass
        finally:
            return 1, data_B
    elif choice == "B" and (data_B['follower_count'] > data_A['follower_count'] or data_A['follower_count'] == data_B['follower_count']):
        try:
            data_list.remove(data_B)
        except ValueError:
            pass
        finally:
            return 1, data_B
    else:
        return 0, data_B
    
def play_game(): 
    result = -1
    score = 0
    print(art.logo)
    data_A = random.choice(data_list)
    data_list.remove(data_A)

    while result != 0:
      result, data_A = compare(data_A)
      if result == 1:
          score += 1
          print("\n" * 10)
          print(art.logo)
          print(f"You are right! Current score: {score}")
      elif result == 2:
          print(f"No more data to compare, You win! Final score: {score}")
          return 
      else:
          print(f"Sorry, that's wrong. Final score: {score}")
          return

play_game()
