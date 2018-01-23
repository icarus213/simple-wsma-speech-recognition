from fastdtw import fastdtw as dtw
from pydub import AudioSegment
import numpy as np
import time
import os

def normalizedSample(filename):
	s = AudioSegment.from_wav(filename)
	sample = np.array(s.get_array_of_samples()) / (2**((s.sample_width*8)-1)-1)
	return sample

while True:
	print('WAITING FOR DATA...')
	a = time.strftime("%e-%m-%Y_%I/%M/%S-%p_wsma.wav").replace('/0','/').replace('_0','_').replace('/','-')[0:]
	while a not in os.listdir('.'):
		a = time.strftime("%e-%m-%Y_%I/%M/%S-%p_wsma.wav").replace('/0','/').replace('_0','_').replace('/','-')[0:]
		print(a)

	print('RECEIVED')
	import time
	time.sleep(1)
	filename = 'voice.tmp'
	if filename in os.listdir('.'):
		os.remove(name)
		os.rename(a,name)
	else:
		os.rename(a,name)
	data = normalizedSample(filename)
	source = []
	name = []

	for x in os.listdir('data/'):
		source.append(normalizedSample('data/'+x))
		name.append(x)

	distance = []

	for x in source:
		distance.append(dtw(data,x))

	print(name[distance.index(min(distance))])
