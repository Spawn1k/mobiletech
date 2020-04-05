import os
from docxtpl import DocxTemplate

os.system('cd ../lab1/ && python3 Mobile.py')
f = open('../lab1/schet.txt', 'r')
tel = float(f.read())
f.close()
os.system('cd ../lab2/ && python3 Mobile2.py')
f = open('../lab2/schet2.txt', 'r')
inet = float(f.read())
f.close()
sch = tel + inet
doc = DocxTemplate('template.docx')
context = {'number': '231', 'date': '07.04.2020', 'bank': 'Настоящий Банк', 'bik': '12345678', 'inn': '123456789', 'kpp': '01234567', 'sch1': '12348765', 'sch2': '87651234', 'supplier': 'БестТелеком', 'customer': 'Богачев Богач Богачевич', 'osn': 'Договор 3 от 15 июля 1960г', 'service': 'Связь и интернет', 'scount': '1', 'sed': '1', 'price': f'{sch}', 'finsum': f'{sch}', 'nds': '13%', 'oplata': f'{sch}', 'director': 'Жадный В.А.', 'buch': 'Петрова О.Е.'}
doc.render(context)
doc.save('template-final.docx')
os.system('abiword --to=pdf template-final.docx 2>/dev/null')
