#meaningpedia api

import replit
from replit import db
import re
import requests
import random
from time import sleep
import constants

curUser = "Guest"
curPasw = "123"
hidword = "NO"
back_up = hidword

def conClear():
		print("Clearing.", end="")
		print("\r", end="")
		sleep(0.3)
		print("Clearing..", end="")
		print("\r", end="")
		sleep(0.3)
		print("Clearing...", end="")
		print("\r", end="")
		sleep(0.3)
		replit.clear()
	
class Accounts():
	def __init__(self, username, password):
		self.user = username
		self.pasW = password
		
	def login (self):
		print(constants.White)
		if self.user not in db.keys():
			print(f"That is not a valid username")
			return False
		if db[self.user][0] == self.pasW:
			print(f"Login successful.")
			curUser = db[self.user]
			return True
		else:
			print("I'm sorry, that is incorrect")
			return False

	def signup(self):
		while True:
			user = input("What is your new username?: ")
			while user in db.keys():
				print("That is not a valid username! Please try again.\n")
				user = input("What is your new username?")
			
			passW = input("Okay! What is the password?")
			print("Sure. Registering the account... this might take a while.")
			db[user] = [passW, "0", "0"]
			print(f'''Done. Your account is registered. \nUsername: {user}, Password: {passW}, Wins: {db[user][1]}, Loses: {db[user][2]}	\nDon't forget! Please don't make multiple accounts.''')
			curUser = user
			conClear()
			return

	def delete(self):
		confirm = input("\nAre you sure you want to delete your account? All your data will be wiped. (yes/no): ")
		if confirm.lower() == "yes":
			del db[curUser]
			
	def change_password(self):
		newPass = input("What is the new password?")
		db[curUser][0] = newPass
		print("Success!", end="")
		print("\r", end="")

	def __repr__(self):
		return self.user

#login
    
userAcc = input("Do you have an account? (yes/no): ")

if userAcc.lower() == "yes":
	attempts = 0
	logres = False
	while not logres and attempts < 5:
		logres = Accounts(input("Username? "), input(f"Password? {constants.invisible}")).login()
		attempts += 1
	if attempts >= 5:
		print("You have reached your maximum attempt limit.")
else:
	signup = input('''Do you want to sign up? 
A guest account works too, except your stats will not be saved. yes/no: ''')

	if signup.lower() == "yes":
		Accounts(curUser, curPasw).signup()

def checkBad(num):
	if num == 4043:
		return False
	elif num == 566:
		return False
	else:
		return True

class Wordle():
	def __init__(self):
		pass
		
	#following code imported from https://gist.github.com/iancward/afe148f28c5767d5ced7a275c12816a3 cause I can't api
	def fetch_word(self, letters):
		meaningpedia_resp = requests.get(
			f"https://meaningpedia.com/{letters}-letter-words?show=all")
		pattern = re.compile(r'<span itemprop="name">(\w+)</span>')
		word_list = pattern.findall(meaningpedia_resp.text)
		#4043 is bad word, 566: 6363 total
	
		finalIn = random.randint(0, 6364)
		ohno = False
	
		if not checkBad(finalIn):
			ohno = True
			
		while ohno:
			finalIn = random.randint(0, 6364)
	
			if checkBad(finalIn):
				return word_list[finalIn]
			
		hidword = word_list[finalIn]
		back_up = hidword

  def guess(guess):
    greens = [""]
    yellows = [""]
    none = [""]
    
    back_upup = guess

		for i in len(back_upup):
			if guess[i] == back_up[i]:
        print(f"{constants.green}{guess[i]}{constants.White}")
      elif guess.find(str, beg=0, end=len(string)) != -1:
        
    
	#games begin
	def wordle():
		guess = input("Game has begun! Insert your first guess\nNote: Yellow means it is in the string.\nGreen means it is at the correct place.")
		guess(guess)
    guess(input("Next guess?"))

		for i in len(back_upup):
			if guess[i] == back_up[i]
		
	def insOption():
		option = input(f'''{constants.bright_blue}What would you like to do?
		{constants.Blue}1. Start a new game
		{constants.Red}2. Delete acccount
        {constants.cyan}3. Change password
		{constants.Green}4. Log out
		{constants.Orange}5. View profile\n{constants.White}''') #keep #3 like that, there's an issue
	
		return option

	def reOpt ():
		option = Wordle.insOption()
		if option == "1":
			Wordle.wordle()
		elif option == "2" and curUser != "Guest":
			Accounts(curUser, curPasw).delete
		elif option == "4":
			raise SystemExit
		elif option == "5":
			print(f'''Stats for user: {curUser}:
	Wins: {db[curUser][1]}
	Losses: {db[curUser][2]}''')
		elif option == "3" and curUser != "Guest":
			Accounts(curUser, curPasw).change_password()
		else:
			print("Not a valid option. Try again.")
			Wordle.reOpt() #recursion but not recursion?

Wordle.reOpt()
