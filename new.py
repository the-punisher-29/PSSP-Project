# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 23:27:01 2023

@author: soumen
"""
import numpy as np
import matplotlib.pyplot as plt

# Function to generate, visualize, and plot Poisson data
def generate_visualize_and_plot(seed_value):
    np.random.seed(seed_value)

    lambda_value = 3  # Average rate of occurrence

    poisson_data = np.random.poisson(lambda_value, size=1000)

    # Step 3: Visualize the simulated data with a histogram
    plt.subplot(2, 1, 1)
    plt.hist(poisson_data, bins=20, density=True, alpha=0.7, label=f'Seed = {seed_value}')
    plt.title('Simulated Poisson Distribution - Histogram')
    plt.xlabel('Number of Events')
    plt.ylabel('Probability')
    plt.legend()

    # Step 4: Visualize the simulated data with a line graph (probability vs number of events)
    plt.subplot(2, 1, 2)
    count, bins, _ = plt.hist(poisson_data, bins=20, density=True, alpha=0.7, label=f'Seed = {seed_value}')
    plt.plot(bins[:-1], count, linestyle='-', marker='o', color='green')  # Plotting probability vs number of events
    plt.title('Simulated Poisson Distribution - Line Graph')
    plt.xlabel('Number of Events')
    plt.ylabel('Probability')
    plt.legend()

    plt.tight_layout()  # Adjust layout to prevent overlap

    plt.show()

    # Print the generated Poisson data
    print("Data for Seed =", seed_value, ":\n", poisson_data, "\n\n")


# Generate, visualize, and plot for three different seed values
generate_visualize_and_plot(42)
generate_visualize_and_plot(123)
generate_visualize_and_plot(789)

