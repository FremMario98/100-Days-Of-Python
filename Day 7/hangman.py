import random
import hangman_words
import hangman_art

stages = hangman_art.stages
word_list = hangman_words.word_list
lives = 6

randomWord = random.choice(word_list)
dashed_word =  ["_" for x in randomWord]

print("Welcome to Hangman!!!")
print(hangman_art.logo)

guessed_letters_history = []

while lives > 0:
    # Print Dashed word + Hangman Progress
    print(f"Guess the word: {dashed_word}")
    print(stages[lives])

    # Add/Check history
    guessed_letter = input("Guess a letter: ").lower()
    if guessed_letter in guessed_letters_history:
        print(f'You\'ve already guessed the letter "{guessed_letter}". Try again')
        continue
    else:
        guessed_letters_history += guessed_letter
    
    # Evaluate Guessed Letter
    if guessed_letter in randomWord:
        for index, letter in enumerate(randomWord):
            if letter == guessed_letter:
                dashed_word[index] = guessed_letter
        if not "_" in dashed_word:
            print("You won!!!")
            break
    else:
        lives -= 1
        if lives <= 0:
            print(stages[lives])
            print("Game lost")
        else:
            print(f"Wrong guess, try other than '{guessed_letter}'. Try again")
    

# Show Resulted Word 
print(f"Word: {randomWord}")