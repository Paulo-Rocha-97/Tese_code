import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['text.usetex'] = True

path = 'C:/Users/Paulo_Rocha/Desktop/Tese/Tese_code/Data_Analisys/';

Storage_p = pd.read_excel('Storage_Portodemouros.xlsx')
Storage_p = np.array(Storage_p)

Storage_b = pd.read_excel('Storage_Brandariz.xlsx')
Storage_b = np.array(Storage_b)

Storage_t = pd.read_excel('Storage_Touro.xlsx')
Storage_t = np.array(Storage_t)

# %% Storage plot 

fig, (ax1,ax2,ax3) = plt.subplots(1,3, figsize = (10,3))

ax1.plot(Storage_p[:,0], Storage_p[:,1])
ax1.set_xlabel('Heigth $(m)$')
ax1.set_ylabel('Volume $(Hm^3)$')
ax1.set_title('Portodemouros')
ax1.grid()

ax2.plot(Storage_b[:,0], Storage_b[:,1])
ax2.set_xlabel('Heigth $(m)$')
ax2.set_title('Brandariz')
ax2.grid()

ax3.plot(Storage_t[:,0], Storage_t[:,1])
ax3.set_xlabel('Heigth $(m)$')
ax3.set_title('Touro')
ax3.grid()

plt.savefig(path + 'Storage_info.png',dpi=300, bbox_inches='tight')


