import re
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

data = subprocess.Popen(['grep "LoRaGWRadio Reception ended: successfully for" log_N5stationaryGW2-29.elog  | grep "transmissionId"'], shell=True, stdout = subprocess.PIPE)
output = data.stdout.read().decode("utf-8")

rids = []
tids = set()

print('{}Searching logfile...{}'
            .format(bcolors.HEADER, bcolors.ENDC))
for i, item in enumerate(output.split("transmissionId")):
    if i == 0:
        continue
    tid = re.search(r'\d+', item).group()
    rid = re.search(r'\d+', item[10:]).group()
    print(f'TID: {tid} \t RID: {rid}')
    rids.append(rid)
    tids.add(tid)

print(f'\nCummulative successfull transmission count: {len(rids)}\nIndividual count: {Counter(rids)}')
print(f'Successfull non-duplicated transmissions: {len(tids)}')

data = subprocess.Popen(['cat mystats.txt'], shell=True, stdout = subprocess.PIPE)
output = data.stdout.read().decode("utf-8")
total = int(re.search(r'\d+', output).group())

print(f'Total transmissions: {total}')

percentage = len(tids) / total * 100
print('{}{}Successfull transmission percentage: {:.2f}%{}{}'
            .format(bcolors.BOLD, bcolors.OKGREEN, percentage, bcolors.ENDC, bcolors.ENDC))
