"""
Module Description
==================
This module contains the functions allowing for loading the necessary files, and performing the
functions for the program by importing from the functions in the other modules.

Copyright and Usage Information
===============================
This file is intended exclusively for academic use for the University of Toronto St. George Campus
in the CSC110 class of Fall 2021. Any distribution of this code, with or without changes,
are expressly prohibited.

This file is Copyright (c) 2021 Madeline Ahn, and Samuel Weiss.
"""
from menu import run_menu
from data_handler import create_datasets

if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={
        'max-line-length': 100,
        'extra-imports': ['data_handler', 'menu'],
        'disable': ['R1705', 'C0200']
    })
    run_menu(create_datasets('data'))
