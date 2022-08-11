from replit import clear
import random

lives = 6

from hangman_art import logo, stages 
print(logo)

from hangman_words import word_list

chosen_word = random.choice(word_list) 

display = []

for _ in range(len(chosen_word)):
  display += "_"
print(display)

end_of_game = False

while not end_of_game:
  guess = input("Guess a letter ").lower()

  clear()
  
  if guess in display:
    print(f"You have alreadt guessed {guess}")
  
  for position in range(len(chosen_word)):
    if guess == chosen_word[position]:
      display[position] = guess

  if guess not in chosen_word:
    lives -= 1
    print(f"You guessed {guess}, that is not in the word. You lose a life.")
    if lives == 0:
      end_of_game = True
      print("You lose. Game Over!")
      print(f"The word is {chosen_word}")
      
  print(display)

  if "_" not in display:
    end_of_game = True
    print("Game Over. You win!")

  print(stages[lives])

