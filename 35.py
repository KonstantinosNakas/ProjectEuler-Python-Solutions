CircularNums = 0
N = 1000001
num = [True] * N
num[0] = False
num[1] = False
p = 2

while (pow(p,2) < N):	
	for i in range(p,N,p):
		if (i != p):
			num[i] = False
	for i in range(p+1,N):
		if (num[i]):
			p = i
			break		
for i in range(2,N):
	if (num[i]):
		flag = 1
		number = str(i)
		for j in range(0, len(number)):
			rotNumber = number[j:len(number)] + number[0:j]
			if (num[int(rotNumber)] == False):
				flag = 0
		if (flag == 1):
			CircularNums = CircularNums + 1    	
print(CircularNums)	