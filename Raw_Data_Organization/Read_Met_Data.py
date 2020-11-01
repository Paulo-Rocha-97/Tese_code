# Read Metereologic Data Group it and stores it as a Met.p file

# Met_1 - Arzúa 
# Met_2 - Melide 
# Met_3 - Olveda 
# Met_4 - Serra de Faro
# Met_5 -  Mouriscade 
# Met_6 - Camanzo 

# dir_files - directory where the files are stored 

# Data structure of the list of list 

# Value[0] - Time
# Value[1] - Type [1-0]
# Value[2] - Average Temperature (ºC)
# Value[3] - Average Humidity levels (%)
# Value[4] - Total Precipitation (L/m^2)
# Value[5] - Global solar irradiation (kj/m^2.day)
# Value[6] - Average pression (hPa)

Files_name = ['Met_1_T.csv','Met_1_H.csv','Met_1_C.csv','Met_1_I.csv','Met_1_P.csv',
              'Met_2_T.csv','Met_2_H.csv','Met_2_C.csv','Met_2_I.csv','Met_2_P.csv',
              'Met_3_T.csv','Met_3_H.csv','Met_3_C.csv','Met_3_I.csv',
              'Met_4_T.csv','Met_4_H.csv','Met_4_C.csv','Met_4_I.csv','Met_4_P.csv']

dir_files = 'C:\\Users\\Paulo_Rocha\\Desktop\\Tese\\Tese_code\\Raw_Data_Organization\\Met_data'

# Met_3_P did not exist

import datetime as dt
import pickle as pr

# %% Create Time Series

def create_time (year):

    # Start Information
    month = 1
    day = 1
    
    End_year = 2018
    End_month = 7
    End_day = 16
    
    Time_ = []
    
    Time_.append(dt.datetime(year, month, day))
    
    while ( [year,month,day] != [End_year,End_month,End_day]):

        
        if (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12 ) and day == 30 :
            
            day = 31
            
        elif (month == 4 or month == 6 or month == 9 or month == 11) and day == 30 :
            
            month = month + 1    
            day = 1
            
        elif day == 31 and not month == 12 :
            
            month = month + 1
            day = 1
            
        elif day == 31 and month == 12  :
            
            month = 1 
            year = year + 1
            day = 1
            
        elif month == 2 and ( year!= 2012 or year != 2016 or year != 2012 ) and day == 28:
            
            day = 1
            month = 3
            
        elif month == 2 and ( year!= 2012 or year == 2016 or  year == 2012 ) and day == 28 :
            
            day = 29
            
        elif month == 2 and ( year == 2012 or year == 2016 or  year == 2012 ) and day == 29 :
            
            day = 1 
            month = 3
            
        else:
                
            day = day + 1
                        
        Time_.append(dt.datetime(year, month, day))
                
    return Time_ 

# %% Account for missing data

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

# %% Read single file

def read_csv(dir_files, name_file):
    
    dir_file = dir_files + '\\' + name_file

    Data = list(open(dir_file))
    
    del Data[0]
    
    Time = []
    Value = []
    
    for i in range(len(Data)):
        
        Data[i] = Data[i].split(',',1)
        
        Temp_value = Data[i][1].replace ('\n','')
        Temp_value = Temp_value.replace ('"','')
        Temp_value = Temp_value.replace (';','')
        
        if float(Temp_value) == -9999:
            Value.append( None )
        else:
            Value.append( float(Temp_value) )
        
        Temp_time = Data[i][0].replace ('"','')
        Temp_time = Temp_time.split('-')

        Time.append( dt.datetime(int(Temp_time[0]), int(Temp_time[1]), int(Temp_time[2][0:2])) )
                    
    Data_final = [Time, Value]

    return Data_final

# %% Compile multiple CSV file

def Compile_multiple_CSV ( Num_of_var, Files_name, dir_files):
    
    Num_data = [5, 5, 4, 5, 5, 5]
    
    Index_file_name = [0, 5, 10, 14, 19, 24 ]

    range_read = Num_data[Num_of_var-1] 
    
    Time_ref = create_time(2014)
    
    Comp = len(Time_ref)
    
    Type = [0]*Comp 
    
    Data_final = [Time_ref, Type]

    for i in range( 0,  range_read ):
        
        index = Index_file_name[Num_of_var - 1] + i
                
        name_file = Files_name[ index ] 
        
        A = read_csv(dir_files, name_file)
        
        A = account_missing_data_s (A)
        
        Data_final.append( A[1] )
        
    if range_read == 4:
        
        None_vec = [None]*Comp
        
        Data_final.append (None_vec)
        
    for i in range( 0, Comp):
        
        Type_none = []
        
        for j in range(2,  7):
            
            Type_none.append( Data_final[j][i] )
            
        number_of_none = Type_none.count(None)
        
        Data_final[1][i] = 1 - number_of_none/5  
            
    return Data_final

# %% Execute Code
    
Met_1 = Compile_multiple_CSV( 1, Files_name, dir_files)

print( 'Met_1 is complete!' )

Met_2 = Compile_multiple_CSV( 2, Files_name, dir_files)

print( 'Met_2 is complete!' )

Met_3 = Compile_multiple_CSV( 3, Files_name, dir_files)

print( 'Met_3 is complete!' )

Met_4 = Compile_multiple_CSV( 4, Files_name, dir_files)

print( 'Met_4 is complete!' )

pr.dump( [ Met_1, Met_2, Met_3, Met_4], open( "Met.p", "wb" ) )
