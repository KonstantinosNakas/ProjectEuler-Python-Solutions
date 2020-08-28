prime = [2,3,5,7,11,13,17,19]
power = [1,1,1,1,1,1,1,1]
i = 0

for num in range(2,20):
	i = 0
	while (prime[i] <= num):
		n = 0
		while ((num % prime[i]) == 0):
		   	num = num / prime[i]
		   	n = n + 1
		if (power[i] < n):
		   	power[i] = n	
		if (i < 7):   	
			i = i + 1
		else: 
			continue	

result = pow(2,power[0]) * pow(3,power[1]) * pow(5,power[2]) * pow(7,power[3]) * pow(11,power[4]) * pow(13,power[5]) * pow(17,power[6]) * pow(19,power[7])
print(result)

