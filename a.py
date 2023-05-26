from text_classification.classes.PredictResponse import PredictResponse
from text_classification.classes.PreProses import PreProses
from functions.tokenize import token_encoding, token_decoding
from functions.recognition import main

# text = "The number you are calling does not exist. Please check the number. No more young come to you. Sedan tida actives at over add a deluar service area. The number you are calling cannot be reached at the moment. The number you are calling does not exist. Please check the number. Nomor yang kamu tuju, sedang tidak aktif atau berada di luar service area. The number you are calling cannot be reached at the moment."

text = main('valid.wav', 'valid')

pre_proses = PreProses()
predict_response = PredictResponse()
predict = predict_response.predict(text)

tags, all_words = pre_proses.get_raw_data()

tokenized_sentence = pre_proses.tokenizing(text)
sentence_words = [pre_proses.stemming(word) for word in tokenized_sentence]
token_encode = token_encoding(sentence_words, all_words)

print(token_encode)
print(print(token_decoding(token_encode, all_words)))
print(predict)
