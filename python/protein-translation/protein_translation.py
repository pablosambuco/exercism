translation = {
    "UUU": "Phenylalanine",
    "AUG": "Methionine",
    "UUC": "Phenylalanine",
    "UUA": "Leucine",
    "UUG": "Leucine",
    "UCU": "Serine",
    "UCC": "Serine",
    "UCA": "Serine",
    "UCG": "Serine",
    "UAU": "Tyrosine",
    "UAC": "Tyrosine",
    "UGU": "Cysteine",
    "UGC": "Cysteine",
    "UGG": "Tryptophan",
    "UAA": "STOP",
    "UAG": "STOP",
    "UGA": "STOP",
}


def proteins(strand):
    aminoacids = []
    codon = ""
    for letter in strand:
        codon += letter
        if len(codon) == 3:
            aminoacid = translation[codon]
            if aminoacid == "STOP":
                break
            aminoacids.append(aminoacid)
            codon = ""
    return aminoacids
