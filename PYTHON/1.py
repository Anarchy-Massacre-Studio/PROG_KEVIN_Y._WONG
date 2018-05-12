import struct as st
def ROT13(Inputs):
	#Inputs = input('ROT13')
	Output = ''
	CODEX = {'A':'N','B':'O','C':'P','D':'Q','E':'R','F':'S','G':'T','H':'U','I':'V','J':'W','K':'X','L':'Y','M':'Z','a':'n','b':'o','c':'p','d':'q','e':'r','f':'s','g':'t','h':'u','i':'v','j':'w','k':'x','l':'y','m':'z','N':'A','O':'B','P':'C','Q':'D','R':'E','S':'F','T':'G','U':'H','V':'I','W':'J','X':'K','Y':'L','Z':'M','n':'a','o':'b','p':'c','q':'d','r':'e','s':'f','t':'g','u':'h','v':'i','w':'j','x':'k','y':'l','z':'m'}
	for Input in Inputs:
		if Input not in CODEX:Output = Output + Input
		else:Output = Output + CODEX[Input]
	print(Output)
def MINIKEYBROAD(Inputs):
	# = input('MINIKETBROAD')#利用小键盘，字母笔顺
	Output = ''
	CODEX = {'A':'841863456','B':'74178965321','C':'9874123','D':'74178621','E':'741789456123','F':'741789456','G':'987412563','H':'7415963','I':'789852123','J':'7898521','K':'741953','L':'74123','M':'74148525963','N':'1475369','O':'78963214','P':'741789654','Q':'7896321453','R':'74178965453','S':'987456321','T':'789852','U':'7412369','V':'74269','W':'7412585369','X':'753951','Y':'7529','Z':'7895123','a':'841863456','b':'74178965321','c':'9874123','d':'74178621','e':'741789456123','f':'741789456','g':'987412563','h':'7415963','i':'789852123','j':'7898521','k':'741953','l':'74123','m':'74148525963','n':'1475369','o':'78963214','p':'741789654','q':'7896321453','r':'74178965453','s':'987456321','t':'789852','u':'7412369','v':'74269','w':'7412585369','x':'753951','y':'7529','z':'7895123'}
	for Input in Inputs:
		if Input not in CODEX:Output = Output + Input + ','
		else:Output = Output + CODEX[Input] + ','
	print(Output[:len(Output)-1])
def KEYBROAD1():
	Inputs = input('KEYBROAD1\n')
	Output = ''
	CODEX = {'Q':'1:1','M':'7:3','q':'1:1','m':'7:3','W':'2:1','N':'6:3','w':'2:1','n':'6:3','E':'3:1','B':'5:3','e':'3:1','b':'5:3','R':'4:1','V':'4:3','r':'4:1','v':'4:3','T':'5:1','C':'3:3','t':'5:1','c':'3:3','Y':'6:1','X':'2:3','y':'6:1','x':'2:3','U':'7:1','Z':'1:3','u':'7:1','z':'1:3','I':'8:1','L':'9:2','i':'8:1','l':'9:2','O':'9:1','K':'8:2','o':'9:1','k':'8:2','P':'0:1','J':'7:2','p':'0:1','j':'7:2','A':'1:2','H':'6:2','a':'1:2','h':'6:2','S':'2:2','G':'5:2','s':'2:2','g':'5:2','D':'3:2','F':'4:2','d':'3:2','f':'4:2'}
	for Input in Inputs:
		if Input in CODEX:Output = Output + CODEX[Input] + ','
		else:Output = Output + Input + ','
	print(Output)
def BS64(Inputs):
	t=['','','',''];I = '';j = 0;J = '';T = ''
	CODEX = {0:'A',16:'Q',32:'g',48:'w',1:'B',17:'R',33:'h',49:'x',2:'C',18:'S',34:'i',50:'y',3:'D',19:'T',35:'j',51:'z',4:'E',20:'U',36:'k',52:'0',5:'F',21:'V',37:'l',53:'1',6:'G',22:'W',38:'m',54:'2',7:'H',23:'X',39:'n',55:'3',8:'I',24:'Y',40:'o',56:'4',9:'J',25:'Z',41:'p',57:'5',10:'K',26:'a',42:'q',58:'6',11:'L',27:'b',43:'r',59:'7',12:'M',28:'c',44:'s',60:'8',13:'N',29:'d',45:'t',61:'9',14:'O',30:'e',46:'u',62:'+',15:'P',31:'f',47:'v',63:'/'}
	#Inputs = bytes(Inputs,'utf-8')
	if (((len(Inputs) / 3) - (len(Inputs) // 3)) * 2) != 0:Inputs = Inputs + b'\0' * int(3 - (((len(Inputs) / 3) - (len(Inputs) // 3)) * 2))
	for i in Inputs:
		i = bin(i)
		if len(i[2:]) <= 8:i = '0'*(8-(len(i[2:]))) + i[2:];I = I + i
	for i in range(len(Inputs)//3):
		J = I[i*24:i*24+24]
		t[0] = CODEX[int(J[:6],2)];t[1] = CODEX[int(J[6:12],2)];t[2] = CODEX[int(J[12:18],2)];t[3] = CODEX[int(J[18:],2)]
		if t[1] == 'A' and t[2] == 'A' and t[3] == 'A':t[1] = '=';t[2] = '=';t[3] = '='
		elif t[2] == 'A' and t[3] == 'A':t[2] = '=';t[3] = '='
		elif t[3] == 'A':t[3] = '='
		T = T + t[0] + t[1] + t[2] + t[3]
	return(T)
def UnBS64(Inputs):
	t=['','','',''];I = '';j = 0;J = b'';T = ''
	CODEX = {'A':0 ,'Q':16,'g':32,'w':48,'B':1 ,'R':17,'h':33,'x':49,'C':2 ,'S':18,'i':34,'y':50,'D':3 ,'T':19,'j':35,'z':51,'E':4 ,'U':20,'k':36,'0':52,'F':5 ,'V':21,'l':37,'1':53,'G':6 ,'W':22,'m':38,'2':54,'H':7 ,'X':23,'n':39,'3':55,'I':8 ,'Y':24,'o':40,'4':56,'J':9 ,'Z':25,'p':41,'5':57,'K':10,'a':26,'q':42,'6':58,'L':11,'b':27,'r':43,'7':59,'M':12,'c':28,'s':44,'8':60,'N':13,'d':29,'t':45,'9':61,'O':14,'e':30,'u':46,'+':62,'P':15,'f':31,'v':47,'/':63,'=':64}
	for Input in Inputs:
		Input = CODEX[Input]
		if Input != 64:
			Input = bin(Input)[2:]
			if len(Input) < 6:Input = '0' * (6-len(Input)) + Input
			I = I + Input
	for i in range(len(I)//8):
		J = J + st.pack('B',int(I[i*8:i*8+8],2))
	return(J)

path = input('path \'n\' name')
with open(path,'rb') as f:
	with open('1.txt=','w') as F:
		READ = f.read()
		F.write(BS64(READ))
with open(path+'=','r') as f:
	with open('2.txt','wb') as F:
		READ = f.read()
		F.write(UnBS64(READ))

import os
os.system('pause')