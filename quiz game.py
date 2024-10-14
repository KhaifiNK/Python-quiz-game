#quiz gayme

def newgame():
    # Starts a new round of the game, initializes guesses and counters
    guesses = []
    correct_guesses = 0
    questions_num = 1

    # Loops through the questions dictionary
    for key in questions:
        print("----------------------------------")
        print(key)  # Displays the current question
        for i in options[questions_num-1]:  # Displays the corresponding options
            print(i)
        guess = input("enter (A,B,C, or D?)").upper()  # Takes input from the user
        guesses.append(guess)  # Adds the guess to the list
        
        # Checks if the guess is correct and updates the score
        correct_guesses += checkanswer(questions.get(key), guess)
        questions_num += 1

    # Displays the final score after all questions are answered
    display_score(correct_guesses, guesses)

#----------------
def checkanswer(answer, guess):
    # Checks if the player's guess matches the correct answer
    if answer == guess:
        print("Correct!")  # Prints "Correct!" if the answer is right
        return 1  # Returns 1 point for a correct answer
    else:
        print("Wrong")  # Prints "Wrong" if the answer is incorrect
        return 0  # Returns 0 points for a wrong answer
#----------------
def display_score(correct_guesses, guesses):
    # Displays the player's results after the game
    print("----------------------------------")
    print("results")
    print("----------------------------------")
    
    # Prints the correct answers
    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    # Prints the player's guesses
    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    # Calculates and displays the player's score as a percentage
    score = (correct_guesses/len(questions)) * 100
    score = int(score)
    print("your score is: "+str(score)+"%")
#----------------
def play_again():
    # Asks the player if they want to play again
    response = (input("do you want to play again?: (yes or no) ")).upper()

    # Returns True to play again if the player says "YES", otherwise False
    if response == "YES":
        return True 
    else:
        return False
#----------------

# A dictionary containing the quiz questions and their correct answers
questions = {
"who is balanced?: ": "D",
"whos the the exagurated swager of a black teen?: ": "B",
"I Dont Drive _____ I dont like those?: ": "C",
"free larry, free ______?: ": "A"
}

# A list of options for each question, corresponding to the questions above
options = [["A. Ksante", "B. Darius", "C. Zed", "D. All of the above"],
           ["A. Martin Luther king", "B. Miles morals", "C. Faker", "D. Monkey D luffy"],
           ["A. M5's", "B. Daytona's", "C. R8's", "D. GTR's"],
           ["A. Young thug", "B. jeffery epstein", "C. Gunna", "D. P.Diddy"]]

# Starts the game
newgame()

# Asks the player if they want to play again in a loop until they say no
while play_again():
    newgame()

# Ends the game with a thank you message
print("Thanks for playing")
