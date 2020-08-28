def SumOfProperDivisors(n):
	sum = 0;
	for i in range(1, n//2+1):
		if (n%i) == 0:
			sum = sum + i;
	return(sum);		


sum = 0;
abundantNumbers = list();
sumOfAbundant = [0]*28123;
for i in range(0, 28123):
	sumOfAbundant[i] = i;
for i in range(12, 28123):	
	s = SumOfProperDivisors(i);
	if (s > i):
		abundantNumbers.append(i);
for i in range(0,len(abundantNumbers)):
	for j in range(i,len(abundantNumbers)):
		k = abundantNumbers[i]+abundantNumbers[j];
		if (k < 28123):
			sumOfAbundant[k] = 0;		
for i in range(0,28123):
	sum = sum + sumOfAbundant[i];
print(sum);

	
