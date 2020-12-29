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
Update_time = input('Nunber of days between update:')
path = path+'\\Plot_UT_'+Update_time
Update_time = int(Update_time)

if Update_time > 0:
    cont = 0
    T=[]
    T_1=[]
    while cont<=329:
        
        T.append(cont)
        T_1.append(cont+1)
        cont=cont+Update_time
else:
    T=[0]
    T_1=[1]
    
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

# %% Function To Normalize data Output 

def Normalize_data(Var_1,Max_value,Min_value):
      
    A = 1 / ( - Min_value + Max_value ) 
    B = - Min_value / ( - Min_value + Max_value )
        
    if isinstance(Var_1,list):
        Var = []
        for i in range(len(Var_1)):  
            
            Var.append( Var_1[i]*A + B )
                
    else:
        
        Var = Var_1*A + B
        
    return  Var

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

# %% function to add ECO
    
def insert(var,max_d,min_d,max_n,min_n):
    
    var = Denormalize_data(var, max_d, min_d)
    
    var = Normalize_data( var, max_n, min_n)
    
    return var

# %% linear Transformation 

def linear_transformation(X,x1,x2,y1,y2):

    m = (y2-y1)/(x2-x1)

    b = y1-m*x1

    Y = np.copy(m*X+b)

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
    
def read_organize_storage_converter(file_name,T):

    csv_file = open(file_name)
    if T == 1:
        csv_data = csv.reader(csv_file, delimiter=' ')
    else:
        csv_data = csv.reader(csv_file, delimiter=';')
    H = []
    V = []
    
    for row in csv_data:
        
        if T ==1:
            row[4] = row[4].replace(',','.')
        M=row[0].split('-')
                
        m=float(M[-1].replace(',','.'))
        v=float(row[4])
        H.append(m)
        V.append(v)
    
    S = [H,V]
    
    return S

S_2 = read_organize_storage_converter('Model_2_storage.csv',1)
S_3 = read_organize_storage_converter('Model_3_storage.csv',1)
S_4 = read_organize_storage_converter('Model_4_storage.csv',2)

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

# %% Model 1 

MLP_1 = load_model('model_1.h5')

Y_1_only = MLP_1.predict(Test_in_1)

for i in tqdm(range(330)):
    
    if i == 0:
        
        X = np.copy(Test_in_1[i,:])
        Var_1 = X.reshape(1,50)
        Y_1[i] = Predict(MLP_1,Var_1)

    elif i ==1 :
        
        X = np.copy(Test_in_1[i,:])
        Var_1 = X.reshape(1,50)
        Var_1[0,-1] = float(Y_1[i-1])
        Y_1[i]=Predict(MLP_1,Var_1)
        
    else:
        
        X = np.copy(Test_in_1[i,:])
        Var_1 = X.reshape(1,50)
        Var_1[0,-1] = float(Y_1[i-1])
        Y_1[i]=Predict(MLP_1,Var_1)
    
del MLP_1  

r_1,RMSE_1,MAE_1,NS_1 = Calculate_metrics(Test_out_1, Y_1)  
Test_out_1 = Denormalize_data(Test_out_1, 300,0)
Y_1_ = Denormalize_data(Y_1, 300,0 )
Y_1_only =  Denormalize_data(Y_1_only, 300, 0)
r_1,RMSE_1,MAE_1,NS_1 = Calculate_metrics(Test_out_1, Y_1_)  
# make_plot(path, 'Model_1',Time_1,'Date', 'Inflow ($m^3/s$)',Test_out_1,'Real Data',Y_1_only,'Standalone',Y_1_,'Combined')

# %% Model 2 

MLP_2 = load_model('model_2.h5')
MLP_2_sec = load_model('model_2_sec.h5') 
      
Y_2_only = MLP_2.predict(Test_in_2)
Y_2_sec_only = MLP_2_sec.predict(Test_in_sec_2)

