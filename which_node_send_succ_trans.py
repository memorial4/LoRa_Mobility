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

# for all nodes
for node in range(5): 
    # get output from grep commands and transform into utf8
    data = subprocess.Popen(['grep "LoRaGWRadio Reception ended: successfully for" logn5tractormobgw1-29.elog | grep "transmissionId"'], shell=True, stdout = subprocess.PIPE)
    data1 = subprocess.Popen([f'grep "Transmission started:" logn5tractormobgw1-29.elog | grep "transmitterId = {node}" | grep "id"'], shell=True, stdout = subprocess.PIPE)
    output = data.stdout.read().decode("utf-8")
    output1 = data1.stdout.read().decode("utf-8")


    rids = []
    intersection = []
    tids = set() # node duplicates distinct and unordered
    idas = set()


    print('{}Searching logfile...{}'
                .format(bcolors.HEADER, bcolors.ENDC))
    # split grep command output on transmissionid and get second part
    for i, item in enumerate(output.split("transmissionId")):
        if i == 0:
            continue
        
        # get 1st and 2nd numbers with regular expressions
        tid = re.search(r'\d+', item).group()
        rid = re.search(r'\d+', item[10:]).group()
        
        # check for successful transmissions by matching the previous in the other grep command 
        for j, item in enumerate(output1.split("id")):
                if j == 0:
                    continue

                ida = re.search(r'\d+', item).group()
                idas.add(ida)
                #print('Ropaloooooooo', ida)

                if ida == tid :
                    print(f'Node {node} send and Found ID: {ida}')
                    intersection.append(ida)


        #print(f'TID: {tid} \t RID: {rid}')
        rids.append(rid)
        tids.add(tid)            


    
    print(f'Intersection on node {node}: {len(intersection)}')

print(f'\nCummulative successfull transmission count: {len(rids)}\nIndividual count: {Counter(rids)}')
print(f'Successfull non-duplicated transmissions: {len(tids)}')    

data = subprocess.Popen(['cat mystats.txt'], shell=True, stdout = subprocess.PIPE)
output = data.stdout.read().decode("utf-8")
total = int(re.search(r'\d+', output).group())

print(f'Total transmissions: {total}')

percentage = len(tids) / total * 100
print('{}{}Successfull transmission percentage: {:.2f}%{}{}'
            .format(bcolors.BOLD, bcolors.OKGREEN, percentage, bcolors.ENDC, bcolors.ENDC))
