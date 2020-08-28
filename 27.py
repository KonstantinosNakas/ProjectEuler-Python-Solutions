def isPrime(a):
	i = 2;
	if (a<2):
		return False;
	while (a%i != 0):
		i = i + 1;
	if (i == a):
		return True;
	else:
		return False;

max_num_of_cons = 0;
max_a = 0;
max_b = 0;
for a in range(-1000,1000):
	for b in range(-1000,1000):
		n = 0;
		num_of_cons = 0;
		while (isPrime(n*n+a*n+b)):
			num_of_cons = num_of_cons + 1;
			n = n + 1;
		if (num_of_cons > max_num_of_cons):
			max_num_of_cons = num_of_cons;
			max_a = a;
			max_b = b;	
print(max_a * max_b);			