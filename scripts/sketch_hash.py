# Purpose: python script to compute the containment of genomes 
# Name: Hannah Mannering 
import os
from pathlib import Path
directory = '/home/hemannering/Research/data/subset'

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # sketch files  
    os.system('mash sketch ' + f) 
