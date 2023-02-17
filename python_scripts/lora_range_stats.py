import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns
import matplotlib as mpl
#plt.style.use('seaborn-whitegrid')
import numpy as np
import matplotlib.cm


df1=pd.read_excel('ThesisData.xlsx', index_col=0)

df1.Coverage=df1.Coverage.fillna(0)
df1.Coverage=df1.Coverage.astype(int)

df_list=[]
for i in df1['dfid'].unique():
    x='df'+str(i)
    x=df1[df1['dfid'] == i]
    df_list.append(x)
    
sns.set(style="darkgrid")
###########################################################################
for df in df_list:
 
    #df.hist(df.GW, weights=df.Percentage)
    df.plot( x='GW', y='Percentage',style='.-')
    plt.annotate(df.Coverage[-1], xy=(df.GW[-1],df.Percentage[-1]), xytext=(df.GW[-1]-40, df.Percentage[-1]+20),
            arrowprops=dict(facecolor='black', shrink=0.05),ha='left')
    #plt.annotate(df.Coverage[-1], (df.GW[-1]-15, df.Percentage[-1]+5),ha='left')
    plt.xlabel('Distance between Node and GW (m)')
    plt.ylabel('Successful Transmissions (%)')
    plt.title(r"Coverage of GW with $SF={x:.0f}$ and $TP={y:.0f}$".format(x=df['SF'][0],y=df['TP'][0]))
    #plt.legend([r"$SF={x:.0f}$ and $TP={y:.0f}$".format(x=df['SF'][0],y=df['TP'][0])])

################################################################################
NUM_COLORS = 12 
fig, ax = plt.subplots()
cm = plt.get_cmap('nipy_spectral') # tab20b
ax.set_prop_cycle('color', [cm(1.*i/NUM_COLORS) for i in range(NUM_COLORS)])
#a = 0

for df in df_list:
 
    #df.hist(df.GW, weights=df.Percentage)

    df.plot( x='GW', y='Percentage',style='.-', ax=ax, label=r"$SF={x:.0f}$ and $TP={y:.0f}$".format(x=df['SF'][0],y=df['TP'][0]))

    #plt.annotate(df.Coverage[-1], xy=(df.GW[-1], df.Percentage[-1]), xytext=(df.GW[-1]-40, df.Percentage[-1]+20),
     #       arrowprops=dict(facecolor='black', shrink=0.05), ha='left')
    ax.annotate(df.Coverage[-1],
            xy=(df.GW[-1], df.Percentage[-1]),
            xycoords='data',
            xytext=(df.GW[-1], df.Percentage[-1]+20),
            bbox = dict(boxstyle ="round", fc ="0.8"),
            arrowprops=dict(facecolor='black', shrink=0.05))
    #plt.annotate(df.Coverage[-1], (df.GW[-1]-15, df.Percentage[-1]+5),ha='left')
    plt.xlabel('Distance between Node and GW (m)')
    plt.ylabel('Successful Transmissions (%)')
    plt.title('Coverage of GW') #with SF={x:.0f} and TP={y:.0f}".format(x=df['TP'][0],y=df['SF'][0]))
    #plt.legend(["SF={x:.0f} and TP={y:.0f}".format(x=df['SF'][0],y=df['TP'][0])])
    '''if a == 0:
        a = 1
    elif a == 1:
        a = 0'''    

##################################################################################
    #df.hist(column='GW')
    
'''sns.set(style="darkgrid")
fig, ax = plt.subplots()
for df in df_list:
    #df.hist(df.GW, weights=df.Percentage)
    df.plot( x='GW', y='Percentage',style='.-',ax=ax)
    df.hist(column='GW')'''

plt.show()    