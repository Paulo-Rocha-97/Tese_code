# Define inputs and outpus for model 2

# Input (main):
#   - Storage volume (t-1)
#   - Inflow Past
#   - Inflow Future 

# Ouput (main):
#   - Outflow(t)

# Input (storage predictor):
#   - Outflow(t)
#   - Storage volume (t-1)

# Output (storage preditor):
#   - Storage volume (t) 

import pickle as pr
import numpy as np
from scipy.io import savemat
from math import nan

# %% Function to create day index 
    
def day_index(comp):
    
    day_c=[]
    
    cont = 0
    
    j = 0

    data = [365,365,365,366,365,365,365,366,365,365,365,366,365,196]
    
    for i in range(comp):
    
        day_c.append(i-cont+1)
                
        if (i - cont + 1) == data[j] :
            
            cont = cont + data[j]
            j=j+1
            
    return day_c

# %% Function to create manth index

def month_index(Time):
    
    month_value = Time.month
    
    return month_value
    
    month_value = Time.month
    
    return month_value

# %% Function to organize inputs 

# data_type = [ day index, type of storage, number of days in the past, 
#               number of days in the future, outflow type]
    
# day index: 2 - month; 1 - acconut; 0 - disregard
# type of storage: 0 - none;  1 - depth; 2 - volume 
# Number of days past: from 0 to infinity
# Number of days in the future: from 0 to infinity
# outflow type: 0 - unique; 1 - Seperate
# week day info: 0 - week_combine_holiday 1 - week day binary 2 - week day in number 3 - none
# holiday info: 0 - week_combine_holiday 1 - national holiday 2 - national and galiza holiday 3 - none
# remove caudal ecologigo: 0 - not remove; 1 - remove caudal ecologico

def order_vars( Dam, N_holiday, G_holiday, W_n, W_b, W_c, Eco_outflow, data_type ):
  
    in_final=[]
    out_final=[]
    time_plot=[]
    in_final_sec=[]
    out_final_sec=[]
    
    # Min and Max index explanation
    # 0 - days
    # 1 - Heigth (m)
    # 2 - Volume (Hm^3)
    # 3 - Inflow
    # 4 - Outflow total
    # 5 - Out Bottom
    # 6 - Out Flood
    # 7 - Out Power
    # 8 - Week days
    
    Min = [   0, 225,  80,   0,   0,  0,   0,  0, 0]
    Max = [ 365, 260, 300, 300, 250, 50, 180, 90, 7]
    
    comp = len(Dam[0])
    
    day_i = day_index(comp)
        
    # check if predication of the inflow is asked
    if data_type[3] == 0:
        end = 0
    else:
        end = data_type[3]-1
    
    # start organizing 
    for i in range(data_type[2] , comp - end):
        
        list_in=[]
        list_out=[]
        
        list_in_sec=[]
        list_out_sec=[]
        
        # Day index
                
        if data_type[0] == 1:

            x = Normalize_data(day_i[i], Max[0], Min[0])
            list_in.append(x) 
        
        elif data_type[0] == 2:
            
            month = month_index(Dam[0][i])
            x = Normalize_data(month, 12, 1)
            list_in.append(x) 
            
        # Storage 

        if data_type[1] == 1:
            x = Normalize_data(Dam[2][i-1], Max[1], Min[1])
            list_in.append(x)

            y = Normalize_data(Dam[3][i], Max[2], Min[2])
            list_out_sec.append(y)
            
        # Inflow
            
        if data_type[2] > 0:
            for j in range(-data_type[2],0):
                x = Normalize_data(Dam[4][i+j], Max[3], Min[3])
                list_in.append(x)
                
        if data_type[3] > 0:
            for j in range(0,data_type[3]):
                x = Normalize_data(Dam[4][i+j], Max[3], Min[3])
                list_in.append(x)
                
        # Week and holiday info 
                
        if data_type[5] == 0 or data_type[5] == 0:
            x = W_c[i]
            list_in.append(x)
        
        else:
            # week info
            if data_type [5] == 1:
                x = W_b[i]
                list_in.append(x)
                
            else:
                x = Normalize_data(W_n[i], Max[8], Min[8])
                list_in.append(x)
            
            # holiday info
            if data_type [6] == 1:
                x = N_holiday[i]
                list_in.append(x)
            else:
                x = G_holiday[i]
                list_in.append(x)           

        # Outflow
                
        if data_type[4] == 0:
            
            if data_type[7] == 1: 
                
                if Dam[5][i] != None:
                
                    month = month_index(Dam[0][i]) - 1
                    
                    y = Normalize_data(Dam[5][i] - Eco_outflow[ month ], Max[4], Min[4])
                    list_out.append(y)

                    
                else:
                     list_out.append(None)
                
            else:
                y = Normalize_data(Dam[5][i], Max[4], Min[4])
                list_out.append(y)

                
        elif data_type[4] ==1:
            
            y = Normalize_data(Dam[6][i], Max[5], Min[5])
            list_out.append(y)
            y = Normalize_data(Dam[7][i], Max[6], Min[6])
            list_out.append(y)
            
            if data_type[7] == 1 :
            
                if Dam[8][i] != None :
            
                    month = month_index(Dam[0][i]) - 1
        
                    y = Normalize_data(Dam[8][i] - Eco_outflow[ month ], Max[7], Min[7])
                    list_out.append(y)

                    
                else:
                     list_out.append(None)
                
            else:

                y = Normalize_data(Dam[8][i], Max[7], Min[7])
                list_out.append(y)

            
        w = Normalize_data(Dam[5][i], Max[4], Min[4])
        y = Normalize_data(Dam[4][i], Max[3], Min[3]) 
        list_in_sec.append(y)
        list_in_sec.append(w) 
            
        in_final.append(list_in)
        out_final.append(list_out)
        in_final_sec.append(list_in_sec)
        out_final_sec.append(list_out_sec)
        time_plot.append(Dam[0][i])
            
    return in_final, out_final, time_plot, in_final_sec, out_final_sec 

