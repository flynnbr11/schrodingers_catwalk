# Schrodingers Catwalk

This repository holds the LaTeX source code to my PhD thesis, `Schrodinger's Catwalk`, 
[which can be downloaded as a PDF here](https://github.com/flynnbr11/schrodingers_catwalk/blob/main/thesis.pdf). 

## Abstract


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
Corresponding to the list of publications. 

* Papers
  * [1] The quantum model learning agent was written about in this (accepted) [Nature Physics paper](https://arxiv.org/abs/2002.06169). 

* Software
  * The QMLA framework is [available here](https::/github.com/flynnbr11/QMLA). 
  * Documentation, including instructions for installation, customisation and deployment, and a complete tutorial, are [available here](https://quantum-model-learning-agent.readthedocs.io/en/latest/). 

* Conferences (recordings)
  * [Bristol Quantum Information Technology workshop 2020](https://www.youtube.com/watch?v=m0UPG0aA0gY) 
  * [Quantum Techniques in Machine Learning 2020](https://www.youtube.com/watch?v=MppHO9HB2is).