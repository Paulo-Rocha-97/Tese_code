import os
import math
import numpy as np
import sklearn.metrics
from Data_Prep_Model_1 import generate_data as generate_data_1
from Data_Prep_Model_2 import generate_data as generate_data_2
from Data_Prep_Model_3 import generate_data as generate_data_3
from Data_Prep_Model_4 import generate_data as generate_data_4
from tensorflow.keras.models import load_model

path = os.getcwd()

# Full model integration 

# %% Load full data 
Data_1 = [1,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1]
Data_2 = [2,1,2,1,0,2,2,1]
Data_3 = [2,2,1,1,0,1,2,1]
Data_4 = [1,1,2,1,0,0,0,1]
Data_sec = [0,2,1,1,0,0,0,1]
Data_sec2 = [0,2,2,1,0,0,0,1]

# Model 1 Data
In_1, Out_1,Time_plot_1 = generate_data_1(3,0,Data_1)
# Model 2 Data
In_2, Out_2,Time_plot_2,_,_ = generate_data_2(0,Data_2)
_,_,_,In_sec_2,Out_sec_2 = generate_data_2(0,Data_sec2)
# Model 3 Data
In_3, Out_3,Time_plot_3,_,_ = generate_data_3(0,Data_3)
_,_,_,In_sec_3,Out_sec_3 = generate_data_3(0,Data_sec)
# Model 4 Data
In_4, Out_4,Time_plot_4,_,_ = generate_data_4(0,Data_4)
_,_,_,In_sec_4,Out_sec_4 = generate_data_4(0,Data_sec2)

def test_data(In,Out,time_plot,In_2,Out_2):
    
    train_percentage = 0.7
    validation_perentagem = 0.1
    
    data_index=[int(train_percentage*len(In)),int((train_percentage+validation_perentagem)*len(In))]
    
    Test_in = In[data_index[1]+1:,:]
    Test_out = Out[data_index[1]+1:,:]

    time_scale = time_plot[data_index[1]+1:]

    time_scale = np.transpose(time_scale)
    
    Test_in_sec = In_2[data_index[1]+1:,:]
    Test_out_sec = Out_2[data_index[1]+1:,:]
    
    return Test_in, Test_out, time_scale, Test_in_sec, Test_out_sec
                
def test_data1(In,Out,time_plot):
    
    train_percentage = 0.7
    validation_perentagem = 0.1
    
    data_index=[int(train_percentage*len(In)),int((train_percentage+validation_perentagem)*len(In))]
    
    Test_in = In[data_index[1]+1:,:]
    Test_out = Out[data_index[1]+1:,:]

    time_scale = time_plot[data_index[1]+1:]

    time_scale = np.transpose(time_scale)
    
    return Test_in, Test_out, time_scale

Test_in_1,Test_out_1,Time_1 = test_data1(In_1, Out_1, Time_plot_1)
Test_in_2,Test_out_2,Time_2,Test_in_sec_2,Test_out_sec_2 = test_data(In_2, Out_2, Time_plot_2,In_sec_2,Out_sec_2)
Test_in_3,Test_out_3,Time_3,Test_in_sec_3,Test_out_sec_3 = test_data(In_3, Out_3, Time_plot_3,In_sec_3,Out_sec_3)
Test_in_4,Test_out_4,Time_4,Test_in_sec_4,Test_out_sec_4 = test_data(In_4, Out_4, Time_plot_4,In_sec_4,Out_sec_4)


# %% Load Models

MLP_1 = load_model('model_1.h5')
MLP_2 = load_model('model_2.h5')
MLP_2_sec = load_model('model_2_sec.h5')
MLP_3 = load_model('model_3.h5')
MLP_3_sec = load_model('model_3_sec.h5')
MLP_4 = load_model('model_4.h5')
MLP_4_sec = load_model('model_4_sec.h5')

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

# %% Denormalize data

def Denormalize_data( Var, Max_value, Min_value ):
    
    A = 1 / ( - Min_value + Max_value ) 
    
    B = - Min_value / ( - Min_value + Max_value )
        
    for i in range(len(Var)):
            
        Var[i] = (Var[i] - B) / A
            
    return Var

# %% Calculate performance metrics

def Calculate_metrics(real_data,tested_data):
    
    real_data=list(real_data.reshape(330,1))
    tested_data=list(tested_data.reshape(330,1))

    mse = sklearn.metrics.mean_squared_error(real_data, tested_data)
    RMSE = math.sqrt(mse)

    MAE = sklearn.metrics.mean_absolute_error(real_data, tested_data)
    
    Mean_1, St_dev_1 = MEAN_STDEV(real_data)
    Mean_2, St_dev_2 = MEAN_STDEV(tested_data)
    
    Cov = np.cov(real_data,tested_data)
        
    r = Cov[0][1] /  (St_dev_1 * St_dev_2)
        
    Sum_1=0
    Sum_2=0
    
    for i in range(len(real_data)):
        
        Sum_1 = Sum_1 + (tested_data[i]-real_data[i])*(tested_data[i]-real_data[i])
        Sum_2 = Sum_2 + (real_data[i]-Mean_1)*(real_data[i]-Mean_1)
    
    NS = 1 - (Sum_1/Sum_2)
    
    r=float(r)
    NS=float(r)
    
    return r,RMSE,MAE,NS

