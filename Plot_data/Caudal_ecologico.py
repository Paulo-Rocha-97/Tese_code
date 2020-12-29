# this functionn plots and calculates the values of the minimum outflow for reach month

import pickle as pr

#%% This function calculates the values of minimum value within each month

def define_minimum(Dam):
    
    Values = []
    
    Time_month = []
    Time_year = []
    
    Past_month = 0
    Past_year = 0
    
    Min_value = 100000000
    
    for i in range(len(Dam[0])):
        
        Current_month = Dam[0][i].month
        Current_year = Dam[0][i].year
        
        if Current_month == Past_month or i == 0:
            
            if Dam[3][i] is not None:
            
                if Min_value > Dam[5][i]:
                
                    Min_value = Dam[5][i]
                
        else:
            
            Values.append(Min_value)
            Time_month.append(Past_month)
            Time_year.append(Past_year)
            
            Min_value = 100000000
            
        if i == (len(Dam[0])-1):
            
            Values.append(Min_value)
            Time_month.append(Current_month)
            Time_year.append(Current_year)
            
        Past_month = Current_month
        Past_year = Current_year
        
    return Values,Time_month,Time_year

#%% This function defines the ref value of caudal ecologico 
    
def complete_for_years( Caudal_ref, n_year ):
    
    Caudal = []
    
    for i in range(n_year):
        
        for j in range(len(Caudal_ref)):
            
            if i < (n_year-1):
            
                Caudal.append(Caudal_ref[j])
                
            elif i == (n_year-1) and j <7 :
                
                Caudal.append(Caudal_ref[j])
                
    return Caudal

#%% Counter the number of years 

def counter_years(Time_year):

    cont = 1
    
    for i in range(1,len(Time_year)):
        
        if Time_year[i] != Time_year[i-1] :
            
            cont = cont+1
        
    return cont
# %% define label for x
    
def month_x_axes (X,Time_year):
    
    
    year_axis = []
    Z=[]
    Q=[]
        
    j=1
    
    for i in range(len(X)):
        if j==1 or j==7:
            
            if j==1:
                
                year_axis.append(Time_year[i])
                Q.append(i)
                    
        if j==12:
            j=1
        else:
            j=j+1
        
        Z.append(i)
    
    return Z,Q,year_axis

#%% define this specific plot

def make_plot( path, Name, Time_month, Time_year, Y_name, Values ):
    
    import os
    import matplotlib.pyplot as plt
    
    Caudal_ref = [15,15,11.9,9.6,8.6,7.9,5,5,5,8.9,11.9,15]

    Z,Q,year_axis = month_x_axes(Values, Time_year)
    
    Y = Y_name.split('(')
    Y_ = Y[0]
    Y_=Y_.replace('/','_')        
    
    name = Name + '_' + Y_.replace(' ','_')

    n_year = counter_years(Time_year)
    
    Caudal = complete_for_years( Caudal_ref, n_year )
        
    fig = plt.figure(figsize=(16,6))
    ax1 = fig.add_subplot(111)
    
    ax1.plot(Z, Values,'r', linewidth=0.75, label = 'Monthly minimum', marker='.')
    ax1.plot(Z, Caudal,'b', linewidth=0.6, label = 'Reference value', marker='.')
        
    ax1.set_xticks(Q)
    ax1.set_xticklabels(year_axis ,rotation=60)
    
    
    ax1.set_xlabel('Year')
    ax1.set_ylabel(Y_name)
    ax1.grid(linewidth=0.5)
    
    plt.legend()

    if not os.path.exists(path):
        os.makedirs(path)

    plt.savefig(path+'/'+name+'.png',dpi=300)
    # plt.close()
    
#%% execute

_,_,Portodemouros = pr.load(open('Dams_full_time_series.p','rb'))

path = 'C:/Users/Paulo_Rocha/Desktop/Tese/Tese_code/Plot_Data/General_plots';

Values, Time_month, Time_year = define_minimum(Portodemouros)
make_plot(path, 'Caudal_ecologico__', Time_month, Time_year, r'Outflow $(m^3/s)$', Values)