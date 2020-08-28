
def FindNumOfDigits(n):
	m = 0
	while(n > 1):
		n = n//10
		m = m + 1
	return m

f_1 = 1
f_2 = 1
NumOfDigits = 0
index = 0
while (NumOfDigits != 1000):
	f_3 = f_2 + f_1
	f_1 = f_2
	f_2 = f_3
	NumOfDigits = FindNumOfDigits(f_3)
	index = index + 1

print(index)