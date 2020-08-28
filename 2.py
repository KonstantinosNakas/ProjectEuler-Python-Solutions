FirstNum = 1
SecondNum = 2
temp = 0
result = 0

while (temp <=4000000):
    temp = SecondNum
    if (temp % 2 == 0):
        result += temp
    temp = FirstNum + SecondNum
    FirstNum = SecondNum
    SecondNum = temp

print(result)