#!/usr/bin/env python3

import pandas as pd

gene_list = []

#deg extraction
df = pd.read_csv('/Users/yasuhikohaga/desktop/PC9_GEX-ATAC/wnn_analysis/wnn/cluster/cluster0/cluster0_deg.csv')

#import GO gene list and extract genes
with open('/Users/yasuhikohaga/desktop/PC9_GEX-ATAC/wnn_analysis/wnn/GO_gene_list/GO_term_list_mitotic_cell_cycle_process.txt', 'r') as f:
    for gene in f:
        gene = gene.upper()
        if df[df["gene"] == gene.rstrip('\n')].empty: continue
        else:
            gene_list.append(gene.rstrip('\n'))

#export important genes
with open('/Users/yasuhikohaga/desktop/PC9_GEX-ATAC/wnn_analysis/wnn/cluster/cluster0/important_genes_of_mitotic_cell_cycle_process.txt', 'w') as g:
    for d in sorted(list(set(gene_list))):
        g.write("%s\n" % d)