# %% Function To Normalize data Output 

def Normalize_data(Var_1,Max_value,Min_value):
    
    # A = 1 / ( Min_value + Max_value ) 
    # B = - Min_value / ( Min_value + Max_value )
        
    # if isinstance(Var_1,list):
    
    #     for i in range(len(Var_1)):  
            
    #         if Var_1[i] == None: 
    #             Var_1[i] == None
    #         else:    
    #             Var_1[i] = Var_1[i]*A + B
                
    # else:
        
    #     if Var_1 == None: 
    #         Var_1 == None
    #     else:    
    #         Var_1 = Var_1*A + B      
            
    return  Var_1

# %% transform into none into nan

def tranform_none (var,type_var):
    
    var_shape=var.shape
    
    for i in range(var_shape[0]):
        
        if type_var =='in':
            for j in range(var_shape[1]):
            
                if var[i,j] == None:
                
                    var[i,j] = nan
        else :
            if var[i] == None:
                
                var[i] = nan
            
    return var

# %% Execute
    
_, _, Portodemouros = pr.load(open("Dams_2013.p","rb"))
N_holiday, G_holiday, W_n, W_b, W_c  = pr.load(open("Time_model_2.p","rb"))

Eco_outflow = [15,15,11.9,9.6,8.6,7.9,5,5,5,8.9,11.9,15]

data_type = [2,1,0,1,0,2,2,1]

input_value, output_value, _, input_value_sec, output_value_sec = order_vars( Portodemouros, N_holiday, G_holiday, W_n, W_b, W_c, Eco_outflow, data_type )

input_var = np.asarray(input_value).astype(float)
output_var = np.asarray(output_value).astype(float)
input_var_sec = np.asarray(input_value_sec).astype(float)
output_var_sec = np.asarray(output_value_sec).astype(float)

input_var = tranform_none(input_var,'in')
output_var = tranform_none(output_var,'out')
input_var_sec = tranform_none(input_var_sec,'in')
output_var_sec = tranform_none(output_var_sec,'out')

model_2_data  = {'u': input_var,
                 'y':output_var,
                 'u_sec': input_var_sec,
                 'y_sec':output_var_sec,}

savemat("model_2_data_OG.mat", model_2_data)