## This function creates and stores a graph with a predifned settings
    
# path = str directory of the storage place
# Name = str refering to the subject of the plot
# Time = vector of time same length as args*
# Y_name = str the variable being plotted 
# args* = vector one or several vecrtor same length as the time vector

def make_plot_line( path, Name, Time, Y_name, *args ):
    
    import os
    import matplotlib.pyplot as plt
    
    plt.rcParams.update({'font.size': 80})

    comp = len(args)
    
    if comp < 8: 
    
        color = ['r','r','b','b','g','g','c','c','m','m','y','y','k','k']

    else: 
        n = comp/8
        n_int = int(n)
        if n > n_int:
            n_int = n_int+1 
            
        color = ['r','r','b','b','g','g','c','c','m','m','y','y','k','k']*n_int
    
    plt.figure(figsize=(100,50))

    if comp == 1:
        
        Y = Y_name.split('(')
        Y_ = Y[0]
        Y_=Y_.replace('/','_')        
        
        name = Name + '_' + Y_.replace(' ','_')

        plt.plot(Time, args[0],'r', linewidth=6.0, label = Y_name)

    else:
        
        Y = Y_name.split('(')
        Y_ = Y[0]
        Y_=Y_.replace('/','_')        
        
        name = Name + '_' + Y_.replace(' ','_') + 'Compare'
        
        for i in range(comp-1):
            if (i % 2) == 0:
                plt.plot(Time, args[i], color[i], linewidth=6.0, label = args[i+1])

    plt.xlabel('Date')
    plt.ylabel(Y_name)
    plt.title(Name)
    plt.grid(linewidth=5.0)
    plt.grid(linewidth=3.0)
    plt.legend(prop={'size': 60})

    if not os.path.exists(path):
        os.makedirs(path)

    plt.savefig(path+'/'+name+'.png')
    plt.close()
    
def make_plot_marker_line_( path, Name, Time, Y_name, *args ):
    
    import os
    import matplotlib.pyplot as plt
    
    # plt.rcParams.update({'font.size': 8})

    comp = len(args)
    
    if comp < 8: 
    
        color = ['r','r','b','b','g','g','c','c','m','m','y','y','k','k']

    else: 
        n = comp/8
        n_int = int(n)
        if n > n_int:
            n_int = n_int+1 
            
        color = ['r','r','b','b','g','g','c','c','m','m','y','y','k','k']*n_int
    
    plt.figure()

    if comp == 1:
        
        Y = Y_name.split('(')
        Y_ = Y[0]
        Y_=Y_.replace('/','_')        
        
        name = Name + '_' + Y_.replace(' ','_')

        plt.plot(Time, args[0],'r', linewidth=6.0, label = Y_name,marker='o')

    else:        
        
        Y = Y_name.split('(')
        Y_ = Y[0]
        Y_=Y_.replace('/','_')        
        
        name = Name + '_' + Y_.replace(' ','_') + 'Compare'
        
        for i in range(comp-1):
            if (i % 2) == 0:
                plt.plot(Time, args[i], color[i], linewidth=6.0, label = args[i+1],marker='o')

    plt.xlabel('Date')
    plt.ylabel(Y_name)
    plt.title(Name)
    plt.grid(linewidth=5.0)
    plt.grid(linewidth=3.0)
    plt.legend(prop={'size': 60})

    if not os.path.exists(path):
        os.makedirs(path)

    plt.savefig(path+'/'+name+'.png', dpi=3000)
    plt.close()