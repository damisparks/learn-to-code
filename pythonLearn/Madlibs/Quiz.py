from time import sleep
from datetime import datetime

now = datetime.now()
# Here is the Code_Your_Own_Quiz Project by Udacity.
# Basics of the project is for Game to have 3 or more levels and each level contains 4 or more blanks to fill in.
'''Beginning of the game : Immediately after running the program, user is prompted to select a difficulty level from easy / medium / hard
Once a level is selected, game displays a fill-in-the-blank and a prompt to fill in the first blank.
Game Play:When player guesses correctly, new prompt shows with correct answer in the previous blank and a new prompt for the next blank
When player guesses incorrectly, they are prompted to try again
 '''

# introducing the game to the user
print("Damilibs Game, ready...")
print('%s/%s/%s'' %s:%s' % (now.month, now.day, now.year, now.hour, now.minute))
sleep(1)
print("There are different levels in this game \nEasy! Medium!! Hard!!! \nChoose your level")
print("You can choose e or easy or easy for the easy part, m or medium for the medium part and h or hard for the hard"
      "part")

# I decided to comment it out because i may still use it but still thinking about how i am going to incorporate it into the program.
'''
# here the part of speech
words_in_silent = ["Adjective1", "Verb1", "Noun1", "Noun2", "Noun3", "Noun4", "Noun5", "Noun6 "]
'''

# Here is the lyric for the Silent Night Song
# THIS IS THE FIRST QUIZ OF THE PROGRAM
silent_Night_Template = "%s %s \n Holy %s\n All %s calm \n All %s bright" \
                        "\nRound yon %s \n Mother and child \nHoly infant so tender and mild" \
                        "\n%s in heavenly peace\n%s in heavenly peace\n%s %s" \
                        "Holy %s \n Shepeards pray at the sight\nGlory streams from heaven afar" \
                        "Heavenly ? sing hallelujah\nChrist the Savior %s born\nChrist the Savior %s born" \
                        "%s %s \n Holy %s \n All %s calm \n And all %s bright \n Round yon %s" \
                        "Mother and child \n Holy infant so tender and mild \n %s in heavenly peace \n %s in heavenly peace" \
                        "%s %s \n Holy %s \n %s in heavenly peace"

# Answer to the Silent Template
adjective1_answer = "Silent"
noun1_answer = "Night"
verb1_answer = "is"
noun2_answer = "Virgin"
noun3_answer =  "Sleep"
noun4_answer = "Son"
noun5_answer = "Light"
noun6_answer = "Love"

# Joy to the world lyrics 
Joy_to_the_world = "Joy to the %s, the Lord is come! \n Let %s receive her King; \nLet every heart %s Him room,\n " \
"And Heaven and nature %s,\nAnd Heaven and nature %s ,\nAnd Heaven, and Heaven, and nature %s.\n Joy to the %s , the %s reigns!" \
"\n Let men their %s employ; \nWhile fields and %s, rocks, hills and plains" \
"Repeat the sounding joy, \nRepeat the sounding joy,\n%s , %s , the sounding joy. \n%s more let sins and sorrows grow," \
"\nNor thorns infest the ground;\n%s comes to make His blessings flow\n Far as the curse is %s , \nFar as the curse is %s ,\n" \
"Far as, far as, the curse is %s .\n\nHe rules the %s with truth and grace,\nAnd makes the %s prove \n" \
"The glories of His righteousness, \nAnd wonders of His %s , \nAnd wonders of His %s ,\nAnd wonders, wonders, of His %s."


# Filling JTTW with this : this is for the medium level 
planet_with_civilization = "world"  # position 1, 7, 18  on the lyric 
third_planet = "earth"  # position 2
to_get_ready = "prepare"    # position 3
to_produce_vocals = "sing"  # position 4, 5, 6 
savior_input = "savior" # position 8
song_input = "song" # position 9,
flood_input = "flood"   # position 10
repeat_input = "repeat" # position 11, 12
no_input = "no" # position 13
he_input = "he" # postion 14
found_input = "found"   # position 15, 16, 17 
nation_input = "nations"    # positon 19,
love_input = "love" # position 20, 21, 22


# WHAT LEVEL YOU CHOOSE IS TAKEN HERE

def game_level():
    #user_input = input("Please choose game level :")
    # here are the options we have.
    easy_option = ["e", "easy"]
    medium_option = ["m", "medium"]
    hard_option = ["h", "hard"]

    while True:
        user_input = input("Please choose game level :")
        if user_input in easy_option:
            easy_level()
            medium_level()
            hard_level()
            break
        elif user_input in medium_option:
            medium_level()
            easy_level()
            hard_level()
            break
        elif user_input in hard_option:
            hard_level()
            easy_level()
            medium_level()
            break
        else:
            print("Invalid option")
            continue


