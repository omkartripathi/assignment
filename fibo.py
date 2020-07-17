def fibo(n):
	if n == 1:
		return (0)
	elif n ==2:
		return (1)
	s1 = 0
	s2 = 1
	print(s1)
	print(s2)
	while n-2 > 0 :
		n -= 1
		s3 = s1 + s2
		s1 = s2
		s2 = s3
		print(s3)
		

fibo(10)
