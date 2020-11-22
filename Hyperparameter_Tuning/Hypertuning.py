from tensorflow import keras
import kerastuner as kt
import winsound
from Data_Prep_Model_1 import generate_data as generate_data_1
from Data_Prep_Model_2 import generate_data as generate_data_2
from Data_Prep_Model_3 import generate_data as generate_data_3
from Data_Prep_Model_4 import generate_data as generate_data_4
import os 

os.chdir('C:\\Users\\Paulo_Rocha\\Desktop\\Tese\\Tese_code\\Hyperparameter_Tuning')

path = 'C:\\Users\\Paulo_Rocha\\Desktop\\Tese\\Tese_code\\Hyperparameter_Tuning\\Results' 

# %% Set data to be used

train_percentage = 0.70
validation_percentage = 0.15

Data_1 = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,1,1,1]
Data_2 = [2,1,1,2,0,2,2,1]
Data_3 = [2,2,1,1,0,1,2,1]
Data_4 = [1,1,1,2,0,0,0,1]

input_var_1, output_var_1, _ = generate_data_1(3, 0, Data_1)
input_var_2, output_var_2, _, _, _ = generate_data_2( 0, Data_2)
input_var_3, output_var_3, _, _, _ = generate_data_3( 0, Data_3)
input_var_4, output_var_4, _, _, _ = generate_data_4( 0, Data_4)

def cut_var(input_var,output_var):

    data_index=[int(train_percentage*len(input_var)),int((train_percentage+validation_percentage)*len(input_var))]

    Train_in = input_var[:data_index[0],:]
    Train_out = output_var[:data_index[0],:]

    Val_in = input_var[data_index[0]+1:data_index[1],:]
    Val_out = output_var[data_index[0]+1:data_index[1],:]

    Test_in = input_var[data_index[1]+1:,:]
    Test_out = output_var[data_index[1]+1:,:]

    input_shape = input_var.shape
    
    return Train_in, Train_out, Val_in, Val_out, Test_in, Test_out, input_shape

Train_in_1, Train_out_1, Val_in_1, Val_out_1, Test_in_1, Test_out_1, input_shape_1 = cut_var(input_var_1,output_var_1)
Train_in_2, Train_out_2, Val_in_2, Val_out_2, Test_in_2, Test_out_2, input_shape_2 = cut_var(input_var_2,output_var_2)
Train_in_3, Train_out_3, Val_in_3, Val_out_3, Test_in_3, Test_out_3, input_shape_3 = cut_var(input_var_3,output_var_3)
Train_in_4, Train_out_4, Val_in_4, Val_out_4, Test_in_4, Test_out_4, input_shape_4 = cut_var(input_var_4,output_var_4)

#%% Define Model

def model_creation_1(hp):
    
    hp_units_1 = hp.Int('units_1', min_value = 2, max_value = 60, step = 2)
    hp_units_2 = hp.Int('units_2', min_value = 0, max_value = 60, step = 2)
    
    hp_learning_rate = hp.Choice('learning_rate', values = [0.1, 0.01, 0.001, 0.0001, 0.00001],default = 0.01)
    hp_activation_function = hp.Choice('Activation_function', values = ['relu','tanh','sigmoid'])
    
    model = keras.models.Sequential()
    model.add(keras.layers.Dense( hp_units_1 , activation=hp_activation_function , input_shape=(59,)))
    if hp_units_2 != 0:
        model.add(keras.layers.Dense( hp_units_2 , activation=hp_activation_function ))
    model.add(keras.layers.Dense( 1 , activation=hp_activation_function ))

    opt = keras.optimizers.RMSprop(learning_rate = hp_learning_rate)
    model.compile(optimizer=opt, loss='mse', metrics=['mse'])

    return model

def model_creation_2(hp):
    
    hp_units_1 = hp.Int('units_1', min_value = 1, max_value = 10, step = 1, default = 8 )
    hp_units_2 = hp.Int('units_2', min_value = 0, max_value = 10, step = 1, default = 4 )
    
    hp_learning_rate = hp.Choice('learning_rate', values = [0.1, 0.01, 0.001, 0.0001, 0.00001],default = 0.01)
    hp_activation_function = hp.Choice('Activation_function', values = ['relu','tanh','sigmoid'])
    
    model = keras.models.Sequential()
    model.add(keras.layers.Dense( hp_units_1 , activation=hp_activation_function , input_shape=(8,)))
    if hp_units_2 != 0:
        model.add(keras.layers.Dense( hp_units_2 , activation=hp_activation_function ))
    model.add(keras.layers.Dense( 1 , activation=hp_activation_function ))

    opt = keras.optimizers.RMSprop(learning_rate = hp_learning_rate)
    model.compile(optimizer=opt, loss='mse', metrics=['mse'])

    return model

def model_creation_3(hp):
    
    hp_units_1 = hp.Int('units_1', min_value = 1, max_value = 10, step = 1, default = 7)
    hp_units_2 = hp.Int('units_2', min_value = 0, max_value = 10, step = 1, default = 3)

    hp_learning_rate = hp.Choice('learning_rate', values = [0.1, 0.01, 0.001, 0.0001, 0.00001],default = 0.01)
    hp_activation_function = hp.Choice('Activation_function', values = ['relu','tanh','sigmoid'])
    
    model = keras.models.Sequential()
    model.add(keras.layers.Dense( hp_units_1 , activation=hp_activation_function , input_shape=(7,)))
    if hp_units_2 != 0:
        model.add(keras.layers.Dense( hp_units_2 , activation=hp_activation_function ))
    model.add(keras.layers.Dense( 1 , activation=hp_activation_function ))

    opt = keras.optimizers.RMSprop(learning_rate = hp_learning_rate)
    model.compile(optimizer=opt, loss='mse', metrics=['mse'])

    return model

