# File name: problemSetDay9.py
import random
Hangman_words = ["hat", "happy", "slides", "charger", "mice", "phone"]
colors_length = len(Hangman_words)
random_index = random.randint(0,colors_length-1)
word = Hangman_words[random_index]
'''print(list(word))'''
word_length = len(word)
print("lets play hangman!Your word has", len(word), "letters")
blank = "_ " * len(word)
print(blank)
wrong = []
guess = input("Guess a letter")
if guess in word:
  print("alight")
else:
  wrong.append(guess)
  print(wrong)