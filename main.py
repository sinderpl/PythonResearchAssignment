# -*- coding: utf-8 -*-
"""
Reads in text files and analyzes the data contained within it

@author: A00209408
"""

import re
import map_reduce as mpr
import time

user_loop = True
test_book = "data/pride_prejudice_long.txt"

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
            if word in result:
                result[word] = result[word] + 1
            else :
                result[word] = 1
    except TypeError :
        pass
    return result


def test_runtimes(file_content):
    
    # runtime for the default method implementation
    t0 = time.time()
    map_word_count(str(file_content))
    t1 = time.time()
    total_runtime_threaded = t1 - t0
    print("Runtime of default method : ",  total_runtime_threaded)
    
    # runtime for the default python threading library
    t0 = time.time()
    mpr.map_threaded(map_word_count, file_content)
    t1 = time.time()
    total_runtime_threaded = t1 - t0
    print("Runtime of threaded method : ",  total_runtime_threaded)
    
    # runtime for the multiprocessing python library
    t0 = time.time()
    mpr.map_multiprocess(map_word_count, file_content)
    t1 = time.time()
    total_runtime_threaded = t1 - t0
    print("Runtime of multiprocessing method : ",  total_runtime_threaded)
    
if __name__ == "__main__":
    file_content = read_text_file()
    #print(map_word_count(str(file_content)))
    #mpr.map(map_word_count, file_content)
    test_runtimes(file_content)    
    
    