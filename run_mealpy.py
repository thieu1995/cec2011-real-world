#!/usr/bin/env python
# Created by "Thieu" at 13:11, 30/09/2022 ----------%                                                                               
#       Email: nguyenthieu2102@gmail.com            %                                                    
#       Github: https://github.com/thieu1995        %                         
# --------------------------------------------------%

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
