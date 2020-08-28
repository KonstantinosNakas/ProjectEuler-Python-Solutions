def CanBeWritten(n,num):
	i = 2	
	while(n>i):
		if (num[i] == False):
			i = i + 1
			continue
		flag = 0	
		for j in range(1,n):
			if (n == i+(2*j*j)):
				flag = 1;
				break
			if (n < i+(2*j*j)):
				break	
		if (flag == 1):
			return True
		else:
			i = i + 1
			continue
	return False		



N = 10000
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

n = 35
while(1):
	if (num[n]):
		n = n + 2
		continue
	if (CanBeWritten(n,num)):	
		n = n + 2
		continue
	else:
		print (n)
		break			