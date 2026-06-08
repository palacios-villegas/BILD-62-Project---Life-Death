import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
from cleaned_pop_death_data import total_death_array, male_death_array, female_death_array

age = np.arange(0, 111)
year = np.arange(1835, 2026)
transposed_tot_death = total_death_array.T
transposed_m_death = male_death_array.T
transposed_f_death = female_death_array.T


tot_death_percent = transposed_tot_death / \
    transposed_tot_death.sum(axis=0) * 100
# above gives %deaths
# below gives %female death out of all female AND male deaths
mtot_death_percent = transposed_m_death / \
    transposed_tot_death.sum(axis=0) * 100
ftot_death_percent = transposed_f_death / \
    transposed_tot_death.sum(axis=0) * 100


def plot_heatmap(data, years=year, ages=age, y_axis=np.arange(5, 105, 10), title=str, color='viridis', cmap_title='Deaths (%)'):
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
    title: str
        a title for the graph

    Returns
    -------
    Plots a heatmap, does not return a value
    """

    plt.figure(figsize=(10, 5))

    plt.imshow(
        data,
        aspect='auto',
        origin='lower',
        extent=[years[0], years[-1], ages[0], ages[-1]],
        cmap=f'{color}'
    )
    plt.colorbar(label=cmap_title)
    plt.xlabel('Year of Death')
    plt.ylabel('Age at Death')
    plt.xticks(np.arange(1835, 2025, 20))
    plt.yticks(y_axis)
    plt.title(f"Age at Death vs Year in {title}")
    plt.tight_layout()
    plt.show()


def censor_data(uncensored_data):
    return uncensored_data[3:, :], uncensored_data[:3, :]


ci_tot_death_percent, ca_tot_death_percent = censor_data(
    tot_death_percent)  # ci -> censored infants, ca -> censored adults
ci_mtot_death_percent, ca_mtot_death_percent = censor_data(
    mtot_death_percent)
ci_ftot_death_percent, ca_ftot_death_percent = censor_data(ftot_death_percent)

ci_sex_difference_death_percent = ci_ftot_death_percent - ci_mtot_death_percent
# difference between female and male deaths. >0% means more female deaths, <0% means more male deaths


plot_heatmap(ci_tot_death_percent, y_axis=np.arange(  # FIGURE 6 ################################################################
    5, 105, 10), title='Adults')

plot_heatmap(ca_tot_death_percent, y_axis=np.arange(  # FIGURE 8 #############################################################
    0, 3), ages=np.arange(-1, 3, 1), title='Infants')


# FIGURE 7 ###############################################################################################################
plt.figure(figsize=(10, 5))
plt.imshow(
    ci_sex_difference_death_percent,  # better visualization through sex difference
    aspect='auto',
    origin='lower',
    extent=[year[0], year[-1], age[0], age[-1]],
    cmap='bwr', norm=colors.CenteredNorm()
)
plt.colorbar(label='Female (%)deaths - Male (%)deaths')
plt.xlabel('Year of Death')
plt.ylabel('Age at Death')
plt.xticks(np.arange(1835, 2025, 20))
plt.yticks(np.arange(5, 105, 10))
plt.title(f"Age at Death vs Year in Adult Sex %Death Difference")
plt.tight_layout()
plt.show()


def calc_average(counts, ages):
    weighted_age_sum = np.zeros(counts.shape[0])

    for idx, age in enumerate(ages):
        counts_at_age = counts[:, idx]
        weighted_age_sum = weighted_age_sum + (counts_at_age * age)

    total_per_year = counts.sum(axis=1)
    average_age = weighted_age_sum / total_per_year

    return average_age


# calculate averages for everyone, and infant-censored
average_tot_death = calc_average(total_death_array, age)
ci_average_tot_death = calc_average(
    total_death_array[:, 3:], np.arange(3, 111))


# plot line graph ############## FIGURE 9 ####################################################################################
plt.figure(figsize=(10, 5))
plt.plot(year, average_tot_death, label='Average Deaths')
plt.plot(year, ci_average_tot_death, label='Average Deaths Without Infants')
plt.xticks(np.arange(1835, 2025, 20))
plt.title("Average Age at Death vs Year")
plt.xlabel('Year of Death')
plt.ylabel('Average Age at Death')

# plot special points !!
x = [1918, 1945, 1865, 1849]
y = [60, 67, 38, 50]
txt = ['World War I', 'World War II',
       'Second Schleswig War', 'First Schleswig War']
plt.axvspan(1914, 1918, color="yellow", alpha=0.3)
plt.axvspan(1939, 1945, color="yellow", alpha=0.3)
plt.axvspan(1848, 1852, color="yellow",
            alpha=0.3)
plt.axvspan(1864, 1865, color="yellow",
            alpha=0.3)

for i, year in enumerate(x):
    plt.annotate(
        text=(f'{txt[i]}'),
        xy=(x[i], y[i]),
        xytext=(0, 10),
        textcoords="offset points",
        ha='center',
        fontsize=7)
plt.legend()
plt.tight_layout()
plt.show()
