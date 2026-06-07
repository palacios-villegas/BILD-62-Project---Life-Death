import numpy as np
import matplotlib.pyplot as plt
from cleaned_birth_data import age_birth_array

years = np.arange(1916, 2025)  # Years of birth present in the dataset
ages = np.arange(12, 56)  # Age of mothers present in the dataset

# Filtered ages from 15 to 49
# Heatmap was completely dark outside of that range
# This filter better focuses on the clear trend
age_mask = (ages >= 15) & (ages <= 49)
filtered_ages = ages[age_mask]
filtered_birth_counts = age_birth_array[:, age_mask]


def calculate_average_mother_age(filtered_birth_counts, filtered_ages):
    """
    Creates an array with average mother ages for each child birth year.

    Parameters
    ----------
    filtered_birth_counts : array
        Array containing the birth counts for each year filtered by ages 15-49.
    filtered_ages : array
        Array containing the filtered ages 15-49.

    Returns
    -------
    average_mother_age : array
        Array containing the average age of mother ordered for each child birth year
    """
    weighted_age_sum = np.zeros(filtered_birth_counts.shape[0])

    for idx, age in enumerate(filtered_ages):
        births_at_age = filtered_birth_counts[:, idx]
        weighted_age_sum = weighted_age_sum + (births_at_age * age)

    total_births_per_year = filtered_birth_counts.sum(axis=1)
    average_mother_age = weighted_age_sum / total_births_per_year

    return average_mother_age


def plot_average_mother_age(years, average_mother_age):
    """
    Plots a line graph showing the average age of mother by child birth year.

    Parameters
    ----------
    years : array
        Array containing the birth years of children shown on the x-axis.
    average_mother_age : array
        Array containing the average mother's age shown on the y-axis.

    Returns
    -------
    Plots a line graph, does not return a value
    """

    plt.figure(figsize=(10, 5))

    plt.plot(years, average_mother_age)

    plt.xlabel('Birth Year of Child')
    plt.ylabel('Average Age of Mother')
    plt.xticks(np.arange(1920, 2025, 20))
    plt.title("Average Mother's Age by Child Birth Year")
    plt.tight_layout()
    plt.show()

average_mother_age = calculate_average_mother_age(filtered_birth_counts, filtered_ages)
plot_average_mother_age(years, average_mother_age)