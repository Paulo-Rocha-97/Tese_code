# Define inputs and outpus 

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

def order_inputs( var_1, var_2, var_3, var_4 , var_5, var_6, output, n_days_delayed, data_in_use ):
    
    var_final=[]
    var=[]
    out_final = []
    
    Mins = [1,-5, 0, 15, 35, 800, 0, 0, 0]
    Maxs = [366, 30, 110, 100, 3200, 1000, 350, 125, 300]
    
    if len(var_1[0]) == len(var_2[0]) and len(var_1[0]) == len(var_3[0]) and len(var_1[0]) == len(var_4[0]):  
        
        day_i = day_index()
        
        for i in range(len(var_1[0])):
            
            list_in=[]
            n = 1
            k = 1
            
            # temperature 
            av = 0
            cont = 0
            index = 2
            
            if data_in_use[n] == 1:
                x = Normalize_data(var_1[index][i], Maxs[k], Mins[k]) 
                list_in.append(x)
            elif data_in_use[n] == 2 and var_1[index][i] != None:
                av = av + var_1[index][i]
                cont = cont + 1
            n = n + 1 
                
            if data_in_use[n] == 1:
                x = Normalize_data(var_2[index][i], Maxs[k], Mins[k]) 
                list_in.append(x)
            elif data_in_use[n] == 2 and var_2[index][i] != None:
                av = av + var_2[index][i]
                cont = cont + 1
            n = n + 1 
                
            if data_in_use[n] == 1:
                x = Normalize_data(var_3[index][i], Maxs[k], Mins[k]) 
                list_in.append(x)
            elif data_in_use[n] == 2 and var_3[index][i] != None:
                av = av + var_3[index][i]
                cont = cont + 1
            n = n + 1 
                
            if data_in_use[n] == 1:
                x = Normalize_data(var_4[index][i], Maxs[k], Mins[k]) 
                list_in.append(x)
            elif data_in_use[n] == 2 and var_4[index][i] != None:
                av = av + var_4[index][i]
                cont = cont + 1
            n = n + 1 

            if av != 0:
                y = av/cont
                x = Normalize_data(y, Maxs[k], Mins[k])
                list_in.append(x)
            elif av == 0 and ( data_in_use[n-1] == 2 or data_in_use[n-2] == 2 or data_in_use[n-3] == 2 or data_in_use[n-4] == 2):
                list_in.append((None))
            
            k = k + 1
            
            # precipitation 
            av = 0
            cont = 0
            index = 4
            
            if data_in_use[n] == 1:
                x = Normalize_data(var_1[index][i], Maxs[k], Mins[k]) 
                list_in.append(x)
            elif data_in_use[n] == 2 and var_1[index][i] != None:
                av = av + var_1[index][i]
                cont = cont + 1
            n = n + 1 
                
            if data_in_use[n] == 1:
                x = Normalize_data(var_2[index][i], Maxs[k], Mins[k]) 
                list_in.append(x)
            elif data_in_use[n] == 2 and var_2[index][i] != None:
                av = av + var_2[index][i]
                cont = cont + 1
            n = n + 1 
                
            if data_in_use[n] == 1:
                x = Normalize_data(var_3[index][i], Maxs[k], Mins[k]) 
                list_in.append(x)
            elif data_in_use[n] == 2 and var_3[index][i] != None:
                av = av + var_3[index][i]
                cont = cont + 1
            n = n + 1 
                
            if data_in_use[n] == 1:
                x = Normalize_data(var_4[index][i], Maxs[k], Mins[k]) 
                list_in.append(x)
            elif data_in_use[n] == 2 and var_4[index][i] != None:
                av = av + var_4[index][i]
                cont = cont + 1
            n = n + 1 

            if av != 0:
                y = av/cont
                x = Normalize_data(y, Maxs[k], Mins[k])
                list_in.append(x)
            elif av == 0 and ( data_in_use[n-1] == 2 or data_in_use[n-2] == 2 or data_in_use[n-3] == 2 or data_in_use[n-4] == 2):
                list_in.append((None))
            
            k = k + 1    
            
            # humidity 
            av = 0
            cont = 0
            index = 3
            
            if data_in_use[n] == 1:
                x = Normalize_data(var_1[index][i], Maxs[k], Mins[k]) 
                list_in.append(x)
            elif data_in_use[n] == 2 and var_1[index][i] != None:
                av = av + var_1[index][i]
                cont = cont + 1
            n = n + 1 
                
            if data_in_use[n] == 1:
                x = Normalize_data(var_2[index][i], Maxs[k], Mins[k]) 
                list_in.append(x)
            elif data_in_use[n] == 2 and var_2[index][i] != None:
                av = av + var_2[index][i]
                cont = cont + 1
            n = n + 1 
                
            if data_in_use[n] == 1:
                x = Normalize_data(var_3[index][i], Maxs[k], Mins[k]) 
                list_in.append(x)
            elif data_in_use[n] == 2 and var_3[index][i] != None:
                av = av + var_3[index][i]
                cont = cont + 1
            n = n + 1 
                
            if data_in_use[n] == 1:
                x = Normalize_data(var_4[index][i], Maxs[k], Mins[k]) 
                list_in.append(x)
            elif data_in_use[n] == 2 and var_4[index][i] != None:
                av = av + var_4[index][i]
                cont = cont + 1
            n = n + 1 

            if av != 0:
                y = av/cont
                x = Normalize_data(y, Maxs[k], Mins[k])
                list_in.append(x)
            elif av == 0 and ( data_in_use[n-1] == 2 or data_in_use[n-2] == 2 or data_in_use[n-3] == 2 or data_in_use[n-4] == 2):
                list_in.append((None))
            
            k = k + 1
            
            # solar radiation 
            av = 0
            cont = 0
            index = 5
            
            if data_in_use[n] == 1:
                x = Normalize_data(var_1[index][i], Maxs[k], Mins[k]) 
                list_in.append(x)
            elif data_in_use[n] == 2 and var_1[index][i] != None:
                av = av + var_1[index][i]
                cont = cont + 1
            n = n + 1 
                
            if data_in_use[n] == 1:
                x = Normalize_data(var_2[index][i], Maxs[k], Mins[k]) 
                list_in.append(x)
            elif data_in_use[n] == 2 and var_2[index][i] != None:
                av = av + var_2[index][i]
                cont = cont + 1
            n = n + 1 
                
            if data_in_use[n] == 1:
                x = Normalize_data(var_3[index][i], Maxs[k], Mins[k]) 
                list_in.append(x)
            elif data_in_use[n] == 2 and var_3[index][i] != None:
                av = av + var_3[index][i]
                cont = cont + 1
            n = n + 1 
                
            if data_in_use[n] == 1:
                x = Normalize_data(var_4[index][i], Maxs[k], Mins[k]) 
                list_in.append(x)
            elif data_in_use[n] == 2 and var_4[index][i] != None:
                av = av + var_4[index][i]
                cont = cont + 1
            n = n + 1 

            if av != 0:
                y = av/cont
                x = Normalize_data(y, Maxs[k], Mins[k])
                list_in.append(x)
            elif av == 0 and ( data_in_use[n-1] == 2 or data_in_use[n-2] == 2 or data_in_use[n-3] == 2 or data_in_use[n-4] == 2):
                list_in.append((None))
            
            k = k + 1
                
            # pressure 
            av = 0
            cont = 0
            index = 6
            
            if data_in_use[n] == 1:
                x = Normalize_data(var_1[index][i], Maxs[k], Mins[k]) 
                list_in.append(x)
            elif data_in_use[n] == 2 and var_1[index][i] != None:
                av = av + var_1[index][i]
                cont = cont + 1
            n = n + 1 
                
            if data_in_use[n] == 1:
                x = Normalize_data(var_2[index][i], Maxs[k], Mins[k]) 
                list_in.append(x)
            elif data_in_use[n] == 2 and var_2[index][i] != None:
                av = av + var_2[index][i]
                cont = cont + 1
            n = n + 1 
                
            # Var_3 does not exist
                
            if data_in_use[n] == 1:
                x = Normalize_data(var_4[index][i], Maxs[k], Mins[k]) 
                list_in.append(x)
            elif data_in_use[n] == 2 and var_4[index][i] != None:
                av = av + var_4[index][i]
                cont = cont + 1
            n = n + 1 

            if av != 0:
                y = av/cont
                x = Normalize_data(y, Maxs[k], Mins[k])
                list_in.append(x)
            elif av == 0 and ( data_in_use[n-1] == 2 or data_in_use[n-2] == 2 or data_in_use[n-3] == 2):
                list_in.append((None))
            
            k = k + 1
            
            # station 544
            if data_in_use[n] == 1:
                x = Normalize_data(var_5[3][i], Maxs[k], Mins[k])
                list_in.append(x)
            n = n + 1
            
            k = k + 1
                
            # station 546
            if data_in_use[n] == 1:
                x = Normalize_data(var_6[3][i], Maxs[k], Mins[k])
                list_in.append(x)
                
            k = k + 1
            
            var.append(list_in)
            
        for i in range(n_days_delayed,len(var_1[0])):
            
            list_in = []
            
            if data_in_use[0] == 1:
                
                x = Normalize_data(day_i[i], Maxs[0], Mins[0])
                list_in =[x]
            
            for j in range(n_days_delayed,0,-1):
                
                list_in = list_in + var[i-j]
                
            if data_in_use[-1] ==1:
                
                x = Normalize_data(output[4][i-1], Maxs[-1], Mins[-1])
            
                list_in = list_in + [x]
            
            var_final.append(list_in)
            
            out_none = Normalize_data(output[4][i], Maxs[-1], Mins[-1])
            
            out_final.append(out_none)
            
    else:
        
        var_final=None
        
        print('Error vectors not the same size')
        
    return var_final, out_final

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
      
    A = 1 / ( Min_value + Max_value ) 
    B = - Min_value / ( Min_value + Max_value )
        
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
    
def generate_data( n_days_delays, save, data_in_use):
    
    St_544, St_546 = pr.load(open ('Station.p','rb'))
    Met_1, Met_2, Met_3, Met_4, _, _ = pr.load(open("Met.p","rb"))
    _, _, Portodemouros = pr.load(open("Dams.p","rb"))
    
    input_value, output_value = order_inputs( Met_1, Met_2, Met_3, Met_4, St_544, St_546, Portodemouros, n_days_delays, data_in_use )
    
    input_var = np.asarray(input_value).astype(np.float32)
    output_var = np.asarray(output_value).astype(np.float32)
    output_var = output_var.reshape(len(output_var),1)
    
    time_plot = Met_1[0][n_days_delays:]
    
    input_var, output_var, time_plot = clean_nan( input_var, output_var, time_plot )
    
    if save == 1:
    
        name = 'Data_model_1_('+str(n_days_delays)+'_d).p'
        
        pr.dump ( [input_var, output_var, time_plot] , open( name, "wb" ) )
        
    return input_var, output_var, time_plot
