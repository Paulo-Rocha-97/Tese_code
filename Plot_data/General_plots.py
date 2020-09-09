import pickle as pr
from My_plot_ import make_plot_marker_line_ as m_p_m

St_544, St_546 = pr.load(open("Stations.p","rb"))

Met_1, Met_2, Met_3, Met_4, Met_5, Met_6 = pr.load(open("Met.p","rb"))

Touro, Brandariz, Portodemouros = pr.load(open("Dams.p","rb"))

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

# %% Execute plot 
    
Time, Y_var1 = define_vectors(St_544)
_, Y_var2 = define_vectors(St_546)

m_p_m(dir_plots, 'Stations', Time,'Existing data (%)',Y_var1,'Station 544',Y_var2,'Station 546')

Time, Y_var1 = define_vectors(Touro)
_, Y_var2 = define_vectors(Brandariz)
_, Y_var3 = define_vectors(Portodemouros)

m_p_m(dir_plots, 'Dams', Time,'Existing data (%)',Y_var1,'Touro',Y_var2,'Brandariz',Y_var3,'Portodemouros')

#%%

Time, Y_var1 = define_vectors(Met_1)
_, Y_var2 = define_vectors(Met_2)
_, Y_var3 = define_vectors(Met_3)
_, Y_var4 = define_vectors(Met_4)
_, Y_var5 = define_vectors(Met_5)
_, Y_var6 = define_vectors(Met_6)

m_p_m(dir_plots, 'Metereological Stations', Time,'Existing data (%)',Y_var1,'Azúra',Y_var2,'Melide',Y_var3,'Olveda',Y_var4,'Serra do Faro',Y_var5,'Mouriscade',Y_var6,'Camanzo')

