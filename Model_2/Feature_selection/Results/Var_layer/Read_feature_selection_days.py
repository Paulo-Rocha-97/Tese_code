# This function reads the information relevant to the days of delays

import numpy as np 
import pickle as pr

def feature_selections_results(name_file):

    Data, _, Results_r, _, _, _, _, Results_MAE, _, _, _, Results_RMSE , time_taken = pr.load(open(name_file,'rb'))
    
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
        
        for j in range(Results_r.shape[1]):
            
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


#%%  This function organizes de value into a np matrix
    
def matriz_organize(val,n):
    
    val_matriz = np.zeros([n,n])
    
    verify = len(val)/n
    
    k=0
    l=0
    
    if verify==int(verify):
    
        for i in range(len(val)):
            
            val_matriz[k,l] = val[i]
           
            if k==5 :
                k = 0
                l=l+1
            else:
                k=k+1
            
            
    else:
        
        print('-------------ERROR------------\nThe vector is not divisable')
    
    return val_matriz

# %% Plot making function

def make_plot_3d( path, Name, X, Y, Z, X_name, Y_name, Z_name, file_name , extrema):
    
    import os
    import matplotlib.pyplot as plt
    
    if extrema =='min':
        
        value_index = min(Z)
    else:
        value_index = max(Z)
    
    for i in range(len(Z)):
        if Z[i] == value_index:
            index = i
        
    fig = plt.figure()
    ax = plt.axes()
    fig.suptitle(Name)
    
    a = ax.scatter( X, Y, c=Z, cmap='tab20', s=50 )
    fig.colorbar(a)
    a = ax.plot( X[index], Y[index] , 'ko' , markersize=25 , fillstyle='none')
    
    if not os.path.exists(path):
        os.makedirs(path)

    plt.savefig(path+'/'+file_name+'.png',dpi=300)


# %% To read feature_selection_all_2

name_file = 'Feature_selection_days_of_delay.p'

R, RMSE, MAE, N_error, Data = feature_selections_results(name_file)

# X - Days before
# Y - Days after

Y=np.array( [0,1,2,3,4,5,0,1,2,3,4,5,0,1,2,3,4,5,0,1,2,3,4,5,0,1,2,3,4,5,0,1,2,3,4,5])
X=np.array( [0,0,0,0,0,0,1,1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,3,3,4,4,4,4,4,4,5,5,5,5,5,5])

path = 'C:/Users/Paulo_Rocha/Desktop/Tese/Tese_code/Model_2/Feature_Selection/Results/Var_layer/Plots'
Name_r = 'Number of days before and after (r)'
plot_name = 'N_days_r'

make_plot_3d( path, Name_r, X, Y, R, 'Days before', 'Days lags', 'r validation', plot_name ,'max')

Name_r = 'Number of days before and after (RMSE)'
plot_name = 'N_days_RMSE'

make_plot_3d( path, Name_r, X, Y, RMSE, 'Days before', 'Days lags', 'r validation', plot_name ,'min')
Name_r = 'Number of days before and after (MAE)'
plot_name = 'N_days_MAE'

make_plot_3d( path, Name_r, X, Y, MAE, 'Days before', 'Days lags', 'r validation', plot_name ,'min')

