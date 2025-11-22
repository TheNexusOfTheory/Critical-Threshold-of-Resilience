# 🚀 Transversal Critical Resilience Theory (TCRT) Modeling

**Author:** The Nexus Of Theory  
**Development Contact:** [adaptivemodeling@gmail.com]  
**GitHub Handle:** [@CrossDisciplineTheory]  
**Cited Code Version:** v1.0.0 (Corresponding to the arXiv submission)  

***

## 🔬 Project Description

This repository holds the fundamental **computational models** and simulation data for the **Transversal Critical Resilience Theory (TCRT)**. The theory focuses on the analysis of **critical thresholds** ($A_c$) and the dynamics of complex adaptive systems, with applications across various sciences (physics, economics, ecology).

The goal is to facilitate the **total reproducibility** of the results presented in the associated manuscript.

***

## 📂 Repository Structure

| Directory/File | Content | Purpose |
| :--- | :--- | :--- |
| `code/` | Primary Python scripts. | Core model functions and visualization routines. |
| `data/` | Simulation data in CSV format. | Contains the discrete data used for appendix tables. |
| `figures/` | Generated image files. | Graphical results (Figure 1) for quick verification. |
| `README.md` | This file. | Documentation and repository guide. |
| `LICENSE` | Code usage license. | Defines the rights for software use and attribution. |

***

## 💻 Code Files

The following scripts are located in the `code/` folder:

* **`tcr_core_model.py`**: Contains the base Resilience function $R(A, E, n)$ and the logic for calculating critical thresholds. This code corresponds to the function cited in the Appendix of the manuscript.
* **`resilience_curve_plot.py`**: Script that generates the Resilience logistic curve and the visualization of the **Double Critical Separatrix** (Figure 1 of the manuscript).

## 📊 Simulation Data

The file **`data/tcr_simulation_results.csv`** contains the discrete values for $A$, $E$, $n$, and the resulting Resilience ($R$) used to construct the example results table in the Appendix.

***

## 🤝 Code Suggestions Policy

Due to the repository's restrictive license (All Rights Reserved), we do not accept external Pull Requests.

If you have suggestions for bug fixes, optimizations, or new features, please **open a new Issue** and attach your proposed changes as a code block or a .patch file for manual review and inclusion by the primary author.

***

## 🔗 Citation and Permanent Archive

This code has been archived on **Zenodo** to ensure permanence and citability.

If you use this code or rely on the implementation for your own research, please cite the version archived:

**[CITATION PENDING]**

*Once you obtain the DOI from Zenodo, insert it here.*

**Associated Manuscript:** [Title of the TCRT Manuscript], submitted to arXiv (Pre-print ID: [Pending]).
