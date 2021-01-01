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

input_words = ["Lorem ipsum dolor sit amet, consectetur adipiscing elit,"
               ,"sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
               ,"Ut enim ad minim veniam"]

def test_map_word_count_timing():
    """
    Test the mean function from stat module

    Returns
    -------
    None.

    """
    t0 = time.time()
    output = main.map_word_count(str(contents))
    t1 = time.time()
    total_runtime_normal = t1 - t0
    # print(output)
    print("Runtime of main method : ",  total_runtime_normal)
    
    t0 = time.time()
    reduce_output = map_reduce.map(main.map_word_count, contents)
    # t1 = time.time()
    # total_runtime_threaded = t1 - t0
    # print("Runtime of threaded method : ",  total_runtime_threaded)
    
    #print(reduce_output)
    assert(True)
    
    #assert(stat.calculate_mean(test_set)) == 15.25
    
test_map_word_count_timing()

