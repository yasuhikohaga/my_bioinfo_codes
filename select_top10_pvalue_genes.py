#!/usr/bin/env python3

import pandas as pd

df = pd.read_csv('/Users/yasuhikohaga/Desktop/PC9_gefti_GEX/2-2-1/wnn_2-2-1/wnn_analysis_2-2-1/cluster/cluster0/cluster0_up_deg.csv')

df = df[:10]

df.to_csv('/Users/yasuhikohaga/Desktop/PC9_gefti_GEX/2-2-1/wnn_2-2-1/wnn_analysis_2-2-1/cluster/cluster0/cluster0_up_deg_top10.csv', index=False)
