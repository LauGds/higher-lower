# Choose two famous people randomly
import random
from game_data import data
from replit import clear
from art import logo
from art import vs

# Compare who has more followers
option_a = random.choice(data)
game = True
score = 0
print(logo)
while game:
  print(f"Compare A: {option_a['name']}, a {option_a['description']}, from {option_a['country']}")
  option_b = random.choice(data)
  print(vs)
  print(f"Against B: {option_b['name']}, a {option_b['description']}, from {option_b['country']}")
  user_choice = input("Who has more followers? Type 'A' or 'B': ")
  clear()
  # If user type correct answer, show the actual score
  if user_choice == 'A' and option_a['follower_count'] > option_b['follower_count']:
    score += 1
    print(logo)
    print(f"You're right! Current score: {score}")
    option_a = option_b
  elif user_choice == 'B' and option_a['follower_count'] < option_b['follower_count']:
    score += 1
    print(logo)
    print(f"You're right! Current score: {score}")
    option_a = option_b
  elif user_choice == 'A' and option_a['follower_count'] < option_b['follower_count']:
    game = False
    print(f"Sorry, that's wrong. Final score: {score}")
  elif user_choice == 'B' and option_a['follower_count'] > option_b['follower_count']:
    game = False
    print(f"Sorry, that's wrong. Final score: {score}")
