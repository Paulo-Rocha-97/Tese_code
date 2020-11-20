
import time
from tensorflow import keras
from NN_build import build_MLP
import numpy as np
import pickle as pr
from Data_Prep_Model_1 import generate_data


# %% Set optmizer

Learning_rate = 0.0005
Momentum = 0.2
opt = keras.optimizers.RMSprop(learning_rate = Learning_rate, momentum = Momentum)

train_percentage = 0.70
validation_perentagem = 0.10
  
Data=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

Size_data = 10

save_model = 0
Number_of_test_for_model = 10

Results_r = np.zeros((Size_data,Number_of_test_for_model))
Results_RMSE = np.zeros((Size_data,Number_of_test_for_model))
Results_MAE = np.zeros((Size_data,Number_of_test_for_model))

Initial_time = time.perf_counter()

for i in range(10):
    
    print('\n---------- Iteração - %2d ----------\n'% (i))

    for j in range(Number_of_test_for_model):
        
        print('Modelo - %2d'% (j))


        input_var, output_var, time_plot = generate_data(i+1, 0, Data)
        data_index=[int(train_percentage*len(time_plot)),int((train_percentage+validation_perentagem)*len(time_plot))]

        input_size = input_var.shape[1]

        hidden_layer_info=[0,0]

        hidden_layer_info[0] = [ 40 , 'relu' ]
        hidden_layer_info[1] = [ 20 , 'relu' ]

        test_parameters = [350,50]

        name_model = '_'
        
        r, RMSE, MAE = build_MLP(input_var, output_var, time_plot, data_index, hidden_layer_info, opt, test_parameters, name_model, save_model)
        
        Results_r[i,j] = r
        Results_RMSE[i,j] = RMSE        
        Results_MAE[i,j] = MAE
        
    time_passed = time.perf_counter() - Initial_time 
    Inter = ( time_passed )/60
    Inter_s = ( Inter - int(Inter) ) * 60
    
    print('\nTime elapsed: %3d mim :: %2d s'% (Inter,Inter_s))
    
    time_pre = time_passed * ( (Size_data/(i+1)) - 1 ) / 60
    time_pre_s = ( time_pre - int(time_pre) ) * 60
    
    print('\nPredicted time left: %3d mim :: %2d s'% (time_pre, time_pre_s))
    
Final_time = time.perf_counter()

time_taken = Final_time - Initial_time

print('\nTime in seconds to run: %3f'% (time_taken))

pr.dump( [ Data, Results_r, Results_MAE, Results_RMSE , time_taken ] , open('Feature_selection_delays.p','wb'))


