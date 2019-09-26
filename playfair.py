#!/usr/bin/python

import sys

def main():
	CHAR =  "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	CHAR = dict.fromkeys(list(CHAR))

	argc = len(sys.argv) - 1
	if argc != 1:
		print("Improper number of arguments")
		quit()
	elif (not sys.argv[1] == "-e") and (not sys.argv[1] == "-d"):
		print("Only '-e' and '-d' arguments accepted")
		quit()

	string = input("Please enter input: ").upper()
	string = fix_string(string)
	key = input("Please enter key: ").upper()
	key = fix_key(dict.fromkeys(key))
	
	toadd = [x for x in CHAR if x not in key]

	if len(key) > 10:
		print("Key value may not contain more than 10 unique charcters")
		quit()

	key_matrix = key.copy()
	key_matrix.extend(toadd)
	key_matrix.remove("J")
	key_matrix = [key_matrix[i:i+5] for i in range(0, len(key_matrix), 5)]
	print(string)
	print(len(string))



def encrypt(string_list, matrix):
	for pair in string_list:

		pos1 = get_position(pair[0], matrix)
		pos2 = get_position(pair[1], matrix)

		if pos1[0] == pos2[0]:
			pair[0] = matrix[pos1[0]][(pos1[1]+1)%4]
			pair[1] = matrix[pos2[0]][(pos2[1]+1)%4]

		elif pos1[1] == pos2[1]:
			pair[0] = matrix[(pos1[0]+1)%4][pos1[1]]
			pair[1] = matrix[(pos2[0]+1)%4][pos2[1]]
			
		else:
			pair[0] = 




def fix_key(key):
	key = list(key)

	for i in range(len(key)):
		if " " in key:
			key.remove(" ")

	return key


def fix_string(string):
	string = list(string)

	for i in range(len(string)):
		if " " in string:
			string.remove(" ")

	i=0
	for a in range(len(string)//2):
		if string[i]==string[i+1]:
			string.insert(i+1, 'X')
		i=+2

	if len(string)%2==1:
		string.append('X')

	string = [string[i:i+2] for i in range(0, len(string), 2)]

	return string

def get_position(character, matrix):
	for i in range(5):
		for j in range(5):
			if matrix[i][j]==character:
				return i, j

main()    