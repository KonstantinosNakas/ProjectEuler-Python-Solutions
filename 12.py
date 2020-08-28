import math

primes = [0]*5000

def primeSieve(sieveSize):
     sieve = [True] * sieveSize
     sieve[0] = False 
     sieve[1] = False

     for i in range(2, int(math.sqrt(sieveSize)) + 1):
         pointer = i * 2
         while pointer < sieveSize:
             sieve[pointer] = False
             pointer += i
     primes = []
     for i in range(sieveSize):
         if sieve[i] == True:
             primes.append(i)
     return primes

primes = primeSieve(100000)

def FindTheNumOfDivisors(n):
	global sum
	p = 2
	j = 0
	i = 0
	divisors = 1
	exponents = 0
	while(n != 1):
		exponents = 0
		while (exponents == 0):
			while (n % primes[j] == 0):
				exponents = exponents + 1
				n = n / primes[j]	
			j = j + 1	
			divisors = divisors * (exponents + 1)		
	return (divisors)		

num = 1
sum = 1
divisors = 0
	
while (divisors < 500):
	num = num + 1
	sum = sum + num
	divisors = FindTheNumOfDivisors(sum)
print(sum)	