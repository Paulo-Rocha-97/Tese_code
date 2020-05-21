#Function

import pickle as pr 
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_pacf 

# %% function to clean the time series 

def clean_None(var):
    
    for i in range(len(var)):
        
        if i == 0 and var[i] == None:
                                
            if var[1] != None:
                
                var[0] = var[1]
                
            else:
                                    
                if var[2] != None:
                    
                    var[1] = var[2] 
                    var[0] = var[1]
                    
                else: 
                    
                    if var[3] != None:
                       
                       var[2] = var[3]
                       var[1] = var[2] 
                       var[0] = var[1]
                
        elif i > 0 and var[i] == None :
                
            ind = 0
            Value = 0
            
            if var[i-1] != None:
                ind = ind+1
                Value = Value + var[i-1] 
            if var[i+1] != None:
                ind = ind+1
                Value = Value + var[i+1]
            if ind == 0:
                var[i] = None
                print(*['Erro! - line ', i ])
            else: 
                var[i] = Value/ind
                    
        elif i == len(var)-1 and var[i] == None:
            
            var[i] = var[i-1]
            
            if var[i] == None:
                
                print(*['Erro! - line ', i ])
                    
    return var

_, _, Portodemouros = pr.load(open("Dams.p","rb"))
    
Inflow = Portodemouros[4] 

Inflow =  np.asarray(Inflow)

Data = clean_None(Inflow)

plot_pacf( Data, lags = 20, )
