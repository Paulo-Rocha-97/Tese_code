import numpy as np
import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
from tensorflow.keras import layers


# %% Function to calculate mean and st dev

def MEAN_STDEV( Y_values ):
    
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

def calculate_correlation( Var1, Var2 ):
    
    Var_1 = np.ndarray.tolist(Var1)
    Var_2 = np.ndarray.tolist(Var2)
    
    Mean_1, St_dev_1 = MEAN_STDEV(Var_1)
    Mean_2, St_dev_2 = MEAN_STDEV(Var_2)
    
    Cov = np.cov(Var_1,Var_2)
        
    r = Cov[0][1] /  (St_dev_1 * St_dev_2)
    
    return r  
 
# %% Function to denormalize data 

def Denormalize_data( Var, Max_value, Min_value ):
    
    A = 1 / ( - Min_value + Max_value ) 
    
    B = - Min_value / ( - Min_value + Max_value )
        
    for i in range(len(Var)):
            
        Var[i] = (Var[i] - B) / A
            
    return Var

# %% Build MLP main
    
# Data_index (list) --> [ index(row) for data to test, index(row) for data to validate]

# Hidden_layers_info (list of list) --> as many fields as hidden layers each containing a list with:
#                               [Number of neurons, activation function]  - subject to adding more

# opt --> keras optmizer object
    
# test parameters (list) -->  [Epochs, Batch size]

    
def build_MLP_main(input_var, output_var, time_plot, data_index, hidden_layers_info, opt, test_parameters, name_model, data_type, show_progress ):


    input_shape = input_var.shape
    output_shape = output_var.shape
    
    if output_shape[1]==1:
        output_var = output_var.reshape(len(output_var),1)
    
    
    # Train_in = input_var[467:,:]
    # Train_out = output_var[467:,:]
    
    # Val_in = input_var[366:466,:]
    # Val_out = output_var[366:466,:]
    
    # Test_in = input_var[:365,:]
    # Test_out = output_var[:365,:]
    
    # time_scale = time_plot[:365]
    
    
    Train_in = input_var[:data_index[0],:]
    Train_out = output_var[:data_index[0],:]
    
    Val_in = input_var[data_index[0]+1:data_index[1],:]
    Val_out = output_var[data_index[0]+1:data_index[1],:]
    
    Test_in = input_var[data_index[1]+1:,:]
    Test_out = output_var[data_index[1]+1:,:]
    
    time_scale = time_plot[data_index[1]+1:]
    
    time_scale = np.transpose(time_scale)
    
    # Model Train and evaluate
    
    # Create model
    model = keras.models.Sequential()
    
    for i in range(len(hidden_layers_info)):
        if i==0:
            model.add(layers.Dense( hidden_layers_info[i][0], activation=hidden_layers_info[i][1], input_shape=(input_shape[1],)))
        else:
            model.add(layers.Dense( hidden_layers_info[i][0], activation=hidden_layers_info[i][1]))
    
    model.add(layers.Dense( output_shape[1], activation='relu' ))

    model.compile(optimizer=opt, loss='mse')

    # Fitting
    
    if data_index[1]==data_index[0]:
        history = model.fit(Train_in, Train_out, epochs = test_parameters[0], 
                         batch_size = test_parameters[1], verbose=show_progress, use_multiprocessing=True)
    else:
        history = model.fit(Train_in, Train_out, epochs = test_parameters[0], batch_size = test_parameters[1],
                         validation_data = (Val_in, Val_out), verbose=show_progress, use_multiprocessing=True)
            
    # Evaluate
    error = model.evaluate(Test_in, Test_out, verbose=0)
    RMSE = tf.math.sqrt(error)

    print('\nMSE: %2f \nRMSE: %2f'% (error,RMSE))
    
    Test_out_pred = model.predict(Test_in, verbose=0)

    r = []
    MAE = []
    
    r_ = calculate_correlation(Test_out_pred[:,0], Test_out[:,0])
    r.append(r_)
    MAE_ = np.mean(abs(Test_out[:,0] - Test_out_pred[:,0]))
    MAE.append(MAE_)
    
    print('r: %2f'% (r[0]))
    
    if output_shape[1] != 1:
        
        r_ = calculate_correlation(Test_out_pred[:,1], Test_out[:,1])
        r.append(r_)
        MAE_ = np.mean(abs(Test_out[:,1] - Test_out_pred[:,1]))
        MAE.append(MAE_)
        
        r_ = calculate_correlation(Test_out_pred[:,2], Test_out[:,2])
        r.append(r_)
        MAE_ = np.mean(abs(Test_out[:,2] - Test_out_pred[:,2]))
        MAE.append(MAE_)
          
    return r, RMSE, MAE

# %% Build MLP sec
    
# Data_index (list) --> [ index(row) for data to test, index(row) for data to validate]

# Hidden_layers_info (list of list) --> as many fields as hidden layers each containing a list with:
#                               [Number of neurons, activation function]  - subject to adding more

# opt --> keras optmizer object
    
# test parameters (list) -->  [Epochs, Batch size]

