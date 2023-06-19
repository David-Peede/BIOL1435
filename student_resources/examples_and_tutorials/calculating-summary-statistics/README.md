# Calculating Summary Statistics

This directory contains five files (besides this `README.md` and GitHub metadata files):

1. `calculating_summary_statistics.ipynb` (tutorial notebook)
2. `integrated_call_samples_v3.20130502.ALL.panel` (sample metadata file for the phase 3 release of the 1000 genomes project)
3. `tgp_biallelic_snps_chr1_first_1000_lines.vcf.gz` (first 1000 lines of the pre-filtered chromosome 1 VCF file from the phase 3 release of the 1000 genomes project)
4. `tgp_alt_allele_freq.csv` (output from the tutorial notebook)
5. `tgp_het_sites.csv` (output from the tutorial notebook)

Here are the steps to download `integrated_call_samples_v3.20130502.ALL.panel` and to re-create `tgp_biallelic_snps_chr1_first_1000_lines.vcf.gz`.

__1. Download the TGP VCF & Metadata File__

```bash
# Download the vcf file.
wget http://ftp.1000genomes.ebi.ac.uk/vol1/ftp/release/20130502/ALL.chr1.phase3_shapeit2_mvncall_integrated_v5b.20130502.genotypes.vcf.gz
# Download the metadata file.
wget http://ftp.1000genomes.ebi.ac.uk/vol1/ftp/release/20130502/integrated_call_samples_v3.20130502.ALL.panel
```

__2. Filter the TGP VCF for Bi-Allelic SNPs Using [`bcftools`](https://samtools.github.io/bcftools/bcftools.html)__

```bash
bcftools view -m2 -M2 -i 'INFO/VT="SNP"' -Oz -o tgp_biallelic_snps_chr1.vcf.gz ALL.chr1.phase3_shapeit2_mvncall_integrated_v5a.20130502.genotypes.vcf.gz
```

__3. Extract the First 1000 Lines & `bgzip` the VCF File with [`tabix`](http://www.htslib.org/doc/tabix.html)__

```bash
zcat tgp_biallelic_snps_chr1.vcf.gz | head -n 1000 | bgzip > tgp_biallelic_snps_chr1_first_1000_lines.vcf.gz
```

