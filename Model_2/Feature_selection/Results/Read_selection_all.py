# This function reads the information relevant to the feature selection

import numpy as np 
import pickle as pr

def feature_selections_results(name_file):

    Data, _, Results_r_t, Results_r_1, Results_r_2, Results_r_3, _, Results_MAE_t, Results_MAE_1, Results_MAE_2, Results_MAE_3, Results_RMSE, _ = pr.load(open(name_file,'rb'))
    
    R_mean = []
    MAE_mean = []
    RMSE_mean = []
    
    R_st = []
    MAE_st =[]
    RMSE_st = []
    
    N_error_vec_t = []    
    
    
    
    for i in range(Results_r_t.shape[0]):
    
        N_error_t = 0
        
        Values_r = []
        Values_rmse = []
        Values_mae = []
        
        for j in range(Results_r_t.shape[1]):
                
            if np.isnan(Results_r_t[i,j]) or Results_r_t[i,j] < 0:
                    
                 N_error_t = N_error_t + 1
                 
            else:
                 
                Values_r.append(Results_r_t[i,j])
                Values_mae.append(Results_MAE_t[i,j])
                Values_rmse.append(Results_RMSE[i,j])                
                
        R_mean.append( np.mean(Values_r) )
        RMSE_mean.append( np.mean(Values_rmse) )
        MAE_mean.append( np.mean(Values_mae) )
        R_st.append( np.std(Values_r) ) 
        MAE_st.append( np.std(Values_rmse) )
        RMSE_st.append( np.std(Values_mae) )
        
        N_error_vec_t.append(N_error_t)

            
    return R_mean, MAE_mean, RMSE_mean, R_st, MAE_st, RMSE_st, N_error_vec_t, Data

# %% Plot definitiond

def make_plot_point( path, Name, R, MAE, RMSE, R_std, MAE_std, RMSE_std, file_name ):
    
    import os
    import matplotlib.pyplot as plt
    
    X=[]
    
    for i in range(len(R)):
        X.append(i+1)
    
    fig, (ax1, ax2, ax3) = plt.subplots(3, sharex=True, figsize=(7,7))
    fig.suptitle(Name)
    
    ax1.errorbar(X, R , yerr=R_std, color ='red', fmt='o', capsize=6)
    ax1.scatter(X, R , s = 30, color ='red')
    # ax1.axhline(R[0], color='orange', linestyle='--')
    ax1.set_ylim([min(R)-0.005, max(R)+0.005])
        
    ax2.errorbar(X, MAE , yerr=MAE_std, color ='blue' , fmt='o', capsize=6)  
    ax2.scatter(X, MAE, s = 30, color ='blue')
    # ax2.axhline(MAE[0], color='orange', linestyle='--')
    ax2.set_ylim([min(MAE)-0.002, max(MAE)+0.002 ])
    
    ax3.errorbar(X, RMSE , yerr=RMSE_std, color ='green', fmt='o', capsize=6)  
    ax3.scatter(X, RMSE, s = 30, color ='green')
    # ax3.axhline(RMSE[0], color='orange', linestyle='--')
    ax3.set_ylim([min(RMSE)-0.002, max(RMSE)+0.002] )
    
    ax1.set_xticks(X)
    ax2.set_xticks(X)
    ax3.set_xticks(X)
    
    ax1.minorticks_on()
    ax2.minorticks_on()
    ax3.minorticks_on()
    
    ax1.tick_params(axis='x', which='minor', bottom=False)
    ax2.tick_params(axis='x', which='minor', bottom=False)
    ax3.tick_params(axis='x', which='minor', bottom=False)
    
    ax1.set_ylabel('r')
    ax1.grid(b=True,axis='y', which='major', color='#666666', linestyle='-', linewidth=1.0)
    ax1.grid(b=True,axis='y', which='minor', color='#999999', linestyle='-', linewidth=1.0, alpha=0.2)
    ax2.set_ylabel('MAE')
    ax2.grid(b=True,axis='y', which='major', color='#666666', linestyle='-', linewidth=1.0)
    ax2.grid(b=True,axis='y', which='minor', color='#999999', linestyle='-', linewidth=1.0, alpha=0.2)
    ax3.set_ylabel('RMSE')
    ax3.grid(b=True,axis='y', which='major', color='#666666', linestyle='-', linewidth=1.0)
    ax3.grid(b=True,axis='y', which='minor', color='#999999', linestyle='-', linewidth=1.0, alpha=0.2)

    if not os.path.exists(path):
        os.makedirs(path)

    plt.savefig(path+'/'+file_name+'.png')

#%% Execute 
    
name_file = 'Feature_selection_all.p'

R_mean, MAE_mean, RMSE_mean, R_std, MAE_std, RMSE_std, N_error, Data = feature_selections_results(name_file)

path = 'C:/Users/Paulo_Rocha/Desktop/Tese/Tese_code/Model_2/Feature_Selection/Results/Plots'

file_name = 'Tested hypothesis'

make_plot_point( path, file_name, R_mean, MAE_mean, RMSE_mean, R_std, MAE_std, RMSE_std, file_name )
