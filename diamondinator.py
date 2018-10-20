#!/bin/py
#
# daimondinator.py
# 
# Author: Nathaniel Grisham
# 20 October 2018
#

from __future__ import print_function
import sys

class Diamondinator:

	#
	# By default, print output to stdout
	#
	outfile = sys.stdout

	# 
	# Function daimondinate:
	# Print letters from 'A' through the input letter.
	# The printed letters shape the outline of a diamond.
	# Input:
	# letter_in - an alphabet letter, may be uppercase or lowercase
	#
	# Output:
	# Print a diamond starting with 'A' with the supplied letter at the widest point.
	# For example: print-diamond 'C' prints:
	#   A
	#  B B
	# C   C
	#  B B
	#   A
	# The letters in the diamond match the case of the input letter.
	#
	# Return values:
	# 0 on a succesful execution
	# -1 if the input is not a letter
	#
	@classmethod
	def diamondinate(self, letter_in):
		#Return early on invalid input
		try:
			if not letter_in.isalpha() or len(letter_in) != 1:
				print("Invalid input (" + letter_in + ")! diamondinate accepts only a single letter character as input.",
				 file=sys.stderr)
				print("Invalid input!", file=self.outfile)
				return -1
		except:
			print("Invalid input! diamondinate accepts only a single letter character as input.",
			 file=sys.stderr)
			print("Invalid input!", file=self.outfile)
			return -1
		#Determine case of the input letter
		if letter_in.istitle():
			letter_a = 'A'
		else:
			letter_a = 'a'
		#placeholders for space padding
		lead_space = ord(letter_in) - ord(letter_a)
		inner_space = 1
		cursor = chr(ord(letter_a)+1)
		#print initial "a"
		print(" " * lead_space + letter_a, file=self.outfile)
		#if a is the input letter, we are done
		if letter_in == letter_a:
			return 0
		lead_space -= 1
		#Iterate from 'a' through the input letter
		while ord(cursor) < ord(letter_in):
			print(" " * lead_space + cursor + " " * inner_space + cursor, file=self.outfile)
			cursor = chr(ord(cursor) + 1)
			lead_space -= 1
			inner_space += 2
		#Iterate back down to 'a'
		while ord(cursor) > ord(letter_a):
			print(" " * lead_space + cursor + " " * inner_space + cursor, file=self.outfile)
			cursor = chr(ord(cursor) - 1)
			lead_space += 1
			inner_space -= 2
		#Print final 'a'
		print(" " * lead_space + letter_a, file=self.outfile)

# When run from the command line,
# Read a character from stdin and run diamondinate on it.
if __name__ == '__main__':
	myClass = Diamondinator()
	myClass.diamondinate(raw_input("Enter a character to diamondinate: "))
	