day = 2
numSundays = 0

for i in range (1901,2001):
	for j in range (1,13):
		for m in range (1,32):
			if ((j == 4 or j == 6 or j == 9 or j == 11) and m == 31):
				continue
			elif (j == 2 and (m == 30 or m == 31)):
				continue
			elif (j == 2 and (i % 4 != 0 or (i % 100 == 0 and i % 400 != 0)) and m == 29):
				continue	
			else:
				if (day == 7):
					if (m == 1):
						numSundays = numSundays + 1
					day = 0
				day = day + 1		
print(numSundays)
