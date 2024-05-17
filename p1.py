# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 00:50:35 2023

@author: soumen
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

np.random.seed(42)

average_accidents_per_day = 2
days_simulated = 365
time_period = 1

accidents_per_day = np.random.poisson(average_accidents_per_day, days_simulated)

print("Simulated Accidents per Day:", accidents_per_day)

x = np.arange(0, max(accidents_per_day) + 1)
poisson_pmf = poisson.pmf(x, average_accidents_per_day)

print("Poisson PMF:", poisson_pmf)

plt.plot(x, poisson_pmf, 'ro-', label='Poisson PMF (Line Graph)')

plt.title('Simulated Traffic Accidents using Poisson Distribution')
plt.xlabel('Number of Accidents per Day')
plt.ylabel('Probability')
plt.legend()
plt.show()


