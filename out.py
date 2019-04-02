
#radom function to print 5 even randomly


# import random 
# i=0
# while i<5:
# 	a=random.randint(1,20)
# 	if a%2==0:
# 		print a
# 		i=i+1


# import random
# list1=[1,2,3,4,5,6,7,8,9,10]
# a=random.choice(list1)
# print a

#radom function to print 5 even randomly

# import random
# list1=[1,2,3,4,5,6,7,8,9,10]
# i=0
# while i<len(list1):
# 	a=random.choice(list1)
# 	if a%2==0:
# 		print a,
# 		i=i+1




# big_list=[[1,5,4],[5,9,6],[21,54,9,61]]
# i=0
# a_list=0
# while i<len(big_list):
# 	b_list=len(big_list[i])
# 	j=0
# 	while j<b_list:
# 		a_list=a_list+big_list[i][j]
# 		j=j+1
# 	i=i+1
# print a_list








# Roman=["I","II","III","IV","V","VI","VII","VIII","IX","X","XX","XXX","XL","L","LX","LXX","LXXX","XC","C","CC","CCC","CD","D","DC","DCC","DCCC","CM","M","MM","MMM"]
# Number=[1,2,3,4,5,6,7,8,9,10,20,30,40,50,60,70,80,90,100,200,300,400,500,600,700,800,900,1000,2000,3000]
# roman=""
# user=raw_input("Enter your number: ")
# j=len(user)-1
# userlist=[]
# for i in user:
# 	k=i+"0"*j
# 	userlist.append(int(k))
# 	j-=1
# for i in userlist:
# 	for l in range(len(Number)):
# 		if Number[l]==i:
# 			roman=roman+Roman[l]
# print roman




# list1 =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d']
# empty = ""
# user = raw_input("Enter a name.......\n ")
# for i in user:
# 	a = list1.index(i)
# 	c = list1[a+3]
# 	if c == "a" or c == "e" or c == "i" or c == "o" or c == "u":
# 		empty = empty + c.upper()
# 	else:
# 		empty = empty + c
# print empty




# user=input("Enter your age ?")
# user1=input("Enter candels according to their height ?")
# a=list(str(user1))
# b=a[0]
# for i in range(len(a)):
# 	if int(a[i])>int(b):
# 		b=int(a[i])
# c=b
# d=0
# if c==user:
# 	for i in range(len(a)):
# 		if int(a[i])==c:
# 			d=d+1
# 	print  "when you flut the candels for cut the cake when time the candeles whose extinguish by you"
# 	print "there is a numbers of candels", d
# else:
# 	print "you can't put those number whose maximum than age in candels according to their height "



# i=1
# while True:
# 	i=i+1
# 	if i%1==0 and i%2==0 and i%3==0 and i%4==0 and i%5==0 and i%6==0 and i%7==0 and i%8==0 and i%9==0 and i%10==0:
# 		b=i
# 		break
# print b 



# num=1
# while True:
# 	for i in range(1,11):
# 		if num%i!=0:
# 			break
# 	else:
# 		print(num)
# 		break
# 	num+=1




# for i in range(1,10001):
# 	a=0
# 	for j in range(1,i):
# 		if i%j==0:
# 			a=a+j
# 	k=0
# 	for j in range(1,a):
# 		if a%j==0:
# 			k+=j

# 	if k==i:
# 		print(i,a),"ye amicable no.. hai"



# user = input("enter a position for get a prime number on that index........\n")
# a=2
# z=0
# while True:
# 	b=2
# 	n=[]
# 	while b<a:
# 		if a%b==0:
# 			break
# 		b=b+1
# 	else:
# 		c=a
# 		z=z+1
# 		if z==user:
# 			break
# 	a=a+1
# print c


# user=input("enter a consecuitve prime number below user_input......\n")
# i=2
# n=[]
# z=1
# while True:
# 	z=z+1
# 	for j in range(2,i):
# 		if i%j==0:
# 			break
# 	else:
# 		n.append(i)
# 	if z==user or z>user:
# 		break
# 	i=i+1
# s=0
# f=[]
# for k in n:
# 	if k<user:
# 		s=s+k
# 		if s<user:
# 			f.append(s)
# q=[]
# for h in f:
# 	for l in range(2,h):
# 		if h%l==0:
# 			break
# 	else:
# 		q.append(h)
# print q
# print max(q)




