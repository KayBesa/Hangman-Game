# Hangman.py
# Authors: Beamlake Fikadu & Kasonde Besa
# Date: June 24th, 2021

import random
import turtle
from turtle import Turtle

# opens text file and chooses word
def chooseWord(level):
    # Ask for difficulty level
    if level == 1:
        levelFile = "fourLetterWords.txt"
    elif level == 2:
        levelFile = "sixLetterWords.txt"
    elif level == 3:
        levelFile = "eightLetterWords.txt"
    elif level == 4:
        levelFile = "tenLetterWords.txt"
    WORDS = open (levelFile, "r")
    list_of_words = WORDS.readlines()
    theWord = list_of_words[random.randint(0,len(list_of_words))]
    theWord = theWord.lower()
    theWord = theWord.strip()
    return theWord

# Creates turtle interface
def createTurtle():
    # Create our Turtle
    bob = Turtle()
    return bob

# Updates the hagman on the turtle gui
def updateTurtle(HangmanParts,myHangman):
    bob = myHangman
    A=120   #length of base
    B=200   #height upwards
    C = 120
    D = 40
    E = 20  #radius of circle
    Neck = 20
    Arms = 20
    Body = 40
    if HangmanParts == 9:
        bob.forward(A) # A
    elif HangmanParts == 8:
        bob.left(180)
        bob.forward(A/2) # A
        bob.right(90)
        bob.forward(B) # B
    elif HangmanParts == 7:
        bob.left(90)
        bob.forward(C) # C
    elif HangmanParts == 6:
        bob.left(90)
        bob.forward(D) # D
    elif HangmanParts == 5:
        bob.right(90)  # may or may not be necessary
        bob.circle(E) # E
        bob.left(90)
        bob.penup()
        bob.forward(E*2) # E
        bob.pendown()
    elif HangmanParts == 4:
        bob.forward(Neck) # Neck
        bob.right(45)
        bob.forward(Arms) # Arms
        bob.left(180)
        bob.forward(Arms) # Arms
    elif HangmanParts == 3:
        bob.right(90)
        bob.forward(Arms) # Arms
        bob.right(180)
        bob.forward(Arms) # Arms
        bob.left(135)
    elif HangmanParts == 2:
        bob.forward(Body) # Body
        bob.right(45)
        bob.forward(Arms) # Arms
        bob.left(180)
        bob.forward(Arms) # Arms
    elif HangmanParts == 1:
        bob.right(90)
        bob.forward(Arms) # Arms

# adds the correct guess onto all its positions
def replace(blankspaces,guess,listOfIndexes):
    for i in listOfIndexes:
        blankspaces = blankspaces[:2*i] + guess + blankspaces[2*i+1:]
    return blankspaces

# Either they lost or they won
def EndGame(blankSpaces, blank, HangmanParts):
    if blank == 0 or HangmanParts == 1:
        return True
    return False

# gives us a list of the indexes the letter is found in the word
def find(theWord, guess):
    L = []
    count = 0
    for i in theWord:
        if i == guess:
            L.append(count)
        count += 1
    return L

# Controls Text output on Turtle screen
def outputText(num, word):
    turtle.color('blue')
    style = ('Arial', 12, 'italic')
    if num == 0:
        turtle.write("Come again soon...", font=style, align='right')
        turtle.hideturtle()
        return None
    elif num == 1:
        turtle.write("Please enter a characer from the\nEnglish alphabet. Your guess: {}".format(word), font=style, align='right')
        turtle.hideturtle()
        return None
    elif num == 2:
        turtle.write("Try a different Letter.\nYour guess: {}".format(word), font=style, align='right')
        turtle.hideturtle()
        return None
    elif num == 3:
        turtle.write("You guessed right!Here's what you\nhave so far: {}".format(word), font=style, align='right')
        turtle.hideturtle()
    elif num == 4:
        turtle.write("Oops wrong guess!Here's what you \nhave so far: {}".format(word), font=style, align='right')
        turtle.hideturtle()
        return None
    elif num == 5:
        turtle.write("Game Over!!! You lost!\nThe word was: {}".format(word), font = style, align ='right')
        turtle.hideturtle()
        return None
    elif num == 6:
        turtle.write("You Won! The word was: {}".format(word), font = style, align = 'right')
        turtle.hideturtle()
        return None

