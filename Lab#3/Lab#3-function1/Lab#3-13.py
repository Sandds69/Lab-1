import random




def guessTheNumber(answer, numberOfGuesses):
    guessedNumber = int(input("Take a guess.\n"))
    if(guessedNumber == answer):
        print(f"Good job, {name}! You guessed my number in {numberOfGuesses} guesses")
    elif (guessedNumber > answer):
        print("Your guess is too high.")
        guessTheNumber(answer, numberOfGuesses + 1)
    else:
        print("Your guess is too low.")
        guessTheNumber(answer, numberOfGuesses + 1)

name = input("Hello! What is your name?\n")
print((f"Well {name}, i am thinking of a number between 1 and 20."))
answer = random.randrange(1, 21)   
guessTheNumber(answer, 0)