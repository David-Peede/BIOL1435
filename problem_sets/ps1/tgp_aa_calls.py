# Import modules
import gzip
import re
import sys

# Intialize the input and output file.
infile = '{0}.vcf.gz'.format(sys.argv[1])
outfile = sys.stdout

# Using the gzip package open the infile.
with gzip.open(infile, 'rt') as file:
    # For every line in the vcf...
    for line in file:
        # If the line contains meta information.
        if '##' in line:
            # Write the line.
            outfile.write(line)
        # Else-if the line is the header line.
        elif '#' in line:
            # Split the line by tabs.
            spline = line.split()
            # Append a placeholder individual.
            spline.append('Ancestor')
            # Join and write the line.
            outLine = '\t'.join(spline)
            outfile.write(outLine+'\n')
        # Else...
        else:
            # Split the line by tabs.
            spline = line.split()
            # If the site has ancestral allele information and is a SNP.
            if 'AA' in spline[7] and 'VT=SNP' in spline[7]:
                # Extrtact the ancestral allele.
                anc_allele_search = re.search('^.+;AA=(\S+)\|\|\|.+', spline[7])
                anc_allele = anc_allele_search.group(1)
                # Assign the genotype for the placeholder individual.
                if spline[3] == anc_allele.upper():
                    anc_allele = '0|0'
                elif spline[4] == anc_allele.upper():
                    anc_allele = '1|1'
                else:
                    anc_allele = './.'
            # Else set to missing.
            else:
                anc_allele = './.'
            # Append the ancestral allele call.
            spline.append(anc_allele)
            # Join and write the line.
            outLine = '\t'.join(spline)
            outfile.write(outLine+'\n')