for i in tqdm(range(330)):

    Eco = Eco_outflow[int(Time_1[i].month) -1]
    Eco_1 = Eco_outflow[int(Time_1[i-1].month) - 1]

    if i in T:
        
        if i == 0:
        
            X=np.copy(Test_in_2[i,:])
            Var_2 = X.reshape(1,8)
            Var_2[0,4] = float(Y_1[i])
            Y_2[i]=Predict(MLP_2,Var_2)
            
        else:
            
            X = np.copy(Test_in_2[i,:])
            Var_2 = X.reshape(1,8)
            Var_2[0,1] = converter(Y_sec_2[i-1],'v2h', S_2)
            Var_2[0,-1] = float(Y_2[i-1]) 
            Var_2[0,4] = float(Y_1[i])
            Var_2[0,3] = float(Y_1[i-1])
            Var_2[0,2] = float(Y_1[i-2])
            Y_2[i]=Predict(MLP_2,Var_2)
            
            
        
        X=np.copy(Test_in_sec_2[i,:])
        Var_2_sec = X.reshape(1,5)
        Var_2_sec[0,1] = float(Y_1[i])
        P_out=insert_eco(Eco, float(Y_2[i]), 250, 0, 250, 0)
        Var_2_sec[0,2] = P_out
        Y_sec_2[i]=Predict(MLP_2_sec,Var_2_sec)
        
        
    elif i in T_1:
        
        if i == 1:
        
            X = np.copy(Test_in_2[i,:])
            Var_2 = X.reshape(1,8)
            Var_2[0,1] = converter(float(Y_sec_2[i-1]),'v2h', S_2)
            Var_2[0,-1] = float(Y_2[i-1])
            Var_2[0,4] = float(Y_1[i])
            Var_2[0,3] = float(Y_1[i-1])
            Y_2[i]=Predict(MLP_2,Var_2)
            
        else:
            
            X = np.copy(Test_in_2[i,:])
            Var_2 = X.reshape(1,8)
            Var_2[0,1] = converter(Y_sec_2[i-1],'v2h', S_2)
            Var_2[0,-1] = float(Y_2[i-1]) 
            Var_2[0,4] = float(Y_1[i])
            Var_2[0,3] = float(Y_1[i-1])
            Var_2[0,2] = float(Y_1[i-2])
            Y_2[i]=Predict(MLP_2,Var_2)
                
        
        X = np.copy(Test_in_sec_2[i,:])
        Var_2_sec = X.reshape(1,5)
        Var_2_sec[0,0] = float(Y_sec_2[i-1])
        Var_2_sec[0,1] = float(Y_1[i])
        P_out = insert_eco(Eco, float(Y_2[i]), 250, 0, 250, 0)
        P_out_1 = insert_eco(Eco_1, float(Y_2[i-1]), 250, 0, 250, 0) 
        Var_2_sec[0,2] = P_out
        Var_2_sec[0,3] = float(Y_1[i-1])
        Var_2_sec[0,4] = P_out_1
        Y_sec_2[i]=Predict(MLP_2_sec,Var_2_sec)
        
    else:
        
        X = np.copy(Test_in_2[i,:])
        Var_2 = X.reshape(1,8)
        Var_2[0,1] = converter(Y_sec_2[i-1],'v2h', S_2)
        Var_2[0,-1] = float(Y_2[i-1]) 
        Var_2[0,4] = float(Y_1[i])
        Var_2[0,3] = float(Y_1[i-1])
        Var_2[0,2] = float(Y_1[i-2])
        Y_2[i]=Predict(MLP_2,Var_2)
    
        X = np.copy(Test_in_sec_2[i,:])     
        Var_2_sec = X.reshape(1,5)
        Var_2_sec[0,0] = float(Y_sec_2[i-1])
        Var_2_sec[0,1] = float(Y_1[i])
        P_out = insert_eco(Eco, float(Y_2[i]), 250, 0, 250, 0)
        P_out_1 = insert_eco(Eco_1, float(Y_2[i-1]), 250, 0, 250, 0) 
        Var_2_sec[0,2] = P_out
        Var_2_sec[0,3] = float(Y_1[i-1])
        Var_2_sec[0,4] = P_out_1
        Y_sec_2[i]=Predict(MLP_2_sec,Var_2_sec)
     
del MLP_2
del MLP_2_sec

MLP_2 = load_model('model_2.h5')
MLP_2_sec = load_model('model_2_sec.h5') 

