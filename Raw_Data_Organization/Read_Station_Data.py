# this fucntion reads and organises

import pickle as pr
from Create_time_series import create_time
import datetime as dt

# %% Complete the full time series 

def account_missing_data_s (Data):
    
    Time_ref = create_time(2014)
        
    comp = len(Time_ref)
        
    Variable = [None]*comp
        
    for i in range (0,comp,1):

        for l in range (0,len(Data[0]),1):
            
            t=Data[0][l]
                       
            if Time_ref[i] == t:
                
                Variable[i] = Data[1][l]

    Result = [Time_ref, Variable ]
        
    return Result

# %% Read data from Stations

def read_and_cut(name_file,cut_year):

    dir_file='Flow_Data/'+ name_file
    
    F = open(dir_file,'r')
        
    Data = list(F)
    
    Time_ref = []
    Time_ref_2 = []
    Heigth = []
    Output = []
    T1=[]
    T2=[]
    
    del Data[0:27]
    
    for i in range(0,len(Data)-1):
        
        line = Data[i]
                
        Line_distinct = line.split()
        
        if Line_distinct[2] == 'Nivel':

            Day,Month,Year = Line_distinct[1].split('/')
        
            Time_ref.append(dt.datetime(int(Year),int(Month),int(Day)))
        
            if Line_distinct[0] != '1':
            
                Heigth.append(None)
                T1.append(0)
            else:
            
                Heigth.append(float(Line_distinct[7].replace(',','.')))
                T1.append(1)
        else:
            
            Day,Month,Year = Line_distinct[1].split('/')
        
            Time_ref_2.append(dt.datetime(int(Year),int(Month),int(Day)))
            
            if Line_distinct[0] != '1':
            
                Output.append(None)
                T2.append(0)
            else:
            
                Output.append(float(Line_distinct[7].replace(',','.')))
                T2.append(1)
                
    Data_1 = [Time_ref,Heigth]
    Data_2 = [Time_ref_2,Output]

    comp = len(Data_1[0])

    for i in range((comp-1),-1,-1):

        Time = Data_1[0][i]
        Ano = Time.year

        if  Ano < cut_year:

           del Data_1[0][i]
           del Data_1[1][i]

    comp = len(Data_2[0])

    for i in range((comp-1),-1,-1):

        Time = Data_2[0][i]
        Ano = Time.year

        if  Ano < cut_year:

           del Data_2[0][i]
           del Data_2[1][i]
           
    Data_1 = account_missing_data_s (Data_1)
    Data_2 = account_missing_data_s (Data_2)
    
    Time_ref = create_time(cut_year)
    
    comp=len(Time_ref)
    
    Type = [2] * comp
    Var_1 = [None]*comp
    Var_2 = [None]*comp    
        
    for i in range (comp):
        
        if Data_1[1][i] is None and Data_2[1][i] is None:

            Type[i] = 0
            
        elif Data_1[1][i] is not None and Data_2[1][i] is not None:
            
            Type[i] = 1
        
        if  Data_1[1][i] is not None:
            Var_1[i] = Data_1[1][i]
                        
        if Data_2[1][i] is not None:
            Var_2[i] = Data_2[1][i]
        
    Data_ = [Time_ref,Type,Var_1,Var_2]
    
    return Data_

# %% Execute

cut_year = 2014

St_544 = read_and_cut('544_data_caudal.txt',cut_year)
St_546 = read_and_cut('546_data_caudal.txt',cut_year)

pr.dump( [St_544, St_546], open( "Station.p", "wb" ) )
