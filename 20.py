def FindFactorial(n):
	result = 1
	for i in range(1,n+1):
		result = result * i
	return result		

sum = 0
result = FindFactorial(100)

while(result > 0):
	a = result % 10
	sum = sum + a
	result = result // 10

print(sum)	