# Import modules.
import numpy as np
import pandas as pd


# Define a function to calculate the Fst for a given locus.
def avg_fst(pop_a_freqs, pop_b_freqs):
    # Calculate the average gene diversity within the populations.
    H_w = ((pop_a_freqs * (1 - pop_a_freqs)) + (pop_b_freqs * (1 - pop_b_freqs)))
    # Calculate the average gene diversity between populations.
    H_b = ((pop_a_freqs * (1 - pop_b_freqs)) + (pop_b_freqs * (1 - pop_a_freqs)))
    # Calculatae the numerator and denominator of Fst.
    fst_num = H_b - H_w
    fst_den = H_b
    # Calculate the average Fst for this locus.
    fst = np.nansum(fst_num) / np.nansum(fst_den)
    return fst

def dplus(p1, p2, p3, p4):
    # Polarize the alternative allele frequency arrays.
    p1 = np.where(p4 > 0, np.abs(p1 - 1), p1)
    p2 = np.where(p4 > 0, np.abs(p2 - 1), p2)
    p3 = np.where(p4 > 0, np.abs(p3 - 1), p3)
    p4 = np.where(p4 > 0, np.abs(p4 - 1), p4)
    # Calculate site pattern counts.
    abba = np.nansum((1 - p1) * (p2) * (p3) * (1 - p4))
    baba = np.nansum((p1) * (1 - p2) * (p3) * (1 - p4))
    baaa = np.nansum((p1) * (1 - p2) * (1 - p3) * (1 - p4))
    abaa = np.nansum((1 - p1) * (p2) * (1 - p3) * (1 - p4))
    # If the denominator is undefined...
    if ((abba + baba) + (baaa + abaa)) == 0:
        # Set D+ to np.nan.
        dplus = np.nan
    # Else...
    else:
        # Claculate D+.
        dplus = (((abba - baba) + (baaa - abaa)) / ((abba + baba) + (baaa + abaa)))
    return dplus

# Load the aleternative allele count matrix.
heli_chr18_aac = np.loadtxt(
    '/gpfs/data/biol1435/code_and_data_for_students/ps4_heliconius_data/heli_chr18_aac.csv.gz',
    dtype=np.float64, delimiter=',',
)

# Load the positions array.
heli_chr18_pos = np.loadtxt(
    '/gpfs/data/biol1435/code_and_data_for_students/ps4_heliconius_data/heli_chr18_pos.csv.gz',
    dtype=int, delimiter=',',
)

# Load the meta data.
heli_chr18_meta_df = pd.read_csv('/gpfs/data/biol1435/code_and_data_for_students/ps4_heliconius_data/heli_chr18_samps.csv.gz')

# Extract the unique sample ids.
heli_species = heli_chr18_meta_df['species'].unique()
# Intialize a dictionary to store sample ids.
heli_idx_dicc = {}
# For every species...
for spc in heli_species:
    # Fill the dictionary.
    heli_idx_dicc[spc] = heli_chr18_meta_df[heli_chr18_meta_df['species'] == spc].index.values
    
# Intialize an allele count matrix dictionary.
heli_aac_dicc = {}
# intialize a alternative allele frequency dictionary.
heli_freq_dicc = {}
# For every species...
for spc in heli_species:
    # Determine the number of chromosomes with allele calls.
    called_chroms = np.count_nonzero(~np.isnan(heli_chr18_aac[:, heli_idx_dicc[spc]]), axis=1) * 2
    # Determine the allele counts of the alternative allele.
    per_site_aac = np.nansum(heli_chr18_aac[:, heli_idx_dicc[spc]], axis=1)
    # Fill the frequency dictionary.
    heli_freq_dicc[spc] = per_site_aac / called_chroms

# Intialize lists to store bootstrapped values.
fst_bs_list = []
dplus_mal_bs_list = []
dplus_ama_bs_list = []

# For 1000 bootstrap replicates.
for _ in range(1000):
    # Randomly generate a start and end position.
    start = np.random.randint((16803890 - 99999))
    end = start + 100000
    # Identify the variants that fall within the 100 kb window.
    variants = np.where(((start <= heli_chr18_pos) & (heli_chr18_pos <= end)))[0]
    # If there are no variants to perform calculations...
    if (variants.size == 0):
        # Updated the the bootstrapped results.
        fst_bs_list.append(np.nan)
        dplus_mal_bs_list.append(np.nan)
        dplus_ama_bs_list.append(np.nan)
    # Else...
    else:
        # Compute fst.
        fst = avg_fst(
            heli_freq_dicc['mal'][variants],
            heli_freq_dicc['ama'][variants],
        )
        # Compute D+.
        dplus_mal = dplus(
            p1=heli_freq_dicc['chi'][variants],
            p2=heli_freq_dicc['flo'][variants], 
            p3=heli_freq_dicc['mal'][variants],
            p4=heli_freq_dicc['nu_sil'][variants],
        )
        dplus_ama = dplus(
            p1=heli_freq_dicc['chi'][variants],
            p2=heli_freq_dicc['flo'][variants], 
            p3=heli_freq_dicc['ama'][variants],
            p4=heli_freq_dicc['nu_sil'][variants],
        )
        # Updated the the bootstrapped results.
        fst_bs_list.append(fst)
        dplus_mal_bs_list.append(dplus_mal)
        dplus_ama_bs_list.append(dplus_ama)

# Export the bootstrapped results.
np.savetxt(
    './heli_chr18_fst_100kb_bs.csv.gz',
    [np.array(fst_bs_list)], fmt='%1.5f', delimiter=',',
)
np.savetxt(
    './heli_chr18_dplus_mal_100kb_bs.csv.gz',
    [np.array(dplus_mal_bs_list)], fmt='%1.5f', delimiter=',',
)
np.savetxt(
    './heli_chr18_dplus_ama_100kb_bs.csv.gz',
    [np.array(dplus_ama_bs_list)], fmt='%1.5f', delimiter=',',
)
