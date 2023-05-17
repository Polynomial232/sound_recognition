"""
    docstring
"""
import os
import time
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import tensorflow as tf
import tensorflow_io as tfio
from text_classification import get_class
from functions.decision import check_decision

import pathlib

PATH = pathlib.Path(__file__).parent.resolve()
LENGTH = 48000
FRAME_LENGTH = 80
FRAME_STEP = 32
MODEL_PATH = f'{PATH}/model/ringing_1680688942.8656914.h5'

model = tf.keras.models.load_model(MODEL_PATH)

def load_wav_16k_mono(filename):
    """
        docstring
    """

    file_contents = tf.io.read_file(filename)
    wav, sample_rate = tf.audio.decode_wav(file_contents, desired_channels=1)
    # wav, sample_rate = tf.audio.decode_wav(file_contents, desired_channels=1)
    wav = tf.squeeze(wav, axis=-1)
    sample_rate = tf.cast(sample_rate, dtype=tf.int64)
    wav = tfio.audio.resample(wav, rate_in=sample_rate, rate_out=16000)

    return wav

def preprocess_predict(sample, _):
    """
        docstring
    """

    sample = sample[0]
    zero_padding = tf.zeros([48000] - tf.shape(sample), dtype=tf.float32)
    wav = tf.concat([zero_padding, sample],0)
    spectrogram = tf.signal.stft(wav, frame_length=FRAME_LENGTH, frame_step=FRAME_STEP)
    spectrogram = tf.abs(spectrogram)
    spectrogram = tf.expand_dims(spectrogram, axis=2)

    return spectrogram

def ringing_recognition(file_path, provider):
    """
        docstring
    """

    wav = load_wav_16k_mono(file_path)

    audio_slices = tf.keras.preprocessing.timeseries_dataset_from_array(
        wav, wav,
        sequence_length=LENGTH,
        sequence_stride=LENGTH,batch_size=1
    )
    audio_slices = audio_slices.map(preprocess_predict)
    audio_slices = audio_slices.batch(64)

    yhat = model.predict(audio_slices)
    yhat = [0 if prediction < 0.99 else 1 for prediction in yhat]
    
    
    classes, status = get_class(file_path)
    if status == -1:
        classes, status = check_decision(classes, provider)
        
        return classes, status

    if yhat.count(1) > 1:
        classes = 'valid'
        status = 100
    elif yhat.count(1) == 1:
        classes = 'valid-online'
        status = 100

    return classes, status
