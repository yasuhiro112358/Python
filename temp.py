import numpy as np
import matplotlib.pyplot
import wave_func as wf

fileName = 'soundFile/Polymaster Pitch - UNSW Founders 10x Demo Day 2023.wav'
data = wf.read_wave(fileName)
print(data)

# sampleRate = data.getframerate()
# 変換後のdataはフレームレートのデータを持っていない
sampleRate = 44100

time = np.linspace(0, len(data) / sampleRate, num = len(data))
# # 横軸の１単位の長さを計算してるっぽい。

matplotlib.pyplot.title('Waveform of Audio File')
matplotlib.pyplot.plot(time, data, color = 'blue', lw = 0.5)
matplotlib.pyplot.xlabel('Time [sec]')
matplotlib.pyplot.ylabel('Amplitude')
matplotlib.pyplot.show()

# テストコメント
# GitHubの動作テスト
print('Hello GitHub!')

# This is written after chenge of local place to save Files.