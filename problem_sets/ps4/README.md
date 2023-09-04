# Problem Set 4

Here is how you can recreate the files in the `data` directory for this problem set.

__Step 1: Download the _Heliconius_ VCF file from [Martin et al. 2020](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.2006288)__

```bash
# Download the Heliconius data.
wget https://doi.org/10.5061/dryad.sk2pd88/bar92.DP8MP4BIMAC2HET75.hapFem.minimal.corrected.vcf.gz
```



__Step 2: Index the VCF file with [`tabix`](http://www.htslib.org/doc/tabix.html)__

```bash
# Index the Heliconius data.
tabix -p vcf bar92.DP8MP4BIMAC2HET75.hapFem.minimal.corrected.vcf.gz
```



__Step 3: Subset out the chromosome 18 region and focal samples using [`bcftools`](https://samtools.github.io/bcftools/bcftools.html)__

```bash
# Filter the data to only include the focal samples and chromosome 18.
bcftools view -S heli_focal_samples.txt -r chr18 -Oz -o heli_chrom18.vcf.gz bar92.DP8MP4BIMAC2HET75.hapFem.minimal.corrected.vcf.gz
```



__Step 4: Using [`scikit-allel`](https://scikit-allel.readthedocs.io/en/stable/) convert the VCF file to a HDF5 file__

```python
# Import scikit-allel
import allel

# Convert the vcf file to HDF5 format.
allel.vcf_to_hdf5(
    'heli_chr18.vcf.gz', 'heli_chr18.h5',
    fields=['samples', 'calldata/GT', 'variants/POS'], overwrite=True,
)
```


