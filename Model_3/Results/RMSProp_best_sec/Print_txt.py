
import pickle as pr

_,r,RMSE,MAE = pr.load(open('Value_quality_sec.p','rb'))

f = open('Results.txt','w')
f.write('--------- Data Results ---------\n')
f.write('RMSprop Model\nr - {:4f}\nRMSE - {:4f}\nMAE - {:4f}\n'.format(float(r[0]),float(RMSE[0]),float(MAE)))
f.close()