# attemp using keras

import numpy as np
import pickle as pr 
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from My_plot import  make_plot_line as make_plot
from Create_time_series import create_time as c_time

# %% Function To Normalize data Output 

def Normalize_data_out(Var_1,Max_value,Min_value):
    
    A = 1 / ( Min_value + Max_value ) 
    
    B = - Min_value / ( Min_value + Max_value )
        
    for i in range(len(Var_1)):
            
        Var_1[i] = Var_1[i]*A + B
        
    return  Var_1

# %% Function to Normalize data Input

def Normalize_data_in(Var, Mins, Maxs):
    
    Day_delays = 3
        
    Var_1 = np.zeros(Var.shape)
    
    for j in range(int((Var.shape[1]-1)/(Day_delays+1)+1)):
            
        A = 1 / ( Mins[j] + Maxs[j] ) 

        B = - Mins[j] / ( Mins[j]  + Maxs[j]  )
        
        for i in range(Var.shape[0]):
            
            Var_1[i,j] = Var[i,j]*A + B
            
            if j != 0:
                
                Var_1[i,j+15] = Var[i,j+15]*A + B
                Var_1[i,j+30] = Var[i,j+30]*A + B
                Var_1[i,j+45] = Var[i,j+45]*A + B
                
    return Var_1

# %% Function to calculate mean and st dev

def MEAN_STDEV(Y_values):
    
    SUM = 0
    
    for i in range (len(Y_values)):
                    
        SUM = SUM + Y_values[i]
                
        Mean = SUM / (len(Y_values))
    
    VAR = 0
    
    for i in range (len(Y_values)):
                    
        VAR = VAR + ( Y_values[i] - Mean ) * ( Y_values[i] - Mean )
    
    St_dev = np.sqrt( VAR / ( len(Y_values) - 1 ) )
    
    return Mean, St_dev

# %% Function to calculate r 

def calculate_correlation(Var1,Var2):
    
    Var1 = Var1.reshape(len(Var1),)
    Var2 = Var2.reshape(len(Var2),)
    Var_1 = np.ndarray.tolist(Var1)
    Var_2 = np.ndarray.tolist(Var2)
    
    Mean_1, St_dev_1 = MEAN_STDEV(Var_1)
    Mean_2, St_dev_2 = MEAN_STDEV(Var_2)
    
    Cov = np.cov(Var_1,Var_2)
        
    r = Cov[0][1] /  (St_dev_1 * St_dev_2)
    
    return r   

# %% Data Prep

Input, Output = pr.load(open ('Data_model_1.p','rb'))

Mins = [ 1, 0, 0, -5, -5, 0, 0, 0, 0, 40, 40, 15, 35, 920, 0, 0]
Maxs = [ 366, 30, 30, 30, 30, 70, 110, 110, 100, 100, 100, 100, 3200, 985, 350, 125]

Input = Normalize_data_in(Input, Mins, Maxs)

Output = Normalize_data_out(Output,300,0)
Output = Output.reshape(len(Output),1)


Output_del = np.copy(Output[1::])
Input = np.delete(Input, (-1), axis=0)
Output = np.delete(Output, (-1), axis=0)
Input = np.concatenate((Input,Output_del),1)

test_data_index= 1092

input_shape = Input.shape

size_input = input_shape[1]

Train_in = Input[:test_data_index,:]
Train_out = Output[:test_data_index,:]

Test_in = Input[test_data_index+1:,:]
Test_out = Output[test_data_index+1:,:]
        
# %% General Parameteres

Epochs = 300
Batch_size = 10

# 1st Layer 
N_neurons_1  = 20
Activation_1 = keras.layers.LeakyReLU(alpha=0.1)
weigth_ini_1 = keras.initializers.Constant(0.0)
Bias_ini_1 = keras.initializers.Constant(1.0)

# 2nd layer
N_neurons_2  =  6
Activation_2 = keras.layers.LeakyReLU(alpha=0.1)
weigth_ini_2 = keras.initializers.Constant(0.0)
Bias_ini_2 = keras.initializers.Constant(1.0)

# output layer 
Constraint = keras.constraints.NonNeg()

#%% Optimizer parameters

Learning_rate = 0.001
Momentum = 0.5
opt = keras.optimizers.RMSprop(learning_rate = Learning_rate, momentum = Momentum)

# %% Model Train and evaluate

# Create model
model = keras.models.Sequential([  
  layers.LSTM( N_neurons_1, activation=Activation_1, input_shape=(size_input,)),
  layers.LSTM( N_neurons_2, activation=Activation_2 ),
  layers.Dense( 1, kernel_constraint = Constraint )
])

model.compile(optimizer=opt, loss='mse')

# Fitting
data = model.fit(Train_in, Train_out, epochs = Epochs, batch_size = Batch_size, 
                 verbose=2, use_multiprocessing=True)

print('\n Fitting Done \n')

# Evaluate
error = model.evaluate(Test_in, Test_out, verbose=0)

print('MSE: %3f \nRMSE: %3f'% (error,tf.math.sqrt(error)))

Test_out_pred = model.predict(Test_in, verbose=0 )

r = calculate_correlation(Test_out_pred, Test_out)

print('R: %3f'% (r))

# %% Function to denormalize data 

def Denormalize_data( Var, Max_value, Min_value):
    
    A = 1 / ( Min_value + Max_value ) 
    
    B = - Min_value / ( Min_value + Max_value )
        
    for i in range(len(Var)):
            
        Var[i] = (Var[i] - B) / A
            
    return Var

# %% Execute 
    
Test_out = Denormalize_data(Test_out, 300, 0)
Test_out_pred = Denormalize_data(Test_out_pred, 300, 0)

# %% Save plot 
path ='C:/Users/Paulo_Rocha/Desktop/Tese/Tese_code/First_Try_Model_1'

Time = c_time()

make_plot(path, 'Model_1', Time, 'Inflow (m^3/s)', Test_out, 'Real Data', Test_out_pred, 'Estimation from NN_1')