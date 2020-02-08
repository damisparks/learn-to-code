# Basics of the project is for Game to have 3 or more levels and each level contains 4 or more blanks to fill in.
'''Beginning of the game : Immediately after running the program,
 user is prompted to select a difficulty level from easy / medium / hard
 Once a level is selected, game displays a fill-in-the-blank and a prompt to fill in the first blank.
 Game Play:When player guesses correctly, 
 new prompt shows with correct answer in the previous blank and a new prompt for the next blank
 When player guesses incorrectly, they are prompted to try again
 '''
# introducing the game to the user
print("Damilibs Game, ready...")
print("There are different levels in this game \nEasy! Medium!! Hard!!! \nChoose your level")
print("You can choose e or easy or easy for the easy part, m or medium for the medium part and h or hard for the hard"
      "part")

# sentence of the user
first_sentence = "__1__, capital __2__ of Portugal is a __3__ in the euruopean __4__."
second_sentence = "Udacity, is an __1__ __2__ platform based in the __3__ States at Silicon __4__."
third_sentence = "__1__ is a __2__ __3__ where you can find information you need about something.!! \nFacebook __4__ is used for chatting !!"

# answer that we want from the user
first_answer = ["lisbon", "city", "country", "union"]
second_answer = ["online", "learning", "united", "valley"]
third_answer = ["google", "search", "engine", "messenger"]


def get_difficult():
    """ 
    This function takes in the choice of the user and then picks up the quiz choice 
    for instance, if the user chooses the easy, the easy quiz will chosen and so for the other quiz 
    """     
    difficulty = ["easy","medium","hard"]
    while True:
        level = input('Choose a difficulty: (easy / medium / hard)\n').lower()
        if level in difficulty:
            print("You have chosen the \n" + level + " quiz chosen\n")
            if level == difficulty[0]:
                play_game(first_sentence,first_answer)
            elif level == difficulty[1]:
                play_game(second_sentence,second_answer)
            else:
                play_game(third_sentence,third_answer)
            break
        else:
            print("That is invalid")

# this function takes in the user sentence and answer from the first function and then loop through for the game play
def play_game(question_level,response_level):
    """ 
    This function helps with movement of the blanks to next one.
    For instance, during the while loop, there is an additon to the index and then the count 
    making it possible for the blank to move and then other activities in the fuctions can work
    """
    index = 0 
    count = 0   # used to move from one answer to the next one and it is checking that the answer is checked for the beginning of the answer set. 
    length_of_quiz = 4  # this is for the length of the quiz to avoid magic number 
    score = 9   # the inital score is 9, since we want the score to count downd when the user get the answer
    counting_score = 0  # the intial counting_score is 0
    while True:
        print(question_level + "\n")
        answer = input("What should be for this : __" + str(index + 1) + "__").lower()
        if answer in response_level:
            if answer in response_level[count]:
                question_level = question_level.replace('__' + str(index + 1) + '__', answer)
                index += 1
                count += 1 
                if index == length_of_quiz:
                    print(question_level + "\n")
                    print("Congratulation!!!")
                    break
        else:
            print(" Oops!!! Wrong Guess :) ")
            score -= 1
            if score > counting_score:  
                print('The number of attempt left is : ', score)
            if score == counting_score:
                print('You have no attempt left, Game over!!')
                break
get_difficult()