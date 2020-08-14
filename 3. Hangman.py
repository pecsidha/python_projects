# -*- coding: utf-8 -*-
"""
Created on Thu May 21 05:26:34 2020

@author: ReDI
"""

import random # we will need this module for drawing a word

# Let's declare two variables that will be useful for our game:
HANGMAN_PICS = ['''
   +---+
       |
       |
       |
      ===''', '''
   +---+
   O   |
       |
       |
      ===''', '''
   +---+
   O   |
   |   |
       |
      ===''', '''
   +---+
   O   |
  /|   |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
  /    |
      ===''', '''
   +---+
   O   |
  /|\  |
  / \  |
      ===''']

words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar \
        coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk \
       lion lizard llama mole monkey moose mouse mule newt otter owl panda \
       parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep \
       skunk sloth snake spider stork swan tiger toad trout turkey turtle \
       weasel whale wolf wombat zebra'.split()

# Variable >words< is a list of words for the game. It is a list - you can check the type of the variable to convince yourself that it's true. >HANGMAN_PICS< is a list with so-called ASCII-ART graphics in it. Take a look: comas separate elements of the list, so each element is a small picture. Try the following code (you need to uncomment it and make sure that the indents are correct!) to print them:
# for i in range(len(HANGMAN_PICS)):
#   print(HANGMAN_PICS[i])

def choose_word(list_of_words):
  n_of_words = len(list_of_words)# write code here
  index = random.randint(0,n_of_words) # draw a random index from range [0,n_of_words)
  chosen_word = list_of_words[index] # write your code for choosing a word here
  return chosen_word 

def make_secret_word(my_word):
  # this function will return a secret string of coded letters 
  # that shows number of letters, but no actual letters.
  # e.g. for a word 'cat' it will return '---'
 
    secret_word = "*" * len(my_word)
    return secret_word

def check_letter_in_word(letter, my_word):
  if letter in my_word: # if letter 'a' in 'cat'
    return True
  else:
    return False

  # You know that a letter is in the word. Now you want to build a new secret word to show the user what their guessed right:
  # e.g. for my_word='cat' and letter='a' and secret word '---', new_secret_word should be '-a-'.
  # for my_word='beaver' and letter='a' and secret word 'b-----', new_secret_word should be 'b-a---'.

def update_secret_word(letter, my_word, secret_word):
    temp_list = list(secret_word)
    for i in range(len(my_word)):
        if letter == my_word[i]:
            temp_list[i] = letter
    new_secret_word = ''.join(temp_list)
    return new_secret_word

def check_input(letter):
    if len(letter) == 1:
        return True
    else: 
        print('Enter only one letter')
        return False
        
while True:
    # Let's initiate two variables: 
    remaining_guesses = len(HANGMAN_PICS)
    number_of_errors = 0
    guesses_list = []
    
    
    # Initiate the game here. Choose a word (draw from the list).
    word = choose_word(words) 
    secret_word = make_secret_word(word)
    
    print("Hello! Let's play hangman. I have drawn a word for you to guess." )
    print(f"Your word is {secret_word}" )
    
    while remaining_guesses != 0:
        # write a condition here (hint: when does the game end? careful, there are two possibilities!):
        # ask the user to input a letter here
      letter_lowercase = input("Enter a letter: ").lower()
     
      if check_input(letter_lowercase) == False:
          print('remaining guesses:', remaining_guesses)
          continue
      
      elif letter_lowercase in guesses_list:
          print('you have already entered this letter, try with other letter')
          print('remaining guesses:', remaining_guesses)
          
      elif check_letter_in_word(letter_lowercase, word):
        guesses_list.append(letter_lowercase)

        # call function and pass argument 'a', cat, ---
        secret_word = update_secret_word(letter_lowercase, word, secret_word) 
        print(f"Well guessed! Letter {letter_lowercase} is in my word. \
          The word looks like that now: {secret_word}" )
        print('remaining guesses:', remaining_guesses)    
    
        # This is also where we should check if the user won
        if secret_word == word:
            print(f'Congratulations! You won, the word is {word}')
            break
      else:
          print('wrong letter! enter again')
          
          remaining_guesses -=1
          guesses_list.append(letter_lowercase)
          print('remaing guesses:', remaining_guesses)
          print(HANGMAN_PICS[number_of_errors])
          number_of_errors += 1
    else:
        print(f'sorry you were not able to guess correct. The word is {word}')
        
       
    choice = input('Do you want to play again? (y/n)')  
    if choice.lower()!= 'y':
        break
    
  
    # Print the hangman image based on the number of errors.

# Finish the program with a message to the user that depends on the outcome of the game. E.g. if the user won, congratulate; if the user lost - offer a re-match. Hint: write a conditional statement to check the outcome.

###################################################################################

# Extra exercise 1.
# Write a function check_input(letter) that checks if the users input was only one letter and returns True or False. Write and extra nested loop that asks user to input a new, correct letter until the ouptup of check_input(letter) is True.

# Extra exercise 2. 
# A forgetful user inputs the same letter several times. Make sure that if the letter has already been checked, you don't use it again and ask the user to input another letter. Hint: use an extra variable to store letters that already appeared. Modify the loop from exercise above to check another condition.

# Extra exercise 3. 
# Restructure the program such that it doesn't need to be run anew to play a re-match. E.g. add an extra question at the end of the game asking if the user wants a re-match. If the user answers 'yes' or 'y', the program automatically start another round: draw a new word, set the errors count to zero etc.
# The program will stop once the user says they don't want to play a new game (the user enters 'no' or 'n').
