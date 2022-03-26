# Gilberto Gonzalez
# NFL Quiz Game

import time

#end= ' ' makes sure that the next line is on the same line as the first
print("Welcome to my" , end = ' ')
print("NFL Quiz Game.")
time.sleep(1.5)
playing = input("Are you ready to begin? ")
#Using .lower() so that when users can type yes any way they want
#example Yes, YES, yES, etc.
#Got the information from w3schools
#For the exit() I found the information on geeksforgeeks
#It stops the program if anything other than yes is answered
if playing.lower() != "yes":
    exit()
time.sleep(1)
print("Okay! Let's test your NFL knowledge.")
time.sleep(1.5)
print("You will have 10 questions to answer.")
time.sleep(1.5)
#,sep = '' makes sure there is no space between good and luck
#If you add a space bewteen ' and ' there will be a space
print("Good","luck!",sep = '')
time.sleep(1.5)

def new_game():

    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("-------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C, or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)

def check_answer(answer, guess):

    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0

def display_score(correct_guesses, guesses):
    print("-------------------------")
    print("RESULTS")
    print("-------------------------")

    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Your score is: "+str(score)+"%")

def play_again():

    response = input("Do you want to play again? (yes or no): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False

# I found it easier to use a dictionary instead of having to keep typing-
# out questions. I found information about dictionaries on w3schools
questions = {
 "Who is the player with the most superbowl wins?": "A",
 "Which team is considered America's team? ": "B",
 "Which team has made the most superbowl appearances? ": "C",
 "Who is the player with the most MVPs in the NFL? ": "A",
 "How many teams are in the NFL? ": "D",
 "Which player has an award named after him? ": "B",
 "Who is the player that is nicknamed megatron? ": "B",
 "Who is the superbowl trophy named? ": "A",
 "Which team won the first superbowl? ": "C",
 "Who is the quarterback that threw the most interceptions? ": "B"
}

# Used a 2d list to help with storing the answers
#Found information about 2d Lists on pythonpool and geeksforgeeks
options = [["A. Tom Brady", "B. Peyton Manning", "C. Joe Montana",
            "D. Troy Aikman"],
          ["A. Green Bay Packers", "B. Dallas Cowboys",
           "C. New England Patriots", "D. Miami Dolphins"],
          ["A. Denver Broncos", "B. Pittsburgh Steelers",
           "C. New England Patriots", "D. Chicago Bears"],
          ["A. Peyton Manning","B. Tom Brady", "C. Aaron Rodgers",
           "D. Dan Marino"],
          ["A. 31", "B. 28", "C. 34", "D. 32"],
          ["A. Aaron Rodgers", "B. Walter Payton", "C. Julio Jones",
           "D. Antonio Brown"],
          ["A. Matt Ryan", "B. Calvin Johnson", "C. J.J. Watt",
           "D. Aaron Donald"],
          ["A. Vince Lombardi", "B. Roger Goodell", "C. Bill Belichick",
           "D. Tom Brady"],
          ["A. Green Bay Packers", "B. Detroit Lions", "C. Cleveland Browns",
           "D. New York Jets"],
          ["A. Tom Brady", "B. Brett Favre", "C. Ben Roethlisberger",
           "D. Drew Brees"]]

new_game()

while play_again():
    new_game()

print("Thanks for playing!")