"""
Juan Zamudio
CSCI051p
Assignment 01
1/21/18
This program asks someone a few questions and creates a greeting card for them.
"""
import string

name = input("What is your name?")

recipient = input("Who is this letter for?")

favAnimal = input("What is your favorite animal?")

favCity = input("Favorite city in the world?")

age = input("How old are you?")

agePlus = str(int(age) + 30)
ageDiv = str(int(age) / 3)

result = "Hi," + recipient + "!\n\n" \
         "I hope this letter finds you well. I have been thinking a lot about you\n and wanted to say how much I " \
         "appreciate you! Thank you for being you. I miss you.\n I hope one day we get to visit my favorite place" \
         " in the world together. You'd love " + favCity + " if you've never been!\n It is a remarkable place. Maybe " \
         "we can go to the zoo there and see the beautiful " + string.lower(favAnimal) + "s.\n They are so cute. " \
         "Let's be sure to see each other soon as we are only getting older!\n Soon I'll be " + str(age) + " moving " \
         "on " + agePlus + "! But, of course, you will always remain young in my mind, forever " + ageDiv + ".\n " \
         "Please write back soon and let me know how you are doing.\n\n" \
         "With much love,\n\n" \
         + string.upper(name)

print(result)

