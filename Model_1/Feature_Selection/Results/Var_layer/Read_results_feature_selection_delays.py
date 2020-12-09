#  function to read results from features selection
import numpy as np 
import pickle as pr

def feature_selections_results(name_file):

    Data, Results_r_t, Results_MAE_t, Results_RMSE, time_taken = pr.load(open(name_file,'rb'))
    
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

def make_plot_point( path, Name, R, MAE, RMSE, R_std, MAE_std, RMSE_std, X_ticks,file_name ):
    
    import os
    import matplotlib.pyplot as plt
    
    X=[]
    
    for i in range(len(R)):
        X.append(i+1)
    
    fig, (ax1, ax2, ax3) = plt.subplots(3, sharex=True, figsize=(7,7))
    fig.suptitle(Name)
    
    ax1.errorbar(X, R , yerr=R_std, color ='red', fmt='o', capsize=6)
    ax1.scatter(X, R , s = 30, color ='red')

        
    ax2.errorbar(X, MAE , yerr=MAE_std, color ='blue' , fmt='o', capsize=6)  
    ax2.scatter(X, MAE, s = 30, color ='blue')

    
    ax3.errorbar(X, RMSE , yerr=RMSE_std, color ='green', fmt='o', capsize=6)  
    ax3.scatter(X, RMSE, s = 30, color ='green')

    
    ax1.set_xticks(X)
    ax2.set_xticks(X)
    ax3.set_xticks(X)
    
    plt.xticks(X, X_ticks)
        
    ax1.minorticks_on()
    ax2.minorticks_on()
    ax3.minorticks_on()
    
    ax1.tick_params(axis='x', which='minor', bottom=False)
    ax2.tick_params(axis='x', which='minor', bottom=False)
    ax3.tick_params(axis='x', which='minor', bottom=False)
        
    ax1.set_ylabel('Days of delay')
    ax1.set_ylabel('r')
    ax3.set_xlabel('Number of delays')
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

    plt.rcParams['figure.dpi'] = 300
# %% To read feature_selection_all_2


name_file = 'Feature_selection_delays.p'

R_mean, MAE_mean, RMSE_mean, R_st, MAE_st, RMSE_st, N_error_vec_t, Data = feature_selections_results(name_file)

X_1_ticks =['1','2','3','4','5','6','7','8','9','10']
Name_1 = ''
path = 'C:/Users/Paulo_Rocha/Desktop/Tese/Tese_code/Model_1/Feature_Selection/Results/Plots'

make_plot_point( path, Name_1, R_mean, MAE_mean, RMSE_mean, R_st, MAE_st, RMSE_st, X_1_ticks, 'delays' )
