# Schrodingers Catwalk

This repository holds the LaTeX source code to my PhD thesis, `Schrodinger's Catwalk`. 
Files are organised according to the *Parts* of the thesis, with each chapter assigned a unique file. 



## Figure reproduction
All data presented in the thesis can be reproduced using the [QMLA framework](https::/github.com/flynnbr11/QMLA). 
Instructions for how to install/operate the codebase are available in the [QMLA documentation](https://quantum-model-learning-agent.readthedocs.io/en/latest/).
The full configurations for each figure can be seen [on this table](https://github.com/flynnbr11/schrodingers_catwalk/blob/main/appendix/figures/figure_implementations.md). 
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