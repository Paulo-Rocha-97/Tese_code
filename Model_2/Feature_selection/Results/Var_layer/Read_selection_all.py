# This function reads the information relevant to the feature selection

import numpy as np 
import pickle as pr

def feature_selections_results(name_file):

    Data, _, Results_r_t, Results_r_1, Results_r_2, Results_r_3, _, Results_MAE_t, Results_MAE_1, Results_MAE_2, Results_MAE_3, Results_RMSE, _ = pr.load(open(name_file,'rb'))
    
    R_t_mean = []
    R_1_mean = []
    R_2_mean = []
    R_3_mean = []
    MAE_t_mean = []
    MAE_1_mean = []
    MAE_2_mean = []
    MAE_3_mean = []
    RSME_s_mean = []
    RSME_t_mean = []
    N_error_vec_t = []
    N_error_vec_s = []
    cont_index= 0
    
    for i in range(Results_r_t.shape[0]):
    
        cont_t = 0
        cont_s = 0
        N_error_t = 0
        N_error_s = 0      
        Av_r_t = 0
        Av_r_1 = 0
        Av_r_2 = 0
        Av_r_3 = 0
        Av_rsme_s = 0
        Av_rsme_t = 0
        Av_mae_t = 0
        Av_mae_1 = 0
        Av_mae_2 = 0
        Av_mae_3 = 0
        
        for j in range(Results_r_t.shape[1]):

            if cont_index < 3 :
                
                if np.isnan(Results_r_t[i,j]) or Results_r_t[i,j] < 0:
                    
                     N_error_t = N_error_t + 1
                     
                else:
                     
                    Av_rsme_t = Av_rsme_t + Results_RMSE[i,j]
                    Av_mae_t = Av_mae_t + Results_MAE_t[i,j]
                    Av_r_t = Av_r_t + Results_r_t[i,j]
                    
                    cont_t = cont_t + 1
                
            elif cont_index > 2 and cont_index < 6:
                
                if np.isnan(Results_r_3[i,j]) or Results_r_3[i,j] < 0:
                    
                     N_error_s = N_error_s + 1
                     
                else:
                
                    Av_rsme_s = Av_rsme_s + Results_RMSE[i,j]
                    Av_mae_1 = Av_mae_1 + Results_MAE_1[i,j]
                    Av_r_1 = Av_r_1 + Results_r_1[i,j]
                    Av_mae_2 = Av_mae_2 + Results_MAE_2[i,j]
                    Av_r_2 = Av_r_2 + Results_r_2[i,j]
                    Av_mae_3 = Av_mae_3 + Results_MAE_3[i,j]
                    Av_r_3 = Av_r_3 + Results_r_3[i,j]
                    
                    cont_s = cont_s + 1
            
                if cont_index == 5:
                    cont_index = 0
                
        
        if cont_index < 3 :
            
            R_t_mean.append((Av_r_t/cont_t))
            RSME_t_mean.append((Av_rsme_t/cont_t))
            MAE_t_mean.append((Av_mae_t/cont_t))
            N_error_vec_t.append(N_error_t)
        
        elif cont_index > 2 and cont_index < 6: 
                
            RSME_s_mean.append((Av_rsme_s/cont_s))
            R_1_mean.append((Av_r_1/cont_s))
            MAE_1_mean.append((Av_mae_1/cont_s))
            R_2_mean.append((Av_r_2/cont_s))
            MAE_2_mean.append((Av_mae_2/cont_s))
            R_3_mean.append((Av_r_3/cont_s))
            MAE_3_mean.append((Av_mae_3/cont_s))
            N_error_vec_s.append(N_error_s)

        cont_index = cont_index +1
                    
            
    R = dict([('Global',R_t_mean),
              ('Bottom',R_1_mean),
              ('Flood',R_2_mean),
              ('Power',R_3_mean)])
    
    MAE = dict([('Global',MAE_t_mean),
                ('Bottom',MAE_1_mean),
                ('Flood',MAE_2_mean),
                ('Power',MAE_3_mean)])
    
    RSME = dict([('Global',RSME_t_mean),
                 ('Separate',RSME_s_mean)])

    N_ERROR = dict([('Global',N_error_vec_t),
                    ('Separate',N_error_vec_s)])
            
    return  R, MAE, RSME, N_ERROR, Data

# %% Plot definitiond

def make_plot_point( path, Name, R, MAE, RSME, file_name ):
    
    import os
    import matplotlib.pyplot as plt
    
    fig, (ax1, ax2, ax3) = plt.subplots(3, sharex=True, figsize=(100,100))
    fig.suptitle(Name)
    
    ax1.scatter( R , s = 2000, color ='red')
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

    plt.savefig(path+'/'+file_name+'.png')
    plt.close()



#%% Execute 
    
name_file = 'Feature_selection_all.p'

R, MAE, RSME, N_ERROR, Data = feature_selections_results(name_file)