# user= input ("enter your natural number for a length for find diffrence between the sum of the square of the first ten natural numbers and the square of the sum ........\n")
# a=0
# b=0
# for i in range(1,user+1):
# 	a=a+i**2
# 	b=b+i
# c=b**2
# print "Diffrence between the sum of the square of the first ten natural numbers and the square of the sum is ",c-a




# # user=input("enter your list and you take big big_list with in three list with three index......  \n")
# user=[[8, 3, 4],[1, 5, 9],[6, 7, 2]]
# a=user
# b=0
# for k in range(1,user+1):
# 	for j in user[k]:
# 		b=b+j
# if a[0[0]]+a[1[0]]+a[2[0]]==b:
# 	print 
# 	c=0
# 	for j in a[1]:
# 		c=c+j
# 	if a[0[1]]+a[1[1]]+a[2[1]]==c:
# 		d=0
# 		for i in a[2]:
# 			d=d+i
# 		if a[0[2]]+a[1[2]]+a[2[2]]==d:
# 			if a[0[0]]+a[1[1]]+a[2[2]]==d:
# 				if a[0[2]]+a[1[1]]+a[2[0]]==d:
# 					print "yes ye magic square hai"

# 			else:
# 				print "ye magic square nhi hai"
# 	else:
# 		print "ye magic square nhi hai"
# else:
# 	print "ye magic square nhi hai"





# user=[[8, 3, 4],
# 	 [1, 5, 9],
# 	 [6, 7, 2]]
# a=user
# n=[]
# for i in a:
# 	d=0
# 	c=0
# 	for j in i:
# 		c=c+j
# 		d=d+1
# 		if d==len(a):
# 			n.append(c)
# for 



# Roman=["I","II","III","IV","V","VI","VII","VIII","IX","X","XX","XXX","XL","L","LX","LXX","LXXX","XC","C","CC","CCC","CD","D","DC","DCC","DCCC","CM","M","MM","MMM"]
# Number=[1,2,3,4,5,6,7,8,9,10,20,30,40,50,60,70,80,90,100,200,300,400,500,600,700,800,900,1000,2000,3000]
# roman=""
# user=raw_input("Enter your number: ")
# j=len(user)-1
# userlist=[]
# for i in user:
# 	k=i+"0"*j
# 	userlist.append(int(k))
# 	j-=1
# for i in userlist:
# 	for l in range(len(Number)):
# 		if Number[l]==i:
# 			roman=roman+Roman[l]
# print roman







# lists = [
# 	[199,288,445,576,609],
# 	[987,510,455,932,912],
# 	[567,452,241,541,320],
# 	[760,452,321,123,321],
# 	[100,567,587,345,543]
# ]
# s=[]
# for i in lists:
# 	t=0
# 	for j in i:
# 		t=t+j
# 	s.append(t)
# a=s[0]
# for i in s:
# 	if i>a:
# 		a=i
# b=s.index(a)
# k=lists[b]
# print "This is a big list in lists"
# print k






# lists = [[1,2,3,4,5,6,7,8],[8,9,789,876,908,10,45,32,12],[56,78,900,908,987,90,54,345,657,32],[76,45,32],[100, 567, 987]]
# max=0
# for i in lists:
# 	s=0
# 	for j in i:
# 		s=s+j
# 	if max<s:
# 		max=s
# 		k=i 
# print k







# user=input("inter your number to find a that's number his two numbers of square those we get output is equal to 81...........\n")
# f=[]
# for i in range(1,user):
#     b=0
#     d=0
#     c=list(str(i))
#     n=None
#     j=0
#     while j<len(c):
#         b=b+int(c[j])**2
#         d=d+1
#         if d==len(c):
#             if b==n:
#                 break
#             elif b!=81:
#                 c=str(b)
#                 n=b
#                 continue
#             else:
#                 if b==81:
#                     f.append(i)
#         j=j+1
# print f


# user=raw_input(" enter your string word....\n")
# list1="abcdefghijklmnopqrstuvwxyz"
# for i in list1:
# 	if i in user:
# 		b=list1.replace(i,'')
# 		list1=b		
# print b9+


