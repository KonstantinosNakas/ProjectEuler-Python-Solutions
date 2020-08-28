import math
P_list = [0] * 1000
p_max = 0
n_max = 0

for a in range (500):
	for b in range (500):
		c = math.sqrt(a**2+b**2)
		if (c%1 == 0):
			p = int(a + b + c)
			if (p<1000):
				P_list[p] = P_list[p] + 1 	

for i in range (2,1000):
	if (P_list[i] > n_max):
		n_max = P_list[i]
		p_max = i
	
print(p_max)


