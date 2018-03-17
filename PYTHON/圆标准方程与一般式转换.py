import math, os
i = input('一般式转标准式（N），标准式转一般式（S）')
def _N2S():
	print('x^2 + y^2 + Dx + Ey + F = 0')
	D = int(input('D is:'))
	E = int(input('E is:'))
	F = int(input('F is:'))
	print('x^2+'+'y^2+'+str(D)+'x+'+str(E)+'y+'+str(F)+'= 0')
	if (D*D + E*E + 4*F) < 0:
		print('UNAVAILABLE')
	else:
		a = D/2
		b = E/2
		c = (D*D + E*E + 4*F)/4
		if str(a)[:1] != '-':
			a = '+' + str(a)
		else:
			a = str(a)
		if str(b)[:1] != '-':
			b = '+' + str(b)
		else:
			b = str(b)	
		print('(x'+a+')^2 + (y'+b+')^2 = ' + str(c))
	return('Finished')
def _S2N():
	print('(x-a)^2 + (y-b)^2 = r^2')
	a = int(input('a is:'))
	b = int(input('b is:'))
	r = int(input('r is:'))
	print('(x('+str(a)+'))^2 + (y('+str(b)+'))^2 = ' + str(r))
	print('x^2+y^2+('+str(2*a)+'x)+('+str(2*b)+'y)+('+str(a*a+b*b-r*r)+')=0')
	return('Finished')
if i == 'N':_N2S()
elif i == 'S':_S2N()
else:pass
os.system('pause')
#copyright Kevin Y. Wong