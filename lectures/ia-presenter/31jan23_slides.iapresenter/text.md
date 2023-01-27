# Describing Variation & Patterns of Diversity

Pleas log in to the hub!
---
#### Outline
	1. DNA and representing DNA
	2. Summarizing genetic diversity
	3. Coding example


---
#### DNA consists of four nucleotides
$$
\begin{matrix}
\\
\\
\text{ATGC}
\end{matrix}
$$

The nucleotides adenine, thymine, guanine, and cytosine are the building blocks for all DNA. DNA
---
#### DNA is organized onto chromosomes
$$
\begin{matrix}
\\
\\
\text{AATGCTAGTA} 
\end{matrix}
$$

Continuous segments of DNA are organized onto chromosomes and a set of all chromosomes make up a genome.
---
#### Ploidy (<#>N): number of sets of chromosomes
$$\text{N = haploid}$$
$$
\begin{matrix}
\text{AATGCTAGTA} \\
\end{matrix}
$$

We are often interested in knowing the number of sets of chromosomes, which we will refer to as ploidy and is represented by an N. For example, human gametes are both haploid, which is represented with just a N, since they only carrying one set of 23 chromosomes. 
---
#### Ploidy (<#>N): number of sets of chromosomes
$$\text{2N = diploid}$$
$$
\begin{matrix}
\text{AATGCTAGTA} \\
\text{TTACGATCAT} \\
\end{matrix}
$$

However, a human individual is diploid, which is represented by a 2N, because they inherit a set of chromosomes from both their mother and father.

Other organisms such as plants can have even higher levels of ploidy but for the purposes of this class we will only work with haploid and diploid genetic data.
---
## Q: How does genetic variation arise?

So now that we all understand what DNA is and how it is organized, does anyone know how genetic variation actually arises? 

A: Mutations, which are caused by errors in DNA replication and expose to mutagens.
---
#### A: Mutations

ADD MUTATION FIGURE HERE.


---
#### How do we encode DNA
$$
\begin{matrix}
\\
\\
m \; \text{(sites)} \, \times n \;  \text{(individuals)}\\
\end{matrix}
$$


---
#### How do we encode DNA
$$
\begin{matrix}
\color{blue}\text{pos} \; \color{white}\text{TTTTT} \\
\color{blue}\text{1} \; \color{black}\text{ TTTTT} \\
\color{blue}\text{2} \; \color{black}\text{ CGGCG} \\
\color{blue}\text{3} \; \color{black}\text{ ATATT} \\
\color{blue}\text{4} \; \color{black}\text{ GGGGC} \\
\color{blue}\text{5} \; \color{black}\text{ TAAAA} \\
\color{orange}\text{id } \color{orange}\text{a b c d e} \\
\end{matrix}
$$


---
#### Genotype matrices
$$
\begin{bmatrix}
0 & 0 & 0 & 0 & 0 \\
0 & 1 & 1 & 0 & 1 \\
0 & 1 & 0 & 1 & 1 \\
0 & 0 & 0 & 0 & 1 \\
1 & 0 & 0 & 0 & 0 \\
\end{bmatrix}
\\
\text{0 = reference or ancestral allele}
\\
\text{1 = alternative or derived allele}
$$


---
#### Genotype matrices
$$
\begin{bmatrix}
\color{red}\text{0} & \color{red}\text{0} & \color{red}\color{red}\text{0} & \color{red}\text{0} & \color{red}\text{0} \\
\text{0} & \text{1} & \text{1} & \text{0} & \text{1} \\
\text{0} & \text{1} & \text{0} & \text{1} & \text{1} \\
\text{0} & \text{0} & \text{0} & \text{0} & \text{1} \\
\text{1} & \text{0} & \text{0} & \text{0} & \text{0} \\
\end{bmatrix}
$$


---
#### Genotype matrices
$$
\begin{bmatrix}
\color{red}\text{0} & \color{red}\text{0} & \color{red}\color{red}\text{0} & \color{red}\text{0} & \color{red}\text{0} \\
\text{0} & \text{1} & \text{1} & \text{0} & \text{1} \\
\text{0} & \text{1} & \text{0} & \text{1} & \text{1} \\
\text{0} & \text{0} & \text{0} & \text{0} & \text{1} \\
\text{1} & \text{0} & \text{0} & \text{0} & \text{0} \\
\end{bmatrix}
=
\begin{bmatrix}
\text{0} & \text{1} & \text{1} & \text{0} & \text{1} \\
\text{0} & \text{1} & \text{0} & \text{1} & \text{1} \\
\text{0} & \text{0} & \text{0} & \text{0} & \text{1} \\
\text{1} & \text{0} & \text{0} & \text{0} & \text{0} \\
\end{bmatrix}
$$


---
#### Some terminology...
	- single nucleotide polymorphism (snp)
	- single nucleotide variant (snv)
	- variant site
	- segregating site

There are subtle differences but they all more or less mean the same thing.
---
#### How would you summarize genetic data?
$$
\begin{bmatrix}
0 & 0 & 0 & 0 & 0 \\
0 & 1 & 1 & 0 & 1 \\
0 & 1 & 0 & 1 & 1 \\
0 & 0 & 0 & 0 & 1 \\
1 & 0 & 0 & 0 & 0 \\
\end{bmatrix}
$$

