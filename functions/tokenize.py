def token_encoding(sentence_words, all_words):
    indexs = list()

    for word in sentence_words:
        try:
            word_index = all_words.index(word)
            indexs.append(word_index)
        except:
            continue
    
    return indexs

def token_decoding(token_encode, all_words):
    words = list()

    for index in token_encode:
        words.append(all_words[index])

    return words