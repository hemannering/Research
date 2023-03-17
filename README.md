# Research
##  Predicting the similarity of bacterial genomes within an environmental DNA sample

The goal of this project is to develop a tool that predicts the type of a bacterial genome in an environmental sample by analyzing the abundance and composition of specific DNA sequences. 

## Mash Screenn -- containment anf abundance
./mash screen /home/hemannering/Mash/data/genome1.fna.msh /home/hemannering/Mash/data/genome2.fna

# Simulation Reads
Art was used to simulate sequencing depths. 
Ex. ./art_illumina -ss HS25 -sam -i /home/hemannering/DNA_Research/DNA_Research/subset/GCF_019273775.1_ASM1927377v1_genomic.fna -l 100 -f 5 -o j

 ## Mixture 
 |  Sequence Depth | Genome  |
|---|---|
|  0.5    | GCF_019273775.1_ASM1927377v1_genomic.fna  |
| 1     | GCF_900795265.1_18456_1_125-5_genomic.fna   |
|  2   |  GCF_900692955.1_17794_7_121-2_genomic.fna |
|  5  | CF_900693065.1_18456_1_111-2_genomic.fna |
| 10 | CF_900795145.1_13415_5_13-5_genomic.fna |


