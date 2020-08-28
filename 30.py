fifth_power = [0] * 9
result = 0

for i in range (9):
	fifth_power[i] = pow((i+1),5)
		
for i in range (2,354294):
	num = i
	part_sum = 0
	while (num > 0): 
		digit = num%10
		if (digit > 0):
			part_sum = part_sum + fifth_power[digit-1]	
		num = num//10
	if (part_sum == i):
		result = result + i

print(result)			
    		
	



