
# ========
# This code is from https://moromisenpy.com/python_wav/
# ========

#-- coding: utf-8 --
import numpy as np
import wave

def binary2float(frames, length, sampwidth):
    if sampwidth == 1:
        data = np.frombuffer(frames, dtype=np.uint8) 
        data = data - 128
    elif sampwidth == 2:
        data = np.frombuffer(frames, dtype=np.int16) 
        # binary to int
        # これが基本的にやりたいこと
        # データタイプにint8やint24がないことが問題らしい
    elif sampwidth == 3:
        a8 = np.frombuffer(frames, dtype=np.uint8)
        tmp = np.empty([length, 4], dtype=np.uint8)
        tmp[:, :sampwidth] = a8.reshape(-1, sampwidth)
        tmp[:, sampwidth:] = (tmp[:, sampwidth - 1 : sampwidth] >> 7) * 255
        data = tmp.view("int32")[:, 0]
        # 理解できない！
    elif sampwidth == 4:
        data = np.frombuffer(frames, dtype=np.int32)
        # これは16 bitと同様に、素直な処理

    # Normalize (int to float)
    data = data.astype(float) / (2**(8*sampwidth - 1)) 
    # 値を-1から1の間に収めている

    return data

def float2binary(data, sampwidth):
    # Normalize (float to int)
    data = (data*(2**(8*sampwidth - 1) - 1)).reshape(data.size, 1)

    if sampwidth == 1:
        data = data + 128
        frames = data.astype(np.uint8).tobytes()
    elif sampwidth == 2:
        frames = data.astype(np.int16).tobytes()
    elif sampwidth == 3:
        a32 = np.asarray(data, dtype=np.int32)
        a8 = (a32.reshape(a32.shape + (1,)) >> np.array([0, 8, 16])) & 255
        frames = a8.astype(np.uint8).tobytes()
        # 理解できない！基礎的な知識が足りない。
    elif sampwidth == 4:
        frames = data.astype(np.int32).tobytes()

    return frames

def read_wave(file_name, start=0, end=0):
    file = wave.open(file_name, "rb") # Open file with read only.
    sampwidth = file.getsampwidth()
    nframes = file.getnframes()

    file.setpos(start)
    if end == 0:
        length = nframes - start
    else:
        length = end - start + 1
    frames = file.readframes(length)

    file.close() # close file

    return binary2float(frames, length, sampwidth) 
    # binary to float

def write_wave(file_name, data, sampwidth=3, fs=48000):
    # なぜfsフレームレートを44100にしていないのか？
    # 44100や96000が適切では？
    # sampwithは2: 16 bitか3:24 bitが適切。
    # 1: 8 bitを試したら面白そう。

    file = wave.open(file_name, "wb") # open file for writing

    # setting parameters
    file.setnchannels(1)
    file.setsampwidth(sampwidth) # サンプルバイト数
    file.setframerate(fs) # サンプリング周波数（フレームレート）の設定

    frames = float2binary(data, sampwidth) # float to binary

    file.writeframes(frames)

    file.close() # close file

def getParams(file_name):
    file = wave.open(file_name) # Open file
    params = file.getparams() 
    file.close() # Close file
    return params


# ========
# 動作確認
# ========

fileName = 'soundFile/Polymaster Pitch - UNSW Founders 10x Demo Day 2023.wav'
data = read_wave(fileName, start=0, end=0)
print(data)