Test_out_2 = Denormalize_data(Test_out_2, 250, 0)
Y_2_ = Denormalize_data(Y_2, 250, 0)
Y_2_only = Denormalize_data(Y_2_only, 250, 0)
Test_out_sec_2 = Denormalize_data(Test_out_sec_2, 300, 80)
Y_sec_2_ = Denormalize_data(Y_sec_2, 300, 80)
Y_2_sec_only = Denormalize_data(Y_2_sec_only, 300, 80)
r_2,RMSE_2,MAE_2,NS_2 = Calculate_metrics(Test_out_2, Y_2_)
r_2s,RMSE_2s,MAE_2s,NS_2s = Calculate_metrics(Test_out_sec_2, Y_sec_2_)
# make_plot(path, 'Model_2',Time_2,'Date', 'Outflow ($m^3/s$)',Test_out_2,'Real Data',Y_2_only,'Standalone',Y_2_,'Combine')
# make_plot(path, 'Model_2_sec',Time_2,'Date', 'Volume ($hm^3$)',Test_out_sec_2,'Real Data',Y_2_sec_only,'Standalone',Y_sec_2_,'Combine')

make_plot(path, 'Sec_model_2',Time_2,'Date', 'Volume ($hm^3$)',Test_out_sec_2,'Real Data',Y_2_sec_only,'Estimation')

# %% Model 3

MLP_3 = load_model('model_3.h5')
MLP_3_sec = load_model('model_3_sec.h5')

Y_3_only = MLP_3.predict(Test_in_3)
Y_3_sec_only = MLP_3_sec.predict(Test_in_sec_3)

