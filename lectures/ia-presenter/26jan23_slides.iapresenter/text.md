# BIOL 1435
	Course Instructor: Dave Peede (he/him/his)
	Meeting Times: Tu/Thu 2:30 pm - 3:50 pm

Welcome to BIOL 1435, you have worked hard to be here; you belong here! Congratulations on all your achievements thus far, and welcome to the course! I’m excited you are here, and I hope it will be a great semester!

My name is David Peede, but please call me Dave. I am a 3rd year PhD candidate studying speciation genetics and I will be the instructor for this course.

---
## This semester we will learn about...

So I would like to start out with two house keeping items. 1) I approved all override requests so it is up to you to decide if this class is a good fit.
2) The course is technically called "Computational Methods for Studying Demographic History with Molecular Data" but a more accurate course title is "Theoretical Aspects and Computational Methods for Studying Evolutionary Genetics."

This semester we will cover four modules and hopefully get to module five.

---
#### Evolutionary Genetics
/assets/26jan23_drift_sim.svg
size: contain
y: bottom

In module one we will go over some foundational concepts in evolutionary genetics. For example, the plot I am showing shows the change in allele frequencies over 1000 generations for a population consisting of 1000 diploid individuals with an initial allele frequency of 0.5.

Question: Can someone explain why the final frequency is different between simulation replicates?

Answer: Random chance aka genetic drift! When we simulate this process over many generations even small fluctuations each generation can lead to large changes over time. Genetic drift is a random process so in each generation an allele may increase or decrease. 

---
#### Coalescent Theory & Tree-Thinking[^Data from: Cui et al., 2013]
/assets/26jan23_fish_trees.svg
size: contain
y: bottom

In module two we will dive into coalescent theory, which is a model used to study how lineages of alleles in a sample have originated from a common ancestor. You may be familiar with this concept in terms of a phylogenetic tree. On the left I have plotted the consensus tree for 26 species of swordtail fish found throughout Mexico. In this class we will refer to these type of trees as species or population trees, as they describe the overall evolutionary relationship among lineages. However, as you all will soon learn, every locus in the genome actually has its own unique evolutionary history. On the right I have plotted the 160 individual genealogical or gene trees for which show variation in both tree topology and size. (Note to self: the node colors correspond to geographic sampling).

Question: Why might an individual gene tree differ from the species tree?

Answer: Gene flow, unequal rates of evolution, ILS

---
#### Population Differentiation & Demography[^Demographic model from: Ragsdale & Gravel, 2019]
/assets/26jan23_ooa_aa.svg
size: contain
y: bottom

In module three we will learn how to identify population structure, make inferences about gene flow, and about different techniques to infer the demographic history from a set of samples. I have plotted a schematic of the "Out of Africa with Archaic Admixture Model" which is a popular model to simulate genetic data in the field of human population genetics.

Question: Does someone what to take a crack at interpreting this schematic?

---
#### Recombination & Selection
/assets/26jan23_sel_sweep.svg
size: contain
y: bottom

In the last module we will discover how the recombination process and natural selection complicate everything we learned in the previous three modules. For example, to generate this figure I simulated a 1 Mb locus where I introduced a beneficial mutation in the middle of the locus. The dashed line represents the neutral expectation for diversity (ie pi = 4 * Ne) but we can see that our simulation differs from this expectation.

Question: What trends might we be able to conclude from this plot?

Answer: Positive selection reduces genetic diversity.

---
## Icebreaker 🥶

I would like everyone to say their name, year, major, and favorite place to eat in Providence.

---
## Syllabus 📑

Go through the syllabus here.

---
## JupyterHub Etiquette 💻

Now I would like to quickly go over some Jupyter Hub etiquette.

---
## [https://biol1435.jupyter.brown.edu](https://biol1435.jupyter.brown.edu) 

So, the hub takes roughly ~10 minutes to warm up if there are no users, and since we will be coding most classes when you come to class please log in.

---
## Do not load anything to JupyterHub unless instructed 🙅‍♀️🙅

We have limited storage and computing resources, so please don't upload anything that I haven't asked you to. These kind of issues will impact everyone so please cognizant. 

---
## Save your work early and often 😅

This is just good rule of thumb in general and you will thank me later for doing so.

---
## For assignments you *may* want to download your work 😰

I have been assured that there hasn't been issues like this yet, but there is a non-zero probability that something may happen to Brown's google server and delete everything. So for problem sets especially, it may be good idea to download your Jupyter notebook after you are done working on it for the day.

---
#### Always shut down your sever
/assets/26jan23_shut_down.png
size: contain
y: bottom

And lastly shutting down your server after you are done working not only is a good practice, but will always free up resources for your classmates!

---
## How to be successful in BIOL 1435 🏆

A lot of students have been emailing about how to be successful in this course so here is a quick guide.
---
## Do the readings 📖

First, and foremost do the readings. All the readings are up on canvas already. It is a lot of reading, but I chose the papers for a reason and will often use the data from. Those papers in assignments.

---
## Ask questions 🙋‍♀️🙋

If you have questions please write them down! Write questions down while you are doing the readings and during the lectures. Ask me about them during class or office hours. Additionally, at the end of every class I will have a google form where you all can let me know what was unclear. I will try my best to address as many of these as possible, and I will make clarification videos for concepts that multiple students are confused about.

---
## Follow the rubrics 🔎

For each assignment I have explicitly indicated what is necessary to receive full credit. If you address all those points then you will be in good shape.

---
#### Look at Dave's coding resources 
/assets/26jan23_biol1435_github.png
size: contain
y: bottom

Sometimes it is hard to find good coding resources, but I will always make my lecture code publicly available along with identifying resources that I find helpful. For example, if you go to the course's GitHub repository you will find some helpful resources.

---
/assets/26jan23_example_nb.png
size: contain

You can also navigate to the lectures directory where you can view all the Jupyter notebooks to reproduce the simulations and plots used in lectures. These may also be helpful for writing your own code!

---
## Exit Ticket ⚠️: https://forms.gle/anDi6iTCxMnNzQFs7

Lastly, I will need every class by posting some type of exit ticket. This is part of how I will determine participation grades as well as receive feedback to make the course better!

---
#### JupyterHub Etiquette 
	1. When you get into class please log on
	2. Do not upload anything to JupyterHub
	3. Save early and often
	4. For assignments you *may* want to download your work
	5. Always shut down your server

---
#### How to be successful in this course
	1. Do the readings
	2. Ask questions
	3. Start assignments early
	4. Follow the rubrics
	5. Look at Dave's code