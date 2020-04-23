# Define inputs and outpus 

import pickle as pr

St_544, St_546 = pr.load(open ('Station.p','rb'))
Met_1, Met_2, Met_3, Met_4, _, _ = pr.load(open("Met.p","rb"))
_, _, Portodemouros = pr.load(open("Dams.p","rb"))

# %% Function to check if var is None

def check_none(Data,i):
    
    if i > 0:
        
        cur=Data[i]
        prev=Data[i-1]
        
        if cur == None:
            out = prev
        else:
            out = cur
    else:
        
        out = Data[i]
        
    return out

# %% Function to average 

def average( var_1, *args ):
      
    args_=list(args)
    
    if len(args_) == 1 :
        
        ind = 0
        Value = 0
        var_2 = args_[0]
        
        if var_1 != None:
            ind = ind+1
            Value = Value + var_1 
        if var_2 != None:
            ind = ind+1
            Value = Value + var_2 
        if ind == 0:
            var_final = None            
        else: 
            var_final = Value/ind

    elif len(args_) == 2 :
        
        ind = 0
        Value = 0
        var_2 = args_[0] 
        var_3 = args_[1] 
        
        if var_1 != None:
            ind = ind+1
            Value = Value + var_1 
        if var_2 != None:
            ind = ind+1
            Value = Value + var_2 
        if var_3 != None:
            ind = ind+1
            Value = Value + var_3 
        if ind == 0:
            var_final = None            
        else: 
            var_final = Value/ind
            
    elif len(args_) == 3 :
        
        ind = 0
        Value = 0
        var_2 = args_[0] 
        var_3 = args_[1] 
        var_4 = args_[2] 
        
        if var_1 != None:
            ind = ind+1
            Value = Value + var_1 
        if var_2 != None:
            ind = ind+1
            Value = Value + var_2 
        if var_3 != None:
            ind = ind+1
            Value = Value + var_3 
        if var_4 != None:
            ind = ind+1
            Value = Value + var_4 
        if ind == 0:
            var_final = None            
        else: 
            var_final = Value/ind
        
    return var_final

# %% Function to create day index 
    
def day_index():
    
    day_c=[]
    
    cont = 0
    
    j = 0

    data = [365,365,366,365,196]
    
    for i in range(1657):
    
        day_c.append(i-cont+1)
        
        if (i - cont + 1) == data[j] :
            
            cont = cont + data[j]
            j=j+1
            
    return day_c

# %% Function to organize into 

def order_inputs( var_1, var_2, var_3, var_4 , var_5, var_6, output):
    
    var_final=[]
    var=[]
    out_final = []
    
    if len(var_1[0]) == len(var_2[0]) and len(var_1[0]) == len(var_3[0]) and len(var_1[0]) == len(var_4[0]):  
        
        day_i = day_index()
        
        Previous_p = 0
        Previous_h = 0
        Previous_s = 0
        Previous_pa = 0
        
        for i in range(len(var_1[0])):
            
            list_in=[]
             
            # temperature 
            temp_1 = check_none(var_1[2],i)
            list_in.append(temp_1)
            temp_2= check_none(var_2[2],i)
            list_in.append(temp_2)
            temp_3 = check_none(var_3[2],i)
            list_in.append(temp_3)
            temp_4 = check_none(var_4[2],i)
            list_in.append(temp_4)
            
            
            # precipitation 
            Precip123 = average(var_1[4][i],var_2[4][i],var_3[4][i])
            if Precip123 == None:
                Precip123 = Previous_p
            Previous_p = Precip123
            list_in.append(Precip123)
            
            Precip4 =check_none(var_4[4], i)
            list_in.append(Precip4)
            
            # humidity 
            Hum12 = average(var_1[3][i],var_2[3][i])
            if Hum12 == None:
                Hum12 = Previous_h
            Previous_h = Hum12
            list_in.append(Hum12)
            
            Hum3=check_none(var_3[3], i)
            list_in.append(Hum3)
            Hum4=check_none(var_4[3], i)
            list_in.append(Hum4)
            
            # solar radiation 
            SolarR = average(var_1[5][i], var_2[5][i], var_3[5][i], var_4[5][i])
            if SolarR == None:
                SolarR = Previous_s
            Previous_s = Hum12
            list_in.append(SolarR)
            
            # pressure 
            Press = average(var_1[6][i], var_2[6][i], var_3[6][i], var_4[6][i]) 
            if Press == None:
                Press = Previous_pa
            Previous_pa = Press
            list_in.append(Press)
            
            # station 544
            list_in.append(var_5[3][i])
            
            # station 546
            list_in.append(var_6[3][i])
            
            var.append(list_in)
            
        for i in range(2,1657):
            
            list_in = []
            
            list_in =[day_i[i]] + var[i-2]+var[i-1]+var[i]
            
            var_final.append(list_in)
            
            out_final.append(output[4][i])
            
    else:
        
        var_final=None
        
        print('Error vectors not the same size')
        
    return var_final, out_final

# %% Execute
    
input_var, output_var = order_inputs( Met_1, Met_2, Met_3, Met_4, St_544, St_546, Portodemouros)

pr.dump ( [input_var, output_var] , open( "Data_model_1.p", "wb" ) )