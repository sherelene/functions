''''
Author: Sherelene De Belen
Class: CS2520
Project2 Task 1
Last Modified: 02/27/22

Purpose: The purpose of this program is to experiment with functions by using text analyzers and modifiers. This code 
outputs number of characters, removes whitespace, creates acronyms, and encrypts phrases through the use of 
Substitution Cypher.  
'''''

from Task1 import *

if __name__ == '__main__':
    repeat = int(input("Number of test runs you'd like to do: "))
    for i in range(repeat):
        main()
