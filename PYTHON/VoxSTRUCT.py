#encoding='utf-8'
import struct,os
PAth=input("PATH:")
V=['','','','','','','','','','']
PATH = os.path.abspath(PAth)
with open(PATH,'rb') as f:
	with open(PATH+'X','w') as F:
		print('Already Opened')
		V[0] = f.read(4) #VOX
		Va = f.read(4)
		V[1] = f.read(4) #MAIN
		Va = f.read(24)
		V[2] = f.read(4)
		def __h__():
			if V[2] == b'SIZE':
				Va = f.read(4) #12
				Va = f.read(4) #0
				V[3] = struct.unpack('i',f.read(4)) #X
				V[4] = struct.unpack('i',f.read(4)) #Y
				V[5] = struct.unpack('i',f.read(4)) #Z
				F.write('SizeX,Y,Z:('+str(V[3][0])+','+str(V[4][0])+','+str(V[5][0])+')\n')
			if V[2] == b'XYZI':
				V[3] = struct.unpack('i',f.read(4)) #ChuckSize
				Va = f.read(4) #0
				V[4] = struct.unpack('i',f.read(4)) #VoxelNum
				F.write('ChuckSize:'+str(V[3][0])+'\n')
				F.write('VoxelNum:'+str(V[4][0])+'\n')
				for x in '0'*V[4][0]:
					V[5] = struct.unpack('c',f.read(1))
					V[6] = struct.unpack('c',f.read(1))
					V[7] = struct.unpack('c',f.read(1))
					V[8] = struct.unpack('c',f.read(1))
					F.write('XYZI:('+str(ord(V[5][0]))+','+str(ord(V[6][0]))+','+str(ord(V[7][0]))+','+str(ord(V[8][0]))+')\n')
			if V[2] == b'RGBA':
				Va = f.read(4) #1024
				Va = f.read(4) #0
				for x in '0'*256:
					V[5] = struct.unpack('c',f.read(1))
					V[6] = struct.unpack('c',f.read(1))
					V[7] = struct.unpack('c',f.read(1))
					V[8] = struct.unpack('c',f.read(1))
					F.write('RGBA:('+str(ord(V[5][0]))+','+str(ord(V[6][0]))+','+str(ord(V[7][0]))+','+str(ord(V[8][0]))+')\n')
		__h__()
		V[2] = f.read(4)
		__h__()
		V[2] = f.read(4)
		__h__()