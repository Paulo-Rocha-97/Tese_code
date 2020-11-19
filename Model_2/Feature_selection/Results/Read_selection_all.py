# This function reads the information relevant to the feature selection

import numpy as np 
import pickle as pr

def feature_selections_results(name_file):

    Data, _, Results_r_t, Results_r_1, Results_r_2, Results_r_3, _, Results_MAE_t, Results_MAE_1, Results_MAE_2, Results_MAE_3, Results_RMSE, _ = pr.load(open(name_file,'rb'))
    
    R_t_mean = []
    MAE_t_mean = []
    RSME_mean = []
    N_error_vec = []
    
    for i in range(Results_r_t.shape[0]):
    
        cont=0
        N_error_t=0
        Av_r_t = 0
        Av_rsme = 0
        Av_mae_t = 0
        
        for j in range(Results_r_t.shape[1]):
            
            if np.isnan(Results_r_t[i,j]) or Results_r_t[i,j] < 0:
                
                N_error_t = N_error_t + 1
                
            else:
                
                Av_r_t= Av_r_t + Results_r_t[i,j]
                Av_mae_t = Av_mae_t + Results_MAE_t[i,j]
                Av_rsme = Av_rsme + Results_RMSE[i,j]
                cont = cont +1
        
        
        
            
        
        
        R_t_mean.append((Av_r_t/cont))
        RSME_mean.append((Av_rsme/cont))
        MAE_t_mean.append((Av_mae_t/cont))
        N_error_vec.append(N_error)
        
    
    
    
    
    
    
    
    
    
    return R_mean, RSME_mean, MAE_mean, N_error_vec, Data


#%%  This function organizes de value into a np matrix


#%% Execute 
    
