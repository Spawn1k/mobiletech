import os
from matplotlib import pyplot as plt
from matplotlib import dates
import datetime

os.system("nfdump -r track > file")
f = open('file', 'r')
d = f.read().splitlines()
f.close()
size = 0
mas = []
ox = []
j = 0
oy = []
k = -1
string = ''
fmt = dates.DateFormatter('%d-%H:%M:%S')
for r in d:
    string = ' '.join(r.split())
    mas.append(string.split())
time = mas[1][1][0:7]
#0 year+day, 1 time, 5&7 ip, 11 size
fig, ax = plt.subplots()
for i in range(1, len(mas)-5):
    if mas[i][5][0:10] == '192.0.73.2' or mas[i][7][0:10] == '192.0.73.2':
        size += int(mas[i][11])
        time = mas[i][0] + '-' + mas[i][1][0:8]
        date = datetime.datetime.strptime(time, "%Y-%m-%d-%H:%M:%S")
        #if date in ox:
        #    oy[k] = size ***for smooth graph****
        #else:
        ox.append(date)
        oy.append(size)
        #    k += 1
#print(ox, '\n', oy) debug
ax.plot(sorted(ox), sorted(oy), "-o")
ax.xaxis.set_major_formatter(fmt)
fig.autofmt_xdate()
#plt.show() debug
fig.savefig('graph.png')
f = open('schet2.txt', 'w')
value = int(oy[-1])
money = 0.5*200 + (value-200)*1
f.write(str(money))
f.close()
