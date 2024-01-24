# Problem Set 1

Here is how you can recreate the files in the `data` directory for this problem set.

__Step 1: Download the TGP VCF file__

```bash
# Download chromosome 2.
wget http://ftp.1000genomes.ebi.ac.uk/vol1/ftp/release/20130502/ALL.chr2.phase3_shapeit2_mvncall_integrated_v5a.20130502.genotypes.vcf.gz
```



__Step 2: Index the VCF file with [`tabix`](http://www.htslib.org/doc/tabix.html)__

```bash
# Index chromosome 2.
tabix -p vcf ALL.chr2.phase3_shapeit2_mvncall_integrated_v5a.20130502.genotypes.vcf.gz
```



__Step 3: Subset out the _LCT_  and _MCM6_ regions using [`bcftools`](https://samtools.github.io/bcftools/bcftools.html)__

```bash
# Filter for the LCT and MCM6 region only retaining biallelic snps.
bcftools view -m2 -M2 -r 2:136545844-136633962 -i 'INFO/VT="SNP"' -Oz -o tgp_lct_mcm6_biallelic_snps.vcf.gz ALL.chr2.phase3_shapeit2_mvncall_integrated_v5a.20130502.genotypes.vcf.gz
```



__Step 4: Append the ancestral allele calls using `tgp_aa_calls.py`__

```bash
# Update the vcf file with the anestral allele information.
python tgp_aa_calls.py tgp_lct_mcm6_biallelic_snps | bgzip > tgp_lct_mcm6_biallelic_snps_anc_calls_unfiltered.vcf.gz
```



__Step 5: Perform the final filtering using [`bcftools`](https://samtools.github.io/bcftools/bcftools.html)__

```bash
# Filter out any missing or triallelic sites.
bcftools view -m2 -M2 -g ^miss -Oz -o tgp_lct_mcm6_biallelic_snps_anc_calls_filtered.vcf.gz tgp_lct_mcm6_biallelic_snps_anc_calls_unfiltered.vcf.gz
```



__Step 6: Using [`scikit-allel`](https://scikit-allel.readthedocs.io/en/stable/) convert the VCF file to a HDF5 file__

```python
# Import scikit-allel
import allel

# Convert the vcf file to HDF5 format.
allel.vcf_to_hdf5(
    'tgp_lct_mcm6_biallelic_snps_anc_calls_filtered.vcf.gz',
    'tgp_lct_mcm6_biallelic_snps_anc_calls_filtered.h5',
    fields=['samples', 'GT', 'POS'], overwrite=True,
)
```



__Step 7: Download the TGP metadata file__

```bash
# Download the metadata file.
wget http://ftp.1000genomes.ebi.ac.uk/vol1/ftp/release/20130502/integrated_call_samples_v3.20130502.ALL.panel
# Change the name of the file to something more informative.
mv integrated_call_samples_v3.20130502.ALL.panel tgp_meta_data.txt
```

