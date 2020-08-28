m = 0
num = 2

def CheckIfPrime(a):
	for i in range(2,a):
		if (a%i == 0):
			return False
	return True		

while (m != 10001):
	if (CheckIfPrime(num)):
		m = m + 1
	num = num + 1
num = num - 1

print(num)		
