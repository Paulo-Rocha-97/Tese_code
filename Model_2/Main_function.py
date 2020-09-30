
from tensorflow import keras
from NN_build import build_MLP_main
from NN_build import build_MLP_sec

from NN_build import build_LSTM
import pickle as pr
from Data_Prep_Model_2 import generate_data

# %% Set optmizer

train_percentage = 0.75
validation_perentagem = 0.1

# model ='LSTM'

# if model == 'MLP':

#     hidden_layer_info=[0,0]
    
#     hidden_layer_info[0] = [20,'relu']
#     hidden_layer_info[1] =[6,'relu']
    
#     test_parameters = [300,10]
    
#     name_model = '20_6_MlP_0.001_300'
    
#     build_MLP(input_var, output_var, time_plot, data_index, hidden_layer_info, opt, test_parameters, name_model, save_model)
    
# elif model == 'LSTM':

#     hidden_layer_info=[5]
    
#     test_parameters = [300,10]
    
#     name_model = '5_LSTM_0.001_300'
    
#     build_LSTM(input_var, output_var, time_plot, data_index, hidden_layer_info, opt, test_parameters, name_model)
    
Data = [0,1,3,1,0,1,3,1]

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
   

model_type = 0
             
save_model = 1

run_model = 1

name_model = 'Example'

# name_model = input('Name_model:')
    
input_var, output_var, time_plot, input_var_sec, output_var_sec = generate_data( 0, Data)
data_index=[int(train_percentage*len(time_plot)),int((train_percentage+validation_perentagem)*len(time_plot))]

#%% Main Model
if run_model == 0 or run_model == 2: 
    
    Learning_rate = 0.005
    Momentum = 0.2
    opt = keras.optimizers.RMSprop(learning_rate = Learning_rate, momentum = Momentum)
    
    if model_type == 0:
        
        hidden_layer_info=[0,0]
        
        hidden_layer_info[0] = [10,'relu']
        hidden_layer_info[1] = [10,'relu']
        
        test_parameters = [200,50]
        
        show_progress = 2
        
        print('\nMain Model 2')
        
        r, RMSE, MAE = build_MLP_main(input_var, output_var, time_plot, data_index, hidden_layer_info, opt, test_parameters, name_model, Data, show_progress)

    else:

        hidden_layer_info=[8]
        
        test_parameters = [500,10]
        
        r, RMSE, MAE = build_LSTM(input_var, output_var, time_plot, data_index, hidden_layer_info, opt, test_parameters, name_model)

#%% Run Secondary

if run_model == 1 or run_model == 2: 
    
    Learning_rate = 0.0001
    Momentum = 0.2
    opt = keras.optimizers.RMSprop(learning_rate = Learning_rate, momentum = Momentum)
    
    hidden_layer_info=[0]
    
    hidden_layer_info[0] = [2,'relu']
    
    test_parameters = [150,10]
    
    show_progress = 2
    
    print('\nSecondary Model 2\n')
    
    r_sec, RMSE_sec, MAE_sec = build_MLP_sec(input_var_sec, output_var_sec, time_plot, data_index, hidden_layer_info, opt, test_parameters, name_model, Data, show_progress)

if save_model == 1 and run_model == 0 or 2:
    
    pr.dump( [ Data, r, MAE, RMSE ] , open('Results/'+name_model+'/'+'Value_quality.p','wb'))
    
elif save_model == 1 and run_model == 1 or 2:

    pr.dump( [ Data, r_sec, MAE_sec, RMSE_sec ] , open('Results/'+name_model+'/'+'Value_quality_sec.p','wb'))

    print('\n---------- DONE ----------' )


