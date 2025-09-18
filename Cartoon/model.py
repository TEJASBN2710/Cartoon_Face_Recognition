import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
import os
from keras.models import load_model 

class Algo:
    def __init__(self,name):
        self.name = name
        

    def cnn_algo(self):
        # Recreate the exact same model, including its weights and the optimizer
        
        classes =['AishwaryaRai', 'AbrahamLincoln', 'AdolfHitler', 'AamirKhan', 'Albert', 
        'AmitabhBach', 'Angela', 'Angelina', 'Arnold', 'Barack', 
        'Beyonce', 'Bhagat', 'BillGates', 'Billi']

        da = self.name
        print(da)
        directory = os.getcwd()
        print(directory)

        #path = 'Sign_Modified/BA/BA1-removebg-preview (1).png'
        loaded_model = load_model("Model/ayur_model.h5")
        path = 'upload/'+self.name
        print(path)

        img = tf.keras.preprocessing.image.load_img(path, target_size=(256, 256))
        img_array = tf.keras.preprocessing.image.img_to_array(img)
        img_array = tf.expand_dims(img_array, 0)


        # new_model = tf.keras.models.load_model('my_model.h5')
        
        predictions = loaded_model.predict(img_array)

        print(predictions[0]*100, "\n", classes)
        print("Prediction: ", classes[np.argmax(predictions)], f"{predictions[0][np.argmax(predictions)]*100}%")
        return classes[np.argmax(predictions)],predictions[0][np.argmax(predictions)]*100
       
        