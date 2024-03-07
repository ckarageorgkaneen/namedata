# coding: utf-8
import csv
import random
with open('arabic.csv') as csvfile, open('arabic.txt', 'w+') as txtfile:
    reader = csv.reader(csvfile, delimiter=' ')
    names = [', '.join(row).split(',')[0] for row in reader]
    random.shuffle(names)
    for name in names:
        if name.isalpha():
            txtfile.write(f'{name}\n')
            
