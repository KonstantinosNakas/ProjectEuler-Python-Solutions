max = 0
maxNumber = 0

for i in range(1,1000001):
	n = i
	m = 0
	while (n != 1):
		if (n%2 == 0):
			n = n/2
			m = m + 1
		else:
			n = 3*n + 1
			m = m + 1
	if (m > max):
		max = m
		maxNumber = i
print(maxNumber)		