# %% Execute simulation 
    
Y_1=np.zeros(330)
Y_2=np.zeros(330)
Y_sec_2=np.zeros(330)
Y_3=np.zeros(330)
Y_sec_3=np.zeros(330)
Y_4=np.zeros(330)
Y_sec_4=np.zeros(330)

for i in range(330):
    
    print(i)
    
    if i == 0:

        Var_1 =Test_in_1[i,:].reshape(1,50)
        Y_1[i]=MLP_1.predict(Var_1)

        Var_2 = Test_in_2[i,:].reshape(1,8)
        Var_2[0,4] = Y_1[i]
        Y_2[i]=MLP_2.predict(Var_2)
        
        Var_3 = Test_in_3[i,:].reshape(1,7)
        Var_3[0,3] = Y_2[i]
        Y_3[i]=MLP_3.predict(Var_3)
        
        Var_4 = Test_in_4[i,:].reshape(1,7)
        Var_4[0,4] = Y_3[i]
        Y_4[i]=MLP_4.predict(Var_3)
        
    elif i == 1:
        
        Var_1 =Test_in_1[i,:].reshape(1,50)
        Var_1[0,-1] = Y_1[i-1]
        Y_1[i]=MLP_1.predict(Var_1)

        Var_2 = Test_in_2[i,:].reshape(1,8)
        Var_2[0,-1] = Y_2[i-1]
        Var_2[0,4] = Y_1[i]
        Var_2[0,3] = Y_1[i-1]
        Y_2[i]=MLP_2.predict(Var_2)

        Var_3 = Test_in_3[i,:].reshape(1,7)
        Var_3[0,-1] = Y_3[i-1]
        Var_3[0,3] = Y_2[i]
        Var_3[0,2] = Y_2[i-1]
        Y_3[i]=MLP_3.predict(Var_3)
        
        Var_4 = Test_in_4[i,:].reshape(1,7)
        Var_4[0,-1] = Y_4[i-1]
        Var_4[0,4] = Y_3[i]
        Var_4[0,3] = Y_3[i-1]
        Y_4[i]=MLP_4.predict(Var_3)
        
    else:
        
        Var_1 =Test_in_1[i,:].reshape(1,50)
        Var_1[0,-1] = Y_1[i-1]
        Y_1[i]=MLP_1.predict(Var_1)

        Var_2 = Test_in_2[i,:].reshape(1,8)
        Var_2[0,-1] = Y_2[i-1]
        Var_2[0,4] = Y_1[i]
        Var_2[0,3] = Y_1[i-1]
        Var_2[0,2] = Y_1[i-2]
        Y_2[i]=MLP_2.predict(Var_2)

        Var_3 = Test_in_3[i,:].reshape(1,7)
        Var_3[0,-1] = Y_3[i-1]
        Var_3[0,3] = Y_2[i]
        Var_3[0,2] = Y_2[i-1]
        Y_3[i]=MLP_3.predict(Var_3)
        
        Var_4 = Test_in_4[i,:].reshape(1,7)
        Var_4[0,-1] = Y_4[i-1]
        Var_4[0,4] = Y_3[i]
        Var_4[0,3] = Y_3[i-1]
        Var_4[0,2] = Y_3[i-2]
        Y_4[i]=MLP_4.predict(Var_3)
        

# %% Calculate metrics
        
r_1,RMSE_1,MAE_1,NS_1 = Calculate_metrics(Test_out_1, Y_1.reshape(330,1))
r_2,RMSE_2,MAE_2,NS_2 = Calculate_metrics(Test_out_2, Y_2.reshape(330,1))
r_3,RMSE_3,MAE_3,NS_3 = Calculate_metrics(Test_out_3, Y_3.reshape(330,1))
r_4,RMSE_4,MAE_4,NS_4 = Calculate_metrics(Test_out_4, Y_4.reshape(330,1))

f = open('Results.txt','w')
f.write('--------- Data Results ---------\n')
f.write('Model 1 \nr - {:4f}\nRMSE - {:4f}\nMAE - {:4f}\nNS - {:4f}\n'.format(r_1,RMSE_1,MAE_1,NS_1))
f.write('Model 2 \nr - {:4f}\nRMSE - {:4f}\nMAE - {:4f}\nNS - {:4f}\n'.format(r_2,RMSE_2,MAE_2,NS_2))
f.write('Model 3 \nr - {:4f}\nRMSE - {:4f}\nMAE - {:4f}\nNS - {:4f}\n'.format(r_3,RMSE_3,MAE_3,NS_3))
f.write('Model 4 \nr - {:4f}\nRMSE - {:4f}\nMAE - {:4f}\nNS - {:4f}\n'.format(r_4,RMSE_4,MAE_4,NS_4))
f.close()
