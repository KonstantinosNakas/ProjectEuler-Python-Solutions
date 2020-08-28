with open("13.txt", "r") as my_file:
	num = my_file.readlines()		
sum = 0

for i in range(100):
	sum = sum + int(num[i])
print(sum)	

