# This function reads the data and plots it 

import pandas as pd 
import pickle as pr
from Create_time_series import create_time

# %% Ler dados das Barragens

Touro = pd.read_excel('Flow_Data\Datos_Diarios_TOURO.xlsx',index_col=0)
Portodemouros = pd.read_excel('Flow_Data\Datos_Diarios_PORTODEMOUROS.xlsx',index_col=0)
Brandariz = pd.read_excel('Flow_Data\Datos_Diarios_BRANDARIZ.xlsx',index_col=0)

# %% Eliminate unwanted information

Index_to_remove = [5]

Touro = Touro.drop(Touro.columns[Index_to_remove],axis=1)
Brandariz = Brandariz.drop(Brandariz.columns[Index_to_remove],axis=1)
Portodemouros = Portodemouros.drop(Portodemouros.columns[Index_to_remove],axis=1)

Touro = Touro.values.tolist()
Brandariz = Brandariz.values.tolist()
Portodemouros = Portodemouros.values.tolist()

# %% Function to switch columns and rows

def switch_rows(List_of_list):
    
    comp = len(List_of_list)

    Time = []
    Type = [0]*comp
    Volume = []
    Heigth = []
    Inflow = []
    Output = []
    Bottom = []
    Flood = []
    Power = []
    
    for i in range(comp):
    
        Time.append( List_of_list[i][0] )
        Heigth.append( List_of_list[i][1] )
        Volume.append( List_of_list[i][2] )
        Inflow.append( List_of_list[i][3] )
        Output.append( List_of_list[i][4] )
        Bottom.append( List_of_list[i][5] )
        Flood.append( List_of_list[i][6] )
        Power.append( List_of_list[i][7] )
    
    Switched = [Time, Type, Heigth, Volume, Inflow, Output, Bottom, Flood, Power]
    
    return Switched

# %% Switch tables
    
Touro = switch_rows(Touro)
Brandariz = switch_rows(Brandariz)
Portodemouros = switch_rows(Portodemouros)

# %% Fucntion to cut previous than 2014

def clean_Dam (value):

    comp = len(value[0])

    for i in range((comp-1),-1,-1):

            Time = value[0][i]
            Time.to_pydatetime()
            Ano = Time.year

            if  Ano < 2014:

               del value[0][i]
               del value[1][i]
               del value[2][i]
               del value[3][i]
               del value[4][i]
               del value[5][i]
               del value[6][i]
               del value[7][i]
               del value[8][i]

    return value

# %% Execute clean

Touro = clean_Dam(Touro)
Brandariz = clean_Dam(Brandariz)
Portodemouros = clean_Dam(Portodemouros)

# %% Clear outlier 

comp =len(Brandariz[1])

for i in range(comp-1,-1,-1):

    if Brandariz[2][i] == 0 : 
    
        del Brandariz[0][i]
        del Brandariz[1][i]
        del Brandariz[2][i]
        del Brandariz[3][i]
        del Brandariz[4][i]
        del Brandariz[5][i]
        del Brandariz[6][i]
        del Brandariz[7][i]
        del Brandariz[8][i]
        
    if Brandariz[3][i] == 0 : 
    
        del Brandariz[0][i]
        del Brandariz[1][i]
        del Brandariz[2][i]
        del Brandariz[3][i]
        del Brandariz[4][i]
        del Brandariz[5][i]
        del Brandariz[6][i]
        del Brandariz[7][i]
        del Brandariz[8][i]
        
comp =len(Touro[1])

for i in range(comp-1,-1,-1):

    if Touro[2][i] > 154 : 
    
        del Touro[0][i]
        del Touro[1][i]
        del Touro[2][i]
        del Touro[3][i]
        del Touro[4][i]
        del Touro[5][i]
        del Touro[6][i]
        del Touro[7][i]
        del Touro[8][i]


# %% Complete the full time series
        
Time_ref = create_time()

def account_missing_data (Data,Time_ref):
        
    comp = len(Time_ref)
    
    Type = [0]*comp
    Height = [None]*comp  
    Volume = [None]*comp  
    Inflow = [None]*comp
    Output = [None]*comp  
    Bottom = [None]*comp  
    Flood = [None]*comp  
    Power = [None]*comp
    
    for i in range (0,comp,1):

        for l in range (0,len(Data[1]),1):
            
            t=Data[0][l]
            
            t.to_pydatetime()
                       
            if Time_ref[i] == t:
                
                Type[i] = 1
                Height[i] = Data[2][l]
                Volume[i] = Data[3][l]
                Inflow[i] = Data[4][l]
                Output[i] = Data[5][l]
                Bottom[i] = Data[6][l]
                Flood[i] = Data[7][l]
                Power[i] = Data[8][l]
                
    Result = [Time_ref, Type, Height, Volume, Inflow,  Output, Bottom, Flood, Power]
        
    return Result

Touro = account_missing_data(Touro, Time_ref)

Brandariz = account_missing_data(Brandariz, Time_ref)

Portodemouros = account_missing_data(Portodemouros,Time_ref)


# %% Save Data 

pr.dump( [ Touro , Brandariz , Portodemouros ], open( "Dams.p", "wb" ) )

