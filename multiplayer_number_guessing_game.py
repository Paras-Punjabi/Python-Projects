'''Multiplayer Numbering Guessing Game'''
import random
def generateRandom(a,b):
    return random.randint(a,b)

def playGame(a,b):
    '''Logic Here'''
    chances = 0
    randomNumber = generateRandom(a,b)
    while(True):
        n = int(input(f"Guess a number between {a} and {b}\n"))
        if(n > randomNumber):
            print("Guess a lower number")
        elif (n < randomNumber):
            print("Guess a higher number")
        elif(n == randomNumber):
            print("You guessed it right!!🔥🔥🔥")
            break
        chances +=1

    return chances

if __name__ == '__main__':
    player1 = input("Enter the name of Player-1\n")
    player2 = input("Enter the name of Player-2\n")
    a = int(input("Enter the lowerst number\n"))
    b = int(input("Enter the highest number\n"))

    print(f"First the turn will be for {player1}")
    total_chances_player1 = playGame(a,b)

    print(f"Now it's turn for {player2}")
    total_chances_player2 = playGame(a,b)

    print("Displaying Scores....")
    print(f"{player1} - {total_chances_player1} chances")
    print(f"{player2} - {total_chances_player2} chances")

    if(total_chances_player1 > total_chances_player2):
        print(f"{player2} win's😊😊")
    
    elif (total_chances_player2 > total_chances_player1):
        print(f"{player1} win's😊😊")

    else:
        print("DRAW!!😎😎😎")


