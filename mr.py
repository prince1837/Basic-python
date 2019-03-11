# for i in range(1001): 
	# if i%3==0:
	# 	print i,"nav"
	# if i%7==0:
	# 	print i,"gurukul"
	# if i%21==0:
	# 	print i,"navgurukul"


# user1= input("number of student")
# user2=input("ek student ka kharcha")
# a=user1*user2
# if a<=50000:
# 	print a, "hum budget ke andar hai"
# else:
# 	print a, "hum budget se bahar hai"


# string_name = "navgurukul"
# if "n" in string_name:
#     print "n hai"
# else:
#     print "n nahi hai"
# print "n" in string_name
# print type("n" in string_name)


# user=raw_input("enter your password\n")
# if len(user)>6 and len(user)<16:
# 	if "@" in user:
# 		if "2" in user or "8" in user :
# 			if "A" in user or "z" in user:
# 				print "password strong hai"
# 		else:
# 			print "password strongnhi hai"
# 	else:
# 		print "password strong nhi hai"
# else:
# 	print "password strong nhi hai"




# user1=input("enter your number")
# user2= input("enter ypur second number")
# user3= input("entr your third number")
# list1=[user1,user2,user3]
# i=0
# b=list1[0]
# while i<len(list1):
# 	if list1[i]>b:
# 		b=list1[i]
# 	i=i+1
# print b




# user = input("enter your number")
# i=1
# c=1
# while i<=user:
# 	c=c*i
# 	i=i+1
# print c




# name = ["Rishabh", "Rishabh", "Abhishek", "Rishabh", "Divyashish", "Divyashish"]
# list=[]
# for i in name:
# 	if i not in list:
# 		list.append(i)
# print list


# list1 = [1, 342, 75, 23, 98]
# list2 = [75, 23, 98, 12, 78, 10, 1]
# a=[]
# for i in list1:
# 	if i in list2:
# 		a.append(i)
# print a		

	
# list1 = [1, 5, 10, 12, 16, 20]
# list2 = [1, 2, 10, 13, 16]
# a=[]
# for i in list1+list2:
# 	a.append(i)
# b=a
# e=[]
# for i in b:
# 	if i not in e:
# 		e.append(i)
# print e



# for i in range(1,1000+1):
# 	a=list(str(i))
# 	b=0
# 	for j in range(len(a)):
# 		b=b+int(a[j])
# 	if i%b==0:
# 		print i



# user1=input("enter your first number")
# user2=input("enter your second number")
# user3=input("enter your third number")
# if user1>user2 and user1>user3:
# 	print user1
# elif user2>user3 and user2>user1:
# 	print user2
# elif user3>user1 and user3>user2:
# 	print user3




# user=input("enter your number\n")
# i=1
# while i<user:
# 	if user%i==0:
# 		print i,
# 	i=i+1



# marks = [[45, 21, 42, 63], [12, 42, 42, 53], [42, 90, 78, 13], [94, 89, 78, 76], [87, 55, 98, 99]]
# for index in marks:
# 	for j in index:
# 		max1=max(index)
# 	print max1


# marks = [[45, 21, 42, 63], [12, 42, 42, 53], [42, 90, 78, 13], [94, 89, 78, 76], [87, 55, 98, 99]]
# for index in marks:
# 	a=index[0]
# 	for j in index:
# 		if j>a:
# 			a=j
# 	print a



# sentence = "NavGurukul is an alternative to higher education reducing the barriers of current formal education system"
# def break_into_words(sentence):
# 	return sentence.split()
# print break_into_words(sentence)



		
# a=raw_input("kkk\n")
# b=raw_input("lll\n")
# if len(a)==len(b):
# 	i=0
# 	while i<len(a):
# 		if a[i] in b and b[i] in a:
# 			i+=1
# 			continue
# 		else:
# 			print "nahi hai"
# 			break
# 	else:
# 		print "hai"
		
# else:
# 	print "nahi hai"





# a=raw_input('name')
# b=raw_input('name1')
# if len(a)==len(b):
# 	i=0
# 	while i<len(a):
# 		if a[i]in b and b[i] in a:
# 			i=i+1
# 			continue
# 		else:
# 			print "nhi hai"
# 			break
# 	else:
# 		print "hai"
# else: 
# 	print "nhi h ena"			





# for i in range(10,50+1):
# 	a=list(str(i))
# 	b=0
# 	for j in range(len(a)):
# 		b=b+int(a[j])
# 	if i%b==0:
# 		print i



