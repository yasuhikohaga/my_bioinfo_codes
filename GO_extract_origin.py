#!/usr/bin/env python3

import pandas as pd

#deg extraction
df = pd.read_csv('.csv')

#import GO gene list and extract genes
with open('.txt', 'r') as f:
    for gene in f:
        if df[df["gene"] == gene.rstrip('\n')].empty: continue
        else:
            print(gene.rstrip('\n'))
