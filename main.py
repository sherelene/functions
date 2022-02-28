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
This is your encrypted phrase:  WIY


Hello please enter a word or sentence: 
are you feeling it now mr.krabs
You inputted: "are you feeling it now mr.krabs"
There are 31 characters in the text you inputted
This is your input without spaces or tabs: areyoufeelingitnowmr.krabs

Enter a new phrase: 
live and let die
This is your new phrase as an acronym: LALD

Now let us do some encryptions
Please input the word or sentence you would like to be encrypted: 
noice
Please input what you would like your key to be: 
bpzhgocvjdqswkimlutneryaxf
This is your encrypted phrase:  ejfbl


Hello please enter a word or sentence: 
a			lj		ij   kjk kjk kjll
You inputted: "a			lj		ij   kjk kjk kjll"
There are 25 characters in the text you inputted
This is your input without spaces or tabs: aljijkjkkjkkjll

Enter a new phrase: 
i'm loving it
This is your new phrase as an acronym: ILI

Now let us do some encryptions
Please input the word or sentence you would like to be encrypted: 
McLovin
Please input what you would like your key to be: 
bpzhgocvjdqswkimlutneryaxf
This is your encrypted phrase:  YbOjsfe

Process finished with exit code 0

'''