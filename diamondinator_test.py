#!/bin/py
#
# daimondinator_test.py
# 
# Author: Nathaniel Grisham
# 20 October 2018
#

from __future__ import print_function
from diamondinator import Diamondinator
myTest = Diamondinator()
myFile = open("myFile.txt",'w')
Diamondinator.outfile = myFile
#Lower boundary
print("Testing diamondinate on the input 'a':", file=myTest.outfile)
myTest.diamondinate('a')
#Another lower-case test
print("Testing diamondinate on the input 'j':", file=myTest.outfile)
myTest.diamondinate('j')
#An upper-case test
print("Testing diamondinate on the input 'R':", file=myTest.outfile)
myTest.diamondinate('R')
#Upper boundary
print("Testing diamondinate on the input 'Z':", file=myTest.outfile)
myTest.diamondinate('Z')
#Test handling of unwanted input
print("Testing diamondinate on the input '-':", file=myTest.outfile)
myTest.diamondinate('-')
print("Testing diamondinate on the input '':", file=myTest.outfile)
myTest.diamondinate('')
print("Testing diamondinate on 'None' input:", file=myTest.outfile)
myTest.diamondinate(None)
print("Testing diamondinate on the input 'abc':", file=myTest.outfile)
myTest.diamondinate(None)
myTest.outfile.close()
