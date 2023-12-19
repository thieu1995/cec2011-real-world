# Install environments

Install based on `requirements.txt` file.  After that, you need to install the `octave` and set up the path to 
the `octave-cli.exe` file.
The tested working version: `oct2py=5.6.0` and `octave=8.4.0 windows 64`. 


### On Windows 

```code
1. Download the octave from here: https://octave.org/download
2. Install it (default is on C:\ drive)
3. Setup the path to the octave-cli. 
    + Search google how to access to: Environment Variables windows (Your version)
    + In tab User variables: click New
    + Add variable name: OCTAVE_EXECUTABLE
    + And variable value: C:\Octave\Octave-5.2.0\mingw64\bin\octave-cli.exe  (This is my path, change with your path).
    + Save it and restart your computer.
```

<p align="center">
<img src=".github/img/01.png" alt="environments path">
</p>

<p align="center">
<img src=".github/img/02.png" alt="environments path">
</p>

### On Ubuntu/Linux

```code
1. Search google how to install Octave on ubuntu/linux.
2. For example: 
    + https://vitux.com/how-to-install-gnu-octave-in-ubuntu/
    + https://blog.eldernode.com/install-gnu-octave-on-ubuntu-20-04/
```



# Usage

Add your Algorithms/Optimizers in current directory (in folder: cec2011-real-world/).
See the run_examples.py to know how to create the problem class and how to use it.

### Problem definition

```python
from cec2011_class import Problem01
import numpy as np

## Create object 
prolem = Problem01()

## Get the ndim, lowerbound, upperbound
print(f"N dimenisons: {prolem.ndim}")
print(f"Lower bound: {prolem.lb}")
print(f"Upper bound: {prolem.ub}")

## Create a random solution
X = np.random.uniform(prolem.lb, prolem.ub)
print(f"Solution: {X}")

## Calculate the fitness value
fitness = prolem.evaluate(X)
print(f"Fitness: {fitness}")
```

<p align="center">
<img src=".github/img/03.png" alt="example with problem">
</p>


### How to use with MEALPY library

```python
from cec2011_class import Problem01
from mealpy import SMA, FloatVar

prob = Problem01()
problem = {
    "bounds": FloatVar(lb=prob.lb, ub=prob.ub),
    "obj_func": prob.evaluate,
    "minmax": "min",
    "log_to": "console"
}

## Run the algorithm
model = SMA.OriginalSMA(epoch=100, pop_size=50, pr=0.03)
g_best = model.solve(problem)
print(f"Best solution: {g_best.solution}, Best fitness: {g_best.target.fitness}")
```

# Support 

### Official Links 

* Official source code repo: https://github.com/thieu1995/cec2011-real-world
* Official chat group: https://t.me/+fRVCJGuGJg1mNDg1

* This project also related to our another projects which are "optimization" and "machine learning", check it here:
    * https://github.com/thieu1995/mealpy
    * https://github.com/thieu1995/metaheuristics
    * https://github.com/thieu1995/opfunu
    * https://github.com/thieu1995/enoppy
    * https://github.com/thieu1995/permetrics
    * https://github.com/thieu1995/MetaCluster
    * https://github.com/thieu1995/pfevaluator
    * https://github.com/thieu1995/IntelELM
    * https://github.com/thieu1995/MetaCluster
    * https://github.com/thieu1995/MetaPerceptron
    * https://github.com/thieu1995/EvoRBF
    * https://github.com/thieu1995/reflame
    * https://github.com/thieu1995/GrafoRVFL
    * https://github.com/aiir-team



### Citation Request 

Please include these citations if you plan to use this repository:

```code

@article{van2023mealpy,
  title={MEALPY: An open-source library for latest meta-heuristic algorithms in Python},
  author={Van Thieu, Nguyen and Mirjalili, Seyedali},
  journal={Journal of Systems Architecture},
  year={2023},
  publisher={Elsevier},
  doi={10.1016/j.sysarc.2023.102871}
}

@article{nguyen2021nqsv,
  title={nQSV-Net: a novel queuing search variant for global space search and workload modeling},
  author={Nguyen, Binh Minh and Hoang, Bao and Nguyen, Thieu and Nguyen, Giang},
  journal={Journal of Ambient Intelligence and Humanized Computing},
  volume={12},
  pages={27--46},
  year={2021},
  publisher={Springer}
}

@article{nguyen2020hybridization,
  title={Hybridization of galactic swarm and evolution whale optimization for global search problem},
  author={Nguyen, Binh Minh and Tran, Trung and Nguyen, Thieu and Nguyen, Giang},
  journal={IEEE Access},
  volume={8},
  pages={74991--75010},
  year={2020},
  publisher={IEEE}
}

```

