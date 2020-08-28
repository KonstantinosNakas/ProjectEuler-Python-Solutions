with open("11.txt", "r") as my_file:
	num = []
	for line in my_file:
		line = line.split()
		num.append(line)   	
max = 0


def CheckHorizontal():
	global num
	global max
	product = 1

	for i in range(0,20):
		for j in range(0,17):
			product = 1
			for k in range(0,4):
				product = product * int(num[i][j+k])
			if (product > max):		
				max = product


def CheckAcross():
	global num
	global max
	product = 1

	for i in range(0,17):
		for j in range(0,20):
			product = 1
			for k in range(0,4):
				product = product * int(num[i+k][j])
			if (product > max):		
				max = product				


def CheckRightDiagonally():
	global num
	global max
	product = 1

	for i in range(0,17):
		for j in range(0,17):
			product = 1
			for k in range(0,4):
				product = product * int(num[i+k][j+k])
			if (product > max):		
				max = product							


def CheckLeftDiagonally():
	global num
	global max
	product = 1

	for i in range(3,20):
		for j in range(0,17):
			product = 1
			for k in range(0,4):
				product = product * int(num[i-k][j+k])
			if (product > max):		
				max = product
					



CheckAcross()
CheckHorizontal()
CheckLeftDiagonally()
CheckRightDiagonally()
print(max)			