def build_MLP_sec(input_var, output_var, time_plot, data_index, hidden_layers_info, opt, test_parameters, name_model, data_type, show_progress ):


    input_shape = input_var.shape
    output_shape = output_var.shape
    
    if output_shape[1]==1:
        output_var = output_var.reshape(len(output_var),1)
    
    Train_in = input_var[:data_index[0],:]
    Train_out = output_var[:data_index[0],:]
    
    Val_in = input_var[data_index[0]+1:data_index[1],:]
    Val_out = output_var[data_index[0]+1:data_index[1],:]
    
    Test_in = input_var[data_index[1]+1:,:]
    Test_out = output_var[data_index[1]+1:,:]
    
    time_scale = time_plot[data_index[1]+1:]
    
    time_scale = np.transpose(time_scale)
    
    # Model Train and evaluate
    
    # Create model
    model = keras.models.Sequential()
    
    for i in range(len(hidden_layers_info)):
        if i==0:
            model.add(layers.Dense( hidden_layers_info[i][0], activation=hidden_layers_info[i][1], input_shape=(input_shape[1],)))
        else:
            model.add(layers.Dense( hidden_layers_info[i][0], activation=hidden_layers_info[i][1]))
    
    model.add(layers.Dense( output_shape[1], activation='relu' ))

    model.compile(optimizer=opt, loss='mean_squared_error')

    # Fitting
    
    if data_index[1]==data_index[0]:
        history = model.fit(Train_in, Train_out, epochs = test_parameters[0], 
                         batch_size = test_parameters[1], verbose=show_progress, use_multiprocessing=True)
    else:
        history = model.fit(Train_in, Train_out, epochs = test_parameters[0], batch_size = test_parameters[1],
                         validation_data = (Val_in, Val_out), verbose=show_progress, use_multiprocessing=True)
            
    # Evaluate
    error = model.evaluate(Test_in, Test_out, verbose=0)
    RMSE = tf.math.sqrt(error)

    Test_out_pred = model.predict(Test_in, verbose=0)
        
    r = calculate_correlation(Test_out_pred[:,0], Test_out[:,0])
    
    MAE = np.mean(abs(Test_out - Test_out_pred))

        
    return r, RMSE, MAE
    
# %% Build LSTM
    
# Data_index (list) --> [ index(row) for data to test, index(row) for data to validate]

# Hidden_layers_info (list of list) --> as many fields as hidden layers each containing a list with:
#                               [Number of neurons]  - subject to adding more

# opt --> keras optmizer object
    
# test parameters (list) -->  [Epochs, Batch size]

def build_LSTM(input_var, output_var, time_plot, data_index, hidden_layer_info, opt, test_parameters, name_model):
    
    output_shape = output_var.shape
    
    if output_shape[1]==1:
        output_var = output_var.reshape(len(output_var),1)
    
    Train_in = input_var[:data_index[0],:]
    Train_out = output_var[:data_index[0],:]
    
    Val_in = input_var[data_index[0]+1:data_index[1],:]
    Val_out = output_var[data_index[0]+1:data_index[1],:]
    
    Test_in = input_var[data_index[1]+1:,:]
    Test_out = output_var[data_index[1]+1:,:]
    
    time_scale = time_plot[data_index[1]+1:]
    
    Train_in = Train_in.reshape( (Train_in.shape[0], 1, Train_in .shape[1]) )
    Val_in = Val_in.reshape( (Val_in.shape[0], 1, Val_in .shape[1]) )
    Test_in = Test_in.reshape((Test_in.shape[0], 1, Test_in.shape[1]))
    
    # Model Train and evaluate
    
    # Create model
    model = keras.models.Sequential()
    
    model.add(layers.LSTM(hidden_layer_info[0], input_shape=[Train_in.shape[1], Train_in.shape[2]] ))
 
    model.add(layers.Dense( output_shape[1], activation='relu' ))

    model.compile(optimizer=opt, loss='mse')

    # Fitting
    
    if data_index[1]==data_index[0]:
        history = model.fit(Train_in, Train_out, epochs = test_parameters[0], 
                         batch_size = test_parameters[1], verbose=2, use_multiprocessing=True)
    else:
        history = model.fit(Train_in, Train_out, epochs = test_parameters[0], batch_size = test_parameters[1],
                         validation_data = (Val_in, Val_out), verbose=2, use_multiprocessing=True)
            
    # Evaluate
    error = model.evaluate(Test_in, Test_out, verbose=0)
    RMSE = tf.math.sqrt(error)
    
    Test_out_pred = model.predict(Test_in, verbose=0)

    r = []
    MAE = []
    
    r_ = calculate_correlation(Test_out_pred[:,0], Test_out[:,0])
    r.append(r_)
    MAE_ = np.mean(abs(Test_out[:,0] - Test_out_pred[:,0]))
    MAE.append(MAE_)
    
    if output_shape[1] != 1:
     
        r_ = calculate_correlation(Test_out_pred[:,1], Test_out[:,1])
        r.append(r_)
        MAE_ = np.mean(abs(Test_out[:,1] - Test_out_pred[:,1]))
        MAE.append(MAE_)
        
        r_ = calculate_correlation(Test_out_pred[:,2], Test_out[:,2])
        r.append(r_)
        MAE_ = np.mean(abs(Test_out[:,2] - Test_out_pred[:,2]))
        MAE.append(MAE_)
        
        
    return r, RMSE, MAE
