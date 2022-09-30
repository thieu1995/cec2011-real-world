#!/usr/bin/env python
# Created by "Thieu" at 13:11, 30/09/2022 ----------%                                                                               
#       Email: nguyenthieu2102@gmail.com            %                                                    
#       Github: https://github.com/thieu1995        %                         
# --------------------------------------------------%

from cec2011_class import Problem01
from mealpy.bio_based import SMA

prob = Problem01()

problem_dict = {
    "fit_func": prob.evaluate,
    "lb": prob.lb,
    "ub": prob.ub,
    "minmax": "min",
    "log_to": "console",
    "save_population": False,
}

## Run the algorithm
model = SMA.BaseSMA(epoch=100, pop_size=50, pr=0.03)
best_position, best_fitness = model.solve(problem_dict)
print(f"Best solution: {best_position}, Best fitness: {best_fitness}")
