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
        
        if cont == 0:
            
            R_mean.append(0)
            RSME_mean.append(0)
            MAE_mean.append(0)
            
        else:
            
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

    plt.savefig(path+'/'+file_name+'.png')
     
# %% Call file
    
name_file = 'Feature_selection_all.p'

R_mean, RSME_mean, MAE_mean, N_error, Data = feature_selections_results(name_file)

# %% To read feature_selection_all_2

R_mean_1 = []
RSME_mean_1 = []
MAE_mean_1 = []
X_1 = []
Cont_1 = 1
R_mean_2 = []
RSME_mean_2 = []
MAE_mean_2 = []
X_2 = []
Cont_2 = 1
R_mean_3 = []
RSME_mean_3 = []
MAE_mean_3 = []
X_3 = []
Cont_3 = 1
R_mean_4 = []
RSME_mean_4 = []
MAE_mean_4 = []
X_4 = []
Cont_4 = 1

for i in range(len(R_mean)):
    
    if i in [0,1,2,3,4,5,6]:
        
        R_mean_1.append(R_mean[i])
        RSME_mean_1.append(RSME_mean[i])
        MAE_mean_1.append(MAE_mean[i])
        X_1.append(Cont_1)
        Cont_1=Cont_1+1
        
    if i in [0,6,7,8,9,10,11,12,13,14,15]:
        
        R_mean_2.append(R_mean[i])
        RSME_mean_2.append(RSME_mean[i])
        MAE_mean_2.append(MAE_mean[i])
        X_2.append(Cont_2)
        Cont_2=Cont_2+1
        
    if i in [0,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38]:
        
        R_mean_3.append(R_mean[i])
        RSME_mean_3.append(RSME_mean[i])
        MAE_mean_3.append(MAE_mean[i])
        X_3.append(Cont_3)
        Cont_3=Cont_3+1
        
    if i in [0,39,40,41,42,43,44,45,46]:
        
        R_mean_4.append(R_mean[i])
        RSME_mean_4.append(RSME_mean[i])
        MAE_mean_4.append(MAE_mean[i])
        X_4.append(Cont_4)
        Cont_4=Cont_4+1
        
X_1_ticks=['Control','Temperature','Precipitation','Humidity','Solar Radiation','Presssure','All']
Name_1 = 'Averaging same type of data from all stations'
path = 'C:/Users/Paulo_Rocha/Desktop/Tese/Tese_code/Model_1/Feature_Selection/Results/Plots'

make_plot_point( path, Name_1, X_1, RSME_mean_1, MAE_mean_1, R_mean_1, X_1_ticks, 'RSME', 'MAE', 'r', 'average_one_by_one' )

X_2_ticks=['Control','None','Day','Temp','Precip','Hum','Solar Rad','Press','St_544','St_546','intflow']
Name_2 = 'Removing one type of variables at a time, the rest averaged'

make_plot_point( path, Name_2, X_2, RSME_mean_2, MAE_mean_2, R_mean_2, X_2_ticks, 'RSME', 'MAE', 'r', 'average_only' )

X_3_ticks =['C','D','T_1','T_2','T_3','T_4','P_1','P_2','P_3','P_4','H_1','H_2','H_3','H_4','S_1','S_2','S_3','S_4','p_1','p_2','p_4','S_4','S_6','In']
Name_3 = 'Removing one variables at a time'

make_plot_point( path, Name_3, X_3, RSME_mean_3, MAE_mean_3, R_mean_3, X_3_ticks, 'RSME', 'MAE', 'r', 'remove_one_by_one' )

X_4_ticks =['Control','Day','Temp','Precip','Hum','Solar Rad','Press','Station','Inflow']
Name_4 = 'Only a type of variables at a time'

make_plot_point( path, Name_4, X_4, RSME_mean_4, MAE_mean_4, R_mean_4, X_4_ticks, 'RSME', 'MAE', 'r', 'one_type_by_one' )

name_file = 'Feature_selection_single_input.p'

R_mean_5, RSME_mean_5, MAE_mean_5, N_error_5, Data_1 = feature_selections_results(name_file)

X_5 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
X_5_ticks =['C','D','T_1','T_2','T_3','T_4','P_1','P_2','P_3','P_4','H_1','H_2','H_3','H_4','S_1','S_2','S_3','S_4','p_1','p_2','p_4','S_4','S_6','In']
Name_5 = 'One variables at a time'

make_plot_point( path, Name_5, X_5, RSME_mean_5, MAE_mean_5, R_mean_5, X_5_ticks, 'RSME', 'MAE', 'r', 'one_by_one' )

name_file = 'Feature_selection_remove_one.p'

R_mean_6, RSME_mean_6, MAE_mean_6, N_error_6, Data_2 = feature_selections_results(name_file)

X_6 = [1,2,3,4,5,6,7,8]
X_6_ticks =['Control','Temp','Precip','Hum','Solar Rad','Press','Station','Inflow']
Name_6 = 'Removing one type variables at a time'

make_plot_point( path, Name_6, X_6, RSME_mean_6, MAE_mean_6, R_mean_6, X_6_ticks, 'RSME', 'MAE', 'r', 'remove_one_type' )


