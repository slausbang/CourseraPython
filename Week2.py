__author__ = 'common'

# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import math
import random



# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number
    global triesRemaining
    triesRemaining = 7
    secret_number = int(random.randrange(0,100))
    print "Guess a number between 1 and 100"
    print "Guesses left", triesRemaining
    print "---------------------------------------"
    print "\n"



    # define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game
    global secret_number
    global triesRemaining
    triesRemaining = 7
    secret_number = int(random.randrange(0,100))
    print "Guess a number between 1 and 100"
    print "Guesses left", triesRemaining
    print "---------------------------------------"
    print "\n"


def range1000():
    # button that changes the range to [0,1000) and starts a new game
    global secret_number
    global triesRemaining
    triesRemaining = 10
    secret_number = int(random.randrange(0,1000))
    print "Guess a number between 1 and 1000"
    print "Guesses left", triesRemaining
    print "---------------------------------------"
    print "\n"


def input_guess(guess):
    global secret_number
    global triesRemaining
    print "Guess was:", int(guess)
    if triesRemaining >= 1:
        if int(guess) > secret_number:
            #decrement remaining guesses by 1
            triesRemaining -= 1
            #print lower and remaining guesses
            print "Lower!"
            print "Guesses left", triesRemaining
            print "\n"
        elif int(guess) < secret_number:
            #decrement the remaining guesses by 1
            triesRemaining -= 1
            #print out higher and remaining guesses
            print "Higher!"
            print "Guesses left", triesRemaining
            print "\n"
        else:
            print "You are correct!"
            print "Press a button to start a new game (1-100, or 1-1000)"
    else:
        print "No more guesses, game over!"
        print "Press a button to start a new game (1-100 or 1-1000)"




# create frame
frame = simplegui.create_frame("Guess the number!", 300, 300)
button100 = frame.add_button("New game 1-100", range100, 200)
button1000 = frame.add_button("New game 1-1000", range1000, 200)

guess = frame.add_input("Enter your guess", input_guess, 100)

# register event handlers for control elements and start frame


# call new_game
new_game()


# always remember to check your completed program against the grading rubric
