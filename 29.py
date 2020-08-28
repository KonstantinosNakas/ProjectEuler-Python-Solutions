numbers = [0] * 10000
pointer = 0
m = 0

for i in range (2,101):
	for j in range (2,101):
		numbers[pointer] = pow(i,j)
		pointer = pointer + 1

for i in range (pointer):
	if (numbers[i] != 0):
		m = m + 1	
		for j in range (i+1,pointer):
			if (numbers[i] == numbers[j]):
				numbers[j] = 0	
				
print(m)			

