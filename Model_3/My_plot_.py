## This function creates and stores a graph with a predifned settings
    
# path = str directory of the storage place
# Name = str refering to the subject of the plot
# Time = vector of time same length as args*
# Y_name = str the variable being plotted 
# args* = vector one or several vecrtor same length as the time vector

def make_plot_point( path, Name, X, Y_1, Y_2, Y_3, X_Axis, Y_name_1, Y_name_2, Y_name_3, file_name ):
    
    import os
    import matplotlib.pyplot as plt
    
              
    fig, (ax1, ax2, ax3) = plt.subplots(3, sharex=True)
    fig.suptitle(Name)
    
    ax1.plot(X, Y_1, 'ro', linewidth=2.0, label = Y_name_1)
    ax2.plot(X, Y_2, 'bo', linewidth=2.0, label = Y_name_2)
    ax2.axhline(Y_2[0], color='y', linestyle='-', linewidth=2.0)
    ax3.plot(X, Y_3, 'go', linewidth=2.0, label = Y_name_3)
    ax3.axhline(Y_3[0], color='y', linestyle='-', linewidth=2.0)
    
    plt.xticks(X, X_Axis)
    ax1.set_ylabel(Y_name_1)
    ax2.set_ylabel(Y_name_2)
    ax3.set_ylabel(Y_name_3)
    
    plt.grid(linewidth=1.0)

    if not os.path.exists(path):
        os.makedirs(path)

    plt.savefig(path+'/'+file_name+'.png')
    
def make_plot_point_nosave( Name, X, Y_1, Y_2, Y_3, X_Axis, Y_name_1, Y_name_2, Y_name_3, file_name ):
    
    import matplotlib.pyplot as plt
    
              
    fig, (ax1, ax2, ax3) = plt.subplots(3, sharex=True)
    fig.suptitle(Name)
    
    ax1.plot(X, Y_1, 'ro', linewidth=1.0, label = Y_name_1)
    ax2.plot(X, Y_2, 'bo', linewidth=1.0, label = Y_name_2)
    ax2.axhline(Y_2[0], color='y', linestyle='-', linewidth=1.0)
    ax3.plot(X, Y_3, 'go', linewidth=1.0, label = Y_name_3)
    ax3.axhline(Y_3[0], color='y', linestyle='-', linewidth=1.0)
    
    plt.xticks(X, X_Axis)
    ax1.set_ylabel(Y_name_1)
    ax2.set_ylabel(Y_name_2)
    ax3.set_ylabel(Y_name_3)
    
    plt.grid(linewidth=0.5)


def make_plot_line( path, Name, Time, Name_time, Y_name, *args ):
    
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
    

    if comp == 1:
        
        Y = Y_name.split('(')
        Y_ = Y[0]
        Y_=Y_.replace('/','_')        
        
        name = Name + '_' + Y_.replace(' ','_')

        plt.plot(Time, args[0],'r', linewidth=1.0, label = Y_name)

    else:
        
        Y = Y_name.split('(')
        Y_ = Y[0]
        Y_=Y_.replace('/','_')        
        
        name = Name + '_' + Y_.replace(' ','_') + 'Compare'
        
        for i in range(comp-1):
            if (i % 2) == 0:
                plt.plot(Time, args[i], color[i], linewidth=1.0, label = args[i+1])

    plt.xlabel(Name_time)
    plt.ylabel(Y_name)
    plt.grid(linewidth=0.5)
    plt.legend()
    plt.xticks(rotation=30, ha='right')

    if not os.path.exists(path):
        os.makedirs(path)

    plt.savefig(path+'/'+name+'.png',dpi =300,bboxinches='tight')
    plt.close()
    
def make_plot_line_nosave( path, Name, Time, Name_time, Y_name, *args ):
    
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
    
    if comp == 1:
        
        Y = Y_name.split('(')
        Y_ = Y[0]
        Y_=Y_.replace('/','_')        
        
        name = Name + '_' + Y_.replace(' ','_')

        plt.plot(Time, args[0],'r', linewidth=1.0, label = Y_name)

    else:
        
        Y = Y_name.split('(')
        Y_ = Y[0]
        Y_=Y_.replace('/','_')        
        
        Name = Name + '_' + Y_.replace(' ','_') + 'Compare'
        
        for i in range(comp-1):
            if (i % 2) == 0:
                plt.plot(Time, args[i], color[i], linewidth=1.0, label = args[i+1])

    plt.xlabel(Name_time)
    plt.ylabel(Y_name)
    plt.grid(linewidth=0.5)
    plt.xticks(rotation=30, ha='right')
    plt.legend()
    plt.show()
