# -*- coding: utf-8 -*-
"""

Here we will use map, filter, reduce to count the words in the data provided
Threading will be used to optimise this process

@author: A00209408
"""

import concurrent.futures
import multiprocessing as mp
from multiprocessing import Pool

max_cores = mp.cpu_count()

def map_threaded(func , data: []) -> {}:
    """
    
    Executes the specified function provided by the user on a number of threads

    Parameters
    ----------
    func : TYPE
        function for processing
    data : []
        Iterable data set

    Returns
    -------
    output : Dictionairy
        List of outputs for further reduction and reconciliation

    """
    output = list()
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_cores) as executor:
        output += executor.map(func, data)
    return output

def map_multiprocess(func, data: []) -> {}:
    """
    Executes the specified function provided by the user on a number of multi process threads

    Parameters
    ----------
    func : TYPE
        function for processing
    data : []
        Iterable data set

    Returns
    -------
    output : Dictionairy
         List of outputs for further reduction and reconciliation

    """
    output = list()
    with Pool(max_cores) as p:
        output += p.map(func, data)
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