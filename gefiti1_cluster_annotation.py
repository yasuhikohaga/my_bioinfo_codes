#/usr/bin/env python3

import pandas as pd

#import gefiti1 deg
df = pd.read_csv('/Users/yasuhikohaga/Desktop/PC9_gefti_GEX/2-2-1_Exon/wnn解析/cluster/cluster9/cluster9_up_deg.csv')

#import gefiti1_2nd deg as df
df_0 = pd.read_csv('/Users/yasuhikohaga/Desktop/PC9_gefti_GEX/2-2_exon_2回目/wnn解析/cluster/cluster0/cluster0_up_deg.csv')
df_0 = df_0["gene"]
df_1 = pd.read_csv('/Users/yasuhikohaga/Desktop/PC9_gefti_GEX/2-2_exon_2回目/wnn解析/cluster/cluster1/cluster1_up_deg.csv')
df_1 = df_1["gene"]
df_2 = pd.read_csv('/Users/yasuhikohaga/Desktop/PC9_gefti_GEX/2-2_exon_2回目/wnn解析/cluster/cluster2/cluster2_up_deg.csv')
df_2 = df_2["gene"]
df_3 = pd.read_csv('/Users/yasuhikohaga/Desktop/PC9_gefti_GEX/2-2_exon_2回目/wnn解析/cluster/cluster3/cluster3_up_deg.csv')
df_3 = df_3["gene"]
df_4 = pd.read_csv('/Users/yasuhikohaga/Desktop/PC9_gefti_GEX/2-2_exon_2回目/wnn解析/cluster/cluster4/cluster4_up_deg.csv')
df_4 = df_4["gene"]
df_5 = pd.read_csv('/Users/yasuhikohaga/Desktop/PC9_gefti_GEX/2-2_exon_2回目/wnn解析/cluster/cluster5/cluster5_up_deg.csv')
df_5 = df_5["gene"]
df_6 = pd.read_csv('/Users/yasuhikohaga/Desktop/PC9_gefti_GEX/2-2_exon_2回目/wnn解析/cluster/cluster6/cluster6_up_deg.csv')
df_6 = df_6["gene"]
df_7 = pd.read_csv('/Users/yasuhikohaga/Desktop/PC9_gefti_GEX/2-2_exon_2回目/wnn解析/cluster/cluster7/cluster7_up_deg.csv')
df_7 = df_7["gene"]
df_8 = pd.read_csv('/Users/yasuhikohaga/Desktop/PC9_gefti_GEX/2-2_exon_2回目/wnn解析/cluster/cluster8/cluster8_up_deg.csv')
df_8 = df_8["gene"]
df_9 = pd.read_csv('/Users/yasuhikohaga/Desktop/PC9_gefti_GEX/2-2_exon_2回目/wnn解析/cluster/cluster9/cluster9_up_deg.csv')
df_9 = df_9["gene"]
df_gefiti1_2nds = [df_0, df_1, df_2, df_3, df_4, df_5, df_6, df_7, df_8, df_9]

#count same genes
for f in df_gefiti1_2nds:
	n=0
	m=0
	for gene in f:
		o=0
		if df[df["gene"] == gene.lstrip()].empty:continue
		else:
			n=n+1
	o=n/len(f)
	print(o)
