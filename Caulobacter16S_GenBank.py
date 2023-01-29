# code to extract all the Caulobacter crescentus 16S rDNA sequences from GenBank


from Bio import Entrez
from Bio import SeqIO

Entrez.email = "berriosl@stanford.edu"

# Search for Caulobacter crescentus, Caulobacter segnis, and Caulobacter sp. 16S rDNA sequences
handle = Entrez.esearch(db="nucleotide", term="Caulobacter crescentus 16S OR Caulobacter segnis 16S OR Caulobacter sp. 16S", retmax=1000000)
record = Entrez.read(handle)
handle.close()

# Fetch the sequence data
handle = Entrez.efetch(db="nucleotide", id=record["IdList"], rettype="fasta", retmode="text")
sequences = handle.read()
handle.close()

# Write the sequences to a FASTA file
with open("caulobacter_16S_sequences.fasta", "w") as f:
    f.write(sequences)

# filter the downloaded Caulobacter sequences because some non-Caulobacter sequences and completed genomes of various genera were also downloaded

from Bio import SeqIO

# Input FASTA file
fasta_file = "/Users/louisberrios/Documents/Python_scripts/caulobacter_16S_sequences.fasta"

# Keyword to search for
keyword = input("Enter keyword to search for in the FASTA file:")

# Open FASTA file and filter by keyword
filtered_records = (record for record in SeqIO.parse(fasta_file, "fasta") if keyword in record.description)

# Write filtered records to a new FASTA file
SeqIO.write(filtered_records, "filtered_Caulobacter_sequences.fasta", "fasta")


# Input FASTA file
fasta_file2 = "/Users/louisberrios/Documents/Python_scripts/filtered_Caulobacter_sequences.fasta"

# Keyword to search for
keyword = input("Enter keyword to search for in the FASTA file:")

# Open FASTA file and filter by keyword
filtered_records = (record for record in SeqIO.parse(fasta_file2, "fasta") if keyword in record.description)

# Write filtered records to a new FASTA file
SeqIO.write(filtered_records, "filtered_Caulobacter16S_sequences.fasta", "fasta")
