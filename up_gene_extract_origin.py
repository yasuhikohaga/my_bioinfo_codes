#!/usr/bin/env python3

import pandas as pd

df = pd.read_csv('/Users/yasuhikohaga/desktop/PC9_GEX-ATAC/wnn_analysis/wnn/cluster0/cluster0_deg.csv')

#extract up-regulated gene
df = df[df.avg_log2FC > 0]

#save up-regurated gene as .csv
df.to_csv('/Users/yasuhikohaga/desktop/PC9_GEX-ATAC/wnn_analysis/wnn/cluster0/cluster0_up_deg.csv')
