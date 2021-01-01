# -*- coding: utf-8 -*-
"""

Here we will use map, filter, reduce to count the words in the data provided
Threading will be used to optimise this process

@author: A00209408
"""

import concurrent.futures
from multiprocessing import Pool


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

def f(x):
    return x * x

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
    output = list()
    # with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    #     executor.map(func, data)
    # return output
    
    # with Pool(2) as p:
    #     p.map(func, data)
    # return {}
    
    output = list()
    with Pool(2) as p:
        output = p.map(func, data)
    return output
    
def reduce(func, data: []) -> {}:
    """
    Reduces the inputs based on the function provided by the caller

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