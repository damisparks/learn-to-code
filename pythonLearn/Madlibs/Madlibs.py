# The Project is about Mab libs.
# Mad Libs consist of a book that has a short story on each page with many key words replaced with blanks.
# Beneath each blank is specified a lexical or other category, such as "noun", "verb", "place", or "part of the body".
# One player asks the other players, in turn, to contribute some word for the specified type for each blank, but without revealing the context for that word.
#  Finally, the completed story is read aloud. The result is usually comic, surreal and somewhat nonsensical.

print("Dear user, Mab Libs has started")
# input the name of the user
character_name = input("Input your name please! : ")
# the user should input 3 adjectives of different choices
character_adjective = input("Input 3 adjectives separately : ")
adjective1, adjective2, adjective3 = character_adjective.split()
# the user should input 3 verbs of different choices
character_verbs = input("Please type in 3 verbs with spaces to split them : ")
verb1, verb2, verb3 = character_verbs.split()
# please input 4 nouns of your choice
character_noun = input("Please input 4 nouns of your choice  separately:")
noun1, noun2, noun3, noun4 = character_noun.split()
# input an animal
character_animal = input("Please input an animal: ")
# input a type of food
character_food = input("Please input your food: ")
# Input a fruit
character_fruit = input("Please input a fruit: ")
# Input a number
character_number = int(input("Please input a number: "))
# Input a superhero name you like
character_hero = input("Please input a superhero name: ")
# Input a country
character_country = input("Please input a country: ")
# Input a dessert
character_dessert = input("Please input your dessert: ")
# input a year
character_year = int(input("Please input your year: "))

# The template for the story
STORY = "This morning I woke up and felt %s because %s was going to finally %s over the big %s %s. " \
        "On the other side of the %s were many %ss protesting to keep %s in stores. " \
        "The crowd began to %s to the rhythm of the %s, which made all of the %ss very %s. %s tried to %s into the sewers and found %s rats." \
        " Needing help, %s quickly called %s. %s appeared and saved %s by flying to %s and dropping %s into a puddle of %s. %s then fell asleep and woke up in the year %s, in a world where %ss ruled the world."

print(STORY % (adjective1, character_name,  verb1, adjective2, noun1, noun2, character_adjective,
               character_food, verb2, noun3, character_fruit, adjective3, character_name,
               verb3, character_number, character_name, character_hero, character_hero, character_name, character_country,
               character_name, character_dessert, character_name, character_year, noun4))
