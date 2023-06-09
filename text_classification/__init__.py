"""
    docstring
"""

import os
from text_classification.classes.PredictResponse import PredictResponse
from text_classification.transcribe_audio import transcribe_audio

def response(text):
    """
        docstring
    """
    
    predict_response = PredictResponse()
    predict = predict_response.predict(text)

    #print({round(predict[1].item(),3})
    print(predict)
    if predict[1].item() < 0.8:
        return 'unknown'

    tag = predict_response.get_response(predict)

    return tag.get('tag')

def get_class(file_path):
    """
        docstring
    """

    predict_response = PredictResponse()
    file_path = file_path.replace('\\', '/')
    filename = file_path.split('/')[-1][:-4]
    # filename = file_path.split('\\')[-1][:-4] # windows

    text = transcribe_audio(file_path, filename)

    tag = response(text)

    os.remove(f'{filename}.txt')
    result = predict_response.get_by_tag(tag)

    return result.get('tag'), result.get('status'), text
