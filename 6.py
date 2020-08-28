sum1 = 0
sum2 = 0

for i in range(1,101):
	sum1 = sum1 + pow(i,2)
sum2 = pow((100*101)/2,2)
result = sum2 - sum1

print(result)