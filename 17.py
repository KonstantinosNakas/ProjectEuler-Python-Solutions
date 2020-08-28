A = [3,3,5,4,4,3,5,5,4,3,6,6,8,8,7,7,9,8,8,6,6,5,5,5,7,6,6]
sum = 0

# gia tous prwtous 99 arithmous
for i in range(19):
	sum = sum + A[i]
for i in range(19,27):
	sum = sum + A[i]
	for j in range(9):
		sum = sum + A[i] + A[j]	

# gia tous arithmous apo to 99-999
for k in range(9):
	sum = sum + A[k] + 7
	for i in range(19):
		sum = sum + A[k] + A[i] + 10
	for i in range(19,27):
		sum = sum + A[i] + A[k] + 10
		for j in range(9):
			sum =  sum + A[k] + A[i] + A[j] + 10

sum = sum + 11		# gia to 1000	

print (sum)


