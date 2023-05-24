from text_classification.classes.PreProses import PreProses
from functions.tokenize import token_encoding, token_decoding

pre_proses = PreProses()

sentence = 'Tidak menjawab coba lagi nanti ya, lagi sibuk'

tags, all_words = pre_proses.get_raw_data()
tokenized_sentence = pre_proses.tokenizing(sentence)
sentence_words = [pre_proses.stemming(word) for word in tokenized_sentence]
token_encode = token_encoding(sentence_words, all_words)

print(token_encode)

token_decode = token_decoding(token_encode, all_words)

print(token_decode)