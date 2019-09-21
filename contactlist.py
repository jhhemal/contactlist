#!/usr/bin/env python3

import pickle
F = open('contacts.txt', 'rb')
contacts = pickle.load(F)
while True:
	print('Enter a name here (blank to quit) :')
	uname = input()
	if uname == '':
		break

	if uname in contacts:
		print(f"Name : {contacts[uname]['name']}\n Mobile Number : {contacts[uname]['number']}")
	else:
		print(f"You don't have information about {uname} ")
		print("DO you want to save it? (y/n) : ")
		while True:
			dec = input().lower()
			if dec == 'y' or dec == 'n':
				break
			print('You need to enter y or n from keyboard')
		if dec == 'y':
			print('What is his Full name : ')
			f_name = input()
			print('What is his mobile number : ')
			m_number = input()
			contacts[uname] = {'name' : f_name, 'number' : m_number}
			print('Your data has been added.')
			F1 = open('contacts.txt', 'wb')
			pickle.dump(contacts, F1)
			F1.close()
		else:
			break