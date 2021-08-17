'''Hangman Game'''

# useful imports for clearing the screen and API call
from requests import get
from os import system

# utility functions..
def getData():
    '''Get data from random words api'''
    url = "https://random-words-api.vercel.app/word"
    data = get(url).json()
    word = data[0]['word']
    definition = data[0]['definition']
    return [word,definition]

def toCharArray(word):
    array = []
    for i in range(len(word)):
        array.append(word[i])
    return array


def checkDashes(array):
    c=0
    for items in array:
        if items=="_":
            c +=1
    if c==0:
        return False
    return True


# MAIN function starts here...
if __name__ == '__main__':

    #clear screen function
    system('cls')
    system('color 06')
    print("*****************WELCOME TO HANGMAN GAME**************")

    chances = 0 # total chances user will take

    # setting up the API call
    myData = getData()
    word = myData[0].upper()
    definition = myData[1].upper()

    # initial instructions
    print(f"Guess the Word\nHINT meaning of the word is {definition}")
    print("NOTE : It may also contains special characters dashes, etc..")
    print("To see the word just write 'show' in the input box")

    # some variables
    dashedWord = "_"*len(word)
    dashedWordArray = toCharArray(dashedWord)
    actualWordArray = toCharArray(word)
    print("\n")

    # Important loop and main logic
    while True:
        if not checkDashes(dashedWordArray):
            print(" ".join(dashedWordArray))
            break
        print(" ".join(dashedWordArray))
        char = input("Guess the alphabet that can be present in that word : ").upper()

        # for quitting the game and wante to see the answer
        if char == "SHOW":
            print(f"Word is {word}")
            print(f"Definition is {definition}")
            print("You Quit the Game so you got💩💩💩💩")
            exit()

        
        for index,items in enumerate(actualWordArray):
            if char==items:
                dashedWordArray[index] = char + " "
        
        chances +=1
        print("\n")


# getting results
print("\n*****************RESULTS**************\n")

print(f"Total Guesses taken {chances}")
print(f"Word is {word}")
print(f"Definition is {definition}")
if chances <= len(word) +2:
    print("Well Done!!😎😎😎😎🔥🔥🔥🔥")
else:
    print("Good!!😊😊")



       

