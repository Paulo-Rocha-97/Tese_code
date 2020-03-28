import pickle as pr
from My_plot import make_plot_marker_line as m_p_m

S_544, S_546, S_550 = pr.load(open("Station.p","rb"))

Touro, Brandariz, Portodemouros = pr.load(open("Dam.p","rb"))

dir_plots = 'C:/Users/Paulo_Rocha/Desktop/Tese/Tese_code/Plot_data/General_plots';

# %% Quantify the amount of missing data by year 

def define_vectors ( Value ):
    
    counter = [0]
    Time = []
    Y_var = []
    
    comp = len(Value[0])
    
    for i in range(comp-1):
        
        Time_element = Value[0][i]
        Ano = Time_element.year
        
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
    
Time, Y_var1 = define_vectors(S_544)
_, Y_var2 = define_vectors(S_546)
_, Y_var3 = define_vectors(S_550)

m_p_m(dir_plots, 'Stations', Time,'Existing data - %',Y_var1,'S_544',Y_var2,'S_546',Y_var3,'S_550')

Time, Y_var1 = define_vectors(Touro)
_, Y_var2 = define_vectors(Brandariz)
_, Y_var3 = define_vectors(Portodemouros)

m_p_m(dir_plots, 'Dams', Time,'Existing data - %',Y_var1,'Touro',Y_var2,'Brandariz',Y_var3,'Portodemouros')

