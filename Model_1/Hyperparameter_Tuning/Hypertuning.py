import tensorflow as tf
from tensorflow import keras
import tensorflow.keras.layers as layers
import kerastuner as kt
from Data_Prep_Model_1 import generate_data
import IPython

path = 'C:\\Users\\Paulo_Rocha\\Desktop\\Tese\\Tese_code\\Model_1\\Hyperparameter_Tuning\\Results' 

# %% Set data to be used

train_percentage = 0.80

Data = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

# data_type = [ day index, type of storage, number of days in the past, 
#               number of days in the future, outflow type]
    
# day index: 2 - month; 1 - acconut; 0 - disregard
# type of storage: 0 - none  1 - depth; 2 - volume 
# Number of days past: from 0 to infinity
# Number of days in the future: from 0 to infinity
# outflow type: 0 - unique; 1 - Seperate
# week day info: 0 - week_combine_holiday 1 - week day binary 2 - week day in number
# holiday info: 0 - week_combine_holiday 1 - national holiday 2 - national and galiza holiday
# remove caudal ecologigo: 0 - not remove; 1 - remove caudal ecologico

input_var, output_var, time_plot = generate_data(1, 0, Data)
data_index=[int(train_percentage*len(input_var))]

Train_in = input_var[:data_index[0],:]
Train_out = output_var[:data_index[0],:]

Test_in = input_var[data_index[0]+1:,:]
Test_out = output_var[data_index[0]+1:,:]

input_shape = input_var.shape
output_shape = output_var.shape

#%% Define Model
 
def model_creation(hp):
    
    hp_units = hp.Int('units', min_value = 1, max_value = 60, step = 1)
    
    hp_learning_rate = hp.Choice('learning_rate', values = [1e-2, 1e-3, 1e-4])
    hp_momentum = hp.Choice('momentum', values = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0])
    
    
    model = keras.models.Sequential()
    model.add(layers.Dense( 23 , activation='relu' , input_shape=(23,)))
    model.add(layers.Dense( units = hp_units , activation='relu' ))
    model.add(layers.Dense( 1 , activation='relu' ))

    opt = keras.optimizers.RMSprop(learning_rate = hp_learning_rate, momentum = hp_momentum)
    model.compile(optimizer=opt, loss='mse', metrics=['mse'])

    return model

#%% Define Tuner

tuner = kt.RandomSearch(model_creation,
                        objective = 'mse',
                        max_trials = 5,
                        seed=None, 
                        hyperparameters=None, 
                        tune_new_entries=True, 
                        allow_new_entries=True,
                        directory = path,
                        project_name = 'Teste_model_5' )

tuner.search_space_summary()

tuner.search(x=Train_in,
             y=Train_out,
             epochs=500,
             validation_data=(Test_in, Test_out))

tuner.results_summary()