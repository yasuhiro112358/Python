import sys
import wave
import numpy
# import matplotlib
import matplotlib.pyplot

audioFile = wave.open('soundFile/Polymaster Pitch - UNSW Founders 10x Demo Day 2023.wav', 'r')

raw = audioFile.readframes(-1) # all frames

raw = numpy.frombuffer(raw, dtype = 'int16') 
# 16進数のデータを読めるように変換。詳しくはよくわからん。

sampleRate = audioFile.getframerate()
# １秒間に何回データを取ったか。（サンプリング周波数）
print('Sample Rate: %s Hz' % (sampleRate))

if audioFile.getnchannels() == 2:
    print('Stereo Files are not suppored. Use Mono Files.')
    sys.exit()

time = numpy.linspace(0, len(raw) / sampleRate, num = len(raw))
# 横軸の１単位の長さを計算してるっぽい。

matplotlib.pyplot.title('Waveform of Audio File')
matplotlib.pyplot.plot(time, raw, color = 'blue', lw = 0.5)
matplotlib.pyplot.xlabel('Time [sec]')
matplotlib.pyplot.ylabel('Amplitude')
matplotlib.pyplot.show()

