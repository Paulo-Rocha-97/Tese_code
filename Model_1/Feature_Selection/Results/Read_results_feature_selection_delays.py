#  function to read results from features selection
import numpy as np 
import pickle as pr

def feature_selections_results(name_file):

    Data, Results_r, Results_MAE, Results_RMSE , time_taken = pr.load(open(name_file,'rb'))
    
    R_mean = []
    MAE_mean = []
    RSME_mean = []
    N_error_vec = []
    
    for i in range(Results_r.shape[0]):
    
        cont=0
        N_error=0
        Av_r = 0
        Av_rsme = 0
        Av_mae = 0
        
        for j in range(8):
            
            if np.isnan(Results_r[i,j]) or Results_r[i,j] < 0:
                
                N_error = N_error + 1
                
            else:
                
                Av_r= Av_r + Results_r[i,j]
                Av_mae = Av_mae + Results_MAE[i,j]
                Av_rsme = Av_rsme + Results_RMSE[i,j]
                cont = cont +1
        
        R_mean.append((Av_r/cont))
        RSME_mean.append((Av_rsme/cont))
        MAE_mean.append((Av_mae/cont))
        N_error_vec.append(N_error)
        
    
    return R_mean, RSME_mean, MAE_mean, N_error_vec, Data

# %% Plot making function

def make_plot_point( path, Name, X, Y_1, Y_2, Y_3, X_Axis, Y_name_1, Y_name_2, Y_name_3, file_name ):
    
    import os
    import matplotlib.pyplot as plt
    
    plt.rcParams.update({'font.size': 80})
                  
    fig, (ax1, ax2, ax3) = plt.subplots(3, sharex=True, figsize=(100,100))
    fig.suptitle(Name)
    
    ax1.scatter(X, Y_1, s = 2000, color ='red')
    ax1.axhline(Y_1[0], color='orange', linestyle='--', linewidth=6.0)
    ax2.scatter(X, Y_2, s = 2000, color ='blue')
    ax2.axhline(Y_2[0], color='orange', linestyle='--', linewidth=6.0)
    ax3.scatter(X, Y_3, s = 2000, color ='green')
    ax3.axhline(Y_3[0], color='orange', linestyle='--', linewidth=6.0)

    ax1.minorticks_on()
    ax2.minorticks_on()
    ax3.minorticks_on()
    
    ax1.tick_params(axis='x', which='minor', bottom=False)
    ax2.tick_params(axis='x', which='minor', bottom=False)
    ax3.tick_params(axis='x', which='minor', bottom=False)
    
    plt.xticks(X, X_Axis)
    ax1.set_ylabel(Y_name_1)
    ax1.grid(b=True, which='major', color='#666666', linestyle='-', linewidth=4.0)
    ax1.grid(b=True, which='minor', color='#999999', linestyle='-', linewidth=4.0, alpha=0.2)
    ax2.set_ylabel(Y_name_2)
    ax2.grid(b=True, which='major', color='#666666', linestyle='-', linewidth=4.0)
    ax2.grid(b=True, which='minor', color='#999999', linestyle='-', linewidth=4.0, alpha=0.2)
    ax3.set_ylabel(Y_name_3)
    ax3.grid(b=True, which='major', color='#666666', linestyle='-', linewidth=4.0)
    ax3.grid(b=True, which='minor', color='#999999', linestyle='-', linewidth=4.0, alpha=0.2)

    if not os.path.exists(path): 
        os.makedirs(path)

    plt.savefig(path+'/'+file_name+'.png',bbox_inches='tight')
    
# %% To read feature_selection_all_2

R_mean_1 = []
RSME_mean_1 = []
MAE_mean_1 = []
X_1 = []
Cont_1 = 1

name_file = 'Feature_selection_delays.p'

R_mean_1, RSME_mean_1, MAE_mean_1, N_error_1, Data_1 = feature_selections_results(name_file)

X_1 = [1,2,3,4,5,6,7,8,9,10]
X_1_ticks =['1','2','3','4','5','6','7','8','9','10']
Name_1 = 'Delays'
path = 'C:/Users/Paulo_Rocha/Desktop/Tese/Tese_code/Model_1/Feature_Selection/Results/Plots'

make_plot_point( path, Name_1, X_1, RSME_mean_1, MAE_mean_1, R_mean_1, X_1_ticks, 'RSME', 'MAE', 'r', 'delays' )
