#!/usr/bin/env python3

import pandas as pd

df = pd.read_csv('/Users/yasuhikohaga/desktop/PC9_GEX-ATAC_exon/wnn_analysis/wnn/フィルタリング変更後_解析/SeuratObjectDataExtraction/cluster5_cell_info.csv', index_col=1)

df = df.drop(columns="Unnamed: 0")

df.to_csv('/Users/yasuhikohaga/desktop/PC9_GEX-ATAC_exon/wnn_analysis/wnn/フィルタリング変更後_解析/SeuratObjectDataExtraction/cluster5_cell_info.csv')
