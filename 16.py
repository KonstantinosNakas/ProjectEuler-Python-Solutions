num = pow(2,1000)
sum = 0

while(num > 0):
	a = num % 10
	sum = sum + a
	num = num // 10
	
print(sum)