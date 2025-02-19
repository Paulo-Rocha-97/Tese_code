import pickle as pr
from My_plot_ import make_plot_line as m_p_m

St_544, St_546 = pr.load(open("Station_full_timeseries.p","rb"))

Met_1, Met_2, Met_3, Met_4 = pr.load(open("Met.p","rb"))

Touro, Brandariz, Portodemouros = pr.load(open("Dams.p","rb"))
Touro_, Brandariz_, Portodemouros_ = pr.load(open("Dams_full_time_series.p","rb"))

dir_plots = 'C:/Users/Paulo_Rocha/Desktop/Tese/Tese_code/Plot_Data/General_plots';

# %% Quantify the amount of missing data by year 

def define_vectors ( Value ):
    
    counter = [0]
    Time = []
    Y_var = []
    
    comp = len(Value[0])
    
    for i in range(comp-1):
        
        Time_element = Value[0][i]
        Ano = int(Time_element.year)

        if i == 0:
            Ano_at = Ano
        else:
            if Ano_at != Ano:
                
                counter.append(i)
                
                Time.append(Ano_at)
                
                Y = Value[1][counter[-2]:counter[-1]]
                
                S = sum(Y)/len(Y)*100
                
                Y_var.append(S)
                
                Ano_at = Ano
                
    Time.append(Ano)
                
    Y = Value[1][counter[-1]:]
    
    S = sum(Y)/len(Y)*100
    
    Y_var.append(S)
    
    return Time, Y_var 

#%% Execute plot 
    
# Time, Y_var1_ = define_vectors(St_544)
# _, Y_var2_ = define_vectors(St_546)

# m_p_m(dir_plots, 'Stations', Time,'Existing data (%)',Y_var1_,'Station 544',Y_var2_,'Station 546')

# Time, Y_var1 = define_vectors(Touro)
# _, Y_var2 = define_vectors(Brandariz)
# _, Y_var3 = define_vectors(Portodemouros)

# m_p_m(dir_plots, 'Dams', Time,'Existing data (%)',Y_var1,'Touro',Y_var2,'Brandariz',Y_var3,'Portodemouros')

#%%

Time, Y_var1 = define_vectors(Met_1)
_, Y_var2 = define_vectors(Met_2)
_, Y_var3 = define_vectors(Met_3)
_, Y_var4 = define_vectors(Met_4)

m_p_m(dir_plots, 'Metereological Stations', Time,'Existing data (%)',Y_var1,'Arzúa',Y_var2,'Melide',Y_var3,'Olveda',Y_var4,'Serra do Faro')

#%% plot Full time line

# Time_1, Y_var1 = define_vectors(Touro_)
# Time_2, Y_var2 = define_vectors(Brandariz_)
# Time_3, Y_var3 = define_vectors(Portodemouros_)

# m_p_m(dir_plots, 'Touro_Brandariz ', Time_1,'Existing data (%)',Y_var1,'Touro',Y_var2,'Brandariz')
# m_p_m(dir_plots, 'Portodemouros full timeseries ', Time_3,'Existing data (%)',Y_var3 )