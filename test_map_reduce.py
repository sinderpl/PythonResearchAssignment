# -*- coding: utf-8 -*-
"""
Testing for the map reduce methods

@author: A00209408
"""
import map_reduce
import time
import main

contents = {}
with open("data/pride_prejudice_long.txt", encoding='utf8') as file:
    contents = file.readlines()

input_words = ["Lorem ipsum , lorem"
               ,"magna aliqua."
               ,"veniam"]

expected_outputs = [{'lorem': 2, 'ipsum': 1},
                    {'magna': 1, 'aliqua': 1},
                    {'veniam': 1}]

def test_threaded_word_count():
    """
    Test the threaded map function

    Returns
    -------
    None.

    """
    output = map_reduce.map_threaded(main.map_word_count, input_words)
    assert(output == expected_outputs)
    
def test_multiprocess_word_count():
    """
    Test the multiprocess map function
    Returns
    -------
    None.

    """
    output = map_reduce.map_multiprocess(main.map_word_count, input_words)
    assert(output == expected_outputs)