for i in tqdm(range(330)):

    Eco = Eco_outflow[int(Time_1[i].month) - 1]
    Eco_1 = Eco_outflow[int(Time_1[i-1].month) - 1]
    Eco_2 = Eco_outflow[int(Time_1[i-2].month) - 1]  

    if i in T:
        
        if i == 0:

            Var_3 = np.copy(Test_in_3[i,:]).reshape(1,7)
            P_in = insert_eco(Eco, float(Y_2[i]), 250, 0, 230, 5)
            Var_3[0,3] = P_in
            Y_3[i]=Predict(MLP_3,Test_in_3[i,:].reshape(1,7))
            
        else:
            
            Var_3 = np.copy(Test_in_3[i,:]).reshape(1,7)
            Var_3[0,1] = float(Y_sec_3[i-1])
            Var_3[0,-1] = float(Y_3[i-1])
            P_in = insert_eco(Eco, float(Y_2[i]), 250, 0, 230, 5)
            Var_3[0,3] = P_in
            P_in_1 = insert_eco(Eco_1, float(Y_2[i-1]), 250, 0, 230, 5)
            Var_3[0,2] = P_in_1
            Y_3[i]=Predict(MLP_3,Var_3) 
            
        
        Var_3_sec = np.copy(Test_in_sec_3[i,:]).reshape(1,5)
        P_in = insert_eco(Eco,float(Y_2[i]), 250, 0, 230, 5)
        Var_3_sec[0,1] = P_in
        P_out = insert_eco(Eco, float(Y_3[i]), 230, 0, 230, 0)
        Var_3_sec[0,2] = P_out
        Y_sec_3[i]=Predict(MLP_3_sec,Var_3_sec)
        
    elif i in T_1:
        
        if i == 1:

            Var_3 = np.copy(Test_in_3[i,:]).reshape(1,7)
            Var_3[0,1] = float(Y_sec_3[i-1])
            Var_3[0,-1] = float(Y_3[i-1])
            P_in = insert_eco(Eco, float(Y_2[i]), 250, 0, 230, 5)
            Var_3[0,3] = P_in
            P_in_1 = insert_eco(Eco_1, float(Y_2[i-1]), 250, 0, 230, 5)
            Var_3[0,2] = P_in_1
            Y_3[i]=Predict(MLP_3,Var_3) 
        
        else:
        
            Var_3 = np.copy(Test_in_3[i,:]).reshape(1,7)
            Var_3_sec[0,0] = float(Y_sec_3[i-1])
            Var_3[0,-1] = float(Y_3[i-1])
            P_in = insert_eco(Eco, float(Y_2[i]), 250, 0, 230, 5)
            Var_3[0,3] = P_in
            P_in_1 = insert_eco(Eco_1, float(Y_2[i-1]), 250, 0, 230, 5)
            Var_3[0,2] = P_in_1
            Y_3[i]=Predict(MLP_3,Var_3)
        
        
        Var_3_sec = np.copy(Test_in_sec_3[i,:]).reshape(1,5)
        Var_3_sec[0,0] = float(Y_sec_3[i-1])
        P_in = insert_eco(Eco,float(Y_2[i]), 250, 0, 230, 5)
        Var_3_sec[0,1] = P_in
        P_out = insert_eco(Eco, float(Y_3[i]), 230, 0, 230, 0)
        P_out_1 = insert_eco(Eco_1, float(Y_3[i-1]), 230, 0, 230, 0) 
        Var_3_sec[0,2] = P_out
        P_in_1 = insert_eco(Eco_1, float(Y_2[i-1]), 250, 0, 230, 5)
        Var_3_sec[0,3] = P_in_1
        Var_3_sec[0,4] = P_out_1
        Y_sec_3[i]=Predict(MLP_3_sec,Var_3_sec)
        
    else:

        Var_3 = np.copy(Test_in_3[i,:]).reshape(1,7)
        Var_3_sec[0,0] = float(Y_sec_3[i-1])
        Var_3[0,-1] = float(Y_3[i-1])
        P_in = insert_eco(Eco, float(Y_2[i]), 250, 0, 230, 5)
        Var_3[0,3] = P_in
        P_in_1 = insert_eco(Eco_1, float(Y_2[i-1]), 250, 0, 230, 5)
        Var_3[0,2] = P_in_1
        Y_3[i]=Predict(MLP_3,Var_3)
        
        Var_3_sec = np.copy(Test_in_sec_3[i,:]).reshape(1,5)
        Var_3_sec[0,0] = float(Y_sec_3[i-1])
        P_in = insert_eco(Eco,float(Y_2[i]), 250, 0, 230, 5)
        Var_3_sec[0,1] = P_in
        P_out = insert_eco(Eco, float(Y_3[i]), 230, 0, 230, 0)
        P_out_1 = insert_eco(Eco_1, float(Y_3[i-1]), 230, 0, 230, 0) 
        Var_3_sec[0,2] = P_out
        P_in_1 = insert_eco(Eco_1, float(Y_2[i-1]), 250, 0, 230, 5)
        Var_3_sec[0,3] = P_in_1
        Var_3_sec[0,4] = P_out_1
        Y_sec_3[i]=Predict(MLP_3_sec,Var_3_sec)
            
Test_out_3 = Denormalize_data(Test_out_3, 230, 0)
Y_3_ = Denormalize_data(Y_3, 230, 0)
Y_3_only = Denormalize_data(Y_3_only, 230, 0)
Test_out_sec_3 = Denormalize_data(Test_out_sec_3, 3, 0.4)
Y_sec_3_ = Denormalize_data(Y_sec_3, 3, 0.4)
Y_3_sec_only = Denormalize_data(Y_3_sec_only, 3, 0.4)
r_3,RMSE_3,MAE_3,NS_3 = Calculate_metrics(Test_out_3, Y_3_)
r_3s,RMSE_3s,MAE_3s,NS_3s = Calculate_metrics(Test_out_sec_3, Y_sec_3_)
# make_plot(path, 'Model_3',Time_3,'Date', 'Outflow ($m^3/s$)',Test_out_3,'Real Data',Y_3_only,'Standalone',Y_3_,'Combined')
# make_plot(path, 'Model_3_sec',Time_3,'Date', 'Volume ($hm^3$)',Test_out_sec_3,'Real Data',Y_3_sec_only,'Standalone',Y_sec_3_,'Combined')

make_plot(path, 'Sec_model_3',Time_3,'Date', 'Volume ($hm^3$)',Test_out_sec_3,'Real Data',Y_3_sec_only,'Estimation')

del MLP_3
del MLP_3_sec

# %% Model 4

MLP_4 = load_model('model_4.h5')
MLP_4_sec = load_model('model_4_sec.h5')
        
