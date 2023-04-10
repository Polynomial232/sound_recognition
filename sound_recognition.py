"""
    docstring
"""
import os
import tensorflow as tf
import tensorflow_io as tfio
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

CLASSES = ['invalid','valid']
STATUS = [2, 1]
LENGTH = 48_000
FRAME_LENGTH = 80
FRAME_STEP = 32

model = tf.keras.models.load_model('ringing_1680676815.3388605.h5')

def load_wav_16k_mono(filename):
    """
        docstring
    """

    file_contents = tf.io.read_file(filename)
    wav, sample_rate = tf.audio.decode_wav(file_contents, desired_channels=1)
    wav = tf.squeeze(wav, axis=-1)
    sample_rate = tf.cast(sample_rate, dtype=tf.int64)
    wav = tfio.audio.resample(wav, rate_in=sample_rate, rate_out=16000)

    return wav

def preprocess_predict(sample, index):
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

def recognition(file_path):
    """
        docstring
    """

    wav = load_wav_16k_mono(file_path)

    audio_slices = tf.keras.preprocessing.timeseries_dataset_from_array(
        wav,
        wav,
        sequence_length=LENGTH,
        sequence_stride=LENGTH,
        batch_size=1
    )
    audio_slices = audio_slices.map(preprocess_predict)
    audio_slices = audio_slices.batch(64)

    yhat = model.predict(audio_slices)
    yhat = [0 if prediction < 1 else 1 for prediction in yhat]
    yhat = [1 if sum(yhat) >= 1 else 0][0]

    return CLASSES[yhat], STATUS[yhat]
