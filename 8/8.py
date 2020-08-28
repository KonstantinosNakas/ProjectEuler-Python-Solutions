with open("8.txt") as f: 
	num = f.readlines() 
pstart = 0
pend = 13
max = 0
m = 0
digits = [None]*1000
for i in range(0,20):
	for j in range(0,50):
		digits[m] = num[i][j]
		m = m + 1

while (pend < 1000):
	product = 1
	for j in range(pstart,pend):
		product = product * int(digits[j])
	if (product > max):		
		max = product
	pstart = pstart + 1
	pend = pend + 1	

print(max)