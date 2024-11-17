from math import gamma

from art import logo, vs
from game_data import data
import random



def format_data(account):
    """Format account data for display"""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr} from {account_country}"

def check_answer(guess, a_followers, b_followers):
    """Checks if answer is correct"""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


print(logo)

# Initialise Var
score = 0
game_should_continue = True
# Generate first random choice
account_b = random.choice(data)

# game loop
while game_should_continue:
    # Swap accounts: make account B the next account A
    account_a = account_b
    account_b = random.choice(data)
    # Ensure the two accounts are not the same
    while account_a == account_b:
        account_b = random.choice(data)

    # Display the accounts to the player
    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    guess = input("Who has more followers? Type A or B?: ").lower()

    #clear scree
    print("\n" * 20)
    print(logo)

    #follower count for both
    account_a_followers = account_a["follower_count"]
    account_b_followers = account_b["follower_count"]

    #is correct?
    is_correct = check_answer(guess, account_a_followers, account_b_followers)

    if is_correct:
        score += 1
        print(f"You're right, current score: {score}")
    else:
        print(f"You're wrong, final score: {score}")
        game_should_continue = False
