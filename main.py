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
            if word.isalpha():
                word = word.lower()
                if word in result:
                    result[word] = result[word] + 1
                else :
                    result[word] = 1
    except TypeError :
        pass
    return result

def map_word_reduce(data: [], result_dictionary: {}) -> {}:
    """
    Reconciles the output data and parses it back into a single dictionary
    using basic Python code

    Parameters
    ----------
    data : []
        Otuput data from map methods split into chunks.
    result_dictionary : {}
        DESCRIPTION.

    Returns
    -------
    result_dictionary : dictionairy of word occurences

    """
    for word, occurence in data.items():
        if word in result_dictionary:
            result_dictionary[word] += occurence
        else:
            result_dictionary[word] = occurence
    return result_dictionary

def map_word_reduce(data: [], result_dictionary: {}) -> {}:
    """
    Reconciles the output data and parses it back into a single dictionary
    using thread locks to avoid race conditions

    Parameters
    ----------
    data : []
        Otuput data from map methods split into chunks.
    result_dictionary : {}
        DESCRIPTION.

    Returns
    -------
    result_dictionary : dictionairy of word occurences

    """
    for word, occurence in data.items():
        if word in result_dictionary:
            result_dictionary[word] += occurence
        else:
            result_dictionary[word] = occurence
    return result_dictionary

def map_word_reduce_iterate(data: [], result_dictionary: {}) -> {}:
    """
    Iterates over the outer structures of the file so that it can be used 
    with normal array with the reduce method

    Parameters
    ----------
    data : []
          Lines of data to iterate over and reduce
    result_dictionary : {}
        Output word counts

    Returns
    -------
    result_dictionary :Dictionairy of word counts

    """
    for line in data:
         map_word_reduce(line, result_dictionary)
    return result_dictionary

if __name__ == "__main__":
    file_content = read_text_file(test_book_short)
    
        #Normal code map and reduce
        #The mapping in this case also reduces by default
    # output_map = map_word_count(str(file_content))
    # print(output_map)
    
        #Here you can test the reduce method based on the output from the threaded method
    #output_map = map_reduce.map_threaded(map_word_count, file_content)
    #output_reduce_normal = map_reduce.map_word_reduce_iterate(output_map, {})
    #print(output_reduce_normal)
    
        #Threaded map and reduce
    #output_map = map_reduce.map_threaded(map_word_count, file_content)
    #output_reduce_threaded = map_reduce.reduce_multiprocess(map_word_reduce, output_map)
    #print(output_reduce_multiprocess)
    
        #Multiprocess map and reduce 
    #output_map = map_reduce.map_multiprocess(map_word_count, file_content)
    #output_reduce_multiprocess = map_reduce.reduce_multiprocess(map_word_reduce, output_map)
    #print(output_reduce_multiprocess)
    
        #Time testing and comparison functions
    assistance_functions.test_runtimes_map(file_content)
    
    