def model_creation_4(hp):
    
    hp_units_1 = hp.Int('units_1', min_value = 1, max_value = 10, step = 1, default = 7)
    hp_units_2 = hp.Int('units_2', min_value = 0, max_value = 10, step = 1, default = 3)
    
    hp_learning_rate = hp.Choice('learning_rate', values = [0.1, 0.01, 0.001, 0.0001, 0.00001], default = 0.01)
    hp_activation_function = hp.Choice('Activation_function', values = ['relu','tanh','sigmoid'])
    
    model = keras.models.Sequential()
    model.add(keras.layers.Dense( hp_units_1 , activation=hp_activation_function , input_shape=(7,)))
    if hp_units_2 != 0:
        model.add(keras.layers.Dense( hp_units_2 , activation=hp_activation_function ))
    model.add(keras.layers.Dense( 1 , activation=hp_activation_function ))

    opt = keras.optimizers.RMSprop(learning_rate = hp_learning_rate)
    model.compile(optimizer=opt, loss='mse', metrics=['mse'])

    return model
#%% Define Tuner

print('Model_1')

tuner_1 = kt.BayesianOptimization(model_creation_1,
                                  objective = 'mse',
                                  max_trials = 200,
                                  seed=None, 
                                  hyperparameters=None, 
                                  tune_new_entries=True, 
                                  allow_new_entries=True,
                                  directory = path,
                                  project_name = 'Model_1_HP',
                                  overwrite=True,
                                  executions_per_trial=2)

tuner_1.search(x=Train_in_1,
               y=Train_out_1,
               validation_data=(Val_in_1, Val_out_1),
               verbose = 0)


print('\nModel_1_Summary\n')
tuner_1.results_summary()

freq_1 = 200
freq_2 = 1000  
duration = 1000  
winsound.Beep(freq_1, duration)
winsound.Beep(freq_2, duration)
winsound.Beep(freq_1, duration)

print('Model_2')

tuner_2 = kt.BayesianOptimization(model_creation_2,
                                  objective = 'mse',
                                  max_trials = 100,
                                  seed=None, 
                                  hyperparameters=None, 
                                  tune_new_entries=True, 
                                  allow_new_entries=True,
                                  directory = path,
                                  project_name = 'Model_2_HP',
                                  overwrite=True,
                                  executions_per_trial=2)

tuner_2.search(x=Train_in_2,
               y=Train_out_2,
               validation_data=(Val_in_2, Val_out_2),
               verbose = 0)


print('\nModel_2_summary\n')
tuner_2.results_summary()
 
winsound.Beep(freq_1, duration)
winsound.Beep(freq_2, duration)
winsound.Beep(freq_1, duration)

print('Model_3')

tuner_3 = kt.BayesianOptimization(model_creation_3,
                                  objective = 'mse',
                                  max_trials = 100,
                                  seed=None, 
                                  hyperparameters=None, 
                                  tune_new_entries=True, 
                                  allow_new_entries=True,
                                  directory = path,
                                  project_name = 'Model_3_HP',
                                  overwrite=True,
                                  executions_per_trial=2)

tuner_3.search(x=Train_in_3,
               y=Train_out_3,
               validation_data=(Val_in_3, Val_out_3),
               verbose = 0)


print('\nModel_3_summary\n')
tuner_3.results_summary()

winsound.Beep(freq_1, duration)
winsound.Beep(freq_2, duration)
winsound.Beep(freq_1, duration)

print('Model_4')

tuner_4 = kt.BayesianOptimization(model_creation_4,
                                  objective = 'mse',
                                  max_trials = 100,
                                  seed=None, 
                                  hyperparameters=None, 
                                  tune_new_entries=True, 
                                  allow_new_entries=True,
                                  directory = path,
                                  project_name = 'Model_4_HP',
                                  overwrite=True,
                                  executions_per_trial=2)

tuner_4.search(x=Train_in_4,
               y=Train_out_4,
               validation_data=(Val_in_4, Val_out_4),
               verbose = 0)

print('\nModel_4_summary\n')
tuner_4.results_summary()

print('\n --------------Parameter summary------------ \n')
print('\n Model 1 Best Parameters \n')
tuner_1.get_best_hyperparameters(1)[0]
print('\n Model 2 Best Parameters \n')
tuner_1.get_best_hyperparameters(1)[0]
print('\n Model 3 Best Parameters \n')
tuner_1.get_best_hyperparameters(1)[0]
print('\n Model 4 Best Parameters \n')
tuner_1.get_best_hyperparameters(1)[0]

freq_1 = 200
freq_2 = 1000  
duration = 1000  
winsound.Beep(freq_1, duration)
winsound.Beep(freq_2, duration)
winsound.Beep(freq_1, duration)
winsound.Beep(freq_2, duration)
winsound.Beep(freq_1, duration)