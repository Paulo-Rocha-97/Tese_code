import os
import warnings 
from tensorflow import keras
from NN_build import build_MLP
import pickle as pr
from Data_Prep_Model_4 import generate_data

warnings.filterwarnings("ignore", category=RuntimeWarning)

path = os.getcwd()

# %% Set comand window prompts

# name_model = input('Introduce the name of the model: ')

# Number_trial = input('Number of trials: ')

name_model = 'RMSprop_best'

Number_trial =30

Number_trial =int(Number_trial)

# %% Set optmizer

Trial_RMSE = 1

for i in range(Number_trial):

    Learning_rate = 0.1
    opt = keras.optimizers.RMSprop(learning_rate = Learning_rate)
    
    train_percentage = 0.70
    validation_perentagem = 0.1
    
    Data = [1,1,2,1,0,0,0,1]
        
    input_var, output_var, time_plot,_,_= generate_data( 0, Data)
    data_index=[int(train_percentage*len(time_plot)),int((train_percentage+validation_perentagem)*len(time_plot))]

#%% Main Model
              
    print('\n----Trial nº{:2d}----'.format(i+1))
    
    hidden_layer_info=[0]
    
    hidden_layer_info[0] = [7,'sigmoid']
    
    test_parameters = [500,50]
    
    show_progress = 0
        
    r, RMSE, MAE = build_MLP(input_var, output_var, time_plot, data_index, hidden_layer_info, opt, test_parameters, name_model, Data, show_progress, Trial_RMSE)
    
    if RMSE < Trial_RMSE:

        Trial_RMSE =RMSE
        File_path = path+'\\Results\\'+name_model;
        
        pr.dump( [ Data, r, MAE, RMSE ] , open(File_path+'\\'+'Value_quality.p','wb'))
        
#%% secondary model

# name_model = name_model + '_sec'

# # %% Set optmizer

# Trial_RMSE = 1

# for i in range(Number_trial):

#     Learning_rate = 0.001
#     opt = keras.optimizers.RMSprop(learning_rate = Learning_rate)
    
#     train_percentage = 0.70
#     validation_perentagem = 0.1
    
#     Data = [0,2,0,0,0,0,0,1]
        
#     _,_,time_plot, input_var, output_var = generate_data( 0, Data)
#     data_index=[int(train_percentage*len(time_plot)),int((train_percentage+validation_perentagem)*len(time_plot))]

# #%% Main Model
              
#     print('\n----Trial nº{:2d}----'.format(i+1))
    
#     hidden_layer_info=[0]
    
#     hidden_layer_info[0] = [4,'relu']
    
#     test_parameters = [500,50]
    
#     show_progress = 0
        
#     r, RMSE, MAE = build_MLP(input_var, output_var, time_plot, data_index, hidden_layer_info, opt, test_parameters, name_model, Data, show_progress, Trial_RMSE)
    
#     if RMSE < Trial_RMSE:

#         Trial_RMSE =RMSE
#         File_path = path+'\\Results\\'+name_model;
        
#         pr.dump( [ Data, r, MAE, RMSE ] , open(File_path+'\\'+'Value_quality_sec.p','wb'))
        
        