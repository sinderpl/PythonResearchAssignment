# -*- coding: utf-8 -*-
"""
Reads in text files and analyzes the data contained within it

@author: A00209408
"""

import re
import map_reduce
import assistance_functions

user_loop = True
test_book_long = "data/pride_prejudice_long.txt"
test_book_short = "data/pride_prejudice.txt"

def read_text_file(file_to_read)-> []:
    """
    Reads in a user specified file and returns it as an array of lines

    Returns
    -------
    []
        Array of lines from the text file

    """
    #while user_loop:
    #user_choice = input("")
    try:
        with open(file_to_read, encoding='utf8') as file:
            contents = file.readlines()
            return contents
    except FileNotFoundError:
        print("The file could not be found")
        return None
    
def map_word_count(data: []) -> {}:
    """
     Maps the words in a array treating each item in array as a line

    Parameters
    ----------
    data : []
        Array of lines from the book

    Returns
    -------
    result : dictionairy of word occurences

    """
    result = {}
    try:
        words  = re.findall(r'\w+', data)
        for word in words:
            word = word.lower()
            if word in result:
                result[word] = result[word] + 1
            else :
                result[word] = 1
    except TypeError :
        pass
    return result

def map_word_reduce(data: []) -> {}:
    """
    

    Parameters
    ----------
    data : []
        DESCRIPTION.

    Returns
    -------
    None.

    """
    return {}



def test_runtimes_reduce(outputs):
    return 0
    
if __name__ == "__main__":
    file_content = read_text_file()
    #assistance_functions.test_runtimes_map(file_content)
    #print(map_word_count(str(file_content)))
    #mpr.map(map_word_count, file_content)
    #test_runtimes(file_content)
    
    