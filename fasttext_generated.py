# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 15:22:57 2018

@author: khanhle
"""
import re

fout = open('enhancer_output1.txt','w')

spe_character = ['X','U','B','Z']
#spe_character = []

fpos = 'enhancer.txt'
with open(fpos) as f:
    for line in f:
        if (line.startswith('>') == False) and (any(x in line for x in spe_character) == False):
            sequence = ''.join(line).replace('\n','')
            print(sequence)
            fout.write('__label__positive ' + ' '.join(list(sequence)) + '\n')
            
fneg = 'non.txt'
with open(fneg) as f:
    for line in f:
        if len(line.strip()) > 0:
            if (line.startswith('>') == False) and (any(x in line for x in spe_character) == False):
    #        if (line.startswith('>') == False) and (any(x in line for x in spe_character) == False):
                sequence = ''.join(line).replace('\n','')
                print(sequence)
                fout.write('__label__negative ' + ' '.join(list(sequence)) + '\n')
            
fout.close()