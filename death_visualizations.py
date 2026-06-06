import numpy as np
import matplotlib.pyplot as plt
from cleaned_pop_death_data import total_death_array, male_death_array, female_death_array

age = np.arange(0, 110)
year = np.arange(1835, 2025)
transposed_tot_death = total_death_array.T
transposed_m_death = male_death_array.T
transposed_f_death = female_death_array.T

tot_death_percent = transposed_tot_death / \
    transposed_tot_death.sum(axis=0) * 100
m_death_percent = transposed_m_death / \
    transposed_m_death.sum(axis=0) * 100
f_death_percent = transposed_f_death / \
    transposed_f_death.sum(axis=0) * 100
# above gives %female death out of all female deaths
# below gives %female death out of all female AND male deaths
mtot_death_percent = transposed_m_death / \
    transposed_tot_death.sum(axis=0) * 100
ftot_death_percent = transposed_f_death / \
    transposed_tot_death.sum(axis=0) * 100


def plot_heatmap(data, years=year, ages=age, y_axis=np.arange(5, 105, 10), title=str):
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
        extent=[years[0], years[-1], ages[0], ages[-1]]
    )

    plt.colorbar(label='Deaths (%)')
    plt.xlabel('Year of Death')
    plt.ylabel('Age at Death')
    plt.xticks(np.arange(1835, 2025, 20))
    plt.yticks(y_axis)
    plt.title(f"Age at Death vs Year in {title}")
    plt.tight_layout()
    plt.show()


def censor_data(uncensored_data):
    return uncensored_data[2:, :], uncensored_data[:3, :]


ci_tot_death_percent, ca_tot_death_percent = censor_data(
    tot_death_percent)  # ci -> censored infants
ci_m_death_percent, ca_m_death_percent = censor_data(
    m_death_percent)  # ca -> censored adults
ci_f_death_percent, ca_f_death_percent = censor_data(f_death_percent)

ci_mtot_death_percent, ca_mtot_death_percent = censor_data(
    mtot_death_percent)
ci_ftot_death_percent, ca_ftot_death_percent = censor_data(ftot_death_percent)

ci_sex_difference_death_percent = ci_mtot_death_percent - ci_ftot_death_percent
ca_sex_difference_death_percent = ca_mtot_death_percent - ca_ftot_death_percent
# difference between male and female deaths. >0% means more male deaths, <0% means more female deaths

plot_heatmap(tot_death_percent, title='Total Population')
plot_heatmap(ca_tot_death_percent, y_axis=np.arange(
    0, 3), ages=np.arange(-1, 3, 1), title='Infants')
plot_heatmap(ci_tot_death_percent, title='Adults')
# plot_heatmap(ci_m_death_percent, title='Adult Males')
# plot_heatmap(ci_f_death_percent, title='Adult Females')
# plot_heatmap(ca_m_death_percent, y_axis=np.arange(
#    0, 3), ages=np.arange(-1, 3, 1), title='Infant Males')
# plot_heatmap(ca_f_death_percent, y_axis=np.arange(
#    0, 3), ages=np.arange(-1, 3, 1), title='Infant Females')


# better visualization through sex difference than sex alone
plot_heatmap(ci_sex_difference_death_percent, title='Adult Sex Difference')
plot_heatmap(ca_sex_difference_death_percent, y_axis=np.arange(
    0, 3), ages=np.arange(-1, 3, 1), title='Infant Sex Difference')
