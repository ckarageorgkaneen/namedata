# coding: utf-8
import csv
import random
with open('female-japanese.txt') as femalejapfile, open('male-japanese.txt') as malejapfile, open('japanese.txt', 'w+') as outfile:    
    femreader = csv.reader(femalejapfile, delimiter=' ')
    malereader = csv.reader(malejapfile, delimiter=' ')
    names = []
    for reader in [femreader, malereader]:
        for row in reader:
            name = ', '.join(row).split(',')[-1].strip('/').strip()
            if name.isalpha():
                names.append(name)
    random.shuffle(names)
    for name in names:
        outfile.write(f'{name}\n')
        
