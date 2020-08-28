N = 20

def CalculateFactor(n):
	result = 1
	for i in range(1,n+1):
		result = result * i
	return result
	

path = CalculateFactor(2*N) / (pow(CalculateFactor(N),2))	
print(int(path))