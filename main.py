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




'''
C:\Users\shere\OneDrive\Documents\CPP\SP2022\CS2520\project2\functions\venv\Scripts\python.exe C:/Users/shere/OneDrive/Documents/CPP/SP2022/CS2520/project2/functions/main.py
Number of test runs you'd like to do: 3


Hello please enter a word or sentence: 
The only thing we have to fear is fear itself.
You inputted: "The only thing we have to fear is fear itself."
There are 46 characters in the text you inputted
This is your input without spaces or tabs: Theonlythingwehavetofearisfearitself.

Enter a new phrase: 
random access memory
This is your new phrase as an acronym: RAM

Now let us do some encryptions
Please input the word or sentence you would like to be encrypted: 
RAM
Please input what you would like your key to be: 
bpzhgocvjdqswkimlutneryaxf
This is your encrypted phrase:  UBW


Hello please enter a word or sentence: 
lifes a garden, dig it
You inputted: "lifes a garden, dig it"
There are 22 characters in the text you inputted
This is your input without spaces or tabs: lifesagarden,digit

Enter a new phrase: 
life's a garden, dig it
This is your new phrase as an acronym: LAGDI

Now let us do some encryptions
Please input the word or sentence you would like to be encrypted: 
run
Please input what you would like your key to be: 
bpzhgocvjdqswkimlutneryaxf
This is your encrypted phrase:  uek


Hello please enter a word or sentence: 
aa			kj		kj      ds
You inputted: "aa			kj		kj      ds"
There are 19 characters in the text you inputted
This is your input without spaces or tabs: aakjkjds

Enter a new phrase: 
peace love unity respect
This is your new phrase as an acronym: PLUR

Now let us do some encryptions
Please input the word or sentence you would like to be encrypted: 
PLUR
Please input what you would like your key to be: 
bpzhgocvjdqswkimlutneryaxf
This is your encrypted phrase:  MSEU

Process finished with exit code 0
'''