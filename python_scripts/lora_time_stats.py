import re
import seaborn as sns
import matplotlib.pyplot as plt
import subprocess
from collections import Counter

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

data = subprocess.Popen(['grep "Transmission started:" log_N5stationaryGW2-29.elog | grep "startTime"'], shell=True, stdout = subprocess.PIPE)
output = data.stdout.read().decode("utf-8")

tids = set()

print('{}Searching logfile...{}'
            .format(bcolors.HEADER, bcolors.ENDC))
for i, item in enumerate(output.split("startTime")):
    if i == 0:
        continue
    tid = re.search(r'\d+', item).group()
    print(f'TIMESTAMP: {int(tid)}')
    tids.add(int(tid))


data = subprocess.Popen(['cat mystats.txt'], shell=True, stdout = subprocess.PIPE)
output = data.stdout.read().decode("utf-8")
total = int(re.search(r'\d+', output).group())

print(f'Total transmissions: {total}')

percentage = len(tids) / total * 100
print('{}{}Successfull transmission percentage: {:.2f}%{}{}'
            .format(bcolors.BOLD, bcolors.OKGREEN, percentage, bcolors.ENDC, bcolors.ENDC))

#print(sorted(tids))


#plt.hist(tids, 1000, density=True, facecolor='g', alpha=0.75)
plt.xlabel('TIMESTAMP')
plt.ylabel('Packets')
plt.title('Timestamps of sent packets')
#plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
#plt.xlim(400, 9000)
#plt.ylim(0, 10000)
#plt.grid(True)
#plt.show()

sns.set(style="darkgrid")
df = sns.load_dataset('iris')
sns.histplot(tids, bins=100, kde=True)
plt.xticks(range(0, 86400, 1000), rotation=90 )

#sns.histplot(tids, x="TIMESTAMP", bins=20, kde=True)
plt.show()
