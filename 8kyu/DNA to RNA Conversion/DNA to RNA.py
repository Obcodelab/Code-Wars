def dna_to_rna(dna):
    if "T" in dna :
        return dna.replace("T", "U")
    elif len(dna) != 4:
        return dna
