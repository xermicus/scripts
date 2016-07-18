# Some python-fu I found useful for solving some stego ctf tasks

# unsigned int to 8 digit binary string
format(130, '08b')

# signed 16bit int to binary
format(130 & hex(2**16-1), 'b')

# signed 32bit int to binary
format(130 & hex(2**32-1), 'b')

# binary string to int
int('01110111', 2)

# int to char
chr(119)

# char to int 
ord('w')

# lsb of a number
lsb = number & 1

# print binary string
print ''.join(chr(int(data[i:i+8], 2)) for i in xrange(0, len(data), 8))

# ternary operator in python
a if c else b

# loop through pixels of an image
from PIL import Image, ImageFilter
im = Image.open("img.png").convert("RGB")
pixs = im.load()
w, h = im.size
for y in xrange(h):
	for x in xrange(w):
		pixel = pixs[x,y]

# loop through frames of a (stereo) wave audio file (python-wavefile)
import wave
wave_file = wave.open('audio_file.wav', 'rb')
for i in range(wave_file.getnframes()):
  val = struct.unpack("hh", str(wave_file.readframes(1))) # convert frame to int values

# loop through frames of a (stereo) wave audio file (scipy)
from scipy.io import wavfile
fs, data = wavfile.read('audio_file.wav')
for i in range(len(data) - 1):
        frame = data[i]
