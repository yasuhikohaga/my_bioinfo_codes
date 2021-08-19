#!/usr/bi/Users/yasuhikohaga/desktop/PC9_GEX-ATAC/wnn_analysis/wnn/cluster/cluster0/n/env python3

import pandas as pd

#import cell cycle genes as data frame
df = pd.read_excel('/Users/yasuhikohaga/desktop/PC9_GEX-ATAC/wnn_analysis/wnn/gene_list/Cell_cycle_genes_from_Drop-seq_paper.xlsx', sheet_name='Gene Sets Used in Analysis')
df_G1_S = df["G1/S"].dropna(how='all')
df_S = df["S"].dropna(how='all')
df_G2_M = df["G2/M"].dropna(how='all')
df_M = df["M"].dropna(how='all')
df_M_G1 = df["M/G1"].dropna(how='all')

#import deg genes as data frame
df_deg = pd.read_csv('/Users/yasuhikohaga/desktop/PC9_GEX-ATAC/wnn_analysis/wnn/cluster/cluster0/cluster0_up_deg.csv')

#count cell cycle genes in deg
n = 0
for gene in df_G1_S:
	if df_deg[df_deg["gene"] == gene.lstrip()].empty: continue
	else:
		n = n + 1
rate_of_G1_S = n / len(df_G1_S) / len(df_deg)
G1_S = str(rate_of_G1_S) + "\t(G1/S)\n"

n = 0
for gene in df_S:
        if df_deg[df_deg["gene"] == gene.lstrip()].empty: continue
        else:
                n = n + 1
rate_of_S = n / len(df_S) / len(df_deg)
S = str(rate_of_S) + "\t(S)\n"

n = 0
for gene in df_G2_M:
        if df_deg[df_deg["gene"] == gene.lstrip()].empty: continue
        else:
                n = n + 1
rate_of_G2_M = n / len(df_G2_M) / len(df_deg)
G2_M = str(rate_of_G2_M) + "\t(G2/M)\n"

n = 0
for gene in df_M:
        if df_deg[df_deg["gene"] == gene.lstrip()].empty: continue
        else:
                n = n + 1
rate_of_M = n / len(df_M) / len(df_deg)
M = str(rate_of_M) + "\t(M)\n"

n = 0
for gene in df_M_G1:
        if df_deg[df_deg["gene"] == gene.lstrip()].empty: continue
        else:
                n = n + 1
rate_of_M_G1 = n / len(df_M_G1) / len(df_deg)
M_G1 = str(rate_of_M_G1) + "\t(M/G1)\n"

dict_result = {G1_S:rate_of_G1_S, S:rate_of_S, G2_M:rate_of_G2_M, M:rate_of_M, M_G1:rate_of_M_G1}
final_result = [G1_S, S, G2_M, M, M_G1, "\n最大は\n", max(dict_result, key=dict_result.get)]

#export the result to .txt
f = open('/Users/yasuhikohaga/desktop/PC9_GEX-ATAC/wnn_analysis/wnn/cluster/cluster0/cl0_cell_cycle_result.txt', 'w')
f.writelines(final_result)
f.close()
