# Purpose: python script to compute the containment of genomes 
# Name: Hannah Mannering 
import os
import glob
from pathlib import Path

# get fasta files
# write what path you want to look at
path = '/home/hemannering/Research/data/subset/*.fna.gz'
fasta_files = glob.glob(path)

# get mash files
# write what path you want to look at 
path2 = '/home/hemannering/Research/data/subset/*.fna.gz.msh'
mash_files = glob.glob(path2)

# iterate through fasta files
for filename_fasta in fasta_files:
    # check to ensure it is printing out fasta 
    #print(filename_fasta)
    for filename_mash in mash_files:
        # check to ensure it is printing mash 
        #print(filename_mash)
        os.system('./mash screen ' + filename_mash + ' ' + filename_fasta + ' | cut -f1,2 >> cont_within_.txt')

