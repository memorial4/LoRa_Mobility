import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns

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
    plt.title("Coverage of GW with SF={x:.0f} and TP={y:.0f}".format(x=df['TP'][0],y=df['SF'][0]))
    #plt.legend(["SF={x:.0f} and TP={y:.0f}".format(x=df['TP'][0],y=df['SF'][0])])

################################################################################
fig, ax = plt.subplots()

for df in df_list:
 
    #df.hist(df.GW, weights=df.Percentage)

    df.plot( x='GW', y='Percentage',style='.-', ax=ax)

    plt.annotate(df.Coverage[-1], xy=(df.GW[-1],df.Percentage[-1]), xytext=(df.GW[-1]-40, df.Percentage[-1]+20),
            arrowprops=dict(facecolor='black', shrink=0.05),ha='left')
    #plt.annotate(df.Coverage[-1], (df.GW[-1]-15, df.Percentage[-1]+5),ha='left')
    plt.xlabel('Distance between Node and GW (m)')
    plt.ylabel('Successful Transmissions (%)')
    plt.title("Coverage of GW") #with SF={x:.0f} and TP={y:.0f}".format(x=df['TP'][0],y=df['SF'][0]))
    plt.legend(["SF={x:.0f} and TP={y:.0f}".format(x=df['TP'][0],y=df['SF'][0])])

##################################################################################
    #df.hist(column='GW')
    
'''sns.set(style="darkgrid")
fig, ax = plt.subplots()
for df in df_list:
    #df.hist(df.GW, weights=df.Percentage)
    df.plot( x='GW', y='Percentage',style='.-',ax=ax)
    df.hist(column='GW')'''

plt.show()    