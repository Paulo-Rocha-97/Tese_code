import os
import csv
import math
import numpy as np
import sklearn.metrics
from tqdm import tqdm
from My_plot_ import make_plot_line as make_plot
from Data_Prep_Model_1 import generate_data as generate_data_1
from Data_Prep_Model_2 import generate_data as generate_data_2
from Data_Prep_Model_3 import generate_data as generate_data_3
from Data_Prep_Model_4 import generate_data as generate_data_4
from tensorflow.keras.models import load_model
import tensorflow as tf

path = os.getcwd()

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

    Mean=float(Mean)
    St_dev=float(St_dev)
    
    
    return Mean, St_dev

# %% Load full data 
    
Eco_outflow = [15,15,11.9,9.6,8.6,7.9,5,5,5,8.9,11.9,15]

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

# %% Function To Normalize data Output 

def Normalize_data(Var_1,Max_value,Min_value):
      
    A = 1 / ( - Min_value + Max_value ) 
    B = - Min_value / ( - Min_value + Max_value )
        
    if isinstance(Var_1,list):
    
        for i in range(len(Var_1)):  
            
            Var_1[i] = Var_1[i]*A + B
                
    else:
        
        Var_1 = Var_1*A + B
        
    return  Var_1

# %% Denormalize data

def Denormalize_data( Var, Max_value, Min_value ):
    
    A = 1 / ( - Min_value + Max_value ) 
    
    B = - Min_value / ( - Min_value + Max_value )
    
    if isinstance(Var,list):
        
        for i in range(len(Var)):
            
            Var[i] = (Var[i] - B) / A
    
    else:

        Var = (Var-B)/A
        
    return Var

# %% function to add ECO
    
def insert_eco(Eco,var,max_d,min_d,max_n,min_n):
    
    var = Denormalize_data(var, max_d, min_d)
    
    var = var + Eco
    
    var = Normalize_data( var, max_n, min_n)
    
    return var

# %% linear Transformation 

def linear_transformation(X,x1,x2,y1,y2):

    m = (y2-y1)/(x2-x1)

    b = y1-m*x1

    Y = m*X+b

    return Y

# %% Calculate performance metrics

def Calculate_metrics(real_data,tested_data):
    
    real_data = real_data.reshape(330,1)
    tested_data = tested_data.reshape(330,1)

    mse = sklearn.metrics.mean_squared_error(real_data, tested_data)
    RMSE = math.sqrt(mse)

    MAE = sklearn.metrics.mean_absolute_error(real_data, tested_data)
    
    Mean_1, St_dev_1 = MEAN_STDEV(real_data)
    Mean_2, St_dev_2 = MEAN_STDEV(tested_data)
    
    Cov = np.cov(real_data.reshape(330),tested_data.reshape(330))
        
    r = float(Cov[0][1]) /  (St_dev_1 * St_dev_2)
    
    Sum_1=0
    Sum_2=0
    
    NS=float(0)
    
    for i in range(len(real_data)):
        
        Sum_1 = Sum_1 + (float(tested_data[i])-float(real_data[i]))*(float(tested_data[i])-float(real_data[i]))
        Sum_2 = Sum_2 + (float(real_data[i])-Mean_1)*(float(real_data[i])-Mean_1)
    
    NS = float(1) - (float(Sum_1)/float(Sum_2))
        
    r=float(r)
    
    return r,RMSE,MAE,NS

# %% Load Heigth to volume files
    
def read_organize_storage_converter(file_name):

    csv_file = open(file_name)
    csv_data = csv.reader(csv_file, delimiter=' ')
    
    H = []
    V = []
    
    for row in csv_data:
        
        row[4] = row[4].replace(',','.')
        M=row[0].split('-')
                
        m=float(M[-1].replace(',','.'))
        v=float(row[4])
        H.append(m)
        V.append(v)
    
    S = [H,V]
    
    return S

S_2 = read_organize_storage_converter('Model_2_storage.csv')
S_3 = read_organize_storage_converter('Model_3_storage.csv')
S_4 = read_organize_storage_converter('Model_4_storage.csv')

