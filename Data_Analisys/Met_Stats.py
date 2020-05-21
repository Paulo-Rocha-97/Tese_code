""" 
This function analises the metereological data of 6 stations arround the hydrographic basin
"""

from scipy import stats as st
import pickle as pr
import pandas as pd
import numpy as np

# Import data

Met_1, Met_2, Met_3, Met_4, Met_5, Met_6 = pr.load(open("Met.p","rb"))

# Data structure of the data 

# Value[0] - Time
# Value[1] - Type [1-0]
# Value[2] - Average Temperature (ºC)
# Value[3] - Average Humidity levels (%)
# Value[4] - Total Precipitation (L/m^2)
# Value[5] - Global solar irradiation (kj/m^2.day)
# Value[6] - Average pression (hPa)    

# List of the metereological Station

# Met_1 - Arzúa 
# Met_2 - Melide 
# Met_3 - Olveda 
# Met_4 - Serra de Faro
# Met_5 -  Mouriscade 
# Met_6 - Camanzo 

# %% Function to eliminate none type

def eliminate_none( Var_1, Var_2 ):
    
    V_1 = Var_1.copy()
    V_2 = Var_2.copy()
    
    for i in range(len(V_1)-1,-1,-1):
    
        if V_1[i] == None or V_2[i] == None:
            
            del V_1[i]
            del V_2[i]
            
    return V_1,V_2

# %% Function to seperate information in Year or month 

def time_separation_year( Value, Num_of_var, calculation ):

    counter = [0]
        
    comp = len(Value[0])
    
    Time_vec=[]
    Y_vec=[]
    Y_vec_s=[]
    
    for i in range(comp):
        
        Time_element = Value[0][i]
        
        Ano = int(Time_element.year)
        
        if i == 0:
            Ano_at = Ano
        else:
            if Ano_at != Ano:
    
                counter.append(i)
                                
                Y_values = Value[Num_of_var][counter[-2]:counter[-1]]
                
                X1, X2 = calculation(Y_values)
                    
                Time_vec.append(Ano_at)
                    
                Y_vec.append(X1)
                Y_vec_s.append(X2)
    
                Ano_at = Ano
                    
    Y_values = Value[Num_of_var][counter[-1]:]
    
    X1, X2 = calculation(Y_values)

    Time_vec.append(Ano_at)
        
    Y_vec.append(X1)
    Y_vec_s.append(X2)
    
    Ano_at = Ano

    return Time_vec, Y_vec, Y_vec_s

# %% Function Mean and Standart Deviation 
    
def MEAN_STDEV(Y_values):
    
    SUM = 0
    
    for i in range (len(Y_values)):
        
        if Y_values[i] != None:
            
            SUM = SUM + Y_values[i]
    
    if len(Y_values) == Y_values.count(None):

        Mean = 0
        
    else:
                
        Mean = SUM / (len(Y_values) - Y_values.count(None))
    
    VAR = 0
    
    for i in range (len(Y_values)):
        
        if Y_values[i] != None:
            
            VAR = VAR + ( Y_values[i] - Mean ) * ( Y_values[i] - Mean )
            
    
    if len(Y_values) == Y_values.count(None):

        St_dev = 0
        
    else:    
        
        St_dev = np.sqrt( VAR / ( len(Y_values) - Y_values.count(None) - 1 ) )
    
    return Mean, St_dev
  
# %% Function to cycle to names computing mean and standart_deviation
    
def mean_st_dev(Num_of_var, Calc_1):
    
    Time_vec, Y_vec_1, Y_vec_1_s = time_separation_year( Met_1, Num_of_var, Calc_1 )
    _, Y_vec_2, Y_vec_2_s = time_separation_year( Met_2, Num_of_var, Calc_1 )
    _, Y_vec_3, Y_vec_3_s = time_separation_year( Met_3, Num_of_var, Calc_1 )
    _, Y_vec_4, Y_vec_4_s = time_separation_year( Met_4, Num_of_var, Calc_1 )
    _, Y_vec_5, Y_vec_5_s = time_separation_year( Met_5, Num_of_var, Calc_1 )
    _, Y_vec_6, Y_vec_6_s = time_separation_year( Met_6, Num_of_var, Calc_1 )


    df = pd.DataFrame(list(zip(Time_vec,Y_vec_1,Y_vec_1_s,Y_vec_2,Y_vec_2_s,Y_vec_3,Y_vec_3_s,Y_vec_4,Y_vec_4_s,Y_vec_5,Y_vec_5_s
                               ,Y_vec_6,Y_vec_6_s,)),columns =['Year', 'Mean - Met_1','St_dev_Met_1','Mean - Met_2','St_dev_Met_2',
                                                               'Mean - Met_3','St_dev_Met_3','Mean - Met_4','St_dev_Met_4',
                                                               'Mean - Met_5','St_dev_Met_5','Mean - Met_6','St_dev_Met_6']) 
    
    return df

# %% Function to calculate r 
 
def calculate_corelation(Var_1,Var_2):
    
    Mean_1, St_dev_1 = MEAN_STDEV(Var_1)
    Mean_2, St_dev_2 = MEAN_STDEV(Var_2)
    
    Cov = np.cov(Var_1,Var_2)
    
    r = Cov[0][1] /  (St_dev_1 * St_dev_2)
    
    return r   

# %% Execute 

