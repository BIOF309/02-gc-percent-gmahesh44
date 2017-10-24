dna_string = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
print(dna_string)
ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT
dna_list = list(dna_string)
print(dna_list)
['A', 'C', 'T', 'G', 'A', 'T', 'C', 'G', 'A', 'T', 'T', 'A', 'C', 'G', 'T', 'A', 'T', 'A
', 'G', 'T', 'A', 'T', 'T', 'T', 'G', 'C', 'T', 'A', 'T', 'C', 'A', 'T', 'A', 'C', 'A',
'T', 'A', 'T', 'A', 'T', 'A', 'T', 'C', 'G', 'A', 'T', 'G', 'C', 'G', 'T', 'T', 'C', 'A'
, 'T']

dna_list.count("G")
8

dna_list.count("C")
9

len(dna_list)
54

gc_count = dna_list.count("G") + dna_list.count("C")

gc_frac = float(gc_count) / len(dna_list)

100 * gc_frac
31.48148148148148
