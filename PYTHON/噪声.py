import numpy
import scipy
import matplotlib
import skimage
import os
from skimage import io,transform
S = io.imread('Z.png')
io.imshow(skimage.util.random_noise(S,mode='gaussian',seed=None,clip=True))
io.show()
'''
mode:
	gaussian
	localvar
	poisson
	salt
	pepper
	s&p
	speckle
seed:
	int
mean:
	float
	used in Gau. and Spe.
var:
	float
	used in Gau. and Spe.
local_vars:
	used in Loc.
amount:
	used in Sal. Pep. S&P
salt_vs_pepper
	float
'''