# -*- coding: utf-8 -*-
"""
Reads in text files and analyzes the data contained within it

@author: A00209408
"""

import re
import map_reduce as mpr

user_loop = True
test_book = "data/pride_prejudice.txt"

def read_text_file()-> []:
    """
    Reads in a user specified file and returns it as an array of lines

    Returns
    -------
    []
        Array of lines from the text file

    """
    #while user_loop:
    #user_choice = input("")
    with open(test_book, encoding='utf8') as file:
        contents = file.readlines()
        return contents

def map_book(data: []) -> {}:
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
    #for line in data:
    #for word in data:
    print(data)
    words  = re.findall(r'\w+', data)
    
    for word in words:
        if word in result:
            result[word] = result[word] + 1
        else :
            result[word] = 1
    #print(result)
    return result

if __name__ == "__main__":
    file_content = read_text_file()
    mpr.map(map_book, file_content)
    #print(mpr.map(map_book, file_content))