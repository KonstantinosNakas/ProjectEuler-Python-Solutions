import math

for i in range(1,400):
	for j in range(1,400):
		if (i+j+math.sqrt(pow(i,2)+pow(j,2)) == 1000):
			a = i
			b = j
			break
c = int(math.sqrt(pow(a,2)+pow(b,2)))
result = a*b*c
print(result)
