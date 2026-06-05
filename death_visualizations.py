import numpy as np
import matplotlib.pyplot as plt
from cleaned_pop_death_data import total_death_array, male_death_array, female_death_array

ages = np.arange(0, 110)
years = np.arange(1835, 2025)
transposed_tot_death_data = total_death_array.T
transposed_male_death_data = male_death_array.T

tot_death_percent_data = transposed_tot_death_data / \
    transposed_tot_death_data.sum(axis=0) * 100
male_death_percent_data = transposed_male_death_data / \
    transposed_male_death_data.sum(axis=0) * 100


def plot_heatmap(data, years, ages):
    """
    Plots a heatmap showing the distribution of births by mother's age and child birth year.

    Parameters
    ----------
    birth_percent_data : array
        2D array containing the percentage of deats for each age and year.
    years : array
        Array containing the death years shown on the x-axis.
    ages : array
        Array containing the ages shown on the y-axis.

    Returns
    -------
    Plots a heatmap, does not return a value
    """

    plt.figure(figsize=(10, 5))

    plt.imshow(
        data,
        aspect='auto',
        origin='lower',
        extent=[years[0], years[-1], ages[0], ages[-1]]
    )

    plt.colorbar(label='Deaths (%)')
    plt.xlabel('Year of Death')
    plt.ylabel('Age at Death')
    plt.xticks(np.arange(1835, 2025, 20))
    plt.yticks(np.arange(5, 105, 10))
    plt.title("Distribution of Deaths by Year and Age")
    plt.tight_layout()
    plt.show()


censored_tot_death_percent_data = tot_death_percent_data[2:, :]
censored_male_death_percent_data = male_death_percent_data[2:, :]
plot_heatmap(tot_death_percent_data, years, ages)
plot_heatmap(censored_tot_death_percent_data, years, ages)
plot_heatmap(censored_male_death_percent_data, years, ages)

# played around, created some more graphs !!!
# the names of the graphs doesnt change though, needs to be refined
