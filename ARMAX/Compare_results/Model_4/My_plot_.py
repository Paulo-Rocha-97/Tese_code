## This function creates and stores a graph with a predifned settings
    
# path = str directory of the storage place
# Name = str refering to the subject of the plot
# Time = vector of time same length as args*
# Y_name = str the variable being plotted 



def make_plot_line( path, Name, Time, Name_time, Y_name, *args ):
    
    import os
    import matplotlib 
    import matplotlib.pyplot as plt
    import matplotlib.dates as mdates
    import matplotlib.cbook as cbook
    
    years = mdates.YearLocator()   # every year
    months = mdates.MonthLocator()  # every month
    Month = mdates.DateFormatter('%m-%Y')
    
    font = {'size'   : 13}
    matplotlib.rc('font', **font)
    
    comp = len(args)
    
    if comp < 8: 
    
        color = ['k','k','b','b','r','r','g','g','m','m','y','y','c','c']

    else: 
        n = comp/8
        n_int = int(n)
        if n > n_int:
            n_int = n_int+1 
            
        color = ['k','k','b','b','g','g','r','r','m','m','y','y','c','c']*n_int

    if comp == 1:
        
        print('erro')

    else:
        
        fig, [ax1,ax2] = plt.subplots(2,1,figsize=[7,5.5],sharex = True, gridspec_kw={'height_ratios': [2, 1]})

        Y = Y_name.split('(')
        Y_ = Y[0]
        Y_=Y_.replace('/',' ')
        Y_=Y_.replace('$','')        
        
        name = Name
        
        for i in range(comp-1):
            if (i % 2) == 0:
                ax1.plot(Time, args[i], color[i], linewidth=1.0, label = args[i+1])
                
                if i != 0:
                    
                    difference = []
                    for j in range(len(args[i])):
                        difference.append(float(args[0][j])-float(args[i][j]))
                    
                    ax2.scatter(Time,difference,c = color[i], s =1, label = args[i+1])                       
            
    ax1.legend()
    ax2.legend()
    ax2.set_xlabel(Name_time)
    ax1.set_ylabel(Y_name)
    ax2.set_ylabel('Residuals')
    ax1.grid(linewidth=0.5)
    ax2.grid(linewidth=0.5)
    ax1.xaxis.set_major_locator(months)
    ax1.set_xticks(ax1.get_xticks()[0::2])
    ax1.xaxis.set_major_formatter(Month)

    plt.tight_layout()
    plt.savefig(path+'/'+name+'.png', dpi = 300, bboxinches = 'tight')
    plt.close()
    
