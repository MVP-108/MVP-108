#dna strand
dna_string=("AGTCGTTACGGTCATAGCCGATCGAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGC")


#local function
def transcribe_to_rna(dna_sequence):
    
    return dna_sequence.replace("T", "U")
Amount_of_Thymine = dna_string.count("T")
rna_string = transcribe_to_rna(dna_string)
amount_of_Uracil = rna_string.count("U")

#frontend, data analysis, and output
print("DNA and RNA Sequence Analysis Completed:")
print(" ")
print("DNA sequence:", dna_string)
print("Transcribed RNA sequence:", transcribe_to_rna(dna_string))
print("Amount of Thymine in the DNA sequence:", Amount_of_Thymine)
print("Amount of Uracil in the DNA sequence:", amount_of_Uracil)
print("Base number in DNA seequence for Thymine:", [i+1 for i in range(len(dna_string)) if dna_string[i] == "T"])
print("Base number in RNA seequence for Uracil:", [i+1 for i in range(len(rna_string)) if rna_string[i] == "U"])

transcribe_to_rna(dna_string)