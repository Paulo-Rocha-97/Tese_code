# Define inputs and outpus 

import pickle as pr
import numpy as np 
from scipy.io import savemat
from math import nan

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

def order_inputs( var_1, var_2, var_3, var_4 , var_5, var_6, output, data_in_use ):
    
    n_days_delayed = 1
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

# %% Function to simplify function 
    
def Normalize_data (x,Max,Min):
    
    return x

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
    
data_in_use = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,1,1,1]

St_544, St_546 = pr.load(open ('Station.p','rb'))
Met_1, Met_2, Met_3, Met_4,_,_ = pr.load(open('Met.p','rb'))
_, _, Portodemouros = pr.load(open("Dams.p","rb"))

input_value, output_value = order_inputs( Met_1, Met_2, Met_3, Met_4, St_544, St_546, Portodemouros, data_in_use )

input_var = np.asarray(input_value).astype(float)
output_var = np.asarray(output_value).astype(float)

input_var = tranform_none(input_var,'in')
output_var = tranform_none(output_var,'out')

model_1_data  = {'u': input_var,
                 'y':output_var}

savemat("model_1_data.mat", model_1_data)
 
