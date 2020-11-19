#this function compares the outflow of an upstream dam to the input at the dam reservoir 

import pickle as pr
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm


Touro, Brandariz, Portodemouros = pr.load(open("Dams.p","rb"))

dir_plots = 'C:/Users/Paulo_Rocha/Desktop/Tese/Tese_code/Plot_Data/General_plots';

a = np.array(Touro[5])

a = a[a != None]
sm.graphics.tsa.plot_pacf(a,lags=10)
plt.show()