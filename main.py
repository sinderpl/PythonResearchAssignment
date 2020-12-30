# -*- coding: utf-8 -*-
"""
Reads in text files and analyzes the data contained within it

@author: A00209408
"""

user_loop = True
test_book = "data/pride_prejudice.txt"

def read_text_file():
    """

    Returns
    -------
    None.

    """
    while user_loop:
        user_choice = input("")
        with open("test_book") as file:
            contents = file.readlines()
        
if __name__ == "__main__":
