import numpy as np
import matplotlib.pyplot as plt
from cleaned_birth_data import age_birth_array

years = np.arange(1916, 2025)  # Years of birth present in the dataset
ages = np.arange(12, 56)  # Age of mothers present in the dataset

age_mask = (ages >= 15) & (ages <= 49)
ages = ages[age_mask]
# Filtered ages from 15 to 49
# Heatmap was completely dark outside of that range
# This filter better focuses on the clear trend

# Transposes data to put birth years on x axis and ages in y axis in the graph
transposed_birth_data = age_birth_array.T
transposed_birth_data = transposed_birth_data[age_mask, :]

# Convert birth counts to percentages within each year.
birth_percent_data = transposed_birth_data / \
    transposed_birth_data.sum(axis=0) * 100


def plot_heatmap(birth_percent_data, years, ages):
    """
    Plots a heatmap showing the distribution of births by mother's age and child birth year.

    Parameters
    ----------
    birth_percent_data : array
        2D array containing the percentage of births for each mother age and year.
    years : array
        Array containing the birth years of children shown on the x-axis.
    ages : array
        Array containing the mother ages shown on the y-axis.

    Returns
    -------
    Plots a heatmap, does not return a value
    """

    plt.figure(figsize=(10, 5))

    plt.imshow(
        birth_percent_data,
        aspect='auto',
        origin='lower',
        extent=[years[0], years[-1], ages[0], ages[-1]]
    )

    plt.colorbar(label='Births (%)')
    plt.xlabel('Birth Year of Child')
    plt.ylabel('Age of Mother')
    plt.xticks(np.arange(1920, 2025, 20))
    plt.yticks(np.arange(15, 50, 5))
    plt.title("Distribution of Births by Mother's Age and Child Birth Year")
    plt.tight_layout()
    plt.show()


plot_heatmap(birth_percent_data, years, ages)