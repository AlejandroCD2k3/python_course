""" 
IS IT AN ANAGRAM? Write a function that takes two words (String) 
and returns true or false (Bool) depending on whether they are anagrams or not.

An Anagram consists of forming a word by rearranging ALL the letters of another 
initial word.
It is NOT necessary to check if both words exist.
Two identical words are not anagrams. 
"""

def is_anagram(first_word, second_word):

    first_word = first_word.lower()
    second_word = second_word.lower()

    if(first_word == second_word):
        return False
    else:
        return sorted(first_word) == sorted(second_word)
    
print(is_anagram("Listen","Silent"))