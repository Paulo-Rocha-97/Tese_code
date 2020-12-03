#this function compares the outflow of an upstream dam to the input at the dam reservoir 

import pickle as pr
import numpy as np
from My_plot_ import make_plot_line as make_plot_line

Touro, Brandariz, Portodemouros = pr.load(open("Dams.p","rb"))

dir_plots = 'C:/Users/Paulo_Rocha/Desktop/Tese/Tese_code/Plot_Data/General_plots';

# %% Plot compare between PortodeMouros e Brandariz e Touro

make_plot_line( dir_plots, 'Portodemouros vs Brandariz flow data', Portodemouros[0], 'Flow', Portodemouros[5], 'Outflow Portodemouros', Brandariz[4], 'Inflow Brandariz' )

make_plot_line( dir_plots, 'Brandariz vs Touro flow data', Portodemouros[0], 'Flow', Brandariz[5], 'Outflow Brandariz', Touro[4], 'Inflow Touro' )


# %% Necessary function to compare entrada e saida

def calculate_correlation( Var_1, Var_2 ):
        
    Mean_1, St_dev_1 = MEAN_STDEV(Var_1)
    Mean_2, St_dev_2 = MEAN_STDEV(Var_2)
    
    Cov = np.cov(Var_1,Var_2)
        
    r = Cov[0][1] /  (St_dev_1 * St_dev_2)
    
    return r  

def MEAN_STDEV( Y_values ):
    
    SUM = 0
    
    for i in range (len(Y_values)):
                    
        SUM = SUM + Y_values[i]
            
        Mean = SUM / (len(Y_values))
    
    VAR = 0
    
    for i in range (len(Y_values)):
                    
        VAR = VAR + ( Y_values[i] - Mean ) * ( Y_values[i] - Mean )
    
        St_dev = np.sqrt( VAR / ( len(Y_values) ) )
    
    return Mean, St_dev

def clean_var (var_1,var_2):
    
    for i in range (len(var_1)-1,-1,-1):
        
        if var_1[i] is None or var_2[i] is None:
            
            del var_2[i]
            del var_1[i]
    
    var_1 = np.array(var_1)
    var_2 = np.array(var_2)
    
    return var_1,var_2

# %% Implementation of comparison
    
Dam_1_1, Dam_2_1 = clean_var( Portodemouros[5], Brandariz[4])

Dam_2_2, Dam_3_2 = clean_var(Brandariz[5], Touro[4]) 
    
r_1 = calculate_correlation( Dam_1_1, Dam_2_1 )
MAE_1 = np.mean(abs(Dam_1_1 - Dam_2_1))
RMSE_1  =  np.sqrt(((Dam_1_1 -  Dam_2_1) ** 2).mean())

print('\n First Dam Comparison: \n - r= %2f\n - MAE= %2f\n - RMSE= %2f' %(r_1,MAE_1,RMSE_1))

r_2 = calculate_correlation( Dam_2_2, Dam_3_2 )
MAE_2 = np.mean(abs(Dam_2_2 - Dam_3_2))
RMSE_2  =  np.sqrt(((Dam_2_2 -  Dam_3_2) ** 2).mean())

print('\n Second Dam Comparison: \n - r= %2f\n - MAE= %2f\n - RMSE= %2f'%(r_2,MAE_2,RMSE_2))

