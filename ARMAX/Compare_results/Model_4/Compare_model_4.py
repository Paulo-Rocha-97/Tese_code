import csv
import numpy as np
import sklearn.metrics
import math
from My_plot_ import make_plot_line as make_plot
from Create_time_series import create_time 
from Data_Prep_Model_4 import generate_data
from tensorflow.keras.models import load_model

# This function serves to compare and plot results between models type

len_armax = 499

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

# %% Load model NN 

MLP_1 = load_model('model4_RMSprop_best.h5')
MLP_2 = load_model('model4_SGD_best.h5')

# %% Load data

train_percentage = 0.70
validation_perentagem = 0.1

Data = [1,1,2,1,0,0,0,1]

input_var, output_var, time_plot, _, _ = generate_data( 0, Data)
data_index=[int(train_percentage*len(time_plot)),int((train_percentage+validation_perentagem)*len(time_plot))]

Test_in = input_var[data_index[1]+1:,:]
Test_out = output_var[data_index[1]+1:,:]

time_scale = time_plot[data_index[1]+1:]

time_scale = np.transpose(time_scale)

Y_pred_RMSprop = MLP_1.predict(Test_in)
Y_pred_SGD = MLP_2.predict(Test_in) 

Test_out[:,0] = Denormalize_data(Test_out[:,0], 230, 0)
Y_pred_RMSprop[:,0] = Denormalize_data(Y_pred_RMSprop[:,0], 230, 0) 
Y_pred_SGD[:,0] = Denormalize_data(Y_pred_SGD[:,0], 230, 0) 

Test_out = list(Test_out)

for i in range(len(Test_out)):
    
    Test_out[i] = float(Test_out[i])

#%% Load ARMAX resutls 

csv_file = open('Armax_data_model_4.csv')
ARMAX_data_reader = csv.reader(csv_file, delimiter=',')

ARMAX_data = np.empty([len_armax,2])
cont=0
for row in ARMAX_data_reader:
    if row[0] == 'Nan':
        ARMAX_data[cont,0]=None
    else:
        ARMAX_data[cont,0]=row[0]
    ARMAX_data[cont,1]=row[1]
    cont=cont+1

Y_pred_ARMAX = []

for i in range(len(ARMAX_data)):
        
    Y_pred_ARMAX.append(ARMAX_data[i,1])
    
#%% Cut ARMAX resutls
    
time_armax = create_time(2014)
    
time_armax = time_armax[-len_armax:]

time_armax = np.transpose(time_armax)

Y_armax = []
Y_RMSprop = []
Y_SGD = []

for i in range(len(time_armax)):
    
    for j in range(len(time_scale)):
        
        if time_scale[j] == time_armax[i]:
            
            Y_armax.append(float(Y_pred_ARMAX[i]))
            Y_RMSprop.append(float(Y_pred_RMSprop[j]))
            Y_SGD.append(float(Y_pred_SGD[j]))

#%% make plot

path = 'C:\\Users\\Paulo_Rocha\\Desktop\\Tese\\Tese_code\\ARMAX\\Compare_results\\Model_4\\Plot'

make_plot(path, 'Compare_model_4',time_scale,'Date', 'Inflow ($m^3/s$)',Test_out,'Real Data',Y_RMSprop,'MLP - RMSprop',Y_SGD,'MLP - Mini batch GD')

#%% Caclulate metrics

def Calculate_metrics(real_data,tested_data):

    mse = sklearn.metrics.mean_squared_error(real_data, tested_data)
    RMSE = math.sqrt(mse)

    MAE = sklearn.metrics.mean_absolute_error(real_data, tested_data)
    
    Mean_1, St_dev_1 = MEAN_STDEV(real_data)
    Mean_2, St_dev_2 = MEAN_STDEV(tested_data)
    
    Cov = np.cov(real_data,tested_data)
        
    r = Cov[0][1] /  (St_dev_1 * St_dev_2)
        
    return r,RMSE,MAE

# %% Execute and print value
    
r_a,RMSE_a,MAE_a = Calculate_metrics(Test_out, Y_armax)
r_s,RMSE_s,MAE_s = Calculate_metrics(Test_out, Y_SGD)
r_r,RMSE_r,MAE_r = Calculate_metrics(Test_out, Y_RMSprop)

f = open('Results.txt','w')
f.write('--------- Data Results ---------\n')
f.write('ARMAX Model\nr - {:4f}\nRMSE - {:4f}\nMAE - {:4f}\n'.format(r_a,RMSE_a,MAE_a))
f.write('RMSprop Model\nr - {:4f}\nRMSE - {:4f}\nMAE - {:4f}\n'.format(r_s,RMSE_s,MAE_s))
f.write('SGD Model\nr - {:4f}\nRMSE - {:4f}\nMAE - {:4f}\n'.format(r_r,RMSE_r,MAE_r))
f.close()
