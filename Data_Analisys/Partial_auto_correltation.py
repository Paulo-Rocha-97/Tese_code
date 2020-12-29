#Function

import pickle as pr 
import numpy as np
import matplotlib

import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_pacf

path = 'C:\\Users\\Paulo_Rocha\\Desktop\\Tese\\Tese_code\\Data_Analisys\\Plot'  
Touro, Brandariz, Portodemouros = pr.load(open("Dams.p","rb"))

# %% function to clean the time series 

def clean_None(var):
    
    for i in range(len(var)):
        
        if i == 0 and var[i] == None:
                                
            if var[1] != None:
                
                var[0] = var[1]
                
            else:
                                    
                if var[2] != None:
                    
                    var[1] = var[2] 
                    var[0] = var[1]
                    
                else: 
                    
                    if var[3] != None:
                       
                       var[2] = var[3]
                       var[1] = var[2] 
                       var[0] = var[1]
                
        elif i > 0 and var[i] == None :
                
            ind = 0
            Value = 0
            
            if var[i-1] != None:
                ind = ind+1
                Value = Value + var[i-1] 
            if var[i+1] != None:
                ind = ind+1
                Value = Value + var[i+1]
            if ind == 0:
                var[i] = None
                print(*['Erro! - line ', i ])
            else: 
                var[i] = Value/ind
                    
        elif i == len(var)-1 and var[i] == None:
            
            var[i] = var[i-1]
            
            if var[i] == None:
                
                print(*['Erro! - line ', i ])
                    
    return var

Touro, Brandariz, Portodemouros = pr.load(open("Dams.p","rb"))

method_ ='ldb'

font = {'size'   : 20}
matplotlib.rc('font', **font)

Inflow_P =  np.asarray(clean_None(Portodemouros[4]))
plot_pacf( Inflow_P, lags = 30 , title ='', method = method_)
plt.xlabel('Lags')
plt.tight_layout()
plt.savefig(path+'\\Inflow_p_pacf.png',dpi=300)
plt.close()

Outflow_P =  np.asarray(clean_None(Portodemouros[5]))
plot_pacf( Outflow_P, lags = 30 , title ='', method = method_)
plt.xlabel('Lags')
plt.tight_layout()
plt.savefig(path+'\\Outflow_p_pacf.png',dpi=300)
plt.close()

Outflow_B =  np.asarray(clean_None(Brandariz[5]))
plot_pacf( Outflow_B, lags = 30 , title ='', method = method_)
plt.xlabel('Lags')
plt.tight_layout()
plt.savefig(path+'\\Outflow_b_pacf.png',dpi=300)
plt.close()

Outflow_T =  np.asarray(clean_None(Touro[5]))
plot_pacf( Outflow_T, lags = 30 , title ='', method = method_)
plt.xlabel('Lags')
plt.tight_layout()
plt.savefig(path+'\\Outflow_t_pacf.png',dpi=300)
plt.close()

# %%
def make_histogram(Value,name_fig, path):

    font = {'size'   : 20}
    matplotlib.rc('font', **font)
        
    Value = np.asarray(Value)
    Value = clean_None(Value)
    # Value_mean = np.mean(Value)
    
    n, bins, patches = plt.hist(x=Value, bins=30, color='#7E7E7E', alpha=0.7, rwidth=0.85)
    plt.grid(axis='y', alpha=0.75)
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    # plt.text(23, 45, r'$\mu=15, b=3$')
    maxfreq = n.max()
    plt.ylim(ymax=np.ceil(maxfreq / 10) * 10 if maxfreq % 10 else maxfreq + 10)
    plt.tight_layout()
    plt.savefig(path+'\\'+name_fig+'.png',dpi=300)
    plt.close()

# %% execute
    
# St_544, St_546 = pr.load(open ('Station.p','rb'))
# Met_1, Met_2, Met_3, Met_4,_,_ = pr.load(open("Met.p","rb"))

# make_histogram(Portodemouros[4], 'hist_inflow_P', path)
# make_histogram(Portodemouros[2], 'hist_heigth_P', path)
# make_histogram(Portodemouros[3], 'hist_volume_P', path)
# make_histogram(Portodemouros[5], 'hist_outflow_P', path)

# make_histogram(Brandariz[4], 'hist_inflow_B', path)
# make_histogram(Brandariz[2], 'hist_heigth_B', path)
# make_histogram(Brandariz[3], 'hist_volume_B', path)
# make_histogram(Brandariz[5], 'hist_outflow_B', path)

# make_histogram(Touro[4], 'hist_inflow_T', path)
# make_histogram(Touro[2], 'hist_heigth_T', path)
# make_histogram(Touro[3], 'hist_volume_T', path)
# make_histogram(Touro[5], 'hist_outflow_T', path)

# make_histogram(St_544[3], 'hist_st_544', path)
# make_histogram(St_546[3], 'hist_st_546', path)

# def met_hist_maker(Met_X,name):
    
#     make_histogram(Met_X[2], 'hist_'+name+'_temp', path)
#     make_histogram(Met_X[3], 'hist_'+name+'_hum', path)
#     make_histogram(Met_X[4], 'hist_'+name+'_precp', path)
#     make_histogram(Met_X[5], 'hist_'+name+'_solar', path)
#     if name != 'Met_3':
#         make_histogram(Met_X[6], 'hist_'+name+'_press', path)
    
# met_hist_maker(Met_1, 'Met_1')
# met_hist_maker(Met_2, 'Met_2')
# met_hist_maker(Met_3, 'Met_3')
# met_hist_maker(Met_4, 'Met_4')