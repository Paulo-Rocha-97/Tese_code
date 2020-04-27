# attemp using keras

import pickle as pr 
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

# %% Function To Normalize data 

def Normalize_data(Var_1,Max_value,Min_value):
    
    A = 1 / ( Min_value + Max_value ) 
    
    B = - Min_value / ( Min_value + Max_value )
        
    for i in range(len(Var_1)):
            
        Var_1[i] = Var_1[i]*A + B
        
    return  Var_1

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

Output = Normalize_data(Output,300,0)

Output = Output.reshape(len(Output),1)

test_data_index= 1093

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
N_neurons_1  = 40
Activation_1 = keras.layers.LeakyReLU(alpha=0.1)
weigth_ini_1 = keras.initializers.Constant(0.0)
Bias_ini_1 = keras.initializers.Constant(1.0)
Drop_out_1 = 0.0

# 2nd layer
N_neurons_2  =  20
Activation_2 = keras.layers.LeakyReLU(alpha=0.1)
weigth_ini_2 = keras.initializers.Constant(0.0)
Bias_ini_2 = keras.initializers.Constant(1.0)
Drop_out_2 = 0.0

#%% Optimizer parameters

Learning_rate = 0.0001
Momentum = 0.1
opt = keras.optimizers.SGD(learning_rate = Learning_rate, momentum = Momentum)

# %% Model Train and evaluate

# Create model
model = keras.models.Sequential([
  layers.Dense( N_neurons_1, activation=Activation_1, kernel_initializer=weigth_ini_1, bias_initializer=Bias_ini_1 , input_shape=(size_input,)),
  layers.Dense( N_neurons_2, activation=Activation_2, kernel_initializer=weigth_ini_2, bias_initializer=Bias_ini_2 ),
  layers.Dense(1)
])

model.compile(optimizer=opt, loss='mse')

# Fitting
data = model.fit(Train_in, Train_out, epochs = Epochs, batch_size = Batch_size, verbose=2, use_multiprocessing=True)

print('\n Fitting Done \n')

# Evaluate
error = model.evaluate(Test_in, Test_out, verbose=0)

print('MSE: %3f \nRMSE: %3f'% (error,tf.math.sqrt(error)))

Test_out_pred = model.predict(Test_in, verbose=0 )

r = calculate_correlation(Test_out_pred, Test_out)

print('R: %3f'% (r))

# %%

X =input('\n See the model structure(Y/N): \n')

if X == 'y' or X =='Y':

    model.summary()    
    
    cont = 1
    
    for layer in model.layers: 
        
        print('\n--Layer %3f--\n'%(cont))
        
        a = layer.get_weights()
        
        b=a[0]
        
        print(b)

        cont += 1