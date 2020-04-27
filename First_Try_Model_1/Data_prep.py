# Define inputs and outpus 

import pickle as pr
import numpy as np
import math as mt

St_544, St_546 = pr.load(open ('Station.p','rb'))
Met_1, Met_2, Met_3, Met_4, _, _ = pr.load(open("Met.p","rb"))
_, _, Portodemouros = pr.load(open("Dams.p","rb"))

# %% Function to average 

def average( var_1, *args ):
      
    args_=list(args)
    
    if len(args_) == 1 :
        
        ind = 0
        Value = 0
        var_2 = args_[0]
        
        if var_1 != None:
            ind = ind+1
            Value = Value + var_1 
        if var_2 != None:
            ind = ind+1
            Value = Value + var_2 
        if ind == 0:
            var_final = None            
        else: 
            var_final = Value/ind

    elif len(args_) == 2 :
        
        ind = 0
        Value = 0
        var_2 = args_[0] 
        var_3 = args_[1] 
        
        if var_1 != None:
            ind = ind+1
            Value = Value + var_1 
        if var_2 != None:
            ind = ind+1
            Value = Value + var_2 
        if var_3 != None:
            ind = ind+1
            Value = Value + var_3 
        if ind == 0:
            var_final = None            
        else: 
            var_final = Value/ind
            
    elif len(args_) == 3 :
        
        ind = 0
        Value = 0
        var_2 = args_[0] 
        var_3 = args_[1] 
        var_4 = args_[2] 
        
        if var_1 != None:
            ind = ind+1
            Value = Value + var_1 
        if var_2 != None:
            ind = ind+1
            Value = Value + var_2 
        if var_3 != None:
            ind = ind+1
            Value = Value + var_3 
        if var_4 != None:
            ind = ind+1
            Value = Value + var_4 
        if ind == 0:
            var_final = None            
        else: 
            var_final = Value/ind
        
    return var_final

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

# %% Function to organize into 

def order_inputs( var_1, var_2, var_3, var_4 , var_5, var_6, output):
    
    var_final=[]
    var=[]
    out_final = []
    
    if len(var_1[0]) == len(var_2[0]) and len(var_1[0]) == len(var_3[0]) and len(var_1[0]) == len(var_4[0]):  
        
        day_i = day_index()
        
        for i in range(len(var_1[0])):
            
            list_in=[]
             
            # temperature 
            list_in.append(var_1[2][i])
            list_in.append(var_2[2][i])
            list_in.append(var_3[2][i])
            list_in.append(var_4[2][i])
            
            
            # precipitation 
            Precip123 = average(var_1[4][i],var_2[4][i],var_3[4][i])
            list_in.append(Precip123)
            
            list_in.append(var_4[4][i])
            
            # humidity 
            Hum12 = average(var_1[3][i],var_2[3][i])
            list_in.append(Hum12)
            
            list_in.append(var_3[3][i])
            list_in.append(var_4[3][i])
            
            # solar radiation 
            SolarR = average(var_1[5][i], var_2[5][i], var_3[5][i], var_4[5][i])
            list_in.append(SolarR)
            
            # pressure 
            Press = average(var_1[6][i], var_2[6][i], var_3[6][i], var_4[6][i]) 
            list_in.append(Press)
            
            # station 544
            list_in.append(var_5[3][i])
            
            # station 546
            list_in.append(var_6[3][i])
            
            var.append(list_in)
            
        for i in range(3,1657):
            
            list_in = []
            
            list_in =[day_i[i]] + var[i-3] + var[i-2] + var[i-1] + var[i]
            
            var_final.append(list_in)
            
            out_none = output[4][i]
            
            out_final.append(out_none)
            
    else:
        
        var_final=None
        
        print('Error vectors not the same size')
        
    return var_final, out_final

# %% Execute
    
input_value, output_value = order_inputs( Met_1, Met_2, Met_3, Met_4, St_544, St_546, Portodemouros)

input_var = np.asarray(input_value).astype(np.float32)
output_var = np.asarray(output_value).astype(np.float32)

# %% Function to eliminate none
# This function will either use the closest value or do an average of the value arround

def clean_None(var):
    
    if len(var.shape) == 1:
    
        for i in range(len(var)):
            
            if i == 0 and mt.isnan(var[i]):
                                    
                if mt.isnan(var[1]):
                                        
                    if mt.isnan(var[2]):
                        
                        if mt.isnan(var[3]):
                           
                           var[2] = var[3] 
        
                        var[1] = var[2] 
                    
                    var[0] = var[1]
                    
            elif i > 0 and mt.isnan(var[i]) :
                    
                ind = 0
                Value = 0
                
                if not mt.isnan(var[i-1]):
                    ind = ind+1
                    Value = Value + var[i-1] 
                if not mt.isnan(var[i+1]):
                    ind = ind+1
                    Value = Value + var[i+1]
                if ind == 0:
                    var[i] = None
                    print(*['Erro! - line ', i ])
                else: 
                    var[i] = Value/ind
                        
            elif i == len(var)-1 and mt.isnan(var[i]):
                
                var[i] = var[i-1]
                
                if mt.isnan(var[i]):
                    
                    print(*['Erro! - line ', i ])
                    
    elif len(var.shape) == 2:
        
        index = var.shape
        
        for j in range(index[1]):
            
            for i in range(len(var)):
                
                if i == 0 and mt.isnan(var[i,j]) :
                    
                    if not mt.isnan(var[4,j]) and mt.isnan(var[3,j]) and mt.isnan(var[2,j]) and mt.isnan(var[1,j]):
                               
                        var[3,j] = var[4,j]
                        
                        var[2,j] = var[3,j] 
            
                        var[1,j] = var[2,j] 
                        
                        var[0,j] = var[1,j]
                    
                    if not mt.isnan(var[3,j]) and mt.isnan(var[2,j]) and mt.isnan(var[1,j]):
                               
                        var[2,j] = var[3,j] 
            
                        var[1,j] = var[2,j] 
                        
                        var[0,j] = var[1,j]
                                            
                    if not mt.isnan(var[2,j]) and mt.isnan(var[1,j]):
                        
                        var[1,j] = var[2,j] 
                        
                        var[0,j] = var[1,j]       
                        
                    if not mt.isnan(var[1,j]):
                        
                        var[0,j] = var[1,j]
                        
                elif i > 0 and mt.isnan(var[i,j]) :
                        
                    ind = 0
                    Value = 0
                    
                    if not mt.isnan(var[i-1,j]):
                        ind = ind+1
                        Value = Value + var[i-1,j] 
                    if not mt.isnan(var[i+1,j]):
                        ind = ind+1
                        Value = Value + var[i+1,j]
                    if ind == 0:
                        var[i,j] = None
                        print(*['Erro! - line ', i , j])
                    else: 
                        var[i,j] = Value/ind
                            
                elif i == len(var)-1 and mt.isnan(var[i,j]):
                    
                    var[i,j] = var[i-1,j]
                    
                    if mt.isnan(var[i,j]):
                        
                        print(*['Erro! - line ', i, j ])
    
    return var

# %% Save the Final data 
    
input_var = clean_None(input_var)

output_var = clean_None(output_var)

pr.dump ( [input_var, output_var] , open( "Data_model_1.p", "wb" ) )