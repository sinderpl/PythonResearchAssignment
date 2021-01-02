# -*- coding: utf-8 -*-
"""

    In this file I will keep any functions I have written / used / referred to in the report
    but which are not directly related to the programme execution
    
    This is to prove that the code was done while keeping a good encapsulation and separation of concens

@author: A00209408
"""

import map_reduce
import time
import main

def test_runtimes_map(file_content):
    
    # runtime for the default method implementation
    t0 = time.time()
    main.map_word_count(str(file_content))
    t1 = time.time()
    total_runtime_threaded = t1 - t0
    print("Runtime of default method : ",  total_runtime_threaded)
    
    # runtime for the default python threading library
    t0 = time.time()
    map_reduce.map_threaded(main.map_word_count, file_content)
    t1 = time.time()
    total_runtime_threaded = t1 - t0
    print("Runtime of threaded method : ",  total_runtime_threaded)
    
    # runtime for the multiprocessing python library
    t0 = time.time()
    map_reduce.map_multiprocess(main.map_word_count, file_content)
    t1 = time.time()
    total_runtime_threaded = t1 - t0
    print("Runtime of multiprocessing method : ",  total_runtime_threaded)