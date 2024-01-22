n1=float(input('enter first number: '))
n3=input('enter Operator: ')
n2=float(input('enter second number: '))

if n3=='+':
	print(n1+n2)
elif n3=='-':
	print(n1-n2)
elif n3=='*':
	print(n1*n2)
elif n3=='/':
	print(n1/n2)
elif n3=='//':
	print (int(n1//n2))
elif n3=='**':
	print(n1**n2)
else:
	print('please enter valid operator!')