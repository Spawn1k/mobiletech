import csv

def csvpars():
    f = open('data.csv')
    reader = csv.reader(f)
    for line in reader:
        if line[1] == '933156729':
            self = line
        if line[2] == '933156729':
            pas = line
    return self, pas

def tarification(self, pas, kself, kpas, k):
    minself = float(self[3])
    minpas = float(pas[3])
    sms = int(self[4])
    sms -= 10
    if sms < 0: sms = 0
    bill = minself*kself + minpas*kpas + sms*k
    return bill
    
self, pas = csvpars()
kself = 2
kpas = 0
ksms = 1
bill = tarification(self, pas, kself, kpas, ksms)
f = open('schet.txt', 'w')
f.write(str(bill))
f.close()