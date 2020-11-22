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

def make_plot_point( path, Name, R, MAE, RMSE, R_std, MAE_std, RMSE_std,  X_ticks, file_name ):
    
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
    # ax1.set_ylim([min(R)-0.015, max(R)+0.005])
        
    ax2.errorbar(X, MAE , yerr=MAE_std, color ='blue' , fmt='o', capsize=6)  
    ax2.scatter(X, MAE, s = 30, color ='blue')
    # ax2.axhline(MAE[0], color='orange', linestyle='--')
    # ax2.set_ylim([min(MAE)-0.012, max(MAE)+0.014 ])
    
    ax3.errorbar(X, RMSE , yerr=RMSE_std, color ='green', fmt='o', capsize=6)  
    ax3.scatter(X, RMSE, s = 30, color ='green')
    # ax3.axhline(RMSE[0], color='orange', linestyle='--')
    # ax3.set_ylim([min(RMSE)-0.002, max(RMSE)+0.004] )
    
    ax1.set_xticks(X)
    ax2.set_xticks(X)
    ax3.set_xticks(X)
    
    ax1.minorticks_on()
    ax2.minorticks_on()
    ax3.minorticks_on()
    
    ax1.tick_params(axis='x', which='minor', bottom=False)
    ax2.tick_params(axis='x', which='minor', bottom=False)
    ax3.tick_params(axis='x', which='minor', bottom=False)
    
    plt.xticks(X, X_ticks, rotation = 60)
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

path = 'C:/Users/Paulo_Rocha/Desktop/Tese/Tese_code/Model_4/Feature_Selection/Results/Plots'
    
name_file = 'Feature_selection.p'

R_mean, MAE_mean, RSME_mean, R_std, MAE_std, RSME_std, N_error, Data = feature_selections_results(name_file)

# %% To read feature_selection_all_2

R_mean_1 = []
RSME_mean_1 = []
MAE_mean_1 = []
R_std_1 = []
RSME_std_1 = []
MAE_std_1 = []

R_mean_2 = []
RSME_mean_2 = []
MAE_mean_2 = []
R_std_2 = []
RSME_std_2 = []
MAE_std_2 = []

R_mean_3 = []
RSME_mean_3 = []
MAE_mean_3 = []
R_std_3 = []
RSME_std_3 = []
MAE_std_3 = []

R_mean_4 = []
RSME_mean_4 = []
MAE_mean_4 = []
R_std_4 = []
RSME_std_4 = []
MAE_std_4 = []

for i in range(len(R_mean)):
    
    if i in [0,1,2,3,4,5,6]:
        
        R_mean_1.append(R_mean[i])
        RSME_mean_1.append(RSME_mean[i])
        MAE_mean_1.append(MAE_mean[i])
        R_std_1.append(R_std[i])
        RSME_std_1.append(RSME_std[i])
        MAE_std_1.append(MAE_std[i])
        
    if i in [0,6,7,8,9,10,11,12,13,14,15]:
        
        R_mean_2.append(R_mean[i])
        RSME_mean_2.append(RSME_mean[i])
        MAE_mean_2.append(MAE_mean[i])
        R_std_2.append(R_std[i])
        RSME_std_2.append(RSME_std[i])
        MAE_std_2.append(MAE_std[i])
        
    if i in [0,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38]:
        
        R_mean_3.append(R_mean[i])
        RSME_mean_3.append(RSME_mean[i])
        MAE_mean_3.append(MAE_mean[i])
        R_std_3.append(R_std[i])
        RSME_std_3.append(RSME_std[i])
        MAE_std_3.append(MAE_std[i])
        
    if i in [0,39,40,41,42,43,44,45,46]:
        
        R_mean_4.append(R_mean[i])
        RSME_mean_4.append(RSME_mean[i])
        MAE_mean_4.append(MAE_mean[i])
        R_std_4.append(R_std[i])
        RSME_std_4.append(RSME_std[i])
        MAE_std_4.append(MAE_std[i])
        
X_1_ticks=['Control','Temperature','Precipitation','Humidity','Solar Radiation','Presssure','All']
Name_1 = 'Averaging same type of data from all stations'
path = 'C:/Users/Paulo_Rocha/Desktop/Tese/Tese_code/Model_1/Feature_Selection/Results/Plots'

make_plot_point( path, Name_1, R_mean_1, MAE_mean_1, RSME_mean_1, R_std_1, MAE_std_1, RSME_std_1, X_1_ticks , 'average_one_by_one')

X_2_ticks=['Control','None','Day','Temp','Precip','Hum','Solar Rad','Press','St_544','St_546','intflow']
Name_2 = 'Removing one type of variables at a time, the rest averaged'

make_plot_point(  path, Name_2, R_mean_2, MAE_mean_2, RSME_mean_2, R_std_2, MAE_std_2, RSME_std_2, X_2_ticks, 'average_only' )

X_3_ticks =['C','D','T_1','T_2','T_3','T_4','P_1','P_2','P_3','P_4','H_1','H_2','H_3','H_4','S_1','S_2','S_3','S_4','p_1','p_2','p_4','S_4','S_6','In']
Name_3 = 'Removing one variables at a time'

make_plot_point( path, Name_3, R_mean_3, MAE_mean_3, RSME_mean_3, R_std_3, MAE_std_3, RSME_std_3, X_3_ticks, 'remove_one_by_one' )

X_4_ticks =['Control','Day','Temp','Precip','Hum','Solar Rad','Press','Station','Inflow']
Name_4 = 'Only a type of variables at a time'

make_plot_point( path, Name_4, R_mean_4, MAE_mean_4, RSME_mean_4, R_std_4, MAE_std_4, RSME_std_4, X_4_ticks, 'one_type_by_one' )