# FIRST LEVEL OF THE QUIZ PROGRAM
def easy_level():
    print("NAME : Silent Night ")  # title of the the first level mad_libs generator
    while True: 
        user_adjective = input(" When there is no noise ?: ")  # Silent
        if user_adjective != adjective1_answer:
            continue
        if user_adjective in adjective1_answer: 
            break
    print("Here is your first word which is : " + adjective1_answer)

    while True:
        user_first_noun = input("The time from dusk to dawn when no light is visible - NOUN :")  # NIGHT
        if user_first_noun != noun1_answer:
            continue
        if user_first_noun == noun1_answer:
            break
    print("Yes it is " + noun1_answer)

    while True:
        
        user_second_noun = input("A person who has never had sex - NOUN : ")  # Virgin
        if user_second_noun == noun2_answer:
            break
        if user_second_noun != noun2_answer:
            continue 
    print("Yes" + noun2_answer + "Mary!!! Mother of Jesus.")

    while True:
        user_verb = input("3rd Person singular present of the verb -BE- ")  # Answer = is
        if user_verb == verb1_answer:
            break
        if user_verb != verb1_answer:
            continue
    print(verb1_answer + " 3rd person present of the verb to be ? Do you know ?? ")

    while True:
        
        user_third_noun = input("To take rest, afforded by a suspension of voluntarily bodily function - NOUN : ")  # Sleep
        if user_third_noun == noun3_answer:
            break
        if user_third_noun != noun3_answer:
            continue 
    print("Everyone likes to " + noun3_answer)

    while True:
        user_forth_noun = input("Male child of a parent is called ? - NOUN :")  # Son
        if user_forth_noun == noun4_answer:
            break 
        if user_forth_noun != noun4_answer:
            continue 
    print("Jesus is the "+ noun4_answer + " of God!! I am saved ")

    while True :
        user_fifth_noun = input("What is the opposite of darkness ? ")  #Light 
        if user_fifth_noun == noun5_answer:
            break 
        if user_fifth_noun != noun5_answer:
            continue
    print(noun5_answer + "!!!. That was a nice one")

    while True :
        user_sixth_noun = input("Uncondition affection towards something or someone? ")  #Love
        if user_sixth_noun == noun6_answer:
            break 
        if user_sixth_noun != noun6_answer:
            continue
    print(noun6_answer + "!!!. That was a nice one")

    sleep(2)
    print("Thinking about it.....")

    print (silent_Night_Template % (adjective1_answer,noun1_answer, noun1_answer, verb1_answer, verb1_answer,
    noun2_answer,
    noun3_answer, noun3_answer, adjective1_answer,noun1_answer, 
    noun1_answer,
    verb1_answer, verb1_answer, 
    adjective1_answer, noun1_answer, noun1_answer, verb1_answer, verb1_answer, noun2_answer,
    noun3_answer, noun3_answer,
    adjective1_answer, noun1_answer, noun1_answer, noun3_answer))

def medium_level():
    print("Loading.......")
    sleep(2)
    print("This is the medium level so you would not find it that easy like the first one ")

    while True: 
        world = input("The planet where all life live upon, including human civilization. ? " ) # world 
        if world == planet_with_civilization:
            break
        if world != planet_with_civilization:
            continue
    print("The" + planet_with_civilization + "is beautiful")

    while True: 
        earth = input("third planet on the universe") # earth  
        if earth == third_planet: 
            break
        if earth != third_planet:
            continue
    print(" Lets save the" + earth + "from global warming !!!")

    while True:
        prepare = input("To get ready for something, for example like an exam that is upcoming")    # prepare
        if prepare == to_get_ready:
            break
        if prepare != to_get_ready:
            continue
    print("The quiz is still cooking....")

    while True:
        sing = input("To vocalize , think of a verb ? ")    #sing 
        if sing == to_produce_vocals:
            break
        if sing != to_produce_vocals:
            continue
    print("Soon the carol will be ready for singing.. \n for now keep putting the pieces together ")

    while True: 
        savior = input(" Someone who saves is called what ? ")  #savior
        if savior == savior_input:
            break
        if savior == savior_input:
            continue
    print("Jesus is the " + savior_input)

    while True: 
        song = input("what are do you sing, think of a noun ")  # song 
        if song == song_input:
            break
        if song != song_input:
            continue
    print(" I love Rihanna "+ song_input+".")

    while True:
        flood = input("overflow of water that submerges land that is usually dry. ")    # flood 
        if flood == flood_input:
            break 
        if flood != flood_input:
            continue
    print(" Condolences goes to those affected by the flood in the USA ")

    while True: 
        repeat = input(" when you the same thing all over again like the python loop does it ? ")   # repeat 
        if repeat == repeat_input:
            break 
        if repeat != repeat_input:
            continue
    print(" I love loops but they could be complicated !")

    while True:
        no = input(" If it is not a Yes then it is a what ? ")  # no 
        if no == no_input:
            break
        if no != no_input:
            continue
    print(" Know when to say NO and when to say Yes ")

    while True:
        he = input(" male!! first person pronoun ") # he 
        if he == he_input:
            break 
        if he != he_input:
            continue
    print(he_input)

    while True:
        found = input("Past tense of the verb, Find is what ?") #found 
        if found == found_input:
            break 
        if found != found_input:
            continue
    print(" Lost and found, Careless owner ")

    while True: 
        nations = input(" what is the plural of the nation ? ") #nations 
        if nations == nation_input:
            break 
        if nations != nation_input:
            continue
    print(" I love the United Nations ")

    while True:
        love = input(" Uncondtional affections towards to something or someone is called ? ")   #love 
        if love == love_input:
            break
        if love != love_input:
            continue
    print(" Love is a beautiful thing !!!")

    print(Joy_to_the_world % (planet_with_civilization, third_planet, to_get_ready,
    to_produce_vocals, to_produce_vocals, to_produce_vocals, planet_with_civilization, savior_input,
    song_input, flood_input,
    repeat_input, repeat_input, no_input,
    he_input, found_input, found_input,
    found_input, planet_with_civilization, nation_input,
    love_input, love_input, love_input))    

def hard_level():
    print(" THis is the most difficult of them all if you pass, i owe you a chocolate ")

game_level()
#define a function that is going to play the game. 
#   def start_gmae():
