# -*- coding: utf-8 -*-
"""

Here we will use map, filter, reduce to count the words in the data provided
Threading will be used to optimise this process

@author: A00209408
"""

import concurrent.futures


def count_occurences(data: []) -> {}:
    """
    Counts word occurences within the data provided

    Parameters
    ----------
    data : []
          Book data split up into lines

    Returns
    -------
    {}
        A dictionairy of words with their occurences within the book

    """
    return {}

def map(func , data: []) -> {}:
    """
    
    Executes the specified function provided by the user on a number of threads

    Parameters
    ----------
    func : TYPE
        DESCRIPTION.
    data : []
        DESCRIPTION.

    Returns
    -------
    None.

    """
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        output = executor.map(func, data)
        #print(output)
    return func(data)