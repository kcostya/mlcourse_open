import os
import sys
from tqdm import tqdm
from time import time
import numpy as np
from sklearn.metrics import accuracy_score

target_tags = ['javascript', 'java', 'python', 'ruby', 'php', 'c++', 'c#', 'go', 'scala', 'swift']

def iterate_file(fin, fout):
    with open(fin, 'r') as f:
        for line in tqdm(f):
            pair = line.strip().split('\t')
            
            if len(pair) != 2:
                continue                
            
            sentence, tags = pair
            tags = set(tags.split(' '))
            tag = tags&set(target_tags)
            
            if len(tag) != 1:
                continue
            
            label = target_tags.index(tag.pop())
            sentence = sentence.replace(':', ' ').replace('|', ' ')
            vw_format = str(label) + ' | ' + sentence + '\n'
            with open(fout, 'a+') as vw_data:
                vw_data.write(vw_format)

if __name__ == "__main__":
    fin = sys.argv[1]
    fout = sys.argv[2]
    iterate_file(os.path.join('../../../mlco_data/', fin), os.path.join('../../../mlco_data/', fout))