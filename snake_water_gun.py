'''Snake Water Gun'''
import random
def displayPoints():
    print(name + " : " + str(user_points))
    print("Computer" + " : " + str(computer_points) + "\n")
if __name__ == '__main__':
        print("*****Welcome to Snake-Water-Gun**********")
        name = input("Enter your name\n")

        list  = ["s","w","g"]

        a = int(input("How many times you want to play this Game..\n"))

        computer_points = 0
        user_points = 0

        print("Enter s for Snake")
        print("Enter w for Water")
        print("Enter g for Gun")

        for i in range(1,a+1):
            print("Battle-" + str(i))
            computer_choice = list[int(random.random()*len(list))]
            user_choice = input("Enter your choice\n")

            if(user_choice == computer_choice):
                print("Both choose " + user_choice)
                print("So no points will be given to both of you..")

            elif user_choice=="s" and computer_choice=="g":
                print("Computer choose Gun")
                computer_points = computer_points +1
                print("Computer wins this round")

            elif user_choice=="s" and computer_choice=="w":
                print("Computer choose Water")
                user_points = user_points +1
                print("User wins this round")
            
            elif user_choice=="w" and computer_choice=="s":
                print("Computer choose Snake")
                computer_points = computer_points +1
                print("Computer wins this round")

            elif user_choice=="w" and computer_choice=="g":
                print("Computer choose Gun")
                user_points = user_points +1
                print("User wins this round")

            elif user_choice=="g" and computer_choice=="w":
                print("Computer choose Water")
                computer_points = computer_points +1
                print("Computer wins this round")

            elif user_choice=="g" and computer_choice=="s":
                print("Computer choose Snake")
                user_points = user_points +1
                print("User wins this round")
            
            displayPoints()


        if user_points>computer_points:
            displayPoints()
            print(name + " wins......🎉🎉🥇🥇")

        elif computer_points>user_points:
            displayPoints()
            print("Computer wins..🎉🎉🥇🥇")
            print(name + " looses..💩💩")

        else:
            displayPoints()
            print("DRAW!!")