# names = [{'name': 'Pralhad', 'age': 17},
#  {'name': 'Bhavnesh', 'age': 25},
#  {'name': 'Bhavnesh', 'age': 20},
#  {'name': 'Anoop', 'age': 19},
#  {'name': 'Rishabh', 'age': 24},
#  {'name': 'Rishabh', 'age': 24},
#  {'name': 'Bhavnesh', 'age': 18},
#  {'name': 'Pralhad', 'age': 25},
#  {'name': 'Anoop', 'age': 16},
#  {'name': 'Bhavnesh', 'age': 21},
#  {'name': 'Bhavnesh', 'age': 21},
#  {'name': 'Anoop', 'age': 19},
#  {'name': 'Anoop', 'age': 23},
#  {'name': 'Anoop', 'age': 16},
#  {'name': 'Rishabh', 'age': 17},
#  {'name': 'Bhavnesh', 'age': 17},
#  {'name': 'Rishabh', 'age': 15},
#  {'name': 'Anurag', 'age': 19},
#  {'name': 'Bhavnesh', 'age': 20},
#  {'name': 'Rishabh', 'age': 24},
#  {'name': 'Anoop', 'age': 23},
#  {'name': 'Anurag', 'age': 25},
#  {'name': 'Bhavnesh', 'age': 19},
#  {'name': 'Pralhad', 'age': 18},
#  {'name': 'Anoop', 'age': 16},
#  {'name': 'Anoop', 'age': 25},
#  {'name': 'Rishabh', 'age': 23},
#  {'name': 'Anoop', 'age': 23},
#  {'name': 'Anurag', 'age': 23},
#  {'name': 'Bhavnesh', 'age': 22},
#  {'name': 'Anurag', 'age': 20},
#  {'name': 'Rishabh', 'age': 20},
#  {'name': 'Pralhad', 'age': 25},
#  {'name': 'Pralhad', 'age': 16},
#  {'name': 'Rishabh', 'age': 23},
#  {'name': 'Anoop', 'age': 16},
#  {'name': 'Rishabh', 'age': 16},
#  {'name': 'Pralhad', 'age': 23},
#  {'name': 'Rishabh', 'age': 19},
#  {'name': 'Pralhad', 'age': 20},
#  {'name': 'Anoop', 'age': 22},
#  {'name': 'Rishabh', 'age': 16},
#  {'name': 'Rishabh', 'age': 15},
#  {'name': 'Pralhad', 'age': 15},
#  {'name': 'Pralhad', 'age': 20},
#  {'name': 'Pralhad', 'age': 18},
#  {'name': 'Rishabh', 'age': 18},
#  {'name': 'Anoop', 'age': 15},
#  {'name': 'Anoop', 'age': 16},
#  {'name': 'Anoop', 'age': 19},
#  {'name': 'Anurag', 'age': 20},
#  {'name': 'Rishabh', 'age': 17},
#  {'name': 'Bhavnesh', 'age': 17},
#  {'name': 'Pralhad', 'age': 25},
#  {'name': 'Pralhad', 'age': 25},
#  {'name': 'Rishabh', 'age': 18},
#  {'name': 'Rishabh', 'age': 20},
#  {'name': 'Bhavnesh', 'age': 18},
#  {'name': 'Anoop', 'age': 22},
#  {'name': 'Anurag', 'age': 15},
#  {'name': 'Rishabh', 'age': 18},
#  {'name': 'Pralhad', 'age': 18},
#  {'name': 'Bhavnesh', 'age': 17},
#  {'name': 'Anurag', 'age': 25},
#  {'name': 'Anoop', 'age': 23},
#  {'name': 'Anoop', 'age': 15},
#  {'name': 'Pralhad', 'age': 19},
#  {'name': 'Rishabh', 'age': 21},
#  {'name': 'Anurag', 'age': 18},
#  {'name': 'Anurag', 'age': 21},
#  {'name': 'Pralhad', 'age': 23},
#  {'name': 'Anurag', 'age': 16},
#  {'name': 'Pralhad', 'age': 21},
#  {'name': 'Pralhad', 'age': 25},
#  {'name': 'Anurag', 'age': 16},
#  {'name': 'Rishabh', 'age': 22},
#  {'name': 'Bhavnesh', 'age': 16},
#  {'name': 'Pralhad', 'age': 20},
#  {'name': 'Bhavnesh', 'age': 17},
#  {'name': 'Pralhad', 'age': 22},
#  {'name': 'Bhavnesh', 'age': 21},
#  {'name': 'Anurag', 'age': 20},
#  {'name': 'Pralhad', 'age': 16},
#  {'name': 'Rishabh', 'age': 24},
#  {'name': 'Pralhad', 'age': 18},
#  {'name': 'Rishabh', 'age': 23},
#  {'name': 'Rishabh', 'age': 19},
#  {'name': 'Rishabh', 'age': 21},
#  {'name': 'Pralhad', 'age': 23},
#  {'name': 'Rishabh', 'age': 15},
#  {'name': 'Bhavnesh', 'age': 17},
#  {'name': 'Anurag', 'age': 17},
#  {'name': 'Pralhad', 'age': 24},
#  {'name': 'Anurag', 'age': 15},
#  {'name': 'Pralhad', 'age': 25},
#  {'name': 'Bhavnesh', 'age': 24},
#  {'name': 'Anoop', 'age': 23},
#  {'name': 'Pralhad', 'age': 25},
#  {'name': 'Bhavnesh', 'age': 22},
#  {'name': 'Anoop', 'age': 25}]
# list_name = []
# for i in names:
# 	if i['name'] not in list_name:
# 		list_name.append(i['name'])
# for i in list_name:
# 	count=0
# 	for j in names:
# 		if i==j['name']:
# 			count+=1
# 	print i,count


