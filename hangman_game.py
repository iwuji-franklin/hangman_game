import random
import diagrams
from Words import words
from secrets import choice

print(diagrams.logo)
# choosing a word from the list of words in the Word.py module
word = random.choice(words)
# creating hidden word out of the length of the word above
hidden = []
for x in word:
    hidden.append("_")
# we will be getting the extent of the hanging by using the remining_life as the index.
hanging_extent = list()
# must be equal to the length of your hangman diagram list [0:]
remining_life = 5
end_of_game = False
print("Total life is: ", remining_life+1)
print("Fill in the blanks with the correct letters...: _________")
while end_of_game == False:
    user_choice = input("Kindly, enter your chosen letter below:\n").lower()
    # Verifing the inserted letter
    while len(user_choice) != 1:
        user_choice = input("Kindly, enter your chosen letter below:\n").lower()
    # checking if inserted letter is in the "word to find"
    #if found, the user got it right
    if user_choice in word:
        # getting the index and letters of all the word to find
        for x,y in enumerate(word):
            # if a letter is equal to the inserted letter
            # use its value to replace the blank item in the hidden list
            # using a specified index of the letter in th word to find
            # but not so fast, check the logic below to pass the final test
            if y == user_choice:
                # then finetuning the program
                # checking if we have already have the inserted letter in our hidden before
                hidden[x]=y
                if user_choice in hidden:
                    print("You have choosen this letter before!!!")
                # this is where our final test lies, if it is a new letter
                # add it to our hidden list
                else:
                    print("Correct!!!")
    # then , if the inserted letter is not in word to find
    # get set to hang him
    else:
        
        hang_him = diagrams.hangman
        # using the remaining life to get the index of the extent of his hanging
        hanging_extent.append(hang_him[remining_life])
        remining_life -= 1
        print("Failed!!!")
        print(hanging_extent[-1])
        # checking if users life is equal to zero and printing another response
        if (remining_life+1) > 1:
            print("You now have: ",remining_life+1,"lives")
        elif (remining_life+1) == 1:
            print("You now have only: ",remining_life+1,"life")
        else:
            print("You have finally exhausted your life...")
    # breaking out of the loop if the hidden is equal to word
    # this is if the user finds all blank letter
    # This is the way we can be showcasing our hidden value like a string
    show_hidden = ""
    for x in hidden:
        show_hidden += x
    print("Fill in the blanks with the correct letters...: ",show_hidden)

    if show_hidden == word:
        print("YOU WIN!!!")
        # setting_end_of_game to True
        end_of_game = True
    # if "_" not in hidden:
        # end_of_game = True
    # if the users remining life is -1 stop the loop
    # because it will start from the last item of the hang_him to insert items to hanging extent
    if remining_life == -1:
        # setting_end_of_game to True
        print('YOU LOSE!!!')
        end_of_game = True

print("THE GAME HAS ENDED")