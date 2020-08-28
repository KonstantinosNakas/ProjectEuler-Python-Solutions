result = 0

def CkeckPalidrome(a):
    m = len(a)
    for i in range (0,m):
        if (a[i] != a[m-i-1]):
            return False
    return True

for i in range(999,100,-1):
	for j in range(999,100,-1):
		if (CkeckPalidrome(str(i*j))):
			if (i*j > result):
				result = i*j
		
print(result)

		