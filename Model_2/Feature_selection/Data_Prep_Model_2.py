# Define inputs and outpus for model 2

# Input :
#   - Storage volume (t-1)
#   - Inflow Past
#   - Inflow Future 

# Ouput :
#   - Outflow
#   - Storage volume (t)


import pickle as pr
import numpy as np

# %% Function to create day index 
    
def day_index():
    
    day_c=[]
    
    cont = 0
    
    j = 0

    data = [365,365,366,365,196]
    
    for i in range(1657):
    
        day_c.append(i-cont+1)
        
        if (i - cont + 1) == data[j] :
            
            cont = cont + data[j]
            j=j+1
            
    return day_c

# %% Function to organize inputs into a

# data_type = [ day index, type of storage, number of days in the past, 
#               number of days in the future, outflow type]
    
# day index: 1 - acconut; 0 - disregard
# type of storage: 0 - none  1 - depth; 2 - volume 
# Number of days past: from 0 to infinity
# Number of days in the future: from 0 to infinity
# outflow type: 0 - unique; 1 - Seperate
    

def order_vars( Dam, data_type ):
    
    in_final=[]
    out_final = []
    time_plot =[]
    
    Min = [ 0, 225, 80, 0, 0, 0, 0, 0 ]
    Max = [ 365, 260, 320, 300, 250, 10, 130, 130]
    
    day_i = day_index()
    
    comp = len(Dam[0])
    
    # check if predication of the inflow is asked
    if data_type[3] == 0:
        end = 0
    else:
        end = data_type[3]-1
    
    # start organizing 
    for i in range(data_type[2] , comp - end):
        
        list_in=[]
        list_out=[]
        
        # Dai index
                
        if data_type[0] == 1:

            x = Normalize_data(day_i[i], Max[0], Min[0])
            list_in.append(x)  
        
        # Storage 

        if data_type[1] == 1:
            x = Normalize_data(Dam[2][i-1], Max[1], Min[1])
            list_in.append(x)
            y = Normalize_data(Dam[2][i], Max[1], Min[1])
            list_out.append(y)
        elif data_type[1] == 2:
            x = Normalize_data(Dam[3][i-1], Max[2], Min[2])
            list_in.append(x)
            y = Normalize_data(Dam[3][i], Max[2], Min[2])
            list_out.append(y)
            
        # Inflow
            
        if data_type[2] > 0:
            for j in range(-data_type[2],0):
                x = Normalize_data(Dam[4][i+j], Max[3], Min[3])
                list_in.append(x)
                
        if data_type[3] > 0:
            for j in range(0,data_type[3]):
                x = Normalize_data(Dam[4][i+j], Max[3], Min[3])
                list_in.append(x)

        # Outflow
        if data_type[4] == 0:
            y = Normalize_data(Dam[5][i], Max[4], Min[4])
            list_out.append(y)
        elif data_type[4] ==1:
            y = Normalize_data(Dam[6][i], Max[5], Min[5])
            list_out.append(y)
            y = Normalize_data(Dam[7][i], Max[6], Min[6])
            list_out.append(y)
            y = Normalize_data(Dam[8][i], Max[7], Min[7])
            list_out.append(y)
            
            
        in_final.append(list_in)
        out_final.append(list_out)
        time_plot.append(Dam[0][i])
            
    return in_final, out_final, time_plot 

# %% Function to clean any rowa with missing data
    
def clean_nan(Input, Output, Time_plot):
    
    X = Input.shape[0]
    
    for i in range(X-1,-1,-1):
        
        for j in range(Input.shape[1]):
            
            if np.isnan(Input[i,j]) or np.isnan(Output[i,0]):
                                
                Input = np.delete(Input, (i), axis=0)
                Output = np.delete(Output, (i), axis=0)
                del Time_plot[i]
                
    return Input, Output, Time_plot

# %% Function To Normalize data Output 

def Normalize_data(Var_1,Max_value,Min_value):
      
    A = 1 / ( - Min_value + Max_value ) 
    B = - Min_value / ( - Min_value + Max_value )
        
    if isinstance(Var_1,list):
    
        for i in range(len(Var_1)):  
            
            if Var_1[i] == None: 
                Var_1[i] == None
            else:    
                Var_1[i] = Var_1[i]*A + B
                
    else:
        
        if Var_1 == None: 
            Var_1 == None
        else:    
            Var_1 = Var_1*A + B
            
        
    return  Var_1

# %% Execute
    
def generate_data( save, data_type ):
    
    _, _, Portodemouros = pr.load(open("Dams.p","rb"))
    
    input_value, output_value, time_plot = order_vars( Portodemouros, data_type )
    
    input_var = np.asarray(input_value).astype(np.float32)
    output_var = np.asarray(output_value).astype(np.float32)

    input_var, output_var, time_plot = clean_nan( input_var, output_var, time_plot )
    
    if save == 1:
    
        name = 'Data_model_2.p'
        
        pr.dump ( [input_var, output_var, time_plot] , open( name, "wb" ) )
        
    return input_var, output_var, time_plot
