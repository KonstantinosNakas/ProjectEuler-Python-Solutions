m = 0;
num = 0;
mult = 1;

while(1):
	num = num + 1;
	number_string = str(num);
	for ch in number_string:
		temp_num = int(ch);
		m = m + 1;		
		if (m == 1 or m == 10 or m == 100 or m == 1000 or m == 10000 or m == 100000 or m == 1000000):
			mult = mult * temp_num;
			if (m == 1000000):
				break;			
	if (m == 1000000):
		break;	
	
print(mult);				





