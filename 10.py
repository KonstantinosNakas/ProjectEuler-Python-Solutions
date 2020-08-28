sum = 0
N = 2000000
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
		sum = sum + i
print(sum)	