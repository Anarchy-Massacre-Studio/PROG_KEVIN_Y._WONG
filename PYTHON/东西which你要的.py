import random  
LISTT=[];LISTT2=[]
#A=12;B=12;COUNT=12
a=0;b=0
A=int(input('m:\n'))
B=int(input('n:\n'))
COUNT=int(input('COUNT:\n'))
COUNTTtl=int(COUNT/B)+1
for i in range(B):
	resultListM=random.sample(range(0,A),COUNTTtl)
	for j in range(COUNTTtl):
		LISTT.append('('+str(resultListM[j])+','+str(i)+')')
print(LISTT)
for i in LISTT:
	i=i[1:len(i)-1]
	i=i.split(',')
	a=int(i[0]) + int(random.randint(-1,1))
	if a > A:
		a = a - 1
	elif a < 0:
		a = a + 1
	b=int(i[1]) + int(random.randint(-1,1))
	if b > B:
		b = b - 1
	elif b < 0:
		b = b + 1
	LISTT2.append('('+str(a)+','+str(b)+')')
print(LISTT2)
