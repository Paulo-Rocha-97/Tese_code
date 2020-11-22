from tensorflow import keras
import kerastuner as kt
from Data_Prep_Model_1 import generate_data_1
import os 

os.chdir('C:\\Users\\Paulo_Rocha\\Desktop\\Tese\\Tese_code\\Hyperparameter_Tuning')

path = 'C:\\Users\\Paulo_Rocha\\Desktop\\Tese\\Tese_code\\Hyperparameter_Tuning\\Results' 

# %% Set data to be used 

train_percentage = 0.70
validation_percentage = 0.15

Data = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,1,1,1]

input_var, output_var, time_plot = generate_data_1(3, 0, Data)
data_index=[int(train_percentage*len(time_plot)),int((train_percentage+validation_perentagem)*len(time_plot))]

Train_in = input_var[:data_index[0],:]
Train_out = output_var[:data_index[0],:]

Test_in = input_var[data_index[0]+1:,:]
Test_out = output_var[data_index[0]+1:,:]

input_shape = input_var.shape
print(input_shape)
output_shape = output_var.shape

#%% Define Model
 
def model_creation(hp):
    
    hp_units_1 = hp.Int('units_1', min_value = 1, max_value = 60, step = 1)
    hp_units_2 = hp.Int('units_2', min_value = 0, max_value = 60, step = 1)
    hp_learning_rate = hp.Choice('learning_rate', values = [0.1, 0.05, 0.001, 0.0005, 0.00001])
    hp_momentum = hp.Choice('momentum', values = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0])
    hp_activation_function = hp.Choice('Activation_function', values = ['relu','tanh','sigmoid'])
    
    model = keras.models.Sequential()
    model.add(keras.layers.Dense( hp_units_1 , activation=hp_activation_function , input_shape=(59,)))
    if hp_units_2 != 0:
        model.add(keras.layers.Dense( hp_units_2 , activation=hp_activation_function ))
    model.add(keras.layers.Dense( 1 , activation=hp_activation_function ))

    opt = keras.optimizers.RMSprop(learning_rate = hp_learning_rate, momentum = hp_momentum)
    model.compile(optimizer=opt, loss='mse', metrics=['mse'])

    return model

#%% Define Tuner

tuner = kt.BayesianOptimization(model_creation,
                                objective = 'mse',
                                max_trials = 150,
                                seed=None, 
                                hyperparameters=None, 
                                tune_new_entries=True, 
                                allow_new_entries=True,
                                directory = path,
                                project_name = 'Model_1',
                                overwrite = False)

tuner.search_space_summary()

tuner.search(x=Train_in,
             y=Train_out,
             epochs=350,
             batch_size=50,
             validation_data=(Val_in, val_out))

tuner.results_summary()