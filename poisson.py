# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 02:29:22 2023

@author: soumen
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

# Setting the seed for reproducibility
np.random.seed(42)

lambda_value = 3  # Average rate of occurrence

# Generate x values (number of events)
x = np.arange(0, 20)

# Calculate the Poisson PMF
poisson_pmf = poisson.pmf(x, lambda_value)

# Print x and Poisson PMF
print("x values:", x)
print("Poisson PMF:", poisson_pmf)

# Step 3: Visualize the simulated data as a line graph
plt.plot(x, poisson_pmf, 'ro-', label='Poisson PMF (Line Graph)')

plt.title('Simulated Poisson Distribution')
plt.xlabel('Number of Events')
plt.ylabel('Probability')
plt.legend()
plt.show()
