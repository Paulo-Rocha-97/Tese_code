# This function plots the station Data

import pickle as pr
from My_plot_ import make_plot_line as make_plot

# %% Set plot of yearly data

def split_plot_yearly( Name_element, Value, Type_of_data, dir_ ):
        
    counter = [0]
    
    comp = len(Value[0])
    
    for i in range(comp-1):
        
        Time_element = Value[0][i]
        Ano = int(Time_element.year)
        
        if i == 0:
            Ano_at = Ano
        else:
            if Ano_at != Ano:
                if Type_of_data == 'D':

                    counter.append(i)

                    dir_plots = dir_ +'/' +str(Ano_at) 
                    Name = Name_element

                    Time = Value[0][counter[-2]:counter[-1]]
                    
                    Y = Value[1][counter[-2]:counter[-1]]
                    Y_name = 'Type'
                    make_plot( dir_plots, Name, Time, Y_name, Y )
                    Y = Value[2][counter[-2]:counter[-1]]
                    Y_name = 'Heigth (m)'
                    make_plot( dir_plots, Name, Time, Y_name, Y )
                    Y = Value[3][counter[-2]:counter[-1]]
                    Y_name = 'Volume (Hm^3)'
                    make_plot( dir_plots, Name, Time, Y_name, Y )
                    Y = Value[4][counter[-2]:counter[-1]]
                    Y_name = 'InFlow (m^3/s)'
                    make_plot( dir_plots, Name, Time, Y_name, Y )
                    Y = Value[5][counter[-2]:counter[-1]]
                    Y_name = 'OutFlow (m^3/s)'
                    make_plot( dir_plots, Name, Time, Y_name, Y )
                    Y_1 = Value[6][counter[-2]:counter[-1]]
                    name_1 = 'Bottom'
                    Y_2 = Value[7][counter[-2]:counter[-1]]
                    name_2 = 'Flood'
                    Y_3 = Value[8][counter[-2]:counter[-1]]
                    name_3 = 'Power'
                    make_plot( dir_plots, Name, Time, Y_name, Y_1, name_1, Y_2, name_2, Y_3, name_3)

                    Ano_at = Ano

                elif Type_of_data == 'S':

                    counter.append(i)
                    dir_plots = dir_ +'/' +str(Ano_at) 
                    Name = Name_element

                    Time = Value[0][counter[-2]:counter[-1]]
                    Y = Value[1][counter[-2]:counter[-1]]
                    Y_name = 'Type'
                    make_plot( dir_plots, Name, Time, Y_name, Y )
                    Y = Value[2][counter[-2]:counter[-1]]
                    Y_name = 'Heigth (m)'
                    make_plot( dir_plots, Name, Time, Y_name, Y )
                    Y = Value[3][counter[-2]:counter[-1]]
                    Y_name = 'OutFlow (m^3/s)'
                    make_plot( dir_plots, Name, Time, Y_name, Y )
                    
                    Ano_at = Ano
                    

    if Type_of_data == 'D':

        dir_plots = dir_ +'/' +str(Ano)       

        Time = Value[0][counter[-1]:]

        Y = Value[1][counter[-1]:]
        Y_name = 'Type'
        make_plot( dir_plots, Name, Time, Y_name, Y )
        Y = Value[2][counter[-1]:]
        Y_name = 'Heigth (m)'
        make_plot( dir_plots, Name, Time, Y_name, Y )
        Y = Value[3][counter[-1]:]
        Y_name = 'Volume (Hm^3)'
        make_plot( dir_plots, Name, Time, Y_name, Y )
        Y = Value[4][counter[-1]:]
        Y_name = 'InFlow (m^3/s)'
        make_plot( dir_plots, Name, Time, Y_name, Y )
        Y = Value[5][counter[-1]:]
        Y_name = 'OutFlow (m^3/s)'
        make_plot( dir_plots, Name, Time, Y_name, Y )
        Y_1 = Value[6][counter[-1]:]
        name_1 = 'Bottom'
        Y_2 = Value[7][counter[-1]:]
        name_2 = 'Flood'
        Y_3 = Value[8][counter[-1]:]
        name_3 = 'Power'
        make_plot( dir_plots, Name, Time, Y_name, Y_1, name_1, Y_2, name_2, Y_3, name_3) 

    elif Type_of_data == 'S':
        
        dir_plots = dir_ +'/' +str(Ano)    

        Time = Value[0][counter[-1]:]
        Y = Value[1][counter[-1]:]
        Y_name = 'Type'
        make_plot( dir_plots, Name, Time, Y_name, Y )
        Y = Value[2][counter[-1]:]
        Y_name = 'Heigth (m)'
        make_plot( dir_plots, Name, Time, Y_name, Y )
        Y = Value[3][counter[-1]:]
        Y_name = 'OutFlow (m^3/s)'
        make_plot( dir_plots, Name, Time, Y_name, Y )

