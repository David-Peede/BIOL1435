# A Hands On Introduction To OSCAR

## Resources!

As a disclaimer, if you are having problems logging in to OSCAR or setting up an SSH client for a Windows system, I would file a support ticket with ITS support (`support@ccv.brown.edu`) ASAP—ITS support is super helpful and quick! For other OSCAR related issues please refer to the [OSCAR documentation](https://docs.ccv.brown.edu/oscar/) before contacting ITS support or the instructor. Here are some sections that I think will be particularly helpful for our classes purposes:

- [Quick Start Guide](https://docs.ccv.brown.edu/oscar/getting-started)
- [Short "How To" Videos](https://docs.ccv.brown.edu/oscar/short-videos)
- [Common Linux Commands](https://docs.ccv.brown.edu/oscar/quick-reference#common-linux-commands)
- [Transferring Files To & From OSCAR](https://docs.ccv.brown.edu/oscar/managing-files/filetransfer#2.-command-line)
- [Submitting Batch Jobs](https://docs.ccv.brown.edu/oscar/submitting-jobs/batch)
- [Using Modules On OSCAR](https://docs.ccv.brown.edu/oscar/software/modules)

I will go over the most common Linux commands that I use throughout this tutorial, but if you want additional reference material I really like the website [Linuxize](https://linuxize.com/). As a quick reference here are the Linux commands I anticipate students using the most:

- [`cd` - (change directory)](https://linuxize.com/post/linux-cd-command/)
- [`pwd` - (print working directory)](https://linuxize.com/post/current-working-directory/)
- [`mv` - (move)](https://linuxize.com/post/how-to-move-files-in-linux-with-mv-command/)
- [`cp` - (copy)](https://linuxize.com/post/cp-command-in-linux/)
- [`scp` - (secure copy)](https://linuxize.com/post/how-to-use-scp-command-to-securely-transfer-files/)
- [`chmod` - (file permissions)](https://linuxize.com/post/chmod-command-in-linux/)
- [`less` - (inspect files)](https://linuxize.com/post/less-command-in-linux/)

And last, but not least I would be remiss if I did not highlight the resources for MSMC methods:

- [A practical introduction to sequentially Markovian coalescent methods for estimating demographic history from genomic data]( https://doi.org/10.1002/ece3.5888)
- [Inferring human population size and separation history from multiple genome sequences](https://doi.org/10.1038/ng.3015)
- [MSMC and MSMC2: The Multiple Sequentially Markovian Coalescent](https://doi.org/10.1007/978-1-0716-0199-0_7)



## Logging on to OSCAR.

The first thing we will need to do is log on to OSCAR! If you have a Mac you can navigate to the Terminal app or if you have a Windows computer the [OSCAR documentation](https://docs.ccv.brown.edu/oscar/getting-started#connecting-to-oscar-for-the-first-time) suggest you use [PuTTY](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html)—installation for PuTTY can be found [here](https://brown.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=9323efff-236f-4408-8006-acf3012bea9b). Once you have opened the application run the following command to log in to OSCAR.

```bash
# Command to log in to OSCAR.
ssh <username>@ssh.ccv.brown.edu
```

You will then be prompted to log in using your password associated with your Brown University account and then press enter—__NOTE:__ you will not see anything while you are typing, but will get a message from OSCAR once you have successfully logged in! If you were successful your screen should look something like this:

![oscar-login-example](/Users/davidpeede/Dropbox/GitHub/BIOL1435/lectures/figures/oscar-login-example.png)

## Navigating around OSCAR.

So we know that we are now logged on to OSCAR, but where are we really? If you ever want to know where you are on OSCAR simply type `pwd` on the command line and press enter. This command outputs your working directory to standard out (stdout), and if everything worked correctly you should see `/users/<username>` printed to stdout, which means we are in our home directory! However, it is not a good practice to work from our home directory so lets **c**hange **d**irectories by using the `cd` command, specifically I want you to move to the BIOL1435 class directory by typing the following command and then pressing enter.

```bash
# Navigate to the biol1435 directory.
cd /gpfs/data/biol1435
```

Just for good measures, let's check where we are by typing `pwd` and subsequently pressing enter and if everything works correctly you should see  `/gpfs/data/biol1435` printed to stdout. If you were successful your screen should look something like this:

![navigating-oscar-example](/Users/davidpeede/Dropbox/GitHub/BIOL1435/lectures/figures/navigating-oscar-example.png)

So we are in the `biol1435` directory, but now what? Let's take a look at what is actually in our `biol1435` directory—__NOTE:__ You should be working from the `biol1435` directory for any class related project. Type `ll` (which is equivalent to `ls -l`) and press enter. This command lists all the files that are located in your working directory to stdout in long form, which provides us some additional information that you can read more about [here](https://linuxize.com/post/how-to-list-files-in-linux-using-the-ls-command/). Again, if everything worked correctly your terminal should look similar to this:

![biol1435-directory](/Users/davidpeede/Dropbox/GitHub/BIOL1435/lectures/figures/biol1435-directory.png)

You will notice that most directories are associated with the username of students. If you have not already done so please go ahead and make yourself a directory by using the following command and pressing enter.

```bash
# Make a directory for yourself.
mkdir <username>
```

It should be noted that a directory is a lot like a folder on your local computer and much like folders, directories can store files such as documents or even other directories! As a sanity check type `ll` or `ls` and then press enter to make sure your directory is there. For your final projects, I would like you all to exclusively work from this directory, so last let's move into your newly created directory we just created by typing `cd <username>` and then pressing enter.

## The `biol1435` Directory

I want to reiterate that you should work exclusively from the directory you just made for your final project—unless you have a final project that be completed through the Jupyter Hub. The only exception is the directory I created called `code_and_data_for_students` which is where I have downloaded the data that students requested for their final projects—__NOTE:__ if you need me to download data for your final project you need to reach out to me as soon as possible, we have a limited amount of storage for the class so please don't download data to our workspace without permission.

## MSMC2

MSMC2, is a method used to infer population size history and population separation history from whole genome sequencing data. The goal of MSMC2 is to answer two questions: 1) How did the effective population size of a population change through time? 2) When and how did two populations separate from each other in the past? MSMC2 answers such questions by modeling the the entire distribution of pairwise coalescence times, which is then used to infer the coalescence rates scaled by the per base pair per generation mutation rate. Under this model coalescence rates (ie $\lambda = \frac{i(i-1)}{2} \text{ in units of } 2N \text{ generations}$) are inversely proportional to the effective population size, which is quite useful since we are interested in understanding how the effective population sizes have changed both within and between populations. I have already downloaded and preprocessed the data needed for this tutorial, which can be found at the following path: `/gpfs/data/biol1435/code_and_data_for_students/msmc_data/cg_data`. For today's exercise,  we will use two sets of trios from the publicly available "69 genomes" data set published by [Complete Genomics](http://www.completegenomics.com/public-data/69-genomes/). Here are some information on the six samples: The first three form a father-mother-child trio from the West-African Yoruba, people living in Nigeria. Here, NA19240 is the offspring, and NA19238 and NA19239 are the two parents. The second three samples form a father-mother-child trio from Utah (USA), with unspecified European ancestry. Here, NA12878 is the offspring, and NA12891 and NA12892 are the parents. Before beginning make sure you are in your directory for this class—a quick way to check is by typing `pwd` and pressing enter, which should return `/gpfs/data/biol1435/<username>`. Once you are confident that you are in the correct working directory I would like you to create a new directory called `msmc_tutorial`, then change your working directory to  `msmc_tutorial` directory by using the `cd` command, and lastly we will want to make one last directory called `logs` which will store the log files produced by SLURM.

```bash
# Make the msmc tutorial directory.
mkdir msmc_tutorial
# Move into the msmc tutorial directory.
cd msmc_tutorial
# Make the logs directory.
mkdir logs
```

If you were successful your screen should look something like this:

![msmc-directory](/Users/davidpeede/Dropbox/GitHub/BIOL1435/lectures/figures/msmc-directory.png)



## Estimating The Effective Population Size

MSMC2's purpose is to estimate coalescence rates between haplotypes through time. This can then be *interpreted* for example as the inverse effective population size through time. If the coalescence rate is estimated between subpopulations, another interpretation would be how separated the two populations became through time. In this tutorial, we will use both interpretations. In order to do so we need to know how to write files on OSCAR and how to submit them to the scheduler SLURM. For example we will use the script `infer_afr_ne.sh` and `infer_eur_ne.sh` to estimate the change in effective population size as a function of time for the AFR and EUR populations respectively. Let's start with `infer_afr_ne.sh`, to write this script on the command line simply type `vim infer_afr_ne.sh` and then press enter. This will open up a blank text editor in normal mode, to write this file first copy the contents of the SLURM script I wrote (being sure to put in your own email):

```bash
#!/bin/bash
#
#SBATCH -J afr_msmc                        # Job name
#SBATCH -N 1                               # Ensure that all cores are on one machine
#SBATCH -n 6                               # Number of cores.
#SBATCH -t 1:00:00                         # Runtime in D-HH:MM (or use minutes)
#SBATCH --mem 10g                          # Memory in MB
#SBATCH -o logs/afr_msmc-%A.out            # File for STDOUT (with jobid = %j)
#SBATCH -e logs/afr_msmc-%A.err            # File for STDERR (with jobid = %j)
#SBATCH --mail-type=ALL                    # Type of email notification: BEGIN,END,FAIL,ALL
#SBATCH --mail-user=<username>@brown.edu   # Email where notifications will be sent

# Load the msmc module on oscar.
module load msmc/2.1.2

# Initialize the path to the data.
DATA=/gpfs/data/biol1435/code_and_data_for_students/msmc_data/cg_data/

# Run msmc.
msmc2 -p 1*2+15*1+1*2 -o AFR.msmc2 -I 4,5,6,7 ${DATA}/EUR_AFR.chr1.multihetsep.txt
```

Then once it is copied type `i` which lets `vim` know that we are changing from normal mode to insert mode. Once you are in insert mode go ahead and paste the SLURM script you just copied, and then press the escape key to change back to normal mode. If everything went according to plan your screen should look something like this:

![vim-pt1](/Users/davidpeede/Dropbox/GitHub/BIOL1435/lectures/figures/vim-pt1.png)

Lastly, to save our text file and exit `vim ` type `:x`, hit enter, and lastly check the contents of your working directory using `ls` or `ll` to ensure you saved the SLURM script—__NOTE:__ `i` aka "insert", `:x` aka "save and quit", and `:q!`  aka "force quit" are the most basic yet fundamental commands you will need to use `vim` however if you want to learn more I reference [this `vim` cheat sheet](https://vim.rtorr.com/) almost every day! Now, that we have our SLURM script we need to make it executable, to do so we will need to change the [file permissions](https://linuxize.com/post/understanding-linux-file-permissions/) using the following snippet:

```bash
# Make infer_afr_ne.sh executable.
chmod +x infer_afr_ne.sh
```

If you check the contents of your working directory it should look something like this:

![file-permissions](/Users/davidpeede/Dropbox/GitHub/BIOL1435/lectures/figures/file-permissions.png)

Now, using `vim` make another SLURM script called `infer_eur_ne.sh`, fill it with the contents below (make sure you input your email), and change the file permissions such that it is executable.

```bash
#!/bin/bash
#
#SBATCH -J eur_msmc                        # Job name
#SBATCH -N 1                               # Ensure that all cores are on one machine
#SBATCH -n 6                               # Number of cores.
#SBATCH -t 1:00:00                         # Runtime in D-HH:MM (or use minutes)
#SBATCH --mem 10g                          # Memory in MB
#SBATCH -o logs/eur_msmc-%A.out            # File for STDOUT (with jobid = %j)
#SBATCH -e logs/eur_msmc-%A.err            # File for STDERR (with jobid = %j)
#SBATCH --mail-type=ALL                    # Type of email notification: BEGIN,END,FAIL,ALL
#SBATCH --mail-user=<username>@brown.edu   # Email where notifications will be sent

# Load the msmc module on oscar.
module load msmc/2.1.2

# Initialize the path to the data.
DATA=/gpfs/data/biol1435/code_and_data_for_students/msmc_data/cg_data/

# Run msmc.
msmc2 -p 1*2+15*1+1*2 -o EUR.msmc2 -I 0,1,2,3 ${DATA}/EUR_AFR.chr1.multihetsep.txt
```

If everything went according to plan your working directory should look something like this:

![vim-pt2](/Users/davidpeede/Dropbox/GitHub/BIOL1435/lectures/figures/vim-pt2.png)

Now because I know each one of these jobs will take about 15 minutes to run let's go-ahead and submit both jobs to the scheduler using the following code:

```bash
# Submit two jobs to the SLURM scheduler.
sbatch infer_afr_ne.sh
sbatch infer_eur_ne.sh
```

To check the status of your jobs you can type `myq` and press enter—note that `myq` is an OSCAR specific alias—your jobs may be running or waiting in the queue, but eventually your screen should look something like:

![sbatch](/Users/davidpeede/Dropbox/GitHub/BIOL1435/lectures/figures/sbatch.png)

Ok now let's go over a couple things. First, to submit a job to SLURM it needs to be in the form of a SLURM script—ie have a SLURM header—for example:

```bash
#!/bin/bash
#
#SBATCH -J eur_msmc                        # Job name
#SBATCH -N 1                               # Ensure that all cores are on one machine
#SBATCH -n 6                               # Number of cores.
#SBATCH -t 1:00:00                         # Runtime in D-HH:MM (or use minutes)
#SBATCH --mem 10g                          # Memory in MB
#SBATCH -o logs/eur_msmc-%A.out            # File for STDOUT (with jobid = %j)
#SBATCH -e logs/eur_msmc-%A.err            # File for STDERR (with jobid = %j)
#SBATCH --mail-type=ALL                    # Type of email notification: BEGIN,END,FAIL,ALL
#SBATCH --mail-user=<username>@brown.edu   # Email where notifications will be sent
```

Hopefully between the annotated code and the [phenomenal OSCAR documentation](https://docs.ccv.brown.edu/oscar/submitting-jobs/batch#sbatch-command-options) you should be able to tease apart the different components of the SLURM header, but if you have any questions feel free to reach out and ask! Now, let's go over exactly what the code we just submitted is doing. The `-p 1*2+15*1+1*2` option defines the time segment patterning, for which we will estimate coalescent rates for. By default, MSMC2 uses 32 time segments, grouped as `1*2+25*1+1*2+1*3`, which means that the first two segments are joined (forcing the coalescence rate to be the same in both segments), then 25 segments each with their own rate, and then again two groups of two and three, respectively. MSMC2's run time and memory usage scales quadratically with the number of time segments. Since we are only analyzing a single chromosome, we should reduce the number of segments to avoid overfitting. Following the author's recommendations we are using 18 segments, with two groups in the front and back. Grouping helps avoiding overfitting, as it reduces the number of free parameters. The `-o` option denotes an output prefix. The three files generated by MSMC2 will be called using this prefix with endings `.final.txt`, `.loop.txt` and `.log`. The `-I` option denotes the 0-based indices of the haplotypes analysed. In our case we have eight haplotypes, the first four being of European ancestry, the latter of African ancestry. In `infer_eur_ne.sh` we estimate coalescence rates within the European chromosomes (indices 0,1,2,3), and in `infer_afr_ne.sh` within the African chromosomes (indices 4,5,6,7). The last argument to `msmc2` is the multihetsep file. Normally one would run it on all 22 chromosomes, and in that case one would simply give all those 22 files in a row.

## Estimating Population Seperation History

Above we have run MSMC2 on each population individually. In order to better understand when and how the two  populations separated, we will use MSMC2 to estimate the coalescence rate across populations using the following SLURM script `infer_split.sh`: 

```bash
#!/bin/bash
#
#SBATCH -J split_msmc                      # Job name
#SBATCH -N 1                               # Ensure that all cores are on one machine
#SBATCH -n 6                               # Number of cores.
#SBATCH -t 1:00:00                         # Runtime in D-HH:MM (or use minutes)
#SBATCH --mem 5g                           # Memory in MB
#SBATCH -o logs/split_msmc-%A.out          # File for STDOUT (with jobid = %j)
#SBATCH -e logs/split_msmc-%A.err          # File for STDERR (with jobid = %j)
#SBATCH --mail-type=ALL                    # Type of email notification: BEGIN,END,FAIL,ALL
#SBATCH --mail-user=<username>@brown.edu   # Email where notifications will be sent

# Load the msmc module on oscar.
module load msmc/2.1.2

# Initialize the path to the data.
DATA=/gpfs/data/biol1435/code_and_data_for_students/msmc_data/cg_data/

# Run msmc.
msmc2 -t 6 -I 0-4,0-5,1-4,1-5 -s -p 1*2+15*1+1*2 -o AFR_EUR.msmc2 ${DATA}/EUR_AFR.chr1.multihetsep.txt
```

However, instead of using `vim` I would like you to copy, paste, add your email, and then save this script to the downloads folder on your local system. To move local files to OSCAR, as well as move files on OSCAR to your local system, we will use the secure copy (`scp`) command, which has the general form of `scp <source> <destination>`, to securely copy `infer_split.sh` open a new terminal on your local system and make sure you are in your downloads directory. Next execute the following command:

```bash
# Securely copy infer_split.sh from your local system to OSCAR.
scp infer_split.sh <username>@ssh.ccv.brown.edu:/gpfs/data/biol1435/<username>/msmc_tutorial
```

After which you will be prompted to enter your password, just like when you logged in OSCAR! If everything worked out your local terminal should look something like:

![local2oscar](/Users/davidpeede/Dropbox/GitHub/BIOL1435/lectures/figures/local2oscar.png)

And your directory on OSCAR should look something like:

![scp2oscar](/Users/davidpeede/Dropbox/GitHub/BIOL1435/lectures/figures/scp2oscar.png)

Now let's go ahead and submit `infer_split.sh` to the SLURM scheduler by executing `sbatch infer_split.sh ` and while that runs either use `vim` or the secure copy to create and make `compute_cross_coal.sh` executable (BUT DO NOT SUBMIT YET):

```bash
#!/bin/bash
#
#SBATCH -J cross_coal_msmc                 # Job name
#SBATCH -N 1                               # Ensure that all cores are on one machine
#SBATCH -n 6                               # Number of cores.
#SBATCH -t 1:00:00                         # Runtime in D-HH:MM (or use minutes)
#SBATCH --mem 1g                           # Memory in MB
#SBATCH -o logs/cross_coal_msmc-%A.out     # File for STDOUT (with jobid = %j)
#SBATCH -e logs/cross_coal_msmc-%A.err     # File for STDERR (with jobid = %j)
#SBATCH --mail-type=ALL                    # Type of email notification: BEGIN,END,FAIL,ALL
#SBATCH --mail-user=<username>@brown.edu  # Email where notifications will be sent

# Initialize the path to the helper functions.
HELP=/gpfs/data/biol1435/code_and_data_for_students/msmc_data/msmc-tools

# Compute the cross coalescence rates.
${HELP}/combineCrossCoal.py AFR_EUR.msmc2.final.txt EUR.msmc2.final.txt AFR.msmc2.final.txt > AFR_EUR.combined.msmc2.final.txt
```

As well as the same for `msmc_to_demes.sh`:

```bash
#!/bin/bash
#
#SBATCH -J msmc2demes                      # Job name
#SBATCH -N 1                               # Ensure that all cores are on one machine
#SBATCH -n 1                               # Number of cores.
#SBATCH -t 1:00:00                         # Runtime in D-HH:MM (or use minutes)
#SBATCH --mem 2g                           # Memory in MB
#SBATCH -o logs/msmc2demes-%A.out          # File for STDOUT (with jobid = %j)
#SBATCH -e logs/msmc2demes-%A.err          # File for STDERR (with jobid = %j)
#SBATCH --mail-type=ALL                    # Type of email notification: BEGIN,END,FAIL,ALL
#SBATCH --mail-user=<username>@brown.edu   # Email where notifications will be sent

# Load the python module on oscar.
module load python/3.9.0

# Initialize the path to the helper functions.
HELP=/gpfs/data/biol1435/code_and_data_for_students/msmc_data/msmc-tools

# Convert the msmc results to a demes yaml.
python3 ${HELP}/convert_msmc_to_demes.py EUR.msmc2.final.txt 1.25e-8 > EUR.msmc2.final.demes.yaml
python3 ${HELP}/convert_msmc_to_demes.py AFR.msmc2.final.txt 1.25e-8 > AFR.msmc2.final.demes.yaml
```

Once you are done go-ahead and check your queue using `myq` to see if we are ready to submit those last two jobs to the SLURM scheduler. If your  working directory looks something like this:

![empty-queue](/Users/davidpeede/Dropbox/GitHub/BIOL1435/lectures/figures/empty-queue.png)

###### Then go ahead and submit those last two SLURM scripts—ie:

```bash
# Calculate relative cross coalesences rates.
sbatch compute_cross_coal.sh
# Convert the msmc output to demes format for the single population analyses.
sbatch msmc_to_demes.sh
```

 Now, while those run let's go-over what we actually did. In `infer_split.sh` we are using six cores (`-t 6`) and are running the first two parental chromosomes in each subpopulation—if you wanted to analyze all eight haplotypes (which would take considerably longer), you would have had to say `-I 0-4,0-5,0-6,0-7,1-4,1-5,1-6,1-7,2-4,2-5,2-6,2-7,3-4,3-5,3-6,3-7`. The `-s` flag tells MSMC2 to skip sites with ambiguous phasing and in general, for population size estimates the authors of MSMC2 have found that unphased sites are not so much of a problem, but for cross-population analysis those sites should be removed. In `compute_cross_coal.sh` we are computing the  relative cross coalescence rate (rCCR)—ie the ratio of the across-rate to the mean within-rate. The rCCR ranges between 0 and 1, and indicates when and how the two populations diverged. Values close to 1 indicate that the two populations were really one population at that time. At the time when the rCCR drops to zero, the two populations likely separated into two isolated populations. Heuristically, the mid-point of that decline—ie the time when the rCCR hits 0.5—is often taken to be an estimate for the split time between the two populations. The last script `msmc_to_demes.sh` simply converts the within population MSMC2 results to a `demes` yaml so we can utilize `demesdraw`! Now that we know what the code is doing, let's check to see if all our jobs have stoped running by using the command `myq`—it is also good practice to check your email notifications to make sure the jobs actually completed and didn't fail! Once all our jobs have completed lets now securely copy the result files from OSCAR to our local computer using `scp`:

```bash
# Download the msmc results for plotting.
scp <username>@ssh.ccv.brown.edu:/gpfs/data/biol1435/<username>/msmc_tutorial/*.final.txt .
# Download the msmc single population yaml file.
scp <username>@ssh.ccv.brown.edu:/gpfs/data/biol1435/<username>/msmc_tutorial/*.yaml .
```

If you correctly completed the last step your terminal on your local system should look similar to:

![oscar2local](/Users/davidpeede/Dropbox/GitHub/BIOL1435/lectures/figures/oscar2local.png)

And that is it for the introduction to OSCAR, now let's finish the MSMC analyses on the Jupyter Hub!