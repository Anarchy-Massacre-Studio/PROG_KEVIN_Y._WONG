# -*- coding:utf-8 -*-
import os,sys,math,struct
Pw='DEF'
D = {};PwT = 0
print('INFO:\n参数不可以留空\n\nInput1:\n	  InputFilePath\nInput2:\n	  OutputPath\nPlz Enter The Function which Need to Use at Input3(Like \n-m(Merger),\n-d(Dismantling),\n-a(Encryption),\n-x(Decryption),\n-z(Compression),\n-u(Decompression))\nInput4(**):Password(-a,-x.ONLY)')
InputParameter1_InputFilePath =input('请输入需要处理的文件路径及文件名(相对)(e.g. /Windows/TEST.txt)')
InputParameter2_OutputFilePath = input('请输入需要处理的文件的输出文件路径及文件名(相对)(e.g. /Windows/TESTOUTPUT.txt)')
__FUNCTION__ = input('请输入方法(e.g. -m)')
Pw = input('请输入密码(-a,-x:only)(e.g. PASSWORD)')
for PwE in Pw:
	PwM = ord(PwE)
	PwT = PwT + (PwM*315/3)
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
def __AFile2X__(FileNameNPath):
	F = open(FileNameNPath ,'r')
	f = open(os.path.dirname(FileNameNPath)+'~$'+os.path.basename(FileNameNPath) ,'w')
	AChuck = F.read(1)
	while AChuck != b'':
		if AChuck == '':
			break
		AChuck = ord(AChuck)
		AChuck = (float((AChuck**2))*2)-int(PwT)
		AChuckNeedToWrite = '/' + str(AChuck)
		f.write(AChuckNeedToWrite)
		AChuck = F.read(1)
	f.write('/9990')
	with open(os.path.dirname(FileNameNPath)+'~$'+os.path.basename(FileNameNPath) ,'r') as f:
		with open(FileNameNPath,'w') as F:
			Fread = f.read()
			F.write(Fread)
	os.remove(os.path.dirname(FileNameNPath)+'~$'+os.path.basename(FileNameNPath))
def __X2AFile__(FileNameNPath):
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
if __FUNCTION__ == '-m':
	OutputFile = open(InputParameter2_OutputFilePath,'wb')
	__Merge__(InputParameter1_InputFilePath,InputParameter2_OutputFilePath)
	OutputFile.close()
elif __FUNCTION__ == '-d':
	__Dismantlingr__(InputParameter1_InputFilePath,InputParameter2_OutputFilePath)
elif __FUNCTION__ == '-a':
	__AFile2X__(InputParameter1_InputFilePath)
elif __FUNCTION__ == '-x':
	__X2AFile__(InputParameter1_InputFilePath)
elif __FUNCTION__ == '-z':
	__Zip__(InputParameter1_InputFilePath,os.path.getsize(InputParameter1_InputFilePath))
elif __FUNCTION__ == '-u':
	__UnZip__(InputParameter1_InputFilePath,os.path.getsize(InputParameter1_InputFilePath))
elif __FUNCTION__ == '-dr':
	print('GO FUCK URSELF')
else:
	print('Plz Enter the F**king Damn Bloody Function! Lil\' F**ker! Move Ur Ass NOW!')
#	Copyright2017 Anarchy Massacre, Stu. Kevin C. Wong. All rights reserved. All rights are reserved.