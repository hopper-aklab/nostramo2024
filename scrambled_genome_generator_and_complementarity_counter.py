# Copyright (C) 2024 The Ohio State University

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

# Scrambles a genome while maintaining codon usage and searches for continuous complementarity in each scrambled genome (no mismatches).
# Needed for use: properly formatted genome (see: genome formatter) [‘Formatted_Genome’]
# Needed for use: blank text file for scrambled genomes to be generated in [ ‘Scrambled_Regenerated_Genome’]

import random

uracil = "U"
thymine = "T"
adenine = "A"
guanine = "G"
cytosine = "C"
placeholder1 = "X"
placeholder2 = 'Y'

seqOriginal = input('Enter Nucleotide Sequence: ')
seqAdjusted = seqOriginal[::-1].upper().replace(uracil, thymine).replace(thymine, placeholder1).replace(guanine, placeholder2).replace(adenine, thymine).replace(cytosine, guanine).replace(placeholder1, adenine).replace(placeholder2, cytosine)
# transforms input sequence into reverse complement (rc) ssDNA.

seqLength = len(seqAdjusted)
print('Reverse complement ssDNA: ' + seqAdjusted)

segmentLength = int(input('Desired Segment Length (nts perfect complementarity): '))

n1 = 0
n2 = segmentLength
segmentList = []

while n2 <= len(seqAdjusted):
    segmentList.append(seqAdjusted[n1:n2])
    n1 += 1
    n2 += 1
    # splits reverse complement ssDNA into all possible segments of a desired length

loop = int(input('Number of Scrambled Genomes to Generate: '))


def randomize_line(line1):
    subline = [line1[i:i + 3] for i in range(0, len(line1), 3) if line1[i:i + 3].isalpha()]
    random.shuffle(subline)
    randomized_line = ''.join(subline)
    file2.write(randomized_line + "\n")
    # scrambles each line of the genome, maintaining codon usage.


print('Complementary Genes per Scrambled Genome: ')
for x in range(loop):
    originalGenome = open("Formatted_Genome", "r")
    file2 = open("Scrambled_Regenerated_Genome", "a")
    for line in originalGenome:
        randomize_line(line)
    file2.close()
        # generates the scrambled genome by running the function for each line.

    geneCount = 0

    scrambledGenome = open('Scrambled_Regenerated_Genome', 'r+')
    for gene in scrambledGenome:
        exist = False
        for segment in segmentList:
            if segment in gene:
                exist = True
        if exist is True:
            geneCount += 1
        # searches the scrambled genome for each segment of the reverse complement ssDNA.
        # counts number of genes with complementarity to the input sequence in the scrambled genome.
    
    # to save scrambled genomes, include code below and specify a folder (path) to save at:
    # path = 'path to folder'
    # pathFullString = path + "/scrambledGenome" + str(x) + '.txt'
    # _ = open(pathFullString, "x+")
    # savedGenome = open(pathFullString, "w+")
    # scrambledGenome = open('Scrambled_Regenerated_Genome', 'r+')
    # for line in scrambledGenome:
    #    savedGenome.write(line)
    
    scrambledGenome.truncate(0)
    scrambledGenome.close()
    # clears the scrambled genome.
 
    print(geneCount)
    # prints results.
