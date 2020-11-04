# this function reads hyperparameter tunning

#############################################

import os
import tensorflow as tf
from tensorflow import keras
import IPython

import os
import json
import tensorflow as tf

#%% Read and print tests in diretory to chose model

path = 'C:/Users/Paulo_Rocha/Desktop/Tese/Tese_code/Model_1/Hyperparameter_Tuning/Results'

Model_names = next(os.walk(path))[1]

print('###############################\n##   Hyperparameter reader   ##\n###############################')

print('\nNunber - Model to read\n-----------------------')

for i in range(len(Model_names)):
    
    A = [Model_names[i]]
    
    print('{:3d}    - {d[0]}'.format(i,d=A))
 
Chosen = input('Enter number:') 

Index = int(Chosen)

with open(path +'/'+ Model_names[Index]+'/tuner.json') as json_file:
    data = json.load(json_file)

# %%   