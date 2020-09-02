
import time
from tensorflow import keras
from NN_build import build_MLP
# from NN_build import build_LSTM
import numpy as np
import pickle as pr
from Data_Prep_Model_2 import generate_data

# set optimizer settings

Learning_rate = 0.00005
Momentum = 0.2
opt = keras.optimizers.RMSprop(learning_rate = Learning_rate, momentum = Momentum)

train_percentage = 0.60
validation_perentagem = 0.10

# Set diferent test data

Data= np.array([[0,2,2,2,1],
                [1,0,2,2,1],
                [1,2,0,2,1],
                [1,2,2,0,1],
                [1,2,1,1,1],
                [1,2,2,1,1],
                [1,2,3,1,1],
                [1,2,4,1,1],
                [1,2,5,1,1],
                [1,2,6,1,1],
                [1,2,1,2,1],
                [1,2,1,3,1],
                [1,2,1,4,1],
                [1,2,1,5,1],
                [1,2,1,6,1],
                ])

# data_type = [ day index, type of storage, number of days in the past, 
#               number of days in the future, outflow type]
    
# day index: 1 - acconut; 0 - disregard
# type of storage: 0 - none  1 - depth; 2 - volume 
# Number of days past: from 0 to infinity
# Number of days in the future: from 0 to infinity
# outflow type: 0 - unique; 1 - Seperate

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

        input_var, output_var, time_plot = generate_data( 0, data_in_use)
        data_index=[int(train_percentage*len(time_plot)),int((train_percentage+validation_perentagem)*len(time_plot))]

        hidden_layer_info=[0,0]
    
        hidden_layer_info[0] = [10,'relu']
        hidden_layer_info[1] = [10,'relu']
        
        test_parameters = [300,50]
        
        name_model = '_'

        r, RMSE, MAE = build_MLP(input_var, output_var, time_plot, data_index, hidden_layer_info, opt, test_parameters, name_model, save_model, Data)
        
        Results_r_s[i,j] = r[0]
        Results_MAE_s[i,j] = MAE[0]
        
        if data_in_use[4] == 0:
            
            Results_r_t[i,j] = r[1]
            Results_MAE_t[i,j] = MAE[1]
        
        else:

            Results_r_1[i,j] = r[1]
            Results_MAE_1[i,j] = MAE[1]
            Results_r_2[i,j] = r[2]
            Results_MAE_2[i,j] = MAE[2]
            Results_r_3[i,j] = r[3]
            Results_MAE_3[i,j] = MAE[3]

        
        Results_RMSE[i,j] = RMSE        
        
    Inter = ( time.perf_counter() - Initial_time )/60
    Inter_s = ( Inter - int(Inter) ) * 60
    
    print('\nTime elapsed: %3d mim :: %2d s'% (Inter,Inter_s))
    
Final_time = time.perf_counter()

time_taken = Final_time - Initial_time

print('\nTime inm seconds to run: %3f'% (time_taken))

pr.dump( [ Data, Results_r_s, Results_r_t, Results_r_1, Results_r_2, Results_r_3, Results_MAE_s, Results_MAE_t, Results_MAE_1, Results_MAE_2, Results_MAE_3, Results_RMSE , time_taken ] , open('Feature_selection_Volume.p','wb'))


