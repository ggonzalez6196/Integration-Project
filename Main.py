"""
My Program is an NFL Quiz Game. That will show users a question, and they
enter the required to be input. At the end there score will show.
"""
__author__ = "Gilberto Gonzalez"

import time


def main():
    """
The function that incorporates all other functions.
    :return:
    """

    def extra_requirements():
        """
    I will be displaying my knowledge on requirements I was unable
    to fit into my project.
        """
        print("I will be displaying my knowledge on requirements I was unable"
              " to fit into my project.")
        time.sleep(1)
        print("You use ** to find an exponent")
        time.sleep(1)
        print(3 ** 3)
        time.sleep(1)
        print("You use % to determine a remainder of a division operation")
        time.sleep(1)
        print(19 % 3)
        time.sleep(1)
        print("You use // to show the nearest integer of two numbers divided")
        time.sleep(1)
        print(27 // 4)
        time.sleep(1)
        print("An example of the and operator will be shown.")
        time.sleep(1)
        x = 5
        # noinspection PyChainedComparisons
        print(x > 3 and x < 10)
        time.sleep(1)
        print("returns True because 5 is greater than 3 AND 5 is less than 10")
        time.sleep(1)
        print("An example of the or operator will be shown.")
        time.sleep(1)
        x = 5
        print(x > 3 or x < 4)
        time.sleep(1)
        print(" returns True because one of the conditions are true "
              "(5 is greater than 3, but 5 is not less than 4)")
        time.sleep(1)
        print("The not operator is the Boolean or logical operator "
              "that implements negation")
        time.sleep(1)
        names = ("Max", "Mark")
        if "Moe" not in names:
            print("Moe is not in the list of names")
        time.sleep(1)
        print("The range function returns a sequence of numbers,"
              " starting from 0 by default, "
              "and increments by 1 by default, "
              "and stops before a specified number.")
        time.sleep(1)
        x = range(6)
        for n in x:
            print(n)
        time.sleep(1)
        print("Finally, that's over with let's get started.")

    def intro():
        """
    Purpose of this function is to ask the user if they are ready to begin the
    quiz
        """
        # end= ' ' makes sure that the next line is on the same line as the
        # first
        print("Welcome to my", end=' ')
        print("NFL Quiz Game.")
        time.sleep(1)
        playing = input("Are you ready to begin? (yes or no): ")
        # Using .lower() so that when users can type yes any way they want
        # example Yes, YES, yES, etc.
        # Got the information from w3schools
        # For the exit() I found the information on geeksforgeeks
        # It stops the program if anything other than yes is answered
        if playing.lower() == "no":
            print("Come back when you are ready.")
            exit()
        elif playing.lower() == "yes":
            time.sleep(1)
            print("Okay! Let's test your NFL knowledge.")
            time.sleep(1.5)
            print("You will have 10 questions to answer.")
            time.sleep(1.5)
            # ,sep = '' makes sure there is no space between good and luck
            # If you add a space between ' and ' there will be a space
            print("Good", "luck!", sep='')
            time.sleep(1.5)
        elif playing.lower() != "yes" or "no":
            print("That was an odd response. Please try again.")
            intro()

    def new_game():
        """
    Purpose of this function is to keep score for the user.
        """
        guesses = []
        correct_guesses = 0
        question_num = 1
        # I found it easier to use a dictionary instead of having to
        # keep typing out questions
        # I found information about dictionaries on w3schools
        questions = {
            "Who is the player with the most superbowl wins?": "A",
            "Which team is considered America's team? ": "B",
            "Which team has made the most superbowl appearances? ": "C",
            "Who is the player with the most MVPs in the NFL? ": "A",
            "How many teams are in the NFL? ": "D",
            "Which player has an award named after him? ": "B",
            "Who is the player that is nicknamed megatron? ": "B",
            "Who is the superbowl trophy named? ": "A",
            "Which team won the first superbowl? ": "A",
            "Who is the quarterback that threw the most interceptions? ": "B"
        }

        # Used a 2d list to help with storing the answers
        # Found information about 2d Lists on python pool and geeks for geeks
        options = [["A. Tom Brady", "B. Peyton Manning", "C. Joe Montana",
                    "D. Troy Aikman"],
                   ["A. Green Bay Packers", "B. Dallas Cowboys",
                    "C. New England Patriots", "D. Miami Dolphins"],
                   ["A. Denver Broncos", "B. Pittsburgh Steelers",
                    "C. New England Patriots", "D. Chicago Bears"],
                   ["A. Peyton Manning", "B. Tom Brady", "C. Aaron Rodgers",
                    "D. Dan Marino"],
                   ["A. 31", "B. 28", "C. 34", "D. 32"],
                   ["A. Aaron Rodgers", "B. Walter Payton", "C. Julio Jones",
                    "D. Antonio Brown"],
                   ["A. Matt Ryan", "B. Calvin Johnson", "C. J.J. Watt",
                    "D. Aaron Donald"],
                   ["A. Vince Lombardi", "B. Roger Goodell",
                    "C. Bill Belichick",
                    "D. Tom Brady"],
                   ["A. Green Bay Packers", "B. Detroit Lions",
                    "C. Cleveland Browns",
                    "D. New York Jets"],
                   ["A. Tom Brady", "B. Brett Favre", "C. Ben Roethlisberger",
                    "D. Drew Brees"]]

        for key in questions:
            print("-------------------------")
            print(key)
            for i in options[question_num - 1]:
                print(i)
            guess = input("Enter (A, B, C, or D): ")
            guess = guess.upper()
            guesses.append(guess)

            correct_guesses += check_answer(questions.get(key), guess)
            question_num += 1

        display_score(correct_guesses, guesses)

    def check_answer(answer, guess):
        """
    Purpose of this function is to see if the guess that was selected
    matches the correct answer of the question
        :param answer: the correct answer
        :param guess: the answer the users selected
        :return: returns a point for each question answered correctly and
        returns no points for each question answered incorrectly
        """
        if answer == guess:
            print("CORRECT!")
            return 1
        else:
            print("WRONG!")
            return 0

    def display_score(correct_guesses, guesses):
        """
    Purpose of this function is to give the users their score at the end of the
    program
        :param correct_guesses: the amount of questions the user got correct
        :param guesses: the amount of answers the user selected
        """
        questions = {
            "Who is the player with the most superbowl wins?": "A",
            "Which team is considered America's team? ": "B",
            "Which team has made the most superbowl appearances? ": "C",
            "Who is the player with the most MVPs in the NFL? ": "A",
            "How many teams are in the NFL? ": "D",
            "Which player has an award named after him? ": "B",
            "Who is the player that is nicknamed megatron? ": "B",
            "Who is the superbowl trophy named? ": "A",
            "Which team won the first superbowl? ": "A",
            "Who is the quarterback that threw the most interceptions? ": "B"
        }

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

        score = int((correct_guesses / len(questions)) * 100)
        print("Your score is: " + str(score) + "%")

    def play_again():
        """

        :return: returns false so that if the user inputs "no" the game won't
        start again and ends.
        """
        response = input("Do you want to play again? (yes or no): ")
        response = response.upper()

        if response == "YES":
            time.sleep(.5)
            print("Get ready for another round.")
            time.sleep(2)
            new_game()
            print("Did you improve?")
        elif response == "NO":
            print("Thanks for playing!")
            return False
        else:
            print("What was that? Please try again.")
            play_again()

    extra_requirements()
    time.sleep(1.5)
    intro()
    new_game()
    while play_again():
        new_game()


if __name__ == "__main__":
    main()
