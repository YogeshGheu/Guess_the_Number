# this program is made to run on command prompt
import os #relate to line 3
hidden = input("Enter any Number to Hide: ")
os.system('cls') # i found this method on google, because it was important for a good game
chances = 7
guess_took = 0
if str(hidden).isnumeric():
    print("You Can type exit to Terminate anytime ")
    while (True):
        hidden = int(hidden)
        print("")
        usr = input("Enter Your Number: ")
        chances = chances - 1

        guess_took = guess_took + 1
        if usr.isnumeric():
            usr = int(usr)
            if chances <= -1:
                print("Chances left: ", chances)
                print("You Loose!")
                break
            elif usr == hidden:
                print("Congratulations, You Won !!!")
                print("No. of Guesses took to Win: ", guess_took)
                break
            elif usr > hidden:
                print("You Entered a Bigger Number than the Hidden One!, Try Again..!")
                print("Chances left: ", chances)
            elif usr < hidden:
                print("You Entered a Smaller Number than the Hidden One!, Try Again..!")
                print("Chances left: ", chances)
            else:
                pass
        elif usr == "exit" or usr == "Exit" or usr == "EXIT":
            break

else:
    print("Invalid Input!, Please Try Again!")
print("")
ex = input("Press Enter to Exit") # this line is added to hold the screen on command prompt