# %% Comapison bettween MET

def compare_met_yearly( Name_var, Number_var, dir_ , Met_1, Met_2, Met_3, Met_4, Met_5, Met_6):
        
    counter = [0]
    
    comp = len(Met_1[0])
    
    Name = 'Meteorological station'
    
    for i in range(comp-1):
        
        Time_element = Met_1[0][i]
        Ano = int(Time_element.year)
        
        if i == 0:
            Ano_at = Ano
        else:
            if Ano_at != Ano:

                counter.append(i)

                dir_plots = dir_ +'/' +str(Ano_at) 
                
                Time = Met_1[0][counter[-2]:counter[-1]]
                
                Y_name = Name_var 
                
                Y_1 = Met_1[Number_var][counter[-2]:counter[-1]]
                name_1 = 'Arzúa'
                Y_2 = Met_2[Number_var][counter[-2]:counter[-1]]
                name_2 = 'Melide'
                Y_3 = Met_3[Number_var][counter[-2]:counter[-1]]
                name_3 = 'Olveda'
                Y_4 = Met_4[Number_var][counter[-2]:counter[-1]]
                name_4 = 'Serra do Farro'
                Y_5 = Met_5[Number_var][counter[-2]:counter[-1]]
                name_5 = 'Mouriscade'
                Y_6 = Met_6[Number_var][counter[-2]:counter[-1]]
                name_6 = 'Camanzo'
                
                make_plot( dir_plots, Name, Time, Y_name, Y_1, name_1, Y_2, name_2, Y_3, name_3, Y_4, name_4, Y_5, name_5, Y_6, name_6)

                Ano_at = Ano
                    
    dir_plots = dir_ +'/' +str(Ano) 
                
    Time = Met_1[0][counter[-1]:]
    
    Y_name = Name_var 
    
    Y_1 = Met_1[Number_var][counter[-1]:]
    name_1 = 'Arzúa'
    Y_2 = Met_2[Number_var][counter[-1]:]
    name_2 = 'Melide'
    Y_3 = Met_3[Number_var][counter[-1]:]
    name_3 = 'Olveda'
    Y_4 = Met_4[Number_var][counter[-1]:]
    name_4 = 'Serra do Farro'
    Y_5 = Met_5[Number_var][counter[-1]:]
    name_5 = 'Mouriscade'
    Y_6 = Met_6[Number_var][counter[-1]:]
    name_6 = 'Camanzo'
    
    make_plot( dir_plots, Name, Time, Y_name, Y_1, name_1, Y_2, name_2, Y_3, name_3, Y_4, name_4, Y_5, name_5, Y_6, name_6)

# %% Execute 
    
St_544, St_546 = pr.load(open ('Stations.p','rb'))
Met_1, Met_2, Met_3, Met_4 = pr.load(open("Met.p","rb"))
Touro, Brandariz, Portodemouros = pr.load(open("Dams_with_outliers.p","rb"))

dir_plots = 'C:/Users/Paulo_Rocha/Desktop/Tese/Tese_code/Plot_Data/';


# split_plot_yearly( 'Station 544', St_544, 'S', dir_plots )
# print('Done!')
# split_plot_yearly( 'Station 546', St_546, 'S', dir_plots )
# print('Done!')
split_plot_yearly( 'Touro', Touro, 'D', dir_plots )
print('Done!')
split_plot_yearly( 'Brandariz', Brandariz, 'D', dir_plots )
print('Done!')
# split_plot_yearly( 'Portodemouro', Portodemouros, 'D', dir_plots )
# print('Done!')
# compare_met_yearly('Temperature (ºC)', 2, dir_plots, Met_1, Met_2, Met_3, Met_4, Met_5, Met_6)
# print('Done!')
# compare_met_yearly('Humidity (%)', 3, dir_plots, Met_1, Met_2, Met_3, Met_4, Met_5, Met_6)
# print('Done!')
# compare_met_yearly('Precipitation (L/m^2)', 4, dir_plots, Met_1, Met_2, Met_3, Met_4, Met_5, Met_6)
# print('Done!')
# compare_met_yearly('Irradiation (kj/m^2.day)', 5, dir_plots, Met_1, Met_2, Met_3, Met_4, Met_5, Met_6)
# print('Done!')
# compare_met_yearly('Pessure (hPa)', 6, dir_plots, Met_1, Met_2, Met_3, Met_4, Met_5, Met_6)
# print('Done!')


