# Research
##  Predicting the similarity of bacterial genomes within an environmental DNA sample

The goal of this project is to develop a tool that predicts the type of a bacterial genome in an environmental sample by analyzing the abundance and composition of specific DNA sequences. 

## Mash Screenn -- containment anf abundance
./mash screen /home/hemannering/Mash/data/genome1.fna.msh /home/hemannering/Mash/data/genome2.fna

## Simulation Reads
Art was used to simulate sequencing depths. 
Ex. /art_illumina -ss HS25 -sam -i testSeq.fa -l 100 -f 100  -s 5000000 -o single
./art_illumina -ss HS25 -sam -i /home/hemannering/DNA_Research/DNA_Research/subset/GCF_019273775.1_ASM1927377v1_genomic.fna -l 100 -f 100  -s 5000000 -o single
