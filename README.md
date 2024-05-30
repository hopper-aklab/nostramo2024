# tRNA introns function as noncoding regulatory RNAs
Python 3.11 code for the manuscript titled: 'FitRNA for duty: Free introns of tRNAs as complementarity-dependent regulators of gene expression' by Nostramo et al., 2024.
# Programs and usage
-	Genome Formatter 
-	Gene Name Formatter 
-	Gene Name Truncator 
-	Complementarity Counter
-	Random Sequence Generator
-	Random Sequence Generator and Complementarity Counter
-	Scrambled Genome Generator and Complementarity Counter

'genome_formatter' uses an annotated genome to create a file with each gene (or ORF/UTR/etc) sequence on different line, removing the annotations. 

'gene_name_formatter' uses an annotated genome to a create file with each gene annotation on a different line.

Using 'genome_formatter' and 'gene_name_formatter' on the same annotated genome will generate two alligned files, one with the gene sequences and one with the gene annotations.
'gene_nane_truncator' can be used to trim the gene annotation file to only include the gene names. Preparing a formatted genome and gene name file is necessary for usage of the following programs.

'complementarity_counter' can be used to determine the complementary genes (or ORFs/UTRs/etc depending on genome used) of an input sequence. This program can be used to search for mismatched complementarity efficiently.

'random_sequence_generator' generates randomized ssDNA nucleotide sequences at a specified length and GC content. These can then be fed into 'complementarity_counter' or, alternatively, 'random_sequence_generator_and_complementarity_counter' can be used to automatically find the complementarity of each random sequence as it is generated (note: this program only supports perfect complementarity).

'scrambled_genome_generator_and_complementarity_counter' generates scrambled genomes that maintain codon usage in each line. These genomes are automatically searched for complementarity to an input sequence (note: this program only support perfect complementarity).

# Usage in Nostramo et al., 2024
For use in subsequent programs, annotated genomes were formatted using 'genome_formatter’ and ‘gene_name_formatter’. For S. cerevisiae genomes, ‘gene_name_truncator,’ was utilized to trim gene annotations to only include the gene names.

‘complementarity_counter’ was used to identify and determine region of complementarity in each tRNA intron sequence in S. cerevisiae (to ORFs and UTRs) and Humans (to transcripts). Parameters for complementarity were selected to have a reasonable number of genes to test via RT-qPCR.

‘scrambled_genome_generator_and_complementarity_counter’ was used to generate codon scrambled genomes and measure the complementarity of the S. cerevisiae tRNA<sup>Ile</sup> intron in each.

‘random_sequence_generator_and_complementarity_counter’ was used to generate random sequences at a specific length and GC content and measure their complementarity to ORFs in S. cerevisiae. To measure random sequences for complementarity with mismatches, the sequences were first generated at the GC content of the relevant tRNA intron using ‘random_sequence_generator’ and then ran through ‘complementarity_counter’ from a text document. For matching sequence data, the programs were modified as indicated in the code comments. 
Due to their computationally intensive nature, mismatched complementarity searches were run on the Ohio Supercomputer Center.
