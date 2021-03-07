# Schrodingers Catwalk

This repository holds the LaTeX source code to my PhD thesis, `Schrodinger's Catwalk`, 
[accessible for download here](https://github.com/flynnbr11/schrodingers_catwalk/blob/main/thesis.pdf). 
Files are organised into directories according to the *Parts* of the thesis, with each chapter assigned a unique file. 



## Figure reproduction
All data presented in the thesis can be reproduced using the [QMLA framework](https::/github.com/flynnbr11/QMLA). 
Instructions for how to install/operate the codebase are available in the [QMLA documentation](https://quantum-model-learning-agent.readthedocs.io/en/latest/).
The full configurations for each figure can be seen on the [Figure Configuration Table](https://github.com/flynnbr11/schrodingers_catwalk/blob/main/appendix/figures/figure_implementations.md). 

Given the large number of plots available, ranging from high-level perspective of the overall run, 
    down to the training of individual models, we use a ```plot_level``` between 1 and 6
    when running QMLA. 
Higher \ttt{plot\_level} instructs \gls{qmla} to generate more plots.
Note: 
- some figures in the thesis do not correspond directly to automated QMLA analysis figures. 




The figure reproduction table lists

- **Figure label**: Corresponding figure from the thesis.
- **Exploration**: Exploration strategy to implement (explained in [docs](https://quantum-model-learning-agent.readthedocs.io/en/latest/)).
- **Algorithm**: which available algorithm is used, i.e. either complete QMLA, or else QHL.
- **Experiments**: number of experiments models are trained for.
- **Particles** : number of particles models are trained with.
- **Comment**: miscellaneous further information. 
- **Data folder**: QMLA run from which the figure included in the thesis was was, available in the QMLA run data zip file. Note some thesis figures were processed offline, so the precise plot may not be included in the stored data, but can be regenerated following the configuration of this table. 
- **Plot method**: Built-in QMLA method which generates the plot
- **Plot level**: `plot_level` parameter of the QMLA run required to generate the plot
- **Folder 	Name**: subdirectory withiin the results directory (e.g. `Jan_01/01_23`) to which the plot is stored.
- **Instance run time** Time the QMLA took to complete. 
- **Number processes** Number of processes across which QMLA was parallelised to complete in the quoted time.

### Data
Data used in the preparation of figures used in the thesis can be downloaded as a ZIP file
Note some figures presented in the thesis do correspond directly to automated QMLA analysis, 
    but the run reported in the [Figure Configuration Table](https://github.com/flynnbr11/schrodingers_catwalk/blob/main/appendix/figures/figure_implementations.md)
    was analysed offline, so the figure does not exist in the dataset. 
All offline [figure development](https://github.com/flynnbr11/schrodingers_catwalk/tree/main/figure_development) 
    is made available, so it is possible to reconstruct any figure from the dataset and source code. 