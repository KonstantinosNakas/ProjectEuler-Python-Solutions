n = 600851475143
i = 2

while (i <= n):
    while (n % i == 0):
        n = n / i
        result = i
    i = i + 1

print(result)