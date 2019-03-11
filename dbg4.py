# def encrypt():
# 	message = raw_input("Enter the message you want to encrypt\n")
# 	ascii_message = [ord(char)+3 for char in message]
# 	encrypt_message = [ chr(char) for char in ascii_message]  
# 	print ''.join(encrypt_message)
# def decrypt():
# 	message = raw_input("Enter the message you want to decrypt\n")
# 	ascii_message = [ord(char)-3 for char in message]
# 	decrypt_message = [ chr(char) for char in ascii_message]  
# 	print ''.join(decrypt_message)
# flag = True
# while flag != False:
# 	choice = raw_input("What do you want to do? \n1. Encrypt a message 2. Decrypt a message \nEnter e or d respectively!\n")
# 	if choice == 'e':
# 		encrypt()
# 	elif choice == 'd':
# 		decrypt()    
# 	else:
# 	    play_again = raw_input("Do you want to try agian or Do you want to exit? (Y/N)\n")
# 	    if play_again == 'Y':
# 	        continue
# 	    elif play_again == 'N':
# 	        break


#  ........................................................................................................

# import random
# def getSecretNum(numDigits):
# 	numbers = list(range(10))
# 	random.shuffle(numbers)
# 	secretNum = ''
# 	for i in range(numDigits):
# 		secretNum += str(numbers[i])
# 	return secretNum

# def getClues(guess, secretNum):
# 	if guess == secretNum:
# 		return 'You got it!'
#   	else:
#   		clue = []
#   		for i in range(len(guess)):
#   			if guess[i] == secretNum[i]:
#   				clue.append('Fermi')
#   			elif guess[i] in secretNum:
#   				clue.append('Pico')
#   			elif guess[i] not in secretNum:
#   				clue.append('bagels')
#   		a=' '.join(clue)
#   	return a

# def isOnlyDigits(num):
# # Returns True if num is a string made up only of digits. Otherwise returns False.
# 	if num == '':
# 		return False
# 	for i in num:
# 		if i not in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
# 			return False
# 	else:
# 		return True


# def playAgain():
# # This function returns True if the player wants to play again, otherwise it returns False.
# 	play = raw_input("Do you want to play again? Yes or No?").lower()
# 	if play=="y":
# 		return True
# 	else:
# 		return False
  

# NUMDIGITS = 3
# MAXGUESS = 10

# print('I am thinking of a %s-digit number. Try to guess what it is.' % (NUMDIGITS))
# print('Here are some clues:')
# print('When I say:    That means:')
# print('  Pico         One digit is correct but in the wrong position.')
# print('  Fermi        One digit is correct and in the right position.')
# print('  None       No digit is correct.')

# while True:
# 	secretNum = getSecretNum(NUMDIGITS)
# 	print('I have thought up a number. You have %s guesses to get it.' % (MAXGUESS))
# 	numGuesses = 1
# 	while numGuesses <= MAXGUESS:
# 		guess = raw_input("Guess Again")
# 		if len(guess) == NUMDIGITS or isOnlyDigits(guess):
# 			print 'Guess  ' + str(numGuesses)
# 			clue = getClues(guess, secretNum)
# 			print(clue)
# 		numGuesses += 1
# 	if guess == secretNum:
# 		break
# 	if numGuesses < MAXGUESS:
# 		print 'You ran out of guesses. The answer was ' + secretNum
# 	if not playAgain():
# 		break


# ----------------------------------------------------------------------------------------------

# import json
# with open('user.json') as data_file:
# 	data = json.load(data_file)

# users = data['users']

# for user in users:
#   counter = 0
#   print "users full name is " + user['firstName'] + ' ' + user['lastName']
#   while counter < len(user['details']):
#     print "users mobile number is " + str(user['details']['mobileNo'])
#     print "users age  is " + str(user['details']['age'])
#     print "users city is " + user['details']['City']
#     counter=counter+1





    


