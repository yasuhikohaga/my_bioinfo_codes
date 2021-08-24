#!/usr/bin/env python3

import csv

file = open('/home/haga37/PC9_gefti_GEX/working/2-2-1.csv', 'w')

w = csv.writer(file)

w.writerow(['fastqs','sample','library_type'])
w.writerow(['/home/haga37/PC9_gefti_GEX/210818_A01297_0137_AHJ7N5DRXY_ATAC/ATAC_fastq/2-2-1','2-2-1','Gene Expression'])
w.writerow(['/home/haga37/PC9_gefti_GEX/210818_A01297_0138_BHHHWTDRXY_GEX/GEX_fastq/2-2-1','2-2-1','Chromatin Accessibility'])

file.close()
