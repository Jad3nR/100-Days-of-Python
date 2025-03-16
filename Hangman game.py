
stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
import random
from nltk.corpus import words
import nltk

nltk.download('words')
word_list = words.words()


chosen_word=list(random.choice(word_list))

placeholder=list("_"*len(chosen_word))
print ("".join(placeholder))
lives = 6
letters_used=set()
while lives>0 and "_" in placeholder:

    guess = (input("Guess a letter\n")).lower()
    if guess in letters_used:
        print("You already guessed this word")
    letters_used.add(guess)
    print(f"Letters used are {letters_used}")


    if guess in chosen_word:
        print("\n\nRight")
        for index in range(len(chosen_word)):
            if chosen_word[index] == guess:
                placeholder[index] = guess
        print("".join(placeholder))
        print(f"Lives left {lives}")
        print(stages[lives])
    else:
        print("\n\nWrong")
        print("".join(placeholder))
        lives-=1
        print(f"Lives left {lives}")
        print(stages[lives])
        if lives == 0:
            print("You died")
            print(f"The word was {"".join(chosen_word)}")