# lists = [
# 	[1,2,3,4,5,6,7,8],
# 	[8,9,10,45,32,12],
# 	[56,78,90,54,32],
# 	[76,45,32],
# 	[100, 567, 987]
# ]
# s=[]
# for i in lists:
# 	t=0
# 	for j in i:
# 		t=t+j
# 	s.append(t)
# a=s[0]
# for i in s:
# 	if i>a:
# 		a=i
# b=s.index(a)
# k=lists[b]
# print k



# names = [{'name': 'Pralhad', 'age': 17},
#  {'name': 'Bhavnesh', 'age': 25},
#  {'name': 'Bhavnesh', 'age': 20},
#  {'name': 'Anoop', 'age': 19},
#  {'name': 'Rishabh', 'age': 24},
#  {'name': 'Rishabh', 'age': 24},
#  {'name': 'Bhavnesh', 'age': 18},
#  {'name': 'Pralhad', 'age': 25},
#  {'name': 'Anoop', 'age': 16},
#  {'name': 'Bhavnesh', 'age': 21},
#  {'name': 'Bhavnesh', 'age': 21},
#  {'name': 'Anoop', 'age': 19},
#  {'name': 'Anoop', 'age': 23},
#  {'name': 'Anoop', 'age': 16},
#  {'name': 'Rishabh', 'age': 17},
#  {'name': 'Bhavnesh', 'age': 17},
#  {'name': 'Rishabh', 'age': 15},
#  {'name': 'Anurag', 'age': 19},
#  {'name': 'Bhavnesh', 'age': 20},
#  {'name': 'Rishabh', 'age': 24},
#  {'name': 'Anoop', 'age': 23},
#  {'name': 'Anurag', 'age': 25},
#  {'name': 'Bhavnesh', 'age': 19},
#  {'name': 'Pralhad', 'age': 18},
#  {'name': 'Anoop', 'age': 16},
#  {'name': 'Anoop', 'age': 25},
#  {'name': 'Rishabh', 'age': 23},
#  {'name': 'Anoop', 'age': 23},
#  {'name': 'Anurag', 'age': 23},
#  {'name': 'Bhavnesh', 'age': 22},
#  {'name': 'Anurag', 'age': 20},
#  {'name': 'Rishabh', 'age': 20},
#  {'name': 'Pralhad', 'age': 25},
#  {'name': 'Pralhad', 'age': 16},
#  {'name': 'Rishabh', 'age': 23},
#  {'name': 'Anoop', 'age': 16},
#  {'name': 'Rishabh', 'age': 16},
#  {'name': 'Pralhad', 'age': 23},
#  {'name': 'Rishabh', 'age': 19},
#  {'name': 'Pralhad', 'age': 20},
#  {'name': 'Anoop', 'age': 22},
#  {'name': 'Rishabh', 'age': 16},
#  {'name': 'Rishabh', 'age': 15},
#  {'name': 'Pralhad', 'age': 15},
#  {'name': 'Pralhad', 'age': 20},
#  {'name': 'Pralhad', 'age': 18},
#  {'name': 'Rishabh', 'age': 18},
#  {'name': 'Anoop', 'age': 15},
#  {'name': 'Anoop', 'age': 16},
#  {'name': 'Anoop', 'age': 19},
#  {'name': 'Anurag', 'age': 20},
#  {'name': 'Rishabh', 'age': 17},
#  {'name': 'Bhavnesh', 'age': 17},
#  {'name': 'Pralhad', 'age': 25},
#  {'name': 'Pralhad', 'age': 25},
#  {'name': 'Rishabh', 'age': 18},
#  {'name': 'Rishabh', 'age': 20},
#  {'name': 'Bhavnesh', 'age': 18},
#  {'name': 'Anoop', 'age': 22},
#  {'name': 'Anurag', 'age': 15},
#  {'name': 'Rishabh', 'age': 18},
#  {'name': 'Pralhad', 'age': 18},
#  {'name': 'Bhavnesh', 'age': 17},
#  {'name': 'Anurag', 'age': 25},
#  {'name': 'Anoop', 'age': 23},
#  {'name': 'Anoop', 'age': 15},
#  {'name': 'Pralhad', 'age': 19},
#  {'name': 'Rishabh', 'age': 21},
#  {'name': 'Anurag', 'age': 18},
#  {'name': 'Anurag', 'age': 21},
#  {'name': 'Pralhad', 'age': 23},
#  {'name': 'Anurag', 'age': 16},
#  {'name': 'Pralhad', 'age': 21},
#  {'name': 'Pralhad', 'age': 25},
#  {'name': 'Anurag', 'age': 16},
#  {'name': 'Rishabh', 'age': 22},
#  {'name': 'Bhavnesh', 'age': 16},
#  {'name': 'Pralhad', 'age': 20},
#  {'name': 'Bhavnesh', 'age': 17},
#  {'name': 'Pralhad', 'age': 22},
#  {'name': 'Bhavnesh', 'age': 21},
#  {'name': 'Anurag', 'age': 20},
#  {'name': 'Pralhad', 'age': 16},
#  {'name': 'Rishabh', 'age': 24},
#  {'name': 'Pralhad', 'age': 18},
#  {'name': 'Rishabh', 'age': 23},
#  {'name': 'Rishabh', 'age': 19},
#  {'name': 'Rishabh', 'age': 21},
#  {'name': 'Pralhad', 'age': 23},
#  {'name': 'Rishabh', 'age': 15},
#  {'name': 'Bhavnesh', 'age': 17},
#  {'name': 'Anurag', 'age': 17},
#  {'name': 'Pralhad', 'age': 24},
#  {'name': 'Anurag', 'age': 15},
#  {'name': 'Pralhad', 'age': 25},
#  {'name': 'Bhavnesh', 'age': 24},
#  {'name': 'Anoop', 'age': 23},
#  {'name': 'Pralhad', 'age': 25},
#  {'name': 'Bhavnesh', 'age': 22},
#  {'name': 'Anoop', 'age': 25}]
# s=[]
# for i in names:
# 	count = 0
# 	for j in names:
# 		if i['name']==j['name']:
#  			count+=1
# 	a= i['name'],count
# 	for j in a:
# 		if j not in s:
# 			s.append(j)
# print s






