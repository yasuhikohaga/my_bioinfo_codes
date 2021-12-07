#!/usr/bin/env python3

import pandas as pd

df = pd.read_csv('/Users/yasuhikohaga/desktop/PC9_GEX-ATAC_exon/wnn_analysis/wnn/フィルタリング変更後_解析/SeuratObjectDataExtraction/metadata.csv')

df = df[df.seurat_clusters == 5]

df.to_csv('/Users/yasuhikohaga/desktop/PC9_GEX-ATAC_exon/wnn_analysis/wnn/フィルタリング変更後_解析/SeuratObjectDataExtraction/metadata_cluster5.csv')
