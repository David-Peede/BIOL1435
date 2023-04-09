#!/bin/bash
#
#SBATCH -J butterfly_bootstraps            # Job name.
#SBATCH -N 1                               # Ensure that all cores are on one machine.
#SBATCH -n 1                               # Number of cores.
#SBATCH -t 1:00:00                         # Runtime in D-HH:MM (or use minutes).
#SBATCH --mem 2g                           # Memory in GB.
#SBATCH -o butterfly_bootstraps-%A.out     # File for STDOUT (with jobid = %j).
#SBATCH -e butterfly_bootstraps-%A.err     # File for STDERR (with jobid = %j).
#SBATCH --mail-type=ALL                    # Type of email notification: BEGIN,END,FAIL,ALL.
#SBATCH --mail-user=<username>@brown.edu   # Email where notifications will be sent.

# Load the python module on oscar.
module load python/3.11.0

# Perform Fst and D+ bootstrapping for the butterflies.
python heli_chr18_100kb_bootstrapping.py