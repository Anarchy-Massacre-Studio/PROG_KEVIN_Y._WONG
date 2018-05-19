print('Program Strat...')
input0='1+2-(3*4)/5^(6+7*8)*(9+8)'
temp0=[]
def loop(input0):
	for i in input0:
		temp0.append(i)
	j=-1;l=0;m='';N=0;O = 0
	temp = '';temp1=[]
	if '(' in input0 and ')' in input0:
		for k in range(len(input0)):
			if l != 1:
				if temp0[k] == '(':
					temp = temp + temp0[k]
					temp0[k] = ''
					l = 1
			else:
				if temp0[k] == ')':
					l = 0
					temp = temp + temp0[k] + ' '
					temp0[k] = ''
				temp = temp + temp0[k]
				temp0[k] = ''
		for i in range(len(temp0)):
			temp1.append(temp0[i])
		if ' ' in temp:
			temp = temp.split(' ')
		i = 0
		for j in range(len(temp1)):
			if N != 1:
				if temp1[i] == '':
					N = 1
					temp1[i] = temp[O]
					O = O + 1
				i =i + 1
			elif N == 1:
				if temp1[i] == '':
					temp1.pop(i)
				elif temp1[i] != '':
					N = 0
	temp2 = []
	for i in temp1:
		if i != '':
			temp2.append(i)
	print(temp2)
	return(temp2)
loop(input0)