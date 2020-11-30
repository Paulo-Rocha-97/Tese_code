
import pickle as pr
import numpy as np

St_544, St_546 = pr.load(open ('Station.p','rb'))
Met_1, Met_2, Met_3, Met_4,_,_ = pr.load(open("Met.p","rb"))

values = ['Temperature', 'Humidity', 'Precipitation', 'Solar irridation', 'Pressure']
          
for i in range(2,len(Met_1)):

    max_values = [ max([j for j in Met_1[i] if j is not None]) , max([j for j in Met_2[i] if j is not None])  , max([j for j in Met_1[i] if j is not None]) , max([j for j in Met_1[i] if j is not None])  ]
    min_values = [ min([j for j in Met_1[i] if j is not None]) , min([j for j in Met_2[i] if j is not None])  , min([j for j in Met_1[i] if j is not None]) , min([j for j in Met_1[i] if j is not None])  ]
    
    print('\n'+values[i-2]+' max: {:5.2f} min: {:5.2f} '.format( max(max_values) , min(min_values) ))
    
values = ['Heigth','Flow']
    
for i in range(2,len(St_544)):

    max_values = [ max([j for j in St_544[i] if j is not None]) , max([j for j in St_546[i] if j is not None])  ]
    min_values = [ min([j for j in St_544[i] if j is not None]) , min([j for j in St_546[i] if j is not None])  ]
    
    print('\n'+values[i-2]+' max: {:5.2f} min: {:5.2f} '.format( max(max_values) , min(min_values) ))