# names = [{'name': 'Pralhad', 'age': 17},
#  {'name': 'Bhavnesh', 'age': 25},
#  {'name': 'Bhavnesh', 'age': 20},
#  {'name': 'Anoop', 'age': 19},
#  {'name': 'Rishabh', 'age': 24},
#  {'name': 'Rishabh', 'age': 24},
#  {'name': 'Bhavnesh', 'age': 18},
#  {'name': 'Pralhad', 'age': 25},
#  {'name': 'Anoop', 'age': 16},
#  {'name': 'Bhavnesh', 'age': 21},
#  {'name': 'Bhavnesh', 'age': 21},
#  {'name': 'Anoop', 'age': 19},
#  {'name': 'Anoop', 'age': 23},
#  {'name': 'Anoop', 'age': 16},
#  {'name': 'Rishabh', 'age': 17},
#  {'name': 'Bhavnesh', 'age': 17},
#  {'name': 'Rishabh', 'age': 15},
#  {'name': 'Anurag', 'age': 19},
#  {'name': 'Bhavnesh', 'age': 20},
#  {'name': 'Rishabh', 'age': 24},
#  {'name': 'Anoop', 'age': 23},
#  {'name': 'Anurag', 'age': 25},
#  {'name': 'Bhavnesh', 'age': 19},
#  {'name': 'Pralhad', 'age': 18},
#  {'name': 'Anoop', 'age': 16},
#  {'name': 'Anoop', 'age': 25},
#  {'name': 'Rishabh', 'age': 23},
#  {'name': 'Anoop', 'age': 23},
#  {'name': 'Anurag', 'age': 23},
#  {'name': 'Bhavnesh', 'age': 22},
#  {'name': 'Anurag', 'age': 20},
#  {'name': 'Rishabh', 'age': 20},
#  {'name': 'Pralhad', 'age': 25},
#  {'name': 'Pralhad', 'age': 16},
#  {'name': 'Rishabh', 'age': 23},
#  {'name': 'Anoop', 'age': 16},
#  {'name': 'Rishabh', 'age': 16},
#  {'name': 'Pralhad', 'age': 23},
#  {'name': 'Rishabh', 'age': 19},
#  {'name': 'Pralhad', 'age': 20},
#  {'name': 'Anoop', 'age': 22},
#  {'name': 'Rishabh', 'age': 16},
#  {'name': 'Rishabh', 'age': 15},
#  {'name': 'Pralhad', 'age': 15},
#  {'name': 'Pralhad', 'age': 20},
#  {'name': 'Pralhad', 'age': 18},
#  {'name': 'Rishabh', 'age': 18},
#  {'name': 'Anoop', 'age': 15},
#  {'name': 'Anoop', 'age': 16},
#  {'name': 'Anoop', 'age': 19},
#  {'name': 'Anurag', 'age': 20},
#  {'name': 'Rishabh', 'age': 17},
#  {'name': 'Bhavnesh', 'age': 17},
#  {'name': 'Pralhad', 'age': 25},
#  {'name': 'Pralhad', 'age': 25},
#  {'name': 'Rishabh', 'age': 18},
#  {'name': 'Rishabh', 'age': 20},
#  {'name': 'Bhavnesh', 'age': 18},
#  {'name': 'Anoop', 'age': 22},
#  {'name': 'Anurag', 'age': 15},
#  {'name': 'Rishabh', 'age': 18},
#  {'name': 'Pralhad', 'age': 18},
#  {'name': 'Bhavnesh', 'age': 17},
#  {'name': 'Anurag', 'age': 25},
#  {'name': 'Anoop', 'age': 23},
#  {'name': 'Anoop', 'age': 15},
#  {'name': 'Pralhad', 'age': 19},
#  {'name': 'Rishabh', 'age': 21},
#  {'name': 'Anurag', 'age': 18},
#  {'name': 'Anurag', 'age': 21},
#  {'name': 'Pralhad', 'age': 23},
#  {'name': 'Anurag', 'age': 16},
#  {'name': 'Pralhad', 'age': 21},
#  {'name': 'Pralhad', 'age': 25},
#  {'name': 'Anurag', 'age': 16},
#  {'name': 'Rishabh', 'age': 22},
#  {'name': 'Bhavnesh', 'age': 16},
#  {'name': 'Pralhad', 'age': 20},
#  {'name': 'Bhavnesh', 'age': 17},
#  {'name': 'Pralhad', 'age': 22},
#  {'name': 'Bhavnesh', 'age': 21},
#  {'name': 'Anurag', 'age': 20},
#  {'name': 'Pralhad', 'age': 16},
#  {'name': 'Rishabh', 'age': 24},
#  {'name': 'Pralhad', 'age': 18},
#  {'name': 'Rishabh', 'age': 23},
#  {'name': 'Rishabh', 'age': 19},
#  {'name': 'Rishabh', 'age': 21},
#  {'name': 'Pralhad', 'age': 23},
#  {'name': 'Rishabh', 'age': 15},
#  {'name': 'Bhavnesh', 'age': 17},
#  {'name': 'Anurag', 'age': 17},
#  {'name': 'Pralhad', 'age': 24},
#  {'name': 'Anurag', 'age': 15},
#  {'name': 'Pralhad', 'age': 25},
#  {'name': 'Bhavnesh', 'age': 24},
#  {'name': 'Anoop', 'age': 23},
#  {'name': 'Pralhad', 'age': 25},
#  {'name': 'Bhavnesh', 'age': 22},
#  {'name': 'Anoop', 'age': 25}]
# s=[]
# x=[]
# for i in names:
# 	age_count = 0
# 	for j in names:
# 		if i['name']==j['name']:
# 			if i['age']==j['age']:
# 				age_count+=1
# 	a= i['age'],i['name'],age_count
# 	x.append(a)
# for j in x:
# 	if j not in s:
# 		s.append(j)
# print s




