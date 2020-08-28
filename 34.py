factorial = [0] * 10
result = 0

def FindFactorial(n):
	result = 1
	for i in range(1,n+1):
		result = result * i
	return result


for i in range (10):
	factorial[i] = FindFactorial(i)

for i in range (3,2177280):	
	num = i
	part_sum = 0
	while (num > 0): 
		digit = num%10
		part_sum = part_sum + factorial[digit]	
		num = num//10
	if (part_sum == i):
		result = result + i

print(result)	