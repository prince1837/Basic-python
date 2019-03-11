# def numbers_greater_than_twenty(list):
#   counter = 0
#   while counter < len(list):
#     item = list[counter]
#     if item > 20:

#       list.remove(item)
#     else:
#     	counter=counter+1
#   return list

# num_list = [12, 312, 42, 123, 5, 12, 53, 75, 123, 62, 9]
# print "Initial list",num_list

# num_list_20 = numbers_greater_than_twenty(num_list)
# print "List that doesn't contain numbers_less_than_twenty 20",num_list






# from random import randint

# def win():
#     print 'You win!'

# def lose():
#     print 'You lose!'

# while True:
#     player_choice = raw_input('What do you pick? (rock, paper, scissors)')
#     player_choice.strip()
#     random_move = randint(0, 2)
#     moves = ['rock', 'paper', 'scissors']
#     computer_choice = moves[random_move]

#     if player_choice == computer_choice:
#         print 'Draw!'
#     elif player_choice == 'rock' and computer_choice == 'scissors':
#         win()
#     elif  player_choice == 'paper' and computer_choice == 'scissors':
#         lose()
#     elif player_choice == 'scissors' and computer_choice == 'paper':
#         win()
#     elif player_choice == 'scissors' and computer_choice == 'rock':
#         lose()
#     elif player_choice == 'paper' and computer_choice == 'rock':
#         win()
#     elif player_choice == 'rock' and computer_choice == 'paper':
#         lose()
#     again = raw_input('Do you want to play again? (y or n)').strip()
#     if again == 'n':
#         break




# chars =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# shifted_chars = ['c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b']
# def find_in_list(query, mainlist):
#     mainlist_len = len(mainlist)
#     range_for_loop = range(mainlist_len)
#     index = None
#     for i in range_for_loop:
#         element = mainlist[i]
#         if element == query:
#             index = i
#     return index
# def encrypt_message(plain_msg):
#     encrypted_msg = ""
#     for character in plain_msg:
#         if character in chars:
#             char_index = find_in_list(character, chars)
#             new_char = shifted_chars[char_index]
#             encrypted_msg = encrypted_msg + new_char
#         else:
#             encrypted_msg = encrypted_msg + character
#     return encrypted_msg
# def decrypt_message(encrypted_msg):
#     decrypted_msg = ""
#     for character in encrypted_msg:
#         if character in shifted_chars:
#             char_index = find_in_list(character, shifted_chars)
#             new_char = chars[char_index]
#             decrypted_msg = decrypted_msg + new_char
#         else:
#             decrypted_msg = decrypted_msg + character
#     return decrypted_msg
# flag = True
# while flag == True:
#     choice = raw_input("What do you want to do? 1. Encrypt a message 2. Decrypt a message  Enter `e` or `d` respectively!\n")
#     if choice == 'e':
#         plain_message = raw_input("Enter message to dicrypt?\n")
#         print encrypt_message(plain_message)
#     else:
#         if choice == 'd':
#         	encrypted_msg = raw_input("Enter message to encrypt?\n")
#         	print decrypt_message(encrypted_msg)
#     play_again = raw_input("Do you want to try agian or Do you want to exit? (Y/N)")
#     if play_again == 'y':
#         continue
#     elif play_again == 'n':
#         break




# import random
# alive = True
# stamina = 10
# def report(stamina):
#     if stamina > 8:
#         print "The alien is strong! It resists your pathetic attack!"
#     elif stamina > 5:
#         print "With a loud grunt, the alien stands firm."
#     elif stamina > 3:
#         print "Your attack seems to be having an effect! The alien stumbles!"
#     elif stamina > 0:
#         print "The alien is certain to fall soon! It staggers and reels!"
#     else:
#         print "That's it! The alien is finished!"

# def fight(stamina):
#     while stamina > 0:
#         response = raw_input(" Enter a move 1.Hit 2.attack 3.fight 4.run\n")
#         if "hit" in response or "attack" in response :
#             less = random.randint(0, stamina)
#             stamina = less
#             stamina -= less
#             print stamina
#             print less
#             report(stamina)
#         elif "fight" in response:
#             print "Fight how? You have no weapons, silly space traveler!"
#         elif "run" in response:
#             print "Sadly, there is nowhere to run.",
#             print "The spaceship is not very big."
#         else:
#             print "The alien zaps you with its powerful ray gun!"
# print "A threatening alien wants to fight you!"
# fight(stamina)
# if alive == True:
#     print "The alien has been vanquished. Good work!"    
# else:
#     print "The alien lives on, and you, sadly, do not."





# import random
# alive = True
# stamina = 10
# def report(stamina):
#     if stamina > 8:
#         print "The alien is strong! It resists your pathetic attack!"
#     elif stamina > 5:
#         print "With a loud grunt, the alien stands firm."
#     elif stamina > 3:
#         print "Your attack seems to be having an effect! The alien stumbles!"
#     elif stamina > 0:
#         print "The alien is certain to fall soon! It staggers and reels!"
#     else:
#         print "That's it! The alien is finished!"

# def fight(stamina):
#     while stamina > 0:
#         response = raw_input(" Enter a move 1.Hit 2.attack 3.fight 4.run\n")
#         if "hit" in response or "attack" in response :
#             less = random.randint(0, stamina)
#             stamina -= less
#             report(stamina)
#         elif "fight" in response:
#             print "Fight how? You have no weapons, silly space traveler!"
#         elif "run" in response:
#             print "Sadly, there is nowhere to run.",
#             print "The spaceship is not very big."
#         else:
#             print "The alien zaps you with its powerful ray gun!"
# print "A threatening alien wants to fight you!"
# fight(stamina)
# if alive == True:
#     print "The alien has been vanquished. Good work!"    
# else:
#     print "The alien lives on, and you, sadly, do not."



