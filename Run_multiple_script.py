# this function runs multiple file in diferent directories

import os

# %% Define the directoies to work 

Model_1_dir = 'C:/Users/Paulo_Rocha/Desktop/Tese/Tese_code/Model_1/Feature_selection'
Model_2_dir = 'C:/Users/Paulo_Rocha/Desktop/Tese/Tese_code/Model_2/Feature_selection'
Model_3_dir = 'C:/Users/Paulo_Rocha/Desktop/Tese/Tese_code/Model_3/Feature_selection'
Model_4_dir = 'C:/Users/Paulo_Rocha/Desktop/Tese/Tese_code/Model_4/Feature_selection'

File_name_0 ='Feature_selection_delays.py'
File_name = 'Feature_selection.py'
File_name_1 = 'Feature_selection_time_delay.py'
File_name_2 = 'Feature_selection_.py'

#%% Run subprocess

print('-----------------Multiple Model Routine-----------------')
print('\n')
os.chdir(Model_1_dir)
wdir = os.getcwd()
print(wdir)
print('\n')
exec(open(File_name_0).read())
exec(open(File_name).read())
print('\n')
os.chdir(Model_2_dir)
wdir = os.getcwd()
print(wdir)
print('\n')
exec(open(File_name_1).read())
exec(open(File_name_2).read())
os.chdir(Model_3_dir)
print('\n')
wdir = os.getcwd()
print(wdir)
print('\n')
exec(open(File_name_1).read())
exec(open(File_name_2).read())
print('\n')
os.chdir(Model_4_dir)
wdir = os.getcwd()
print(wdir)
print('\n')
exec(open(File_name_1).read())
exec(open(File_name_2).read())
print('\n')

print('Routine ended sucessfully')