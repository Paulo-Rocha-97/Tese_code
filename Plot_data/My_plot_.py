## This function creates and stores a graph with a predifned settings
    
# path = str directory of the storage place
# Name = str refering to the subject of the plot
# Time = vector of time same length as args*
# Y_name = str the variable being plotted 
# args* = vector one or several vecrtor same length as the time vector

def make_plot_line( path, Name, Time, Y_name, *args ):
    
    import os
    import matplotlib 
    import matplotlib.pyplot as plt
    import matplotlib.dates as mdates
    import matplotlib.cbook as cbook
    
    years = mdates.YearLocator()   # every year
    months = mdates.MonthLocator()  # every month
    Month = mdates.DateFormatter('%Y')
    
    plt.rcParams['text.usetex'] = True
    import matplotlib.pyplot as plt
    plt.rcParams.update({'font.size': 13})

    comp = len(args)
    
    if comp < 8: 
    
        color = ['r','r','b','b','g','g','c','c','m','m','y','y','k','k']

    else: 
        n = comp/8
        n_int = int(n)
        if n > n_int:
            n_int = n_int+1 
            
        color = ['r','r','b','b','g','g','c','c','m','m','y','y','k','k']*n_int
    
    if comp == 1:
        
        Y = Y_name.split('(')
        Y_ = Y[0]
        Y_=Y_.replace('/','_')
        Y_=Y_.replace('$','')         
        
        name = Name + '_' + Y_.replace(' ','_')

        plt.plot(Time, args[0],'r', linewidth=1.0, label = Y_name)

    else:
        
        Y = Y_name.split('(')
        Y_ = Y[0]
        Y_=Y_.replace('/','_')        
        Y_=Y_.replace('$','')         

        
        fig,ax=plt.subplots()
        
        name = Name
        
        for i in range(comp-1):
            if (i % 2) == 0:
                ax.plot(Time, args[i], color[i], linewidth=0.8, label = args[i+1])
        
        plt.legend()
    
    ax.xaxis.set_minor_locator(months)
    ax.xaxis.set_major_locator(years)
    ax.xaxis.set_major_formatter(Month)

    plt.xlabel('Date')
    plt.ylabel(Y_name)
    plt.grid(linewidth=1.0)

    if not os.path.exists(path):
        os.makedirs(path)
    
    plt.tight_layout()
    plt.savefig(path+'/'+name+'.png',dpi=300)
    print(path+'/'+name+'.png')
    plt.close()
    
def make_plot_marker_line_( path, Name, Time, Y_name, *args ):
    
    import os
    import matplotlib.pyplot as plt
    
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

        plt.plot(Time, args[0],'r', linewidth=1.0, label = Y_name,marker='o')

    else:        
        
        Y = Y_name.split('(')
        Y_ = Y[0]
        Y_=Y_.replace('/','_')        
        
        name = Name
        
        for i in range(comp-1):
            if (i % 2) == 0:
                plt.plot(Time, args[i], color[i], linewidth=1.0, label = args[i+1],marker='o')

        plt.legend()


    plt.xlabel('Date')
    plt.ylabel(Y_name)
    plt.grid()

    if not os.path.exists(path):
        os.makedirs(path)
    
    plt.tight_layout()
    plt.savefig(path+'/'+name+'.png', dpi=3000)
    plt.close()