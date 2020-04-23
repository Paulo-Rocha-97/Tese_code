# This function simply creates the full time series to understand the missing data 

import datetime as dt

def create_time ():

    # Start Information
    year = 2014
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
            
        elif month == 2 and ( year != 2016 or year != 2012 ) and day == 28:
            
            day = 1
            month = 3
            
        elif month == 2 and ( year == 2016 or  year == 2012 ) and day == 28 :
            
            day = 29
            
        elif month == 2 and ( year == 2016 or  year == 2012 ) and day == 29 :
            
            day = 1 
            month = 3
            
        else:
                
            day = day + 1
                        
        Time_.append(dt.datetime(year, month, day))
                
    return Time_ 


