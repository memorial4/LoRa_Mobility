import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns
import matplotlib as mpl
#plt.style.use('seaborn-whitegrid')
import numpy as np
import matplotlib.cm


 
node_stats = pd.read_excel('merged_circle.xlsx', index_col=[0])
# for x nodes
x=16
node_list=[]
for i in range(x):
  node_list.append(node_stats.loc[node_stats['node'] == i])

node_percentages=[]
for item in node_list:
  node_percentages.append(item['Percentage'].to_numpy())

node_averages=[]
for item in node_percentages:
  node_averages.append(np.mean(item))

node_stds = []
for item in node_percentages:
  node_stds.append(np.std(item))

nodes=[]
for i in range(x):
  nodes.append(str(i))

x_pos = np.arange(len(nodes))
CTEs = node_averages
error = node_stds

sns.set()
fig, ax = plt.subplots(figsize=(12, 6))
plt.ylim([0, 100])

df = pd.DataFrame(node_averages,columns=['Percentage'])
#print(df)
df.to_excel("final_percentagescircle.xlsx") 

pps = ax.bar(x_pos, CTEs, yerr=error, align='center', alpha=0.5, ecolor='maroon', capsize=10, width = 0.5)
for p in pps:
    height = p.get_height()
    ax.text(x=p.get_x() + p.get_width() / 2, y=height+ 4, s="{:.2f}%".format(height), ha='center',  weight='bold')

ax.text(13.1, 90, 'Jain\'s fairness \nindex = 0.81', size=15, color='purple') 
ax.text(13.1, 70, 'Overall PDR = \n17.21%', size=15, color='black')   

ax.set_ylabel('Packet Delivery Rate - PDR (%)')
ax.set_xticks(x_pos)
ax.set_xticklabels(nodes)
ax.set_xlabel('Nodes')
ax.set_title('Successful Rate on each node')


# Save the figure and show
plt.tight_layout()
plt.savefig('bar_plot_with_error_bars.png')
plt.show()
 
    