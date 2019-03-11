# my_file = open("people1.txt")
# file_data = my_file.read()
# print file_data
# my_file.close()




# my_file2 = open("people2.txt", 'w')
# my_file2.write("Abhishek - Gurgaon\n")
# my_file2.write("Ranveer - Delhi\n")
# my_file2.write("sashi-jaipur\n")
# my_file2.write("sarika-delhi\n")
# my_file2.write("deepti-shimla\n")
# print my_file2
# my_file2.close()


# my_file = open("people2.txt")
# file_data = my_file.read()
# print file_data
# my_file.close()
# 


# my_file=open("people1_exercise.txt",'r')
# prince=my_file.read()
# print prince
# my_file.close()


# my_file=open("people1_exercise.txt",'r')
# prince=my_file.read()
# a=0
# for i in range(len(prince)):
# 	if prince[i]=="\n":
# 		a=a+1
# print a


# bank_file=open("file-question3.txt",'w')
# banks_list = ["Kotak", "HDFC", "RBL", "SBI", "bank of baroda"]
# for i in banks_list:
# 	bank_file.write(str(i)+"\n")
# bank_file.close()




# a=open("people1_exercise.txt", "r")
# data=a.read().split()
# for i in data:
# 	if i=="-":
# 		data.remove(i)
# delhi = open("delhi.txt", "w")
# shimla = open("shimla.txt", "w")
# other = open("other.txt", "w")
# a=1
# while a<len(data):
# 	if data[a]=="delhi":
# 		delhi.write(data[a-1]+"\n")
# 	elif data[a]=="shimla":
# 		shimla.write(data[a-1]+"\n")
# 	else:
# 		other.write(data[a-1]+"\n")
# 	a+=2
# delhi.close()
# shimla.close()
# other.close()



# a=open("people1_exercise.txt", "r")
# data=a.read().split()
# for i in data:
# 	if i=="-":
# 		data.remove(i)
# delhi = open("delhi.txt", "w")
# shimla = open("shimla.txt", "w")
# other = open("other.txt", "w")
# a=1
# while a<len(data):
# 	if data[a]=="delhi":
# 		delhi.write(data[a-1]+"\n")
# 	elif data[a]=="shimla":
# 		shimla.write(data[a-1]+"\n")
# 	else:
# 		other.write(data[a-1]+"\n")
# 	a+=2
# delhi.close()
# shimla.close()
# other.close()



