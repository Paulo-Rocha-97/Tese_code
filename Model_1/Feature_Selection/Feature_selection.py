
import time
from tensorflow import keras
from NN_build import build_MLP
import numpy as np
import pickle as pr
from Data_Prep_Model_1 import generate_data

n_days_delays = 3

# %% Set optmizer

Learning_rate = 0.0001
Momentum = 0.2
opt = keras.optimizers.RMSprop(learning_rate = Learning_rate, momentum = Momentum)

train_percentage = 0.70
validation_perentagem = 0.10
  
Data,_,_,_,_= pr.load(open('Results/Feature_selection_all.p','rb'))

Size_data = Data.shape

save_model = 0
Number_of_test_for_model = 60

Results_r = np.zeros((Size_data[0],Number_of_test_for_model))
Results_RMSE = np.zeros((Size_data[0],Number_of_test_for_model))
Results_MAE = np.zeros((Size_data[0],Number_of_test_for_model))

Initial_time = time.perf_counter()

for i in range(Size_data[0]):
    
    print('\n---------- Iteração - %2d ----------\n'% (i))

    for j in range(Number_of_test_for_model):
        
        print('Modelo - %2d'% (j))

        data_in_use = []
        data_in_use = Data[i,:]

        input_var, output_var, time_plot = generate_data(n_days_delays, 0, data_in_use)
        data_index=[int(train_percentage*len(time_plot)),int((train_percentage+validation_perentagem)*len(time_plot))]

        input_size = input_var.shape[1]

        hidden_layer_info=[0,0]

        hidden_layer_info[0] = [ input_size , 'relu' ]
        hidden_layer_info[1] = [ 15 , 'relu' ]

        test_parameters = [500,50]

        name_model = '_'
        
        r, RMSE, MAE = build_MLP(input_var, output_var, time_plot, data_index, hidden_layer_info, opt, test_parameters, name_model, save_model)
        
        Results_r[i,j] = r
        Results_RMSE[i,j] = RMSE        
        Results_MAE[i,j] = MAE
        
    Inter = ( time.perf_counter() - Initial_time )/60
    Inter_s = ( Inter - int(Inter) ) * 60
    
    print('\nTime elapsed: %3d mim :: %2d s'% (Inter,Inter_s))
    
Final_time = time.perf_counter()

time_taken = Final_time - Initial_time

print('\nTime inm seconds to run: %3f'% (time_taken))

pr.dump( [ Data, Results_r, Results_MAE, Results_RMSE , time_taken ] , open('Feature_selection.p','wb'))


