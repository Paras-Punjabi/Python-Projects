'''Tic-Tac-Toe Game'''

# importing modules
from os import system

# utility function
def drawBoard(array):
    print(f"-------------")
    print(f"|{array[0]} || {array[1]} || {array[2]}|")
    print(f"-------------")
    print(f"|{array[3]} || {array[4]} || {array[5]}|")
    print(f"-------------")
    print(f"|{array[6]} || {array[7]} || {array[8]}|")
    print(f"-------------")

def checkArray(array):
    return(
        (1 in array and 2 in array and 3 in array) or 
        (4 in array and 5 in array and 6 in array) or 
        (7 in array and 8 in array and 9 in array) or 
        (1 in array and 4 in array and 7 in array) or 
        (2 in array and 5 in array and 8 in array) or 
        (3 in array and 6 in array and 9 in array) or 
        (1 in array and 5 in array and 9 in array) or 
        (7 in array and 5 in array and 3 in array) 
    )

def checkWinning(array,number,chance):
    if number >=4:
        chanceArray = []
        winningConditions = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[7,5,3]]
        for index,items in enumerate(array):
            if items==chance:
                chanceArray.append(index+1)
        
        for items in winningConditions:
            if checkArray(chanceArray):
                print(f"{chance} is winner🥳🥳🥳🥳")
                if chance == "X":
                    print("O is looser💩💩💩💩")
                else:
                    print("X is looser💩💩💩💩")
                system("color 02")
                return True

def checkDraw(array):
    count = 0
    a = map(lambda x : x=="X" or x=="O",array)
    a = list(a)
    for items in a:
        if items == True:
            count +=1
    if count == len(array):
        return True
    return False

# main function
if __name__ == '__main__':
    # initial variables
    system('color 06')
    cross = "X"
    circle = "O"
    chance = cross
    chanceNumber = 1
    array = [1,2,3,4,5,6,7,8,9]

    # main logic loop
    while True:
        system('cls')
        if checkDraw(array):
            print("Game DRAW!!😎😎😎")
            print("Well Done both the players")
            system("color 04")
            break
        print("*************Welcome to Tic-Tac-Toe Game***************")
        drawBoard(array)
        print(f"It's chance for {chance}")

        try:
            number = int(input("Enter your choice : "))
        except Exception as e:
            print("Wrong Input!!")
            continue

        if array[number-1] in [1,2,3,4,5,6,7,8,9]:
            array[number-1] = chance
        else:
            print("You cannot choose that value")
            continue

        if checkWinning(array,chanceNumber,chance):
            break
        if chanceNumber%2==0:
            chance = cross 
        else:
            chance = circle
        chanceNumber +=1
        

        

