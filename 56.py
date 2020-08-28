sum = 0
max = 0

for i in range(1,100):
	for j in range(1,100):
		num = i**j;
		while (num != 0):
			x = num%10
			sum = sum + x
			num = num//10 
		if (sum > max):
			max = sum	
		sum = 0	
print(max)				