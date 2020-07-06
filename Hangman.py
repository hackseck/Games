import random


with open ('wordlist.txt') as f:
    wordlist = f.read().splitlines()



def randomWord():
    word = random.choice(wordlist)
    return (word).upper()



def display(lives):
    hangmanDisplay =  [        """                        HANGMAN
                      _________
                      |       |
                      |      ( )
                      |      /|\\
                      |       |
                      |      | |
                ______|______              """,
"""                    HANGMAN
              _________
              |       |
              |      ( )
              |      /|\\
              |       |
              |      |
        ______|______              """,
"""                    HANGMAN
              _________
              |       |
              |      ( )
              |      /|\\
              |       |
              |
        ______|______              """,
"""                    HANGMAN
              _________
              |       |
              |      ( )
              |      /|\\
              |
              |
        ______|______              """,
"""                    HANGMAN
              _________
              |       |
              |      ( )
              |      /|
              |
              |
        ______|______              """,

"""                    HANGMAN
              _________
              |       |
              |      ( )
              |       |
              |
              |
        ______|______              """,
"""                      HANGMAN
              _________
              |       |
              |      ( )
              |
              |
              |
        ______|______              """,
"""                      HANGMAN
              _________
              |       |
              |
              |
              |
              |
        ______|______              """]

    return hangmanDisplay[lives]




def playGame(word):

    guessedLetters = []
    gameOver = False
    lives = 7
    hiddenWord = []
    for c in range(len(word)):
        hiddenWord.append('*')
    displayWord = ''.join(hiddenWord)
    print("Welcome to HANGMAN!")
    print(display(lives))
    print(f"Lives remaining: {lives} ")
    print(f"The word is: {displayWord} ")



    while gameOver == False and lives > 0:

        #user input
        guess = input("Please enter your next guess: ").upper()
        print("\n")

        if validInput(guess, guessedLetters):

            if guess in word:
                print(f"That is correct {guess} is in the word")
                guessedLetters.append(guess)
                for i, char in enumerate(word):
                    if char == guess:
                        hiddenWord[i] = char
                        displayWord = ''.join(hiddenWord)
                if '*' not in hiddenWord:
                    gameOver = True

            else:
                print(f"Unlucky, {guess} is not in the word")
                lives -= 1
                guessedLetters.append(guess)


        print(display(lives))
        print(f"Lives remaining: {lives} ")
        print("\n")
        print(f"Guessed letters: {guessedLetters} ")
        print("\n")
        print(f"The word is: {displayWord} ")
        print("\n")
        if guess in word:
            print(f"That is correct {guess} is in the word")
        else:
            print(f"Unlucky, {guess} is not in the word")


    if gameOver == True:
        print("Congratulations you won the game!")

    else:
        print(f"You have lost, the word was {word}")












def validInput(guess, guessedLetters):

    if len(guess) != 1:
        print("Please enter only 1 character at a time ")

    else:
        if guess.isalpha():
            if guess in guessedLetters:
                print(f"You have already guessed {guess}, try again ")
                return False
            else:
                return True

        else:
            print("Please enter an alphabetical letter ")
            return False


def main():
    word = randomWord()
    playGame(word)

if __name__ == "__main__":
    main()
