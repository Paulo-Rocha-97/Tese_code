
import time
from tensorflow import keras
from NN_build import build_MLP_main

import numpy as np
import pickle as pr
from Data_Prep_Model_2 import generate_data

# set optimizer settings

Learning_rate = 0.0005
Momentum = 0.2
opt = keras.optimizers.RMSprop(learning_rate = Learning_rate, momentum = Momentum)

train_percentage = 0.75
validation_perentagem = 0.10

# Set diferent test data

Data= np.array([[1,1,0,0,0,0,0,1],
                [1,1,0,1,0,0,0,1],
                [1,1,0,2,0,0,0,1],
                [1,1,0,3,0,0,0,1],
                [1,1,0,4,0,0,0,1],
                [1,1,0,5,0,0,0,1],
                [1,1,1,0,0,0,0,1],
                [1,1,1,1,0,0,0,1],
                [1,1,1,2,0,0,0,1],
                [1,1,1,3,0,0,0,1],
                [1,1,1,4,0,0,0,1],
                [1,1,1,5,0,0,0,1],
                [1,1,2,0,0,0,0,1],
                [1,1,2,1,0,0,0,1],
                [1,1,2,2,0,0,0,1],
                [1,1,2,3,0,0,0,1],
                [1,1,2,4,0,0,0,1],
                [1,1,2,5,0,0,0,1],
                [1,1,3,0,0,0,0,1],
                [1,1,3,1,0,0,0,1],
                [1,1,3,2,0,0,0,1],
                [1,1,3,3,0,0,0,1],
                [1,1,3,4,0,0,0,1],
                [1,1,3,5,0,0,0,1],
                [1,1,4,0,0,0,0,1],
                [1,1,4,1,0,0,0,1],
                [1,1,4,2,0,0,0,1],
                [1,1,4,3,0,0,0,1],
                [1,1,4,4,0,0,0,1],
                [1,1,4,5,0,0,0,1],
                [1,1,5,0,0,0,0,1],
                [1,1,5,1,0,0,0,1],
                [1,1,5,2,0,0,0,1],
                [1,1,5,3,0,0,0,1],
                [1,1,5,4,0,0,0,1],
                [1,1,5,5,0,0,0,1],
                ])

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
   

Size_data = Data.shape

save_model = 0
Number_of_test_for_model = 20

Results_r_s = np.zeros((Size_data[0],Number_of_test_for_model))
Results_r_t = np.zeros((Size_data[0],Number_of_test_for_model))
Results_r_1 = np.zeros((Size_data[0],Number_of_test_for_model))
Results_r_2 = np.zeros((Size_data[0],Number_of_test_for_model))
Results_r_3 = np.zeros((Size_data[0],Number_of_test_for_model))
Results_RMSE = np.zeros((Size_data[0],Number_of_test_for_model))
Results_MAE_s = np.zeros((Size_data[0],Number_of_test_for_model))
Results_MAE_t = np.zeros((Size_data[0],Number_of_test_for_model))
Results_MAE_1 = np.zeros((Size_data[0],Number_of_test_for_model))
Results_MAE_2 = np.zeros((Size_data[0],Number_of_test_for_model))
Results_MAE_3 = np.zeros((Size_data[0],Number_of_test_for_model))

Initial_time = time.perf_counter()

for i in range(Size_data[0]):
    
    print('\n---------- Iteração - %2d ----------\n'% (i))

    for j in range(Number_of_test_for_model):
        
        print('\nModelo - %2d'% (j))
        
        data_in_use= []
        data_in_use = Data[i,:]

        input_var, output_var, time_plot, input_var_sec, output_var_sec = generate_data( 0, data_in_use)
        data_index = [int(train_percentage*len(time_plot)),int((train_percentage+validation_perentagem)*len(time_plot))]

        hidden_layers_info=[0,0]
    
        input_size = input_var.shape[1]
    
        hidden_layers_info[0] = [ input_size ,'relu']
        hidden_layers_info[1] = [10,'relu']
        
        test_parameters = [600,100]
        
        name_model = '_'
        
        show_progress = 0

        r, RMSE, MAE = build_MLP_main(input_var, output_var, time_plot, data_index, hidden_layers_info, opt, test_parameters, name_model, data_in_use , show_progress )
        
        Results_r_s[i,j] = r[0]
        Results_MAE_s[i,j] = MAE[0]
        
        if data_in_use[4] == 0:
            
            Results_r_t[i,j] = r[0]
            Results_MAE_t[i,j] = MAE[0]
        
        else:

            Results_r_1[i,j] = r[0]
            Results_MAE_1[i,j] = MAE[0]
            Results_r_2[i,j] = r[1]
            Results_MAE_2[i,j] = MAE[1]
            Results_r_3[i,j] = r[2]
            Results_MAE_3[i,j] = MAE[2]

        
        Results_RMSE[i,j] = RMSE        
        
    time_passed = time.perf_counter() - Initial_time 
    Inter = ( time_passed )/60
    Inter_s = ( Inter - int(Inter) ) * 60
    
    print('\nTime elapsed: %3d mim :: %2d s'% (Inter,Inter_s))
    
    time_pre = time_passed * ( (Size_data[0]/(i+1)) - 1 ) / 60
    time_pre_s = ( time_pre - int(time_pre) ) * 60
    
    print('\nPredicted time left: %3d mim :: %2d s'% (time_pre, time_pre_s))
    
Final_time = time.perf_counter()

time_taken = Final_time - Initial_time

print('\nTime in seconds to run: %3f'% (time_taken))

pr.dump( [ Data, Results_r_s, Results_r_t, Results_r_1, Results_r_2, Results_r_3, Results_MAE_s, Results_MAE_t, Results_MAE_1, Results_MAE_2, Results_MAE_3, Results_RMSE , time_taken ] , open('Feature_selection_days_of_delay.p','wb'))