Y_4_only = MLP_4.predict(Test_in_4)
Y_4_sec_only = MLP_4_sec.predict(Test_in_sec_4)

for i in tqdm(range(330)):

    Eco = Eco_outflow[int(Time_1[i].month) - 1]
    Eco_1 = Eco_outflow[int(Time_1[i-1].month) - 1]
    Eco_2 = Eco_outflow[int(Time_1[i-2].month) - 1]  

    if i in T:
        
        if i ==0:
        
            Var_4 = np.copy(Test_in_4[i,:]).reshape(1,7)
            P_in = insert_eco(Eco, float(Y_3[i]), 230, 0, 230, 5)
            Var_4[0,4] = P_in
            Y_4[i]=Predict(MLP_4,Var_4)
       
        else:
            
            Var_4 = np.copy(Test_in_4[i,:]).reshape(1,7)
            Var_4[0,1] = converter(float(Y_sec_4[i-1]),'v2h', S_4)
            Var_4[0,-1] = float(Y_4[i-1])
            P_in = insert_eco(Eco, float(Y_3[i]), 230, 0, 230, 5)
            Var_4[0,4] = P_in
            P_in_1 = insert_eco(Eco_1, float(Y_3[i-1]), 230, 0, 230, 5)
            Var_4[0,3] = P_in_1
            P_in_2 = insert_eco(Eco_2, float(Y_3[i-2]), 230, 0, 230, 5)
            Var_4[0,2] = P_in_2
            Y_4[i]=Predict(MLP_4,Var_4) 
            
        
        Var_4_sec = np.copy(Test_in_sec_4[i,:]).reshape(1,3)
        P_in = insert_eco(Eco, float(Y_3[i]), 230, 0, 230, 5)        
        Var_4_sec[0,1] = P_in
        P_out = insert_eco(Eco, float(Y_4[i]), 230, 0, 230, 0)
        Var_4_sec[0,2] = P_out
        Y_sec_4[i]=Predict(MLP_4_sec,Var_4_sec)
        
    elif i in T_1:
        
        if i == 1: 
        
            Var_4 = np.copy(Test_in_4[i,:]).reshape(1,7)
            Var_4[0,1] = converter(float(Y_sec_4[i-1]),'v2h', S_4)
            Var_4[0,-1] = float(Y_4[i-1])
            P_in = insert_eco(Eco, float(Y_3[i]), 230, 0, 230, 5)
            Var_4[0,4] = P_in
            P_in_1 = insert_eco(Eco_1, float(Y_3[i-1]), 230, 0, 230, 5)
            Var_4[0,3] = P_in_1
            Y_4[i]=Predict(MLP_4,Var_4)
            
        else:
            
            Var_4 = np.copy(Test_in_4[i,:]).reshape(1,7)
            Var_4[0,1] = converter(float(Y_sec_4[i-1]),'v2h', S_4)
            Var_4[0,-1] = float(Y_4[i-1])
            P_in = insert_eco(Eco, float(Y_3[i]), 230, 0, 230, 5)
            Var_4[0,4] = P_in
            P_in_1 = insert_eco(Eco_1, float(Y_3[i-1]), 230, 0, 230, 5)
            Var_4[0,3] = P_in_1
            P_in_2 = insert_eco(Eco_2, float(Y_3[i-2]), 230, 0, 230, 5)
            Var_4[0,2] = P_in_2
            Y_4[i]=Predict(MLP_4,Var_4) 
        
        Var_4_sec = np.copy(Test_in_sec_4[i,:]).reshape(1,3)
        Var_4_sec[0,0] = float(Y_sec_4[i-1])
        P_in = insert_eco(Eco, float(Y_3[i]), 230, 0, 230, 5)        
        Var_4_sec[0,1] = P_in
        P_out = insert_eco(Eco, float(Y_4[i]), 230, 0, 230, 0)
        Var_4_sec[0,2] = P_out
        Y_sec_4[i]=Predict(MLP_4_sec,Var_4_sec)
        
    else:
        
        Var_4 = np.copy(Test_in_4[i,:]).reshape(1,7)
        Var_4[0,1] = converter(float(Y_sec_4[i-1]),'v2h', S_4)
        Var_4[0,-1] = float(Y_4[i-1])
        P_in = insert_eco(Eco, float(Y_3[i]), 230, 0, 230, 5)
        Var_4[0,4] = P_in
        P_in_1 = insert_eco(Eco_1, float(Y_3[i-1]), 230, 0, 230, 5)
        Var_4[0,3] = P_in_1
        P_in_2 = insert_eco(Eco_2, float(Y_3[i-2]), 230, 0, 230, 5)
        Var_4[0,2] = P_in_2
        Y_4[i]=Predict(MLP_4,Var_4)  
        
        Var_4_sec = np.copy(Test_in_sec_4[i,:]).reshape(1,3)
        Var_4_sec[0,0] = float(Y_sec_4[i-1])
        P_in = insert_eco(Eco, float(Y_3[i]), 230, 0, 230, 5)        
        Var_4_sec[0,1] = P_in
        P_out = insert_eco(Eco, float(Y_4[i]), 230, 0, 230, 0)
        Var_4_sec[0,2] = P_out
        Y_sec_4[i]=Predict(MLP_4_sec,Var_4_sec)

