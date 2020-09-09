#This Function serves to create vectors 
# containning information relative to holiday and week day indications

# Input:
# - National holidays
# - Galiza Specific holiday
# - week day info of the first day

import pickle as pr
from datetime import datetime as dt
from Create_time_series import create_time

Time = create_time()

file_national = open('Holiday_Week_Value/National_holiday.txt')
file_galiza = open('Holiday_Week_Value/Galiza_holiday.txt')

Lines_n = file_national.readlines()
Lines_g = file_galiza.readlines()

file_national.close()
file_galiza.close()

#%% Function to create datetime object

def datetime_create( List ):
    
    List_n = []
    
    for i in range(len(List)):
              
        a = []
        b = List[i][0:10]
                
        a = dt.strptime( b, '%d/%m/%Y')
        
        List_n.append(a)
        
    return List_n

#%% This part creates a vector of 1 or 0 considedring if the day was a holiday or not
    
Lines_n = datetime_create( Lines_n )
Lines_g = datetime_create( Lines_g )

National_holiday = []
National_galiza_holiday = []

j=0
k=0

for i in range(len(Time)):
    
    if Time[i] == Lines_n[j]:
        
        j = j + 1
        
        National_holiday.append(1)
        National_galiza_holiday.append(1)
        
    else:
        
        if Time[i] == Lines_g[k]:
        
            k = k + 1
            National_galiza_holiday.append(1)
            National_holiday.append(0)
            
        else:
            
            National_galiza_holiday.append(0)
            National_holiday.append(0)

#%% this part creates two vector with the week day information 
            
# vector 1:
            
# monday - 1 
# tuesday - 2
# wednesday - 3
# thursday - 4
# friday - 5
# saturday - 6
# Sunday - 7 
            
# vector 2:
    
# weekday - 1
# weekend - 0
            
Starting_day = 3 # 1 de janeiro de 2014 wednesday 
Week = []
Week.append(Starting_day)

for i in range(1, len(Time)):
    
    if Week[i-1]==7:
        Week.append(1)
    else: 
        Week.append(Week[i-1]+1)
        
Week_binary = []
            
for i in range(len(Week)):
    
    if Week[i] == 1 or Week[i] == 2 or Week[i] == 3 or Week[i] == 4 or Week[i] == 5 :
        Week_binary.append(1)
    else:
        Week_binary.append(0)
            
Week_Combine = []

for i in range(len(Time)):

    if Week_binary[i] == 1 and National_galiza_holiday[i] == 0:
        
        Week_Combine.append(1)
    else:
        Week_Combine.append(0)

pr.dump( [ National_holiday, National_galiza_holiday, Week, Week_binary, Week_Combine ], open( "Time.p", "wb" ) )
