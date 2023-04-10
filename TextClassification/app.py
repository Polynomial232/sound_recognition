from classes.Train import Train
from classes.PredictResponse import PredictResponse
from classes.PreProses import PreProses
from function import predict_casual
import json
from transcribeAudio import transcribeAudio
import os


def response(text=None, tag=None):

    predict_response = PredictResponse()
    pre_proses = PreProses()

    if text:
        response_bot = predict_casual(text)
        if response_bot:
            return response_bot

        predict = predict_response.predict(text)
        response_bot = predict_response.get_response(predict)
        if response_bot.get('tag') == None:
            print(text)
        return response_bot

    response_bot = predict_response.get_by_tag(tag)
    if response_bot:
        return response_bot
    return pre_proses.get_intents().get('intents')[0]


# with open('model/ringing/tagihan/intents.json') as file:
#     json_intents = json.loads(file.read())
# for i in json_intents.get('intents')[1].get('patterns'):
#     text = i
#     response('ringing', 'tagihan', text)

def getTag(pathWav, NamaWav):
    text = transcribeAudio(pathWav)
    responseBot = response(text)
    os.remove(f'{NamaWav}.txt')
    return responseBot.get('tag')


getTag('raw_0.wav', 'raw_0')
