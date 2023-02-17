import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns
import matplotlib as mpl
#plt.style.use('seaborn-whitegrid')
import numpy as np
import matplotlib.cm


#throughputs = [0.4244, 0.4942, 0.3314, 0.3140, 0.4128]

df1=pd.read_excel('output_nodes_stats_1gw.xlsx', index_col=0)
throughputs=df1['Percentage'].div(100).round(4).tolist()
throughputs

def jains_fairness_index(throughputs):
        
    n = len(throughputs)
    temp = sum([ (x**2) for x in throughputs])
    jains_index = sum(throughputs) ** 2 / (n * temp)
 
    #jains_index = sum(throughputs)**2 /(n*sum([s**2 for s in throughputs]))

    return jains_index


jains_index = jains_fairness_index(throughputs)
print(jains_index)

 

 
    