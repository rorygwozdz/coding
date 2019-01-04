"""Chapter two of mp4f. Capm and linear stuff."""

import pulp
import numpy as np
from scipy import stats as s
import statsmodels.api as sm

stock_r = [.065, .0265, -.0593, -.001, .0346]
mkt_r = [.055, -0.09, -0.041, 0.045, 0.022]

beta, alpha, r_value, p_value, std_err = s.linregress(stock_r, mkt_r)

print(s.linregress(stock_r, mkt_r))

# Least squares with stats model

# Sample data
n_periods = 9
all_values = np.array([np.random.random(8) for i in range(n_periods)])

# filter the data
y_vals = all_values[:, 0]  # first column y
x_vals = all_values[:, 1:]  # others are x
x_vals = sm.add_constant(x_vals)  # adds constant to help ols get done right

results = sm.OLS(y_vals, x_vals).fit()  # regress and fit

print(results.summary())

# big boy pulp coming in

# LpVariable is a "to be solved" variable
x = pulp.LpVariable("x", lowBound=0)  # creating the optimization
y = pulp.LpVariable('y', lowBound=0)  # optimizing bounds, no short selling

# LpProblem is the problem "to be solved" - akin to intializing a ggplot
problem = pulp.LpProblem("a simple maximization objective", pulp.LpMaximize)
problem += 3*x + 2*y, "objective function"
problem += 2*x + y <= 100, "constraint one"
problem += x + y <= 80, "constraint two"
problem += x <= 40, "constraint three"
problem.solve()

print("Some math results:")
for var in problem.variables():
    print(var.name, "=", var.varValue)
