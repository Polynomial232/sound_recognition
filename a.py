from text_classification.classes.PredictResponse import PredictResponse

text = "The number you are calling cannot be reached. Please try again later. Nomor yang anda tuju tidak dapat hubungi."

predict_response = PredictResponse()

predict = predict_response.predict(text)
print(predict)