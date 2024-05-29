# tRNA introns function as noncoding regulatory RNAs
Python 3.11 code for the manuscript titled: 'FitRNA for duty: Free introns of tRNAs as complementarity-dependent regulators of gene expression' by Nostramo et al., 2024.
# Programs and usage
-	Genome Formatter 
-	Gene Name Formatter 
-	Gene Name Truncator 
-	Complementarity Counter
-	Scrambled Genome Generator and Complementarity Counter
-	Random Sequence Generator
-	Random Sequence Generator and Complementarity Counter

genome_formatter uses an annotated genome to create a file with each gene (or ORF/UTR/etc) sequence on different line, removing the annotations. 

gene_name_formatter uses an annotated genome to a create file with each gene annotation on a different.

Using genome_formatter and gene_name_formatter on the same annotated genome, will generate two alligned files, one with the gene sequences and one with the gene annotations.
gene_nane_truncator can be used to trim the gene annotation file to only include the gene names.

Preparing a reformatted genome is necessary for usage of the following programs.


# Usage in paper
For usage in subsequent programs, annotated genomes were formatted using the ‘Genome Formatter’ and ‘Gene Name Formatter’. For S. cerevisiae genomes, ‘Gene Name Truncator,’ was utilized to trim gene annotations to only include the gene names.

The program titled ‘Complementarity Counter’ was used to determine the complementarity of each tRNA intron sequence in S. cerevisiae (to ORFs and UTRs) and Humans (to transcripts). Parameters for complementarity were selected to have a reasonable number of genes to test via RT-qPCR.

The program titled ‘Scrambled Genome Generator and Complementarity Counter’ was used to generate scrambled genomes and measure the complementarity of the tRNA<sup>Ile</sup> intron in each. Each scrambled genome maintains codon usage.

The program titled ‘Random Sequence Generator and Complementarity Counter’ was used to generate random sequences at a specific length and GC content and measure their complementarity (continuous complementarity only). To measure random sequences for complementarity with mismatches, the sequences were first generated at the GC content of the relevant tRNA intron using ‘Random Sequence Generator’ and then ran through ‘Complementarity Counter’ from a text document. For matching sequence data, the programs were modified as indicated in the code comments. 
Due to their computationally intensive nature, mismatched complementarity searches were run on the Ohio Supercomputer Center.
