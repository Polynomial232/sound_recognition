"""
    fungsi untuk mengubah sample rate audio
"""

from pydub import AudioSegment
import time

def samplerate_conv(file_input, file_output=None, sample_rate=48000):
    sound = AudioSegment.from_wav(file_input)
    sound_w_new_fs = sound.set_frame_rate(sample_rate)
    file_output = file_input[:-4]+str(time.time())+".wav" if file_output is None else file_output
    sound_w_new_fs.export(file_output, format="wav")
    
    return file_output
