import numpy as N
import wave

towrite = ''
for freq in [329.63, 440.00, 293.66, 392.00]:
     duration = 1
     samplerate = 44100
     samples = duration*samplerate
     period = samplerate / float(freq) # in sample points
     omega = N.pi * 2 / period

     xaxis = N.arange(samples,dtype = N.float)
     ydata = 16384 * N.sin(xaxis*omega)

     signal = N.resize(ydata, (samples,))

     towrite += ''.join([wave.struct.pack('h',s) for s in signal])

f = wave.open('test.wav', 'wb')
f.setparams((1,2,44100, 44100*4, 'NONE', 'noncompressed'))
f.writeframes(towrite)
f.close()
