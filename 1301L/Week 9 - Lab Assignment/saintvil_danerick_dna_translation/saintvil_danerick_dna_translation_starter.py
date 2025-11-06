"""
Danerick Saint-Vil
October 23, 2025
Program 1
dna_translation.py
starter.py

"""

import saintvil_danerick_dna_translation_helper

def transcription(dna_sequence):
    complement = '' # This is where the Base Pair Complement will be

    temp = dna_sequence.replace("T","U") # Replace Thymine with Uracil (and puts the updated string into a temporary variable)
    
    # Create the Base Pair Complement

    for x in temp: # For all values in temp

        if x == "A": # Switches all iterations of A to U
            complement += "U"
        elif x == "U": # Switches all iterations of U to A
            complement += "A"
        elif x == "C": # Switches all iterations of C to G
            complement += "G"
        elif x == "G": # Switches all iterations of G to C
            complement += "C"
        else: # If none of the above work (which im assuming it's supposed to work), just keep the letter the same
            complement += x

    

    return complement # Returns the variable that now has the mrna 

def translate(mrna): # Translates the mRNA into its amino acids

    chunk_list = saintvil_danerick_dna_translation_helper.chunk(transcription(dna),3) # Gets the seperated list from helper

    # Replace Triplets with Amino Acids
    protein = "" # This is where the amino acids will be
    for x in chunk_list: # For every value in the list
        if x in saintvil_danerick_dna_translation_helper.amino_acids: # If the triple is in the dictionary
            protein += f"{saintvil_danerick_dna_translation_helper.amino_acids[x]} " # Adds the amino acid to the protein string

    return protein


dna = 'TACGCAGAAAAAAATCAGCGGGGTTGTTGGTCATTAGTCTGAATT'

mrna = transcription(dna)

amino_acids = translate(mrna)

print(f"DNA Sequence\n{dna}\n")
print(f"mRNA Sequence\n{mrna}\n")    
print(f"Protein Sequence\n{amino_acids}\n") 