#!/bin/bash
#
#SBATCH -J 1Kgenomes							#job name
#SBATCH -N 1									#ensure that all cores are on one node
#SBATCH -n 4									#number of cores
#SBATCH -t 1-0									#runtime in D-HH:MM
#SBATCH --mem 2G								#memory in GB
#SBATCH -o 1Kgenomes-%A.out						#file for STDOUT
#SBATCH -e 1Kgenomes-%A.err						#file for STDERR
#SBATCH --mail-type=ALL							#type of email notification: BEGIN,END,FAIL
#SBATCH --mail-user=yourUsername@brown.edu		#email where notifications will be sent


###download the 1K Genomes Project Panel file to the current directory
wget http://ftp.1000genomes.ebi.ac.uk/vol1/ftp/release/20130502/integrated_call_samples_v3.20130502.ALL.panel 