# user=[26,32,54,96,22,42,38]
# empty=[]
# q=len(user)
# j=0
# while j<q:
#     j=j+1
#     s=user[0]
#     for i in user:
#         if i<s:
#             s=i
#     empty.append(s)
#     d=user.index(s)
#     user.pop(d)
# print (empty)





# list2=[3,-4,-3]
# d=0
# c=list2[0]
# for i in list2:
# 	if i>c:
# 		c=i
# e=list2[0]
# for i in list2:
# 	if i<e:
# 		e=i
# for i in range(e,c+1):
# 	if i not in list2:
# 		print i,






# list1=[12,78,34,45,50,32]
# l = len(list1)
# list2 = []
# list3=[]
# for i in range(l):
# 	list2.append(list1.pop(0))
# 	d= list2[:-1]+list1   
# 	list3.append(d)
# n=list3
# v=0
# for i in n:
# 	for j in range(len(i)-1):
# 		h=i[j]
# 		if h<i[j+1]:
# 			h=i[j+1]
# 			if h==i[-1]:
# 				v=v+1
# 		else:
# 			break
# if v>0:
# 	print "True"
# else:
# 	print "False"


		




# user=raw_input("enter you ssentence to get a longest words in a sentence\n")
# user1=user.split()
# list1=[]
# for i in user1:
# 	s=0
# 	for j in i:
# 		s+=1
# 	list1.append(s)
# k=max(list1)
# for i in user1:
# 	s=0
# 	for j in i:
# 		s+=1
# 	if s==k:
# 		print i



