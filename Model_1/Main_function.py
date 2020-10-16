
from tensorflow import keras
from NN_build import build_MLP
from NN_build import build_LSTM
import pickle as pr
from Data_Prep_Model_1 import generate_data

# %% Set optmizer

Learning_rate = 0.005
Momentum = 0.2
opt = keras.optimizers.RMSprop(learning_rate = Learning_rate, momentum = Momentum)

train_percentage = 0.75
validation_perentagem = 0.1

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

model_type = 'MLP'
             
name_model = 'Example_2'
    
input_var, output_var, time_plot = generate_data(1, 0, Data)
data_index=[int(train_percentage*len(time_plot)),int((train_percentage+validation_perentagem)*len(time_plot))]

#%% Main Model
    
if model_type == 'MLP':
    
    hidden_layer_info=[0,0]
    
    hidden_layer_info[0] = [10,'relu']
    hidden_layer_info[1] = [10,'relu']
    
    test_parameters = [400,50]
    
    show_progress = 2
    
    print('\nMain Model 1')
    
    r, RMSE, MAE, save_model = build_MLP(input_var, output_var, time_plot, data_index, hidden_layer_info, opt, test_parameters, name_model, Data, show_progress)

else:

    print('what')
    
if save_model == 1:
    
    pr.dump( [ Data, r, MAE, RMSE ] , open('Results/'+name_model+'/'+'Value_quality.p','wb'))

    print('\n---------- DONE ----------' )


