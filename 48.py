sum = 0
result = [0]*10

for i in range (1,1001):
	sum = sum + pow(i,i)
for i in range (10):
	result[i] = sum%10
	sum = sum//10
for i in range (9,-1,-1):
	print(result[i], end="")