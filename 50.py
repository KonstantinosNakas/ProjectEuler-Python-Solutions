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



def sumOfConsecutivePrimesBelowOneMillion():
    primes = primeSieve(1000000)
    size = len(primes)
    max = 0

    for i in range (size-1,0,-1):
        if max != 0:
            break
        for index in range (0,4):
            sum = 0
            while index < size-1:
                sum = sum + primes[index]
                index = index + 1
                if primes[i] == sum:
                    max = primes[i] 
                if sum > primes[i]:
                    break        
    return max



print(sumOfConsecutivePrimesBelowOneMillion())