import random
from hangman_words import word_list
from hangman_art import stages, logo

end_of_game = False
lives = 6
print(logo)
chosen_word = random.choice(word_list)
print(f'ssssshhhhhh, the word is: {chosen_word}')
word_length = len(chosen_word)

guessed_word = ['_'] * word_length

while not end_of_game:
    guess = input('Guess a letter: ').lower()
    if guess in guessed_word:
        print(f"You've already guessed {guess}.")
    for position in range(word_length):
        if chosen_word[position] == guess:
            guessed_word[position] = chosen_word[position]

    print(''.join(guessed_word))
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        print(stages[lives])
        if lives == 0:
            end_of_game = True
            print('You Lose.')

    if '_' not in guessed_word:
        end_of_game = True
        print('You Win.')
