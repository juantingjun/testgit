def is_plaindrome(n):
	b=str(n)
	flag = True
	for i in range(len(b)/2):
		if b[i] != b[len(b)-i-1]:
			flag=False
			break
	return flag
	
output=filter(is_plaindrome,range(1,1000))
print(list(output))