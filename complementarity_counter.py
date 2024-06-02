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

# Searches a genome for complementarity to an input sequence(s). Can allow/specify mismatches.
# Searches for perfect complementarity first, then, if selected, for mismatched complementarity. After each input sequence, complementary genes are listed. Genes that fit both perfect and mismatched criteria are listed only once. As the program runs, data for each region of complementarity is listed.
# Sequence(s) can be manually (1 by 1) or the program can be adjusted to allow multiple sequences to run consecutively from a text file [‘Intron Sequences’, ‘Intron Names’]. Can be used to measure complementarity in a list of sequences generated using ‘Random Sequence Generator.’
# Needed for use: properly formatted genome (see: genome formatter) [‘Formatted_Genome’].
# Needed for use properly formatted gene names (see: gene name formatter) [‘Formatted_Gene_Names’].
# Needed for use: BioPython module.

import multiprocessing
import time
from Bio.Seq import Seq


def substring_match(string1, string2, segment_length, mismatches, gene_index, geneNames):
    # function used for mismatched complementarity
    substrings1 = []
    for i in range(len(string1) - (segment_length - 1)):
        substrings1.append(string1[i:i + segment_length])
    substrings2 = []
    for j in range(len(string2) - (segment_length - 1)):
        substrings2.append(string2[j:j + segment_length])
    # splits the genome and input sequence (rc) into all possible substrings of a specified length.
    for substring1 in substrings1:
        for substring2 in substrings2:
            sum1 = 0
            for x in range(segment_length):
                if substring1[x] == substring2[x]:
                    sum1 += 1
                else:
                    sum1 += 0
                # counts the overlapping nucleotides between each combination of substrings
                if sum1 >= (segment_length - mismatches):
                    seq = Seq(substring1)
                    print('Input: ' + str(seq.reverse_complement()))
                    print('RC Input: ' + substring1)
                    print('Gene Segment: ' + substring2)
                    x = string2.find(substring2)
                    x2 = string1.find(substring1)
                    print('Gene Segment Relative to Input: ' + string2[(x-x2):(x-x2+len(string1))])
                    print(geneNames[gene_index], end='')
                    print(' ')
                    return gene_index
                    # if the overlapping nucleotides exceeds the minimum required, records the gene and prints info.

if __name__ == "__main__":
    uracil = "U"
    thymine = "T"
    adenine = "A"
    guanine = "G"
    cytosine = "C"
    placeholder1 = "X"
    placeholder2 = 'Y'

    seq = input('Input Sequence: ')
    allIntronSeq = [seq, ' ']
    # can also use text file input for multiple sequences at once by including the following lines.
    # allIntronSeq = open('Intron Sequences', 'r').readlines()
    intronSeqNames = ['Sequence 1','Placeholder']
    # intronSeqNames = open('Intron Names', 'r').readlines()
    segmentLength = int(input('Segment Length? (nts of perfect complementarity): '))
    YNmismatch = input('Allow mismatches Y/N: ').upper()
    geneNames = open('Formatted_Gene_Names', 'r').readlines()
    if YNmismatch == 'Y':
        segmentL = int(input('Segment Length? (with mismatches): '))
        allowedMismatches = int(input('Allowed Mismatches: '))
    geneIndexListGlobal = []
    intronSeqComp = []
    genome = open('Formatted_Genome', 'r').readlines()

    seqNumber = 0
    for intronSeq in allIntronSeq:
        print(intronSeqNames[seqNumber])
        seqOriginal = intronSeq.upper()
        seqAdjusted = seqOriginal[::-1].upper().replace(uracil, thymine).replace(thymine, placeholder1).replace(guanine, placeholder2).replace(adenine, thymine).replace(cytosine, guanine).replace(placeholder1, adenine).replace(placeholder2, cytosine)
        # creates the reverse complement of the input sequence.
        # to search for matching sequences, include the following line:
        # seqAdjusted = seqOriginal.upper().replace(uracil, thymine)

        geneIndexList = []
        geneIndexList1 = []
        n1 = 0
        n2 = segmentLength
        segmentList = []

        while n2 <= len(seqAdjusted):
            segmentList.append(seqAdjusted[n1:n2])
            n1 += 1
            n2 += 1
            # splits input sequence (rc) into all possible segments (substrings) of a given length
        geneIndex2 = 0
        for gene in genome:
            exist = False
            for segment in segmentList:
                if segment in gene:
                    if exist is False:
                        print('Input (DNA): ' + str(Seq(segment).reverse_complement()) + '*perfect')
                        print('RC Input: ' + segment)
                        x = gene.find(segment)
                        x2 = seqAdjusted.find(segment)
                        print('Gene Segment Relative to Input: ' + gene[(x - x2):(x - x2 + len(seqAdjusted))])
                    exist = True
                    # searches each gene in the genome for each substring of the input sequence (rc).
                    # if a match is found in a gene, prints information about the gene and the paired region.
                    # used for perfect complementarity
                    # note: if there are multiple positive regions in the same gene, will only detect the first region
            if exist is True:
                geneIndexList.append(geneIndex2)
                # appends list positions for genes with complementarity fitting criteria.

                print(geneNames[geneIndex2])

            geneIndex2 += 1

        if YNmismatch == 'Y' and intronSeqNames[seqNumber] != 'Placeholder':
            # ran only if mismatches are selected (computationally intensive).
            print('*perfect complete, moving to mismatched complementarity')
            pool = multiprocessing.Pool()
            start_time = time.perf_counter()
            processes = [pool.apply_async(substring_match, args=(seqAdjusted, gene, segmentL, allowedMismatches, geneIndex, geneNames)) for gene, geneIndex in zip(genome, range(len(genome)))]
            # runs the mismatched complementarity function in parallel for each gene.
            for z in processes:
                geneIndexList1.append(z.get())
            for data in geneIndexList1:
                if data is not None:
                    geneIndexList.append(data)
                    # appends list positions for genes with complementarity fitting criteria.

            geneIndexList = set(geneIndexList)
            # keeps only one copy of duplicates fitting both perfect and mismatched criteria.
        geneIndexAdapted = []
        for gene in geneIndexList:
            geneIndexAdapted.append(geneNames[gene])
            geneIndexListGlobal.append(geneNames[gene])

        geneIndexAdapted = set(geneIndexAdapted)
        # per input sequence list of genes fitting criteria.

        for entry in geneIndexAdapted:
            print(entry, end='')
        print('ORFs# ' + str(len(geneIndexAdapted)))
        print('')
        # prints number of ORFs/genes/UTRs/etc. fitting criteria.
        intronSeqComp.append(len(geneIndexAdapted))
        seqNumber += 1

    print('')
    for intronName in intronSeqNames:
        print(intronName)
    print('')
    for intronComp in intronSeqComp:
        print(intronComp)

    geneIndexListGlobal = set(geneIndexListGlobal)
    # for all input sequences (global), list of genes fitting criteria.

    print('Total unique genes fitting criteria: ')
    print(len(geneIndexListGlobal))
    # total number of unique genes fitting criteria among all the input sequences.