Temp_stats = mean_st_dev( 2, MEAN_STDEV )
Humidity_stats = mean_st_dev( 3, MEAN_STDEV )
Precipitation_stats = mean_st_dev( 4, MEAN_STDEV )
Solar_radiation = mean_st_dev( 5, MEAN_STDEV )
Pressure_stats = mean_st_dev( 6, MEAN_STDEV )

# %% Function for Paired t-test

def Paired_t_test_r( Var, Ident, DF_mean, DF_st, DF_t, DF_p, DF_r):
    
    List_mean = []
    List_st_dev = []
    List_t = []
    List_p = []
    List_r = []
    Var_1 = []
    Var_2 = []
    
    for i in range(6):
    
        Vec_mean = []
        Vec_st_dev = []
        Vec_t = []
        Vec_p = []
        Vec_r = []
        
        for j in range(6):
            
            if i == j :
                
                Vec_mean.append(0)
                Vec_st_dev.append(0)
                Vec_t.append(None)
                Vec_p.append(None)
                Vec_r.append(1)
                
            else:
                
                Dif=[]
                
                for k in range(len(Var[0])):
                    
                    if Var[i][k] != None and Var[j][k] != None:
                    
                        Dif.append(Var[i][k] - Var[j][k])             
                                
                Mean, St_dev = MEAN_STDEV(Dif)
                
                del Var_1
                del Var_2
                              
                Var_1, Var_2 = eliminate_none( Var[i], Var[j])
                                
                r = calculate_corelation(Var_1,Var_2)
                
                t, p = st.ttest_ind(Var_1,Var_2)
                
                Vec_mean.append(Mean)
                Vec_st_dev.append(St_dev)
                Vec_t.append(t)
                Vec_p.append(p)
                Vec_r.append(r)
                
        List_mean.append(Vec_mean)
        List_st_dev.append(Vec_st_dev)
        List_t.append(Vec_t)
        List_p.append(Vec_p)
        List_r.append(Vec_r)
        
        DF_mean[Ident] = pd.DataFrame.from_records(List_mean)
        DF_st[Ident] = pd.DataFrame.from_records(List_st_dev)
        DF_t[Ident] = pd.DataFrame.from_records(List_t)
        DF_p[Ident] = pd.DataFrame.from_records(List_p)
        DF_r[Ident] = pd.DataFrame.from_records(List_r)
    
    return DF_mean, DF_st, DF_t, DF_p, DF_r

# %% Function to split the necessary data for paired T-test

def Split_paired_t_test_and_r( Num_of_var ):
    
    counter = [0]
    comp = len(Met_1[0])
    
    DF_mean = {}
    DF_st = {}
    DF_t = {}
    DF_p = {}
    DF_r = {}
    Final = {}  
    
    for i in range(comp):
        
        Time_element = Met_1[0][i]
        
        Ano = int(Time_element.year)
        
        if i == 0:
            Ano_at = Ano
        else:
            if Ano_at != Ano:
    
                counter.append(i)
                                
                Y_values_1 = Met_1[Num_of_var][counter[-2]:counter[-1]]
                Y_values_2 = Met_2[Num_of_var][counter[-2]:counter[-1]]
                Y_values_3 = Met_3[Num_of_var][counter[-2]:counter[-1]]
                Y_values_4 = Met_4[Num_of_var][counter[-2]:counter[-1]]
                Y_values_5 = Met_5[Num_of_var][counter[-2]:counter[-1]]
                Y_values_6 = Met_6[Num_of_var][counter[-2]:counter[-1]]
                
                Y_val = [Y_values_1,Y_values_2,Y_values_3,Y_values_4,Y_values_5,Y_values_6]
                
                DF_mean, DF_st, DF_t, DF_p, DF_r= Paired_t_test_r(Y_val, Ano_at, DF_mean, DF_st, DF_t, DF_p, DF_r) 
                    
                Ano_at = Ano
                    
    Y_values_1 = Met_1[Num_of_var][counter[-1]:]
    Y_values_2 = Met_2[Num_of_var][counter[-1]:]
    Y_values_3 = Met_3[Num_of_var][counter[-1]:]
    Y_values_4 = Met_4[Num_of_var][counter[-1]:]
    Y_values_5 = Met_3[Num_of_var][counter[-1]:]
    Y_values_6 = Met_4[Num_of_var][counter[-1]:]
    
    Y_val = [Y_values_1,Y_values_2,Y_values_3,Y_values_4,Y_values_5,Y_values_6]
                
    DF_mean, DF_st, DF_t, DF_p, DF_r = Paired_t_test_r(Y_val, Ano_at, DF_mean, DF_st, DF_t, DF_p, DF_r) 
                    
    Ano_at = Ano 
    
    Final['Difference Mean'] = DF_mean
    Final['Difference Standart Deviation'] = DF_st
    Final['Difference t value'] = DF_t
    Final['Difference p value'] = DF_p
    
    return Final, DF_r

# %% Execute 
    
Temp_t_test, Temp_r = Split_paired_t_test_and_r(2)
Hum_t_test, Hum_r = Split_paired_t_test_and_r(3)
Precip_t_test, Precip_r = Split_paired_t_test_and_r(4)
Solar_t_test, Solar_r  = Split_paired_t_test_and_r(5)
Pressure_t_test, Preassure_r = Split_paired_t_test_and_r(6)                  