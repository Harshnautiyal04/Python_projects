#Step 1
from replit import clear
#TODO-1 Randomly choose a word from the word_list and assign it to ta variable called chosen_word.
import random
from hangman_art import word_list,stages,logo

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game=False
lives = 6
#TODO- create an empty list called display
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_","_","_","_","_","_"] with 5 "_" representing each letter to guess.
#TODO-2- Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

print(logo)

# Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Creates Blanks
display = []
for _ in range(word_length):
    display += "_"
#TODO: Use a while loop to let the user guess again. the loop should only stop once the users has guessed all the letters in the chosen_word and 'dsplay' has no more blanks"_". then you can tell teh user they have won.

while not end_of_game:
    guess= input("Guess a letter: ").lower()
    clear()
    if guess in display:
        print(f"You already guessed {guess}.")
#TODO :LOOP through each position in the chosen_word:
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_","_","_","_","_","_"].
#TODO-3 - Check if the letter the user guessed(guess) is one of the letters in the chosen_word.
#Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position:{position}\n"
        #     f"Current letter:{letter}\n"
        #     f"Guessed letter:{guess}\n  ")
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word.You lose a life.")
        lives -=1
        if lives == 0:
            end_of_game=True
            print("You Lose.")
    print(f"{''.join(display)}")

    if "_" not in display:
        end_of_game=True
        print("You Win!")
    print(stages[lives])