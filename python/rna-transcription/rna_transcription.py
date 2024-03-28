translator = {
    "G": "C",
    "C": "G",
    "T": "A",
    "A": "U",
}

def to_rna(dna_strand):
    rna = [translator[x] for x in dna_strand]
    return "".join(rna)
