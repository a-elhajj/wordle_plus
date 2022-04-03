#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 12:50:20 2022

@author: alexanderel-hajj
"""




            if letter == word_split[index]:
                print(f'Correct guess! letter {index} matches')
                letter_color = colored(letter, 'green')
                print(letter_color)
                
                if index==0:
                    index_0 = letter_color + word[1:5]
                    print(index_0)
                    
                if index==1:
                    index_1 = index_0 + letter_color + word[1:5]
                    print(index_1)
                    
                if index==2:
                    index_2 = index_1 + letter_color + word[3:5]
                    print(index_2)
                    
                if index==3:
                    index_3 = index_2 + letter_color + word[4:5]
                    print(index_3)
                    
                if index==4:
                    index_4 = index_3 + letter_color
                    print(index_4)







    
    
    
    if letter in word:
        index_of_match = [p for p, c in enumerate(word) if c == letter]
        print("letter in word")
        print(f"index_of_match: {index_of_match}")
        print(f"Number of letters that match: {len(index_of_match)}")
        
        letter_color = colored(letter, 'green')
        guess_word = [letter_color if idx in index_of_match else lett \
                      for idx, lett in enumerate(guess_1)]
        guess_word = ''.join(guess_word)
        print(f"guess_word: {guess_word}")





        if guess_1_split[0] == word_split[0]:
            print(Fore.GREEN + str(guess_1_split[0]) + Style.RESET_ALL)
            print(Fore.GREEN + str(guess_1_split[0]) + Style.RESET_ALL + \
                  str(guess_1[1:5]))
                
                
                
                
        if guess_1_split[0] in word:
            print('first letter in word')
        break
            
            
            
        elif guess_1_split[0] in word:
            print(Fore.YELLOW + str(guess_1_split[0])+ Style.RESET_ALL)
        
        
        
        break
    
    






print("Input a word")
guess_1 = input()

print(guess_1)







