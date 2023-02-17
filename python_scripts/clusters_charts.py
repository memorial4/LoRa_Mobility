import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors


# set width of bar
barWidth = 0.25
fig, ax = plt.subplots(figsize =(10, 6))
plt.ylim([0, 100])
width = 0.2


# set height of bar
C1 = [20.63, 28.40]
C2 = [30.04, 33.18]
C3 = [20.46, 25.83]
avg = [22.65, 28.31]

# Set position of bar on X axis
br1 = np.arange(len(C1))
br2 = [x + barWidth for x in br1]
br3 = [x + barWidth for x in br2]

# Make the plot
pps1 = plt.bar(br1, C1, color ='m', width = barWidth,
    edgecolor ='grey', label ='C1')
pps2 = plt.bar(br2, C2, color ='c', width = barWidth,
    edgecolor ='grey', label ='C2')
pps3 = plt.bar(br3, C3, color ='y', width = barWidth,
    edgecolor ='grey', label ='C3')

pps4 = plt.bar([i for i in br2], avg, color ='salmon', width = 0.15,
    edgecolor ='grey', label ='avg')

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
#ax.invert_yaxis()


# Adding Xticks
ax.set_title('Successful Rate on each cluster')
plt.ylabel('Packet Delivery Rate - PDR (%)', fontweight ='bold', fontsize = 15)
#ax.text(80, 80, 'Overall PDR = \n28.31%', size=15, color='black')

#plt.xlabel('Branch', fontweight ='bold', fontsize = 15)
#plt.xlabel('3rd Scenario', fontweight ='bold', fontsize = 15)
plt.xticks([r + barWidth for r in range(len(C1))],
    ['Stationary gateway', 'Circle mobility'], fontweight ='bold')

plt.legend()
plt.show()
