import array as arr

def CheckIfPrime(a):
	for i in range(2,a):
		if (a%i == 0):
			return False
	return True		


res = 1;
primes = arr.array('i',(0 for i in range(0,100)))
limit = 1000000;
m = 0
num = 2
j = 0

while (m != 100):
	if (CheckIfPrime(num)):
		primes[m] = num
		m = m + 1
	num = num + 1

while(res * primes[j] < limit):
    res = res * primes[j]
    j = j + 1
print(res)
