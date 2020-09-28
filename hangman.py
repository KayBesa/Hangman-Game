# Hangman.py
import random

WORDS = open ("words.txt", "r")
list_of_words = WORDS.readlines()
theWord = list_of_words[random.randint(0,len(list_of_words))]
theWord = theWord.lower()
theWord = theWord.strip()
blankSpaces = len(theWord) * "_ " 
print (blankSpaces)
print (theWord)

end = False
while not end:
    end = EndGame(blankSpaces)
    guess = input ("Guess a letter: ")
    usedLetters = list()
    # 1st checking: Check if guess is in theWord. 
    if guess in theWord:
        # usedIndex = []
        indexOfGuess = theWord.find(guess)
        blankSpaces = blankSpaces[0:indexOfGuess*2] + theWord[indexOfGuess] + blankSpaces[indexOfGuess*2 + 1:]
        # usedIndex.append(indexOfGuess)
        # theWord[indexOfGuess + 1:]
        print (blankSpaces)

    # 2nd checking: Come here when guess is not in word
    else:
        usedLetters.append(guess)
        # CODE HERE: Add abody part to the hangman in turtle.
        
    # 3rd checking


def EndGame(blankSpaces):
    if blankSpaces.count("_") == 0:
        return True
    return False
