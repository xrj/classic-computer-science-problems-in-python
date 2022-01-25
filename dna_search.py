# 没有类型提示的DNA搜索代码
from enum import IntEnum

Nuelcotide =  IntEnum('Nucleotide', ('A', 'C', 'G', 'T'))

# 原始基因字符串
gene_str = "ACGTGGCTCTCTAACGTACGTACGTACGGGGTTTATATATACCCTAGGACTCCCTTT"
def string_to_gene(s): # 读取基因字符串
    gene = []
    for i in range(0, len(s), 3):
        if (i + 2) >= len(s): # don't run off end!
            return gene
        # initialize codon out of three nucleotides
        codon = (Nuelcotide[s[i]], Nuelcotide[s[i + 1]], Nuelcotide[s[i + 2]])
        gene.append(codon) # add codon to gene
    return gene

def linear_contains(gene, key_codon):
    for codon in gene:
        if codon == key_codon:
            return True
    return False

def binary_contains(gene, key_codon) :
    low = 0
    high = len(gene) - 1
    while low <= high: # while there is still a search space
        mid: int = (low + high) // 2
        if gene[mid] < key_codon:
            low = mid + 1
        elif gene[mid] > key_codon:
            high = mid - 1
        else:
            return True
    return False


my_gene = string_to_gene(gene_str)
acg = (Nuelcotide.A, Nuelcotide.C, Nuelcotide.G)
gat = (Nuelcotide.G, Nuelcotide.A, Nuelcotide.T)
print(linear_contains(my_gene, acg)) # True
print(linear_contains(my_gene, gat)) # False
my_sorted_gene = sorted(my_gene)
print(binary_contains(my_sorted_gene, acg)) # True
print(binary_contains(my_sorted_gene, gat)) # False