Test_out_4 = Denormalize_data(Test_out_4, 230, 0)
Y_4_ = Denormalize_data(Y_4, 230, 0)
Y_4_only = Denormalize_data(Y_4_only, 230, 0)
Test_out_sec_4 = Denormalize_data(Test_out_sec_4, 6, 2)
Y_sec_4_ = Denormalize_data(Y_sec_4, 6, 2)
Y_4_sec_only = Denormalize_data(Y_4_sec_only, 6, 2)
r_4,RMSE_4,MAE_4,NS_4 = Calculate_metrics(Test_out_4, Y_4_)
r_4s,RMSE_4s,MAE_4s,NS_4s = Calculate_metrics(Test_out_sec_4, Y_sec_4_)
# make_plot(path, 'Model_4',Time_4,'Date', 'Outflow ($m^3/s$)',Test_out_4,'Real Data',Y_4_only,'Standalone',Y_4_,'Combined')
# make_plot(path, 'Model_4_sec',Time_4,'Date', 'Volume ($hm^3$)',Test_out_sec_4,'Real Data',Y_4_sec_only,'Standalone',Y_sec_4_,'Combined')

make_plot(path, 'Sec_model_4',Time_4,'Date', 'Volume ($hm^3$)',Test_out_sec_4,'Real Data',Y_4_sec_only,'Estimation')

del MLP_4
del MLP_4_sec

# %% wrtie results

f = open('Results'+ str(Update_time)  +'.txt','w')
f.write('--------- Data Results ---------\n')
f.write('Model 1 \nr - {:4f}\nRMSE - {:4f}\nMAE - {:4f}\nNS - {:4f}\n'.format(r_1,RMSE_1,MAE_1,NS_1))
f.write('Model 2 \nr - {:4f}\nRMSE - {:4f}\nMAE - {:4f}\nNS - {:4f}\n'.format(r_2,RMSE_2,MAE_2,NS_2))
f.write('Model 3 \nr - {:4f}\nRMSE - {:4f}\nMAE - {:4f}\nNS - {:4f}\n'.format(r_3,RMSE_3,MAE_3,NS_3))
f.write('Model 4 \nr - {:4f}\nRMSE - {:4f}\nMAE - {:4f}\nNS - {:4f}\n'.format(r_4,RMSE_4,MAE_4,NS_4))
f.write('Model 2 Sec \nr - {:4f}\nRMSE - {:4f}\nMAE - {:4f}\nNS - {:4f}\n'.format(r_2s,RMSE_2s,MAE_2s,NS_2s))
f.write('Model 3 Sec \nr - {:4f}\nRMSE - {:4f}\nMAE - {:4f}\nNS - {:4f}\n'.format(r_3s,RMSE_3s,MAE_3s,NS_3s))
f.write('Model 4 Sec \nr - {:4f}\nRMSE - {:4f}\nMAE - {:4f}\nNS - {:4f}\n'.format(r_4s,RMSE_4s,MAE_4s,NS_4s))
f.close()
