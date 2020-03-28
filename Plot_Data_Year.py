# This function plots the station Data

import pickle as pr
from My_plot import make_plot_line as make_plot

# %% Set plot of yearly data

def split_plot_yearly( Name_element, Value, Type_of_data, dir_ ):
        
    counter = [0]
    
    comp = len(Value[0])
    
    for i in range(comp-1):
        
        Time_element = Value[0][i]
        Ano = Time_element.year
        
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
                    Y_name = 'Heigth'
                    make_plot( dir_plots, Name, Time, Y_name, Y )
                    Y = Value[3][counter[-2]:counter[-1]]
                    Y_name = 'OutFlow'
                    make_plot( dir_plots, Name, Time, Y_name, Y )
                    Y_1 = Value[4][counter[-2]:counter[-1]]
                    name_1 = 'Bottom'
                    Y_2 = Value[5][counter[-2]:counter[-1]]
                    name_2 = 'Flood'
                    Y_3 = Value[6][counter[-2]:counter[-1]]
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
                    Y_name = 'Heigth'
                    make_plot( dir_plots, Name, Time, Y_name, Y )
                    Y = Value[3][counter[-2]:counter[-1]]
                    Y_name = 'OutFlow'
                    make_plot( dir_plots, Name, Time, Y_name, Y )
                    
                    Ano_at = Ano

    if Type_of_data == 'D':

        dir_plots = dir_ +'/' +str(Ano)       

        Time = Value[0][counter[-1]:]

        Y = Value[1][counter[-1]:]
        Y_name = 'Type'
        make_plot( dir_plots, Name, Time, Y_name, Y )
        Y = Value[2][counter[-1]:]
        Y_name = 'Heigth'
        make_plot( dir_plots, Name, Time, Y_name, Y )
        Y = Value[3][counter[-1]:]
        Y_name = 'OutFlow'
        make_plot( dir_plots, Name, Time, Y_name, Y )
        Y_1 = Value[4][counter[-1]:]
        name_1 = 'Bottom'
        Y_2 = Value[5][counter[-1]:]
        name_2 = 'Flood'
        Y_3 = Value[5][counter[-1]:]
        name_3 = 'Power'
        make_plot( dir_plots, Name, Time, Y_name, Y_1, name_1, Y_2, name_2, Y_3, name_3) 

    elif Type_of_data == 'S':
        
        dir_plots = dir_ +'/' +str(Ano)    

        Time = Value[0][counter[-1]:]
        Y = Value[1][counter[-1]:]
        Y_name = 'Type'
        make_plot( dir_plots, Name, Time, Y_name, Y )
        Y = Value[2][counter[-1]:]
        Y_name = 'Heigth'
        make_plot( dir_plots, Name, Time, Y_name, Y )
        Y = Value[3][counter[-1]:]
        Y_name = 'OutFlow'
        make_plot( dir_plots, Name, Time, Y_name, Y )

# %% Execute
    
S_544, S_546, S_550 = pr.load(open ('Station.p','rb'))

Touro, Brandariz, Portodemouros = pr.load(open("Dam.p","rb"))

dir_plots = 'C:/Users/Paulo_Rocha/Desktop/Tese/Tese_code/Plot_data/';

split_plot_yearly( 'Touro', Touro, 'D', dir_plots )
split_plot_yearly( 'Brandariz', Brandariz, 'D', dir_plots )
split_plot_yearly( 'Portodemouro', Portodemouros, 'D', dir_plots )

split_plot_yearly( '544', S_544, 'S', dir_plots )
split_plot_yearly( '546', S_546, 'S', dir_plots )


