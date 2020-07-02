#!/usr/bin/env python3
import csv
import os
import shutil

dance_dict  = {}

with open('train.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        
        #bypassing the headers
        if '.jpg' not in row[0]:
            pass
        else:
            try:
                dance_dict[row[1]].append(row[0])
            except:
                dance_dict[row[1]] = [row[0]]

#segregating the files acc. to dance forms
for k in dance_dict.keys():
    for v in dance_dict[k]:
        shutil.copy2('./train/'+v, './dance_forms/' + k + '/' + v) 
    