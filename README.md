# ICGR_NeuralNetwork
This is the GitHub repo of the Graduation project ICGR &amp; Neural network  
In recent years, huge DNA, Ribonucleic acid (RNA), and protein sequences have been widely available as a result of Next generation sequencing (NGS).
The analysis of the resulting sequences is one of the most important applications in Bioinformatics field. 
Using the right tools and methods,the analysis of these sequences can help identifying similarities/dissimilarities between DNA sequences of the same type, from different organisms to discover the evolutionary relationship between species and also helps in early disease diagnosis especially in cancer which was earlier not possible with conventional tech¬nologies.


1. Problem Definition and Motivation

One way for efficiently analyzing them, is converting the symbolic sequence to a graphical or numerical sequence which is essential to genome comparison, compression and encryption. By merging the idea of chaotic dynamics with the sequence bases (4 letters) of DNA or RNA, rather than yielding in a random struc¬ture (no consistent result each run), the randomness of the structure is taken out by the sequence governing (by using only four corners). The resulted image is the genetic structure of the entered sequence.
This technique is known as CGR, which is a numerical mapping of sequences that is represented in a graph. The last edited version of it is ICGR which allows to encode and decode the sequence into 3 integer number, but this is limited by a specific length of the sequence which is our first problem.
So, let us discuss our second problem in the next few lines.

One of the most essential vital processes happening in every living organism is the production of protein. This happens as a result of transcription of DNA coding genes, which consist of intron and exons, into pre-messenger ribonucleic acid (pre-mRNA), then this pre-mRNA needs to be processed so it can be translated into corresponding amino acids which form proteins.

The process, in which introns are removed to allow combination of exons, is known as splicing, and sites which separate introns and exons are known as splice sites.
Identifying splice sites is a necessary step to analyze the location and structure of genes. Two dinucleotides, GT (GU in RNA) and AG, are highly frequent on splice sites (consensus).

Meanwhile, the dinucleotides occur frequently at the sequences without splice sites, which make the prediction prone to generate false positives. Many splice site prediction tools use alignment-based approach which avoids this problem but needs a reference, that’s not exist in most cases.
Recently, deep Neural network (NN) have been employed to predict splice
 
Chapter 1. Introduction	3

sites from arbitrary pre-mRNA transcript sequences, but the problem here is the non-canonical splice sites.





1.2	Project Objectives and Contribution

The proposed website aims to combine some bioinformatics services in one place. To handle the statements above, the website will produce:

•	A tool to represent DNA or RNA in a form of an image (graph) or a number for easier and less time and space consuming analysis.
•	A tool that provides compression of long DNA, RNA sequences in a form of a graph (image) or a number.
•	A tool that provides availability of handling sequence lengths over 1024 base pair (bp), encoding into 3 integers and decoding it back.
•	A tool to perform exact pattern matching for 2 sequences using computer vision algorithm.
•	A tool to predict canonical and non-canonical splice sites from DNA se¬quence.





1.3	Project Scope

The website targeted users are bioinformaticians, and all who concern with bioin¬formatics (computational biology)field, as the website provide variety of bioinformatics tools help them with their studies and research.