# inputString1="abacaba"
# inputString=list(inputString1)
# distance=3
# count=0
# for i in range(len(inputString)):
# 	new=inputString[i]
# 	n1=i+distance+1
# 	if n1<len(inputString):
# 		if inputString[n1]==new:
# 			count=count+1
# print count




# user= "my name is khan"
# list1="abcdefghijklmnopqrstuvwxyz"
# for i in list1:
# 	if i in user:
# 		b=list1.replace(i,'')
# 		list1=b
# print list1


# =======================================================================================================================================================



# list1=[100,100,50,40,20,10]
# user=input("enter your no....")
# user.sort()
# user.reverse()
# list2=[]
# for i in list1:
# 	if i not in list2:
# 		list2.append(i)
# for i in user:
# 	if i not in list2:
# 		list2.append(i)
# list2.sort()
# list2.reverse()
# d=0
# for i in list2:
# 	d+=1
# 	for j in user:
# 		if j==i:
# 			print "rank",d,j







# list1=[[1,2,3],
# [4,5,6],
# [9,8,9]]
# n=len(list1)
# d1=0
# d2=0
# d3=[]
# for i in range(len(list1)):
#     d1=d1+list1[i][i]
#     d2=d2+list1[i][n-i-1]
# d3.append(d1)
# d3.append(d2)
# ma=max(d3)
# mi=min(d3)
# print ma-mi





 





