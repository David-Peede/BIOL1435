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

In module two we will dive into coalescent theory, which is a model used to study how lineages of alleles in a sample have originated from a common ancestor. You may be familiar with this concept in terms of a phylogenetic tree, which is depicted on the left. In this class we will refer to these type of trees as species or population trees, as they describe the overall evolutionary relationship among lineages. On the right I have plotted the 160 individual genealogical or gene trees which described the evolutionary relationship among lineages for a particular locus. (Note to self: the node colors correspond to geographic sampling).

Question: Why might an individual gene tree differ from the species tree?

Answer: Gene flow, unequal rates of evolution, ILS

---
#### Population Differentiation & Demography[^Demographic model from: Ragsdale & Gravel, 2019]
/assets/26jan23_ooa_aa.svg
size: contain
y: bottom

In module three we will learn how to identify population structure, make inferences about gene flow, and about different techniques to infer the demographic history from a set of samples.

Question: Who would like to take a guess about what the arrows mean in this figure.

Answer: Divergence and gene flow.

---
#### Recombination & Selection
/assets/26jan23_sel_sweep.svg
size: contain
y: bottom

In the last module we will discover how the recombination process and natural selection complicate everything we learned in the previous three modules. For example, to generate this figure I simulated a 1 Mb locus where I introduced a beneficial in the middle of the locus. The dashed line represents the neutral expectation for diversity (ie pi = 4 * Ne) but we can see that our simulation differs from this expectation.

Question: What trends might we be able to conclude from this plot?

Answer: Positive selection reduces genetic diversity.

---
## Icebreaker

I would like everyone to say there name, year, major, and favorite place to eat in Providence.

---
## Syllabus

Go through the syllabus here.

---
## JupyterHub Etiquette 

Now I would like to quickly go over some Jupyter Hub etiquette.

---
## [https://biol1435.jupyter.brown.edu](https://biol1435.jupyter.brown.edu) 

So, the hub takes roughly ~10 minutes to warm up if there are no users, and since we will be coding most classes when you come to class please log in.

---
## Do not load anything to JupyterHub unless instructed

We have limited storage and computing resources, so please don't upload anything that I haven't asked you to. These kind of issues will impact everyone so please cognizant. 

---
## Save your work early and often

This is just good rule of thumb in general and you will thank me later.

---
## For assignments you *may* want to download your work

I have been told that there hasn't been issues yet but it is a non-zero probability that something happened to Brown's google server and delete everything. So for problem sets especially, it may be good idea to download your Jupyter notebook after you are done working on it for the day.

---
#### Always shut down your sever
/assets/26jan23_shut_down.png
size: contain
y: bottom

Shutting down your server after you are done working not only  is a good practice, but will always free up resources for your classmates!

---
## How to be successful in BIOL 1435

So here is a quick guide for how to be successful in this course.

---
## Do the readings

First, and foremost do the readings. All the readings are up on canvas already. It is a lot of reading, but I chose the papers for a reason and will use them in assignments.

---
## Ask questions

If you have questions please write them down! Write questions down while you are doing the readings and during the lectures. Ask me about them during class or office hours. Additionally, at the end of every class I will have a google form where you all can let me know what was unclear. I will try my best to address as many of these as possible, and I will make clarification videos for concepts that multiple students are confused about.

---
## Follow the rubrics

For each assignment I have explicitly indicated what is necessary to receive full credit. Address all those points and you will be in good shape.

---

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

---
## Exit Ticket