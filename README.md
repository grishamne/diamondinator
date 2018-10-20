# diamondinator

### Introduction

The Diamondinator class provides an API for printing a diamond shape outlined by letters. It is written in Python 2 and can be used within a program, or called from the command line. 

### diamondinate

The class method `Diamondinator.diamondinate` takes a single letter character as input and prints a diamond shape outlined by letters. The top and bottom of the diamond are made up of the letter 'A'. Each line further inside is the next letter in the alphabet, with the widest part of the diamond containing the letter that was input. The letters that make up the diamond match the case of the letter that is input.

Ouput is printed to `Diamondinator.outfile`, which is `stdout` by default.

### Running diamondinator from the command line

When run from the command line, diamondinator prompts the user to enter a character, then runs diamondinate to print a diamond to `stdout`. Example:
```
PS C:\Users\Nate\Documents\diamondinator> python diamondinator.py
Enter a character to diamondinate: G
      A
     B B
    C   C
   D     D
  E       E
 F         F
G           G
 F         F
  E       E
   D     D
    C   C
     B B
      A
 ```