S_2[0]=Normalize_data(S_2[0], 260, 225)
S_2[1]=Normalize_data(S_2[1], 300, 80)

S_3[0]=Normalize_data(S_3[0], 170, 158)
S_3[1]=Normalize_data(S_3[1], 3, 0.4)

S_4[0]=Normalize_data(S_4[0], 150, 140)
S_4[1]=Normalize_data(S_4[1], 6, 2)

# %% Function to storage converter

def converter(X,conv_type,S):
    
    
    if conv_type == 'h2v':
        
        for i in range(len(S[0])-1):
        
            if X == S[0][i] and i == 0:
                
                Y = S[1][i]

            if X > S[0][i] and X < S[0][i+1]:
               
                Y = linear_transformation(X, S[0][i], S[0][i+1], S[1][i], S[1][i+1])
                
            if X == S[0][i+1]:
                
                Y = S[1][i+1]
                
    elif conv_type == 'v2h':
    
        for i in range(len(S[1])-1):
                    
            if X == S[1][i] and i == 0:
                
                Y = S[0][i]

            if X < S[1][i] and X > S[1][i+1]:
               
                Y = linear_transformation(X, S[1][i], S[1][i+1], S[0][i], S[0][i+1])
                
            if X == S[1][i+1]:
                
                Y = S[0][i+1]
                
            if X > S[1][0]:
                
                Y = 1
                
    else: 
        
        print('erro')
        Y =999999
              
    return Y

# %% Predict MLP

def Predict(Model,X):
    
    Y = Model.predict(X)
    
    tf.keras.backend.clear_session()
    
    return Y 

# %% Execute simulation 
    
Y_1=np.zeros(330)
Y_2=np.zeros(330)
Y_sec_2=np.zeros(330)
Y_3=np.zeros(330)
Y_sec_3=np.zeros(330)
Y_4=np.zeros(330)
Y_sec_4=np.zeros(330)

# %% Calculate metrics
Y_1_only = Predict(MLP_1,Test_in_1)        
Y_2_only = Predict(MLP_2,Test_in_2)
Y_2_sec_only = Predict(MLP_2_sec,Test_in_sec_2)     
Y_3_only = Predict(MLP_3,Test_in_3)
Y_3_sec_only = Predict(MLP_3_sec,Test_in_sec_3)
Y_4_only = Predict(MLP_4,Test_in_4)
Y_4_sec_only = Predict(MLP_4_sec,Test_in_sec_4)

path = path+'\\Plot_'

make_plot(path, 'Model_1',Time_1,'Date', 'Inflow ($m^3/s$)',Test_out_1,'Real Data',Y_1,'Integration',Y_1_only,'Standalone')
make_plot(path, 'Model_2',Time_2,'Date', 'Outflow ($m^3/s$)',Test_out_2,'Real Data',Y_2,'Integration',Y_2_only,'Standalone')
make_plot(path, 'Model_3',Time_3,'Date', 'Outflow ($m^3/s$)',Test_out_3,'Real Data',Y_3,'Integration',Y_3_only,'Standalone')
make_plot(path, 'Model_4',Time_4,'Date', 'Outflow ($m^3/s$)',Test_out_4,'Real Data',Y_4,'Integration',Y_4_only,'Standalone')

make_plot(path, 'Model_2_sec',Time_2,'Date', 'Volume ($hm^3$)',Test_out_sec_2,'Real Data',Y_sec_2,'Integration',Y_2_sec_only,'Standalone')
make_plot(path, 'Model_3_sec',Time_3,'Date', 'Volume ($hm^3$)',Test_out_sec_3,'Real Data',Y_sec_3,'Integration',Y_3_sec_only,'Standalone')
make_plot(path, 'Model_4_sec',Time_4,'Date', 'Volume ($hm^3$)',Test_out_sec_4,'Real Data',Y_sec_4,'Integration',Y_4_sec_only,'Standalone')