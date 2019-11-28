#!/usr/bin/env python3
#
# contactlist.py - A python program to store your contact data
#
# Author : Jahidul Hasan Hemal
#
# url: https://jhhemal.github.io
# 
import json
print("ContactList.py".center(50,'*'))
filename = 'contacts.json'
while True:
	print('Enter a name here (blank to quit) :')
	uname = input()
	if uname == '':
		break
	try:
		with open(filename) as f:
			contacts = json.load(f)
		
	except FileNotFoundError:
		print("You don't have the file contact.json, Let's create it first.")
		print("The file will be creating with the name you have entered.")
		print("DO you want to save it? (y/n) : ")
		contacts = {}
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
			with open(filename,'w') as f:
				json.dump(contacts, f)
			print('Your data has been added.')
		else:
			break
	
	else:
		if uname in contacts:
			print("Name ".ljust(14) + ": ".ljust(2) + contacts[uname]['name'])
			print("Mobile Number :".ljust(16) + contacts[uname]['number'])
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
				with open(filename,'w') as f:
					json.dump(contacts, f)
				print('Your data has been added.')
			else:
				break
