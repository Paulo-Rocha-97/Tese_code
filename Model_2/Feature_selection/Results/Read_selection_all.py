# This function reads the information relevant to the feature selection

import numpy as np 
import pickle as pr

def feature_selections_results(name_file):

    Data, _, Results_r_t, Results_r_1, Results_r_2, Results_r_3, _, Results_MAE_t, Results_MAE_1, Results_MAE_2, Results_MAE_3, Results_RMSE, _ = pr.load(open(name_file,'rb'))
    
    R_t_mean = []
    MAE_t_mean = []
    RSME_t_mean = []
    N_error_vec_t = []
    
    for i in range(Results_r_t.shape[0]):
    
        cont_t = 0
        N_error_t = 0     
        Av_r_t = 0
        Av_rsme_t = 0
        Av_mae_t = 0

        
        for j in range(Results_r_t.shape[1]):
                
            if np.isnan(Results_r_t[i,j]) or Results_r_t[i,j] < 0:
                    
                 N_error_t = N_error_t + 1
                 
            else:
                 
                Av_rsme_t = Av_rsme_t + Results_RMSE[i,j]
                Av_mae_t = Av_mae_t + Results_MAE_t[i,j]
                Av_r_t = Av_r_t + Results_r_t[i,j]
                
                cont_t = cont_t + 1
            
                
                    
        R_t_mean.append((Av_r_t/cont_t))
        RSME_t_mean.append((Av_rsme_t/cont_t))
        MAE_t_mean.append((Av_mae_t/cont_t))
        N_error_vec_t.append(N_error_t)
            
    R = R_t_mean

    
    MAE = MAE_t_mean
    
    RSME = RSME_t_mean

    N_ERROR = N_error_vec_t
            
    return  R, MAE, RSME, N_ERROR, Data

# %% Plot definitiond

def make_plot_point( path, Name, R, MAE, RMSE, file_name ):
    
    import os
    import matplotlib.pyplot as plt
    
    X=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
    
    fig, (ax1, ax2, ax3) = plt.subplots(3, sharex=True, figsize=(10,10))
    fig.suptitle(Name)
    
    ax1.scatter(X, R , s = 20, color ='red')
    ax1.axhline(R[0], color='orange', linestyle='--')
    ax1.set_ylim([min(R)-0.001, max(R)+0.001])
    ax2.scatter(X, MAE, s = 20, color ='blue')
    ax2.axhline(MAE[0], color='orange', linestyle='--')
    ax2.set_ylim([min(MAE)-0.0002, max(MAE)+0.0002 ])
    ax3.scatter(X, RMSE, s = 20, color ='green')
    ax3.axhline(RMSE[0], color='orange', linestyle='--')
    ax3.set_ylim([min(RMSE)-0.0002, max(RMSE)+0.0002] )
        
    ax1.minorticks_on()
    ax2.minorticks_on()
    ax3.minorticks_on()
    
    ax1.tick_params(axis='x', which='minor', bottom=False)
    ax2.tick_params(axis='x', which='minor', bottom=False)
    ax3.tick_params(axis='x', which='minor', bottom=False)
    
    ax1.set_ylabel('r')
    ax1.grid(b=True, which='major', color='#666666', linestyle='-', linewidth=1.0)
    ax1.grid(b=True, which='minor', color='#999999', linestyle='-', linewidth=1.0, alpha=0.2)
    ax2.set_ylabel('MAE')
    ax2.grid(b=True, which='major', color='#666666', linestyle='-', linewidth=1.0)
    ax2.grid(b=True, which='minor', color='#999999', linestyle='-', linewidth=1.0, alpha=0.2)
    ax3.set_ylabel('RMSE')
    ax3.grid(b=True, which='major', color='#666666', linestyle='-', linewidth=1.0)
    ax3.grid(b=True, which='minor', color='#999999', linestyle='-', linewidth=1.0, alpha=0.2)

    if not os.path.exists(path):
        os.makedirs(path)

    plt.savefig(path+'/'+file_name+'.png')

#%% Execute 
    
name_file = 'Feature_selection_all.p'

R, MAE, RMSE, N_ERROR, Data = feature_selections_results(name_file)

path = 'C:/Users/Paulo_Rocha/Desktop/Tese/Tese_code/Model_2/Feature_Selection/Results/Plots'

file_name = 'Tested hypothesis'

make_plot_point( path, file_name, R, MAE, RMSE, file_name )
