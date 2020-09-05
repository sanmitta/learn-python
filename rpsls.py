# Rock-paper-scissors-lizard-Spock template

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

import random

def name_to_number(name):
    if name.lower() == 'rock':
        return 0
    elif name.lower() == 'spock':
        return 1
    elif name.lower() == 'paper':
        return 2
    elif name.lower() == 'lizard':
        return 3
    elif name.lower() == 'scissors':
        return 4
    else:
        print("invalid input")
        return False


#print(name_to_number("rock"))
#print(name_to_number("Spock"))
#print(name_to_number("saneev"))
   
    
    
def number_to_name(number):

    if number == 0:
        return 'rock'
    elif number == 1:
        return 'spock'
    elif number == 2:
        return 'paper'
    elif number == 3:
        return 'lizard'
    elif number == 4:
        return 'scissors'
    else:
        print("invalid number, don't know what happened")
        return False
    

def rpsls(player_choice):
    
    # print a blank line to separate consecutive games
    print("")

    # print out the message for the player's choice
    print("Player chooses "+ player_choice)
    

    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)

    # compute random guess for comp_number using random.randrange()
    
    comp_number = random.randrange(0,5)

    # convert comp_number to comp_choice using the function number_to_name()
    
    comp_choice = number_to_name(comp_number)
    
    # print out the message for computer's choice
    print("Computer chooses "+ comp_choice)

    # compute difference of comp_number and player_number modulo five
    
    diff_val = (comp_number - player_number) % 5
    

    # use if/elif/else to determine winner, print winner message
    if diff_val == 0:
        print("Player and computer tie!")
    elif diff_val <= 2:
        print("Player wins!")
    else:
        print("Computer wins!")

    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric

