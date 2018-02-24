# This program is about Number Guess
# it is built on a pair of dice and asks the user to guess a number. Based on the user's guess, the program should determine a winner. If the user's guess is greater than the total value of the dice roll, they win! Otherwise, the computer wins.

# The program should do the following:
# Randomly roll a pair of dice
# Add the values of the roll
# Ask the user to guess a number
# Compare the user's guess to the total value
# Decide a winner (the user or the program)
# Inform the user who the winner is

# this gives random numbers.
from random import randint
# imports time into the program
from time import sleep
# here we are prompting the user for their guess
def get_user_guess():
# Text was wrapped since we need an integer because raw_input takes in variable and then stores them as strings
  user_guess = int(raw_input("Please, guess a number : "))
  return user_guess

def roll_dice(number_of_sides):
  # first role of the dice
  first_roll = randint(1,number_of_sides)
  # second role of the dice, since the user needs to roll 2 dices at ther same time
  second_roll = randint(1,number_of_sides)
  # the outcome should be 2 mutiply by the number of outcome, remember we have two dices
  max_val = number_of_sides * 2
  print("Your possible maximum is " + str(max_val))
  #sleep for one second.
  sleep(1)
  # calling the get function and assigning to a variable called user_guess
  user_guess = get_user_guess()
  # we cannot have the user possible output to be greater than the outcome of the dice. so we then the
  if user_guess > max_val:
    print " That is invalid, You cannot have your guess greater than the value of the dice "
  else:
    print("Rolling....")
    #sleep for 2 seconds
    sleep(2)
    #print the first roll using string formatting
    print "The first value is %d" % first_roll
    # the program is sleeping for 1 second.
    sleep(1)
    # print the second_roll
    print "The second value is  %d" % second_roll
    total_roll = first_roll + second_roll
    print "Result... %d" % total_roll
    sleep(1)
    if user_guess > total_roll:
        print ("You have won the game. ")
    else:
        return "You have lost the game."

roll_dice(6)


