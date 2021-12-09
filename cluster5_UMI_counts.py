#!/usr/bin/env python3

import pandas as pd

df = pd.read_csv('/Users/yasuhikohaga/desktop/PC9_GEX-ATAC_exon/wnn_analysis/wnn/フィルタリング変更後_解析/SeuratObjectDataExtraction/metadata_cluster5.csv')

df_UMI = pd.read_csv('/Users/yasuhikohaga/desktop/PC9_GEX-ATAC_exon/wnn_analysis/wnn/フィルタリング変更後_解析/SeuratObjectDataExtraction/UMI_counts.csv')
#print(df_UMI.columns)

for f in df_UMI.columns.values:
	f = f.replace('.', '-')
	if f in list(df["cell_barcode"]) or f == "gene":
		print(f)
	else:
		f = f.replace('-', '.')
		df_UMI = df_UMI.drop(columns = f)

df_UMI.to_csv('/Users/yasuhikohaga/desktop/PC9_GEX-ATAC_exon/wnn_analysis/wnn/フィルタリング変更後_解析/SeuratObjectDataExtraction/cluster5_cell_info.csv')
