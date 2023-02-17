import matplotlib.pyplot as plt
#import matplotlib.colors as mcolors
import numpy as np
import seaborn as sns


fig, ax = plt.subplots(figsize =(10, 6))
plt.ylim([0, 100])

# Define the data for each bar chart
bar1_data = [70.93, 41.86, 27.32, 26.74, 20.93]
bar2_data = [99.42, 76.30, 43.93, 29.47, 28.90]
bar3_data = [97.10, 84.39, 73.98, 51.44, 38.15]
bar4_data = [94.76, 81.97, 84.88, 70.93, 47.67]
bar5_data = [15.69, 17.44, 27.90, 41.86, 48.83]

# Define the X-axis labels
labels = ['r = 100m', 'r = 200m', 'r = 300m', 'r = 400m', 'r = 500m']

# Plot the bar charts
x = range(len(bar1_data))
bar_width = 0.1

pps1 = plt.bar(x, bar1_data, bar_width, color='skyblue', label='Node 1', edgecolor ='grey')
pps2 = plt.bar([i + bar_width for i in x], bar2_data, bar_width, color='skyblue', label='Node 2', edgecolor ='grey')
pps3 = plt.bar([i + bar_width*2 for i in x], bar3_data, bar_width, color='skyblue', label='Node 3', edgecolor ='grey')
pps4 = plt.bar([i + bar_width*3 for i in x], bar4_data, bar_width, color='skyblue', label='Node 4', edgecolor ='grey')
pps5 = plt.bar([i + bar_width*4 for i in x], bar5_data, bar_width, color='lightcoral', label='Node 5', edgecolor ='grey')
'''
for p in pps1:
    height = p.get_height()
    ax.text(x=p.get_x() + p.get_width() / 2, y=height+ 4, s="{:.2f}%".format(height), ha='center',  weight='bold')

for p in pps2:
    height = p.get_height()
    ax.text(x=p.get_x() + p.get_width() / 2, y=height+ 4, s="{:.2f}%".format(height), ha='center',  weight='bold')

for p in pps3:
    height = p.get_height()
    ax.text(x=p.get_x() + p.get_width() / 2, y=height+ 4, s="{:.2f}%".format(height), ha='center',  weight='bold')


for p in pps4:
    height = p.get_height()
    ax.text(x=p.get_x() + p.get_width() / 2, y=height- 12, s="{:.2f}%".format(height), ha='center',  weight='bold')
'''
for p in pps5:
    height = p.get_height()
    ax.text(x=p.get_x() + p.get_width() / 2, y=height+ 2, s="{:.2f}%".format(height), ha='center',  weight='bold')

# Add X-axis labels
plt.xticks([i + bar_width*2 for i in x], labels, fontweight ='bold')

# Add a title and labels to the Y-axis
#plt.title('1st scenario increasing the radius ')
plt.ylabel('Packet Delivery Rate - PDR (%)', fontweight ='bold', fontsize = 15)

# Add a legend
plt.legend()

# Show the plot
plt.savefig('all_radius.png')
plt.show()
