# Schrodingers Catwalk

This repository holds the LaTeX source code to my PhD thesis, `Schrodinger's Catwalk`, 
[which can be downloaded as a PDF here](https://github.com/flynnbr11/schrodingers_catwalk/blob/main/thesis.pdf). 

## Abstract

Quantum technologies exploit quantum mechanical processes to achieve outcomes beyond the reach of classical machinery.
One of their most promising applications is quantum simulation, 
    whereby particles, atoms and molecules can be examined thoroughly for the first time, 
    having been beyond the scope of even the most powerful supercomputers. 

*Models* have been useful tools in understanding physical systems:
    these are mathematical structures encoding physical interactions,
    which allow us to predict how the system will behave under various conditions. 
Models of quantum systems are particularly difficult to design and test, 
    owing to the huge computational resources required to represent them accurately.
In this thesis, we introduce and develop an algorithm to characterise quantum systems efficiently, 
    by inferring a model consistent with their observed dynamics.
The *Quantum Model Learning Agent* (QMLA) is an extensible framework which permits 
    the study of any quantum system of interest, 
    by combining quantum simulation with state of the art machine learning.
QMLA iteratively proposes candidate models and trains them against the target system,
    finally declaring a single model as the best representation for the system of interest.  

We describe QMLA and its implementation through open source software,
    before testing it under a series of physical scenarios.
First, we consider idealised theoretical systems in simulation, 
    verifying the core principles of QMLA. 
Next, we incorporate strategies for generating candidate models
    by exploiting the information QMLA has gathered to date;
    by incorporating a genetic algorithm within QMLA, 
    we explore vast spaces of valid candidate models, with QMLA reliably identifying the precise target model.
Finally, we apply QMLA to *realistic* quantum systems, 
    including operating on experimental data measured from an electron spin in a nitrogen vacancy centre. 

QMLA is shown to be effective in all cases studied in this thesis;
    however, of greater interest is the platform it provides for examining quantum systems.
QMLA can aid engineers in configuring experimental setups, 
    facilitate calibration of near term quantum devices,
    and ultimately enable complete characterisation of natural quantum structures.
This thesis marks the beginning of a new line of research, 
    into automating the understanding of quantum mechanical systems.

## In this repository
* Tex files used to generate the thesis PDF. 
  * Files are organised into directories according to the *Parts* of the thesis.
  * Each chapter is written in a unique file.
    * e.g. the genetic algorithm chapter in the Theroetical Study Part is in ```theoretical_study/genetic_algorithm.tex```. 
  * Figures are stored in ```figures``` sub-directories of the corresponding Part.
    * e.g. ```theoretical_study/figures```.
* Jupyter notebooks with Python scripts to generate figures used in the thesis. 
  * Contained in ```figure_development```. 

## Figure reproduction
All data presented in the thesis can be reproduced using the [QMLA framework](https::/github.com/flynnbr11/QMLA). 
Instructions for how to install/operate the codebase are available in the [QMLA documentation](https://quantum-model-learning-agent.readthedocs.io/en/latest/).
The full configurations for each figure can be seen on the [Figure Configuration Table](https://github.com/flynnbr11/schrodingers_catwalk/blob/main/appendix/figures/figure_implementations.md). 

Given the large number of plots available, ranging from high-level perspective of the overall run, 
    down to the training of individual models, we use a ```plot_level``` between 1 and 6
    when running QMLA. 
Higher ```plot_level``` instructs QMLA to generate more plots.
Note some figures in the thesis do not correspond directly to automated QMLA analysis figures. 


The figure reproduction table lists

- **Figure label**: Corresponding figure from the thesis.
- **Exploration**: Exploration strategy to implement (explained in [docs](https://quantum-model-learning-agent.readthedocs.io/en/latest/)).
- **Algorithm**: which available algorithm is used, i.e. either complete QMLA, or else QHL.
- **Experiments**: number of experiments models are trained for.
- **Particles** : number of particles models are trained with.
- **Comment**: miscellaneous further information. 
- **Data folder**: QMLA run from which the figure included in the thesis was was, available in the QMLA run data zip file. Note some thesis figures were processed offline, so the precise plot may not be included in the stored data, but can be regenerated following the configuration of this table. 
- **Plot method**: Built-in QMLA method which generates the plot.
- **Plot level**: `plot_level` parameter of the QMLA run required to generate the plot
- **Folder 	Name**: subdirectory withiin the results directory (e.g. `Jan_01/01_23`) to which the plot is stored.
- **Instance run time** Time the QMLA took to complete. 
- **Number processes** Number of processes across which QMLA was parallelised to complete in the quoted time.

### Data
Data used in the preparation of figures used in the thesis can be [downloaded as a ZIP file here](https://drive.google.com/file/d/1tSMhjMccnvDvZGocN9avpbAvbpHhiWY8/view?usp=sharing).

Notes:
* The data set is quite large (ZIP is 5GB and unzipped 11GB).
* Some figures presented in the thesis do correspond directly to automated QMLA analysis, but the run reported in the [Figure Configuration Table](https://github.com/flynnbr11/schrodingers_catwalk/blob/main/appendix/figures/figure_implementations.md) was analysed offline, so the figure does not exist in the dataset. 
* All offline [figure development](https://github.com/flynnbr11/schrodingers_catwalk/tree/main/figure_development) is made available, so it is possible to reconstruct any figure from the dataset and source code. 

## Links
Corresponding to the `List of Publications`. 

* Papers
  * [1] The quantum model learning agent was written about in this [Nature Physics paper](https://www.nature.com/articles/s41567-021-01201-7) ([arxiv](https://arxiv.org/abs/2002.06169)). 

* Software
  * The QMLA framework is [available here](https::/github.com/flynnbr11/QMLA). 
  * Documentation, including instructions for installation, customisation and deployment, and a complete tutorial, are [available here](https://quantum-model-learning-agent.readthedocs.io/en/latest/). 

* Conferences (recordings)
  * [Bristol Quantum Information Technology workshop 2020](https://www.youtube.com/watch?v=m0UPG0aA0gY) 
  * [Quantum Techniques in Machine Learning 2020](https://www.youtube.com/watch?v=MppHO9HB2is).
