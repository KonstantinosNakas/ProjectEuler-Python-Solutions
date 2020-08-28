def SumOfProperDivisors(n):
	sum = 0;
	for i in range(1, n//2+1):
		if (n%i) == 0:
			sum = sum + i;
	return(sum);		


sum = 0;
for i in range(1, 10000):
	a = SumOfProperDivisors(i);
	if (a == i):
		continue;
	b = SumOfProperDivisors(a);
	if (i == b):
		sum = sum + a;
print(sum);