# controls input window prompt message
def prompts(promptNum,screen):
    screen = turtle.Screen()
    if promptNum == 1:
        prompt = screen.textinput("Hangman.py","Would you like to continue? 'Y' for yes, 'N' for no: ")
        prompt = prompt.lower()
        return prompt
    elif promptNum == 2:
        prompt = screen.textinput("Hangman.py", "Guess a letter or click cancel to quit.")
        prompt.lower() 
        return prompt
    elif promptNum == 3:
        prompt = screen.textinput("Hangman.py","Want to go to the next level? Enter 'Y' for yes 'N' for no: ")
        prompt.lower()
        return prompt
    elif promptNum == 4:
        prompt = screen.textinput("Hangman.py","Want to try this level again? 'y' for yes, 'n' for no.")
        prompt.lower()
        return prompt

# main function for program control
def main():
    level = 1
    done = False
    promptNum = 0
    num = 0
    screen = turtle.Screen()
    while not done:
        promptNum = 1
        prompt = prompts(promptNum,screen)
        if prompt == "n":
            num = 0
            outputText(num)
            done = True
        elif prompt  == "y":
            HangmanParts = 10
            theWord = chooseWord(level)
            blank = len(theWord)
            myHangman= createTurtle()
            blankSpaces = len(theWord) * "_ "
            end = False
            usedLetters = list()

            while not end:# we only let them continue guessing if the game has not ended(they have lost or they have won)
                #guess a letter in the word
                promptNum = 2
                guess = prompts(promptNum,screen)
                # 1st checking: Check if guess is in theWord(they guessed right!).
                turtle.reset()
                if guess in "01234567890~`\\\"'!@#$%^&*()_-+={[}]|:;?/>.<," or len(guess)>1 or len(guess)<0:
                    num = 1
                    outputText(num, blankSpaces)
                    turtle.write("{}".format(usedLetters), font = ("Arial", 12, 'italic'),align ='left')
                elif guess in usedLetters:
                    num = 2
                    outputText(num, blankSpaces)
                    turtle.write("{}".format(usedLetters), font = ("Arial", 12, 'italic'), align='left')
                # Now that we know this word has not been guessed before  we can continue to check if it was right or wrong.
                elif guess in theWord:
                    # find all indexes that the guessed letter is found in the word
                    # replace the blank space at all the original guessed words index
                    listOfIndexes = find(theWord, guess)
                    blankSpaces = replace(blankSpaces,guess,listOfIndexes)
                    num = 3
                    outputText(num, blankSpaces)
                    usedLetters.append(guess)
                    turtle.write("{}".format(usedLetters), font = ("Arial", 12, 'italic'),align = 'left')
                    blank = blank-len(listOfIndexes)  
                else:
                    num = 4
                    outputText(num, blankSpaces)
                    usedLetters.append(guess)
                    HangmanParts = HangmanParts-1
                    updateTurtle(HangmanParts, myHangman)
                    turtle.write("{}".format(usedLetters), font = ("Arial", 12, 'italic'), align = 'left')
                end = EndGame(blankSpaces,blank,HangmanParts)
            turtle.reset()    
            if HangmanParts == 1:
                num = 5
                outputText(num, theWord)
            elif blank == 0:
                num =  6
                outputText(num, theWord)
            if num == 6:
                promptNum = 3
                response = prompts(promptNum,screen)
                if response == 'y':
                    if level == 4:
                        turtle.write("You finished all the levels! Congratulations", font = ("Arial",12,"italic"), align = 'right')
                        done == True
                    level += 1
                    myHangman.clear()
                    myHangman.reset()
                    turtle.clear()
                    turtle.reset()
                elif response == 'n':
                    continue
            elif num == 5:
                promptNum = 4
                response = prompts(promptNum,screen)
                if response == 'y':
                    myHangman.clear()
                    myHangman.reset()
                    turtle.clear()
                    turtle.reset()
                else:
                    done = True

            

if __name__ == "__main__":
    main()
