def get_genes(dna_string):
    genes = []
    for pos in range(len(dna_string)):
        gene_string = ""
        if dna_string[pos:pos + 3] == "ATG":
            start = pos + 3
            while (
                dna_string[start:start + 3] != "TAG"
                and dna_string[start:start + 3] != "TAA"
                and dna_string[start:start + 3] != "TGA"
            ):
                gene_string += dna_string[start]
                start += 1
            genes.append(gene_string)
    return genes


if __name__ == "__main__":
    print(get_genes("TCATGTGCCCAATTCTGACCTACGATGGCCCAATAGCG"))  # ["TGCCCAATTC", "GCCCAA"]
    print(get_genes("ATTGCGCTACGCATC"))  # []
    print(get_genes("ATGGTATCGTAAGATGGGGGTAGATATGTGA"))  # ['GTATCG', 'GGGG', '']

# start = ATG
# stop = TAG, TAA or TGA
# TC:ATG:TGCCCAATTC:TGA:CCTACG:ATG:GCCCAA:TAGCG
#        TGCCCAATTC                GCCCAA
#        TGCCCAATTC                GCCCAA
