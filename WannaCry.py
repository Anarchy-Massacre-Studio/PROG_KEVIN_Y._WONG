import os,struct,string
Q = input('Please Enter What You Wanna Do:Encrypt, DisEncrypt, KEYRAN...\nPress')
D = input('Please Enter Your File Which Need To (Dis)Encrypt...\n')
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
	with open(data,'w') as f:
		f.write(str.strip(str(fr)))
	with open(data,'a') as f:
		f.write(' '*int(16-(len(str.strip(str(fr)))-(len(str.strip(str(fr)))//16)*16)))
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
def _KEYRAN_(data):
	with open('KEY.txt','wb') as K:
		K.write(os.urandom(256))
if Q == 'Encrypt':				
	_EN_AES_(D)
if Q == 'DisEncrypt':
	_DN_AES_(D)
if Q == 'KEYRAN':
	_KEYRAN_(D)
Q = input('FINISHED\nPress ENTER To Continue')
#Kevin Y. Wong,AMStudio COPYRIGHT 2018