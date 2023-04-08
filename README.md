# Research
##  Predicting the similarity of bacterial genomes within an environmental DNA sample

The goal of this project is to develop a tool that predicts the type of a bacterial genome in an environmental sample by analyzing the abundance and composition of specific DNA sequences. 

The following is a guide to some of the Softwares we use in our research:

## Mash Screen (https://github.com/marbl/Mash) -- (used for containment and abundance calculations) 
Here is the command to use to screen two genomes, the mash to the FASTA reference:
./mash screen genome1.fna.msh genome2.fna

An example of my command: 
./mash screen /home/hemannering/Mash/data/genome1.fna.msh /home/hemannering/Mash/data/genome2.fna

** Mashscreen was modified, this modified file is in scripts under CommandScreen.cpp. I modified it to output mean. Which means:
- Aim to calculate if value is greater than zero because the zero doesn’t really tell us anything 
- Have counter of non zero values
- Divide sum by counter 

# Simulation Reads (https://www.niehs.nih.gov/research/resources/software/biostatistics/art/index.cfm)
Art was used to simulate sequencing depths. Before simulating a genome with ART, it is important to note that you must untar it with tar -xvf so that MashScreen simulation works.  

Here is a command to simulate a genome:
./art_illumina -ss HS25 -sam -i fastaFileName -l 100 -f 5 -o outputFileName

An example of my command:
./art_illumina -ss HS25 -sam -i /home/hemannering/DNA_Research/DNA_Research/subset/GCF_019273775.1_ASM1927377v1_genomic.fna -l 100 -f 5 -o outputFileName

You can modifiy the f value to the value you want to use for containment. We used the following to calculate our sequencing depths, this equation is the power law distribution: y=(10*x^-1.1). We subsetted our data of 41 into 4 different random subsets of 10,10,10, and 11 individual genomes and had sequencing depths of {10, 4.66516, 2.98653, 2.17638, 1.70268, 1.39326, 1.17596, 1.01532, 0.891935, 0.794328, ...} so for genome1_subsetx it would be a depth of 10, genome2_subsetx = depth 4.66516, and so on. For each subset, we had values ranging from 1-11 for x in the power law distibutoon formula.




