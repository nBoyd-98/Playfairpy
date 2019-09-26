#!/usr/bin/python

import sys

#Create list of alphabetic chars to check against
CHAR =  "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
CHAR = dict.fromkeys(list(CHAR))

def main():

	#Input validation
	argc = len(sys.argv) - 1
	if argc != 1:
		print("Improper number of arguments")
		quit()
	elif (not sys.argv[1] == "-e") and (not sys.argv[1] == "-d"):
		print("Only '-e' and '-d' arguments accepted")
		quit()

	#Send input string to fix_string in order to get needed format
	string = input("Please enter input: ").upper()
	string = fix_string(string)

	#send key to fix_key in order to get needed format
	key = input("Please enter key: ").upper()
	key = fix_key(dict.fromkeys(key))
	
	#toadd is list of chars in already in key, add to key matrix
	toadd = [x for x in CHAR if x not in key]

	#now that key has been fixed, test that there is at least one char and no more than 10
	if len(key) > 10:
		print("Key value may not contain more than 10 unique charcters")
		quit()
	elif len(key) < 1:
		print("Key value must contain at least one character")
		quit()

	#add chars to key matrix, remove J char, slice into 2d list
	key_matrix = key.copy()
	key_matrix.extend(toadd)
	key_matrix.remove("J")
	key_matrix = [key_matrix[i:i+5] for i in range(0, len(key_matrix), 5)]
	
	#if '-e', encrypt data and print out
	if sys.argv[1] == "-e":
		print("Encrypting data...")
		string = encrypt(string, key_matrix)
		l=[]
		for item in string:
			l.extend(item)
		l = ''.join(l)
		print(l)

	#if '-d', decrypt data and print out
	elif sys.argv[1] == "-d":
		print("Decrypting data...")
		string = decrypt(string, key_matrix)
		l=[]
		for item in string:
			l.extend(item)
		l = ''.join(l)
		print(l)



def encrypt(string_list, matrix):
	for item in string_list:

		if len(item) >= 2:
			pos1 = get_position(item[0], matrix)
			pos2 = get_position(item[-1], matrix)


			if pos1[0] == pos2[0]:
				item[0] = matrix[pos1[0]][(pos1[1]+1)%4]
				item[-1] = matrix[pos2[0]][(pos2[1]+1)%4]

			elif pos1[1] == pos2[1]:
				item[0] = matrix[(pos1[0]+1)%4][pos1[1]]
				item[-1] = matrix[(pos2[0]+1)%4][pos2[1]]
				
			else:
				item[0] = matrix[pos1[0]][pos2[1]]
				item[-1] = matrix[pos2[0]][pos1[1]]

	return string_list

def decrypt(string_list, matrix):
	for item in string_list:

		if len(item) >= 2:
			pos1 = get_position(item[0], matrix)
			pos2 = get_position(item[-1], matrix)

			if pos1[0] == pos2[0]:
				item[0] = matrix[pos1[0]][(pos1[1]-1)%5]
				item[-1] = matrix[pos2[0]][(pos2[1]-1)%5]

			elif pos1[1] == pos2[1]:
				item[0] = matrix[(pos1[0]-1)%5][pos1[1]]
				item[-1] = matrix[(pos2[0]-1)%5][pos2[1]]
				
			else:
				item[0] = matrix[pos1[0]][pos2[1]]
				item[-1] = matrix[pos2[0]][pos1[1]]

	return string_list

#'fixes' key by 
def fix_key(key):
	key = list(key)

	for i in key:
		if i not in CHAR:
			key.remove(i)

	return key


def fix_string(string):
	string = list(string)

	i=0
	for a in range(len(string)//2):
		if string[i]==string[i+1]:
			string.insert(i+1, 'X')
		i=+2

	charcount=0
	for a in string:
		if a in CHAR:
			charcount+=1

	if charcount%2==1:
		string.append('X')

	i=0
	new_string = []
	for a in range(len(string)):
		if i<len(string) and string[i] in CHAR:
			start = i
			i+=1
			while i<len(string) and string[i] not in CHAR:
				i+=1
			seg = string[start:i+1]
			new_string.append(seg)
			i+=1
		elif i<len(string) and string[i] not in CHAR:
			new_string.append(string[i])
			i+=1

	return new_string

def get_position(character, matrix):
	if character != "J":
		for i in range(5):
			for j in range(5):
				if matrix[i][j]==character:
					return i, j
	else:
		return 0, 0

main()    