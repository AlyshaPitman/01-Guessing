import sys, random

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"


quit = False
range = 100

while not quit:
        random_number = random.randint(1,range)
        count = 1
        number = -1
        while number != random_number:
            number= input("Try guessing a number between 1 and {}:".format(range))
            if not number.isdigit():
                print("Try guessing a number!")
            else:
                number = int(number)
                count = count + 1
                print("Sorry, that wasn't the right one")
                if number > random_number:
                    print("Too high!")
                elif number < random_number:
                    print("Too low!")
        print("You got it!")
        print("You guessed it in {} tries!".format(count))
        play_again = input("\nDo you want to play again (yes or no)?")
        play_again = play_again.lower()
        if play_again == "yes" or play_again == "y":
            quit = False
        else:
            quit = True

print("\n\nThanks for playing! Have a nice life!")