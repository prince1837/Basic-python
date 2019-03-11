# user=input("enter your number     ")
# a=user
# for i in range(3):
# 	if user%2==0:
# 		user =user-2
# 	else:
# 		user =user+1
# 	print "3 even number  ",user
# for i in range(3):
# 	if a%2!=0:
# 		a=a+2
# 	else:
# 		a=a+1
# 	print "3 odd number  ",a




# user = input("enter your year\n")
# a=user
# if user%100==0 and user%400==0:
# 	i=0
# 	while i<3:
# 		user=user+4
# 		a=a-4
# 		print "leep year",a,user
# 		i=i+1
# elif a%4==0 and a%100!=0:
# 	i=0
# 	while i<3:
# 		user=user+4
# 		a=a-4
# 		print "leep year",a,user
# 		i=i+1
# else:
# 	print user,"leap year nhi hai" 




# user = input("enter your year\n")
# j=0
# while j<1:
# 	a=user
# 	if user%100==0 and user%400==0:
# 		j=j+1
# 		i=0
# 		while i<3:
# 			user=user+4
# 			a=a-4
# 			print "leep year",a,user
# 			i=i+1
# 	elif a%4==0 and a%100!=0:
# 		j=j+1
# 		i=0
# 		while i<3:
# 			user=user+4
# 			a=a-4
# 			print "leep year",a,user
# 			i=i+1
# 	else:
# 		user=user+1






# user=input("enter your number\n")
# a=list(str(user))
# s=0
# for i in a:
# 	d=int(i)**3
# 	s=s+d
# if s==user:
# 	print user,"hai"
# else:
# 	print "nhi hai"



# user=input("enter your number for find the armstrong \n")
# for j in range(1,user+1):	
# 	a=list(str(j))
# 	s=0
# 	for i in a:
# 		d=int(i)**3
# 		s=s+d
# 	if s==j:
# 		print j
	



# user=input("enter your number...........\n")
# for i in range(1,user):
# 	b=0
# 	for j in range(1,i):
# 		if i%j==0:
# 			b=b+j
# 	if b==i:
# 		print i



# user=input("enter your year")
# a=user
# for i in range(1,11):
# 	if user%4==0:
# 		if user%100!=0:
# 			print "after 3 leap year",user
# 			user=user+1			
# 	if user%100==0:
# 		if user%400==0:
# 			print "after 3 leap year",user
# 			user=user+1
# 	else:
# 		user=user+1
# for i in range(1,11):
# 	if a%4==0:
# 		if a%100!=0:
# 			print "before 3 leap year",a
# 			a=a-1			
# 	if a%100==0:
# 		if a%400==0:
# 			print "before 3 leap year",a
# 			a=a-1
#  	else:
#  		a=a-1





# user=input("enter your first number..........")
# user1=input("enter your second number.........")
# a=[user,user1]
# if user1>user:
# 	b=user1
# elif user>user1:
# 	b=user
# for i in range(1,b):
# 	if user%i==0 and user1%i==0:
# 		c=i
# print c





# user=raw_input("enter your first name..........    ")
# user1=raw_input("enter your second name.........    ")
# a=list(user)
# b=list(user1)
# if len(a)==len(b):
# 	i=0
# 	while i<len(a):
# 		if a[i] in b and b[i] in a:
# 			i=i+1
# 			continue
# 		else:
# 			print "anagram nhi hai"
# 			break
# 	else:
# 		print "anagam hai"
# else:
# 	print "ye anagram nhi hai"




#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------




# user =raw_input("enter your string\n")
# if len(user)==1:
# 	print "empty"
# else:
# 	a=user
# 	b=a[:2]+a[-2:]
# 	print b





# user=raw_input("enter your word-----------\n")
# a=user
# if a[-1:]=="e":
# 	print user[:-1]+"ing"
# elif a[-2:]=="ly":
# 	print user
# elif a[-3:]=="ing":
# 	print user+"ly"
# elif a[-3:]!="ing":
# 	print user+"ing"




# user=raw_input("enter your word-----------\n")
# a=user
# if a[-1:]=="e":
# 	print user[:-1]+"ing"
# elif a[-2:]=="ly":
# 	print user
# elif a[-3:]=="ing":
# 	print user[:-3]+"ly"
# elif a[-3:]!="ing":
# 	print user+"ing"







# user=raw_input("enter your word-----------\n")
# a=user
# if a[-2:]=="ly":
# 	print user
# elif a[-3:]=="ing":
# 	b=a.replace("ing","")
# 	print b+"ly"
# elif a[-3:]!="ing":
# 	print user+"ing"




# user=input("enter your number----------  ")
# a=0
# b=0
# c=1
# if user==0:
# 	print "kuch nhi"
# else:
# 	for i in range(0,user):
# 		a=b
# 		b=c
# 		c=a+b 
# 		if a%2==0:
# 			print a




# user=input("enter your number..........    ")
# a=0
# d=0
# for i in range(1,user+1):
# 	a=a+i
# 	b=i*i
# 	d=d+b
# c= a*a
# e=c-d
# print e



#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------




# user=input("enter your number to get a factorial........\n")
# a=1
# for i in range (1,user+1):
# 	a=a*i
# print a




# user=input("enter your number to get the add of digits..........\n")
# a=list(str(user))
# b=0
# for i in a:
# 	b=b+int(i)
# print b



# user=input("enter your number to get a factorial........\n")
# a=list(str(user))
# for i in a:
# 	b=1
# 	c=0
# 	for j in range(int(a[0]),int(i)+1):
# 		b=j*b
# 		c=c+b
# print c 






# user=raw_input("enter your number.......\n")
# b=user[::-1]
# print b





# user=input("enter your number...... ")
# user1=input("how much give you power of number......    ")
# a=user**user1
# b=list(str(a))
# c=0
# for i in b:
# 	c=c+int(i)
# print c




#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------




# user=raw_input("enter your sentece in string...........  \n")
# a=list(user)
# c=0
# for i in a:
# 	if i==" ":
# 		c=c+1
# print c



# user=raw_input("enter your numbers of words in string...........  \n")
# ekdict={"zero":0,"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9}
# a=user.split()
# c=0
# for i in a:
# 	if i in ekdict:
# 		c=c+ekdict[i]
# print c
		
		




# user=input("enter your number to get a factorial........\n")
# a=list(str(user))
# for i in a:
# 	b=1
# 	c=0
# 	for j in range(int(a[0]),int(i)+1):
# 		b=j*b
# 		c=c+b
# print c 




# user=raw_input("enter your number.......\n")
# i=len(user)
# d="".replace(' ', '')
# while i>0:
# 	b=user[i]
# 	d=d+str(b)
# 	i=i-1
# print d




# user=input("enter your number...... ")
# user1=input("how much give you power of number......    ")
# a=user**user1
# b=list(str(a))
# c=0
# for i in b:
# 	c=c+int(i)
# print c