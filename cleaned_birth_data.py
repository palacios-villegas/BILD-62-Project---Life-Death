
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from cleaned_pop_death_data import make_array

file_birth_contents = open("DNKbirthsTR_01.txt").read()
file_birth_contents = file_birth_contents.replace("+", " ")
file_birth_contents = file_birth_contents.replace('-', ' ')
file_birth_contents = file_birth_contents.replace('   .', '0000')
# cleans the data by removing special characters

# erases old file and replaces it with the "new" cleaned file
with open("DNKbirthsTR_01.txt", "w") as file:
    file.write(file_birth_contents)

birth_data = np.array(np.loadtxt(fname='DNKbirthsTR_01.txt'))
total_births = birth_data[:, 3]
total_births = total_births[:, np.newaxis]


birth_column = birth_data[:, 3]
added_birth = np.empty([0])
border = np.empty([0])
array_data = np.empty([0, 4])

for index, births in enumerate(birth_column):
    if birth_data[index, 1] == 12 or birth_data[index, 1] == 55:  # takes care of the border cases,
        births = np.array(births)  # ie when mothers are 12 or 55
        births = births[np.newaxis]
        border = np.append(border, births, axis=0)
        added_birth = np.append(added_birth, border, axis=0)
        border = np.empty([0])

    # sums together the births of women giving birth at the same age just born different years
    elif birth_data[index, 1] == birth_data[index+1, 1]:
        # 3, because 4th column has
        sum_births = np.array(birth_data[index, 3] + birth_data[index+1, 3])
        sum_births = sum_births[np.newaxis]  # num of births
        added_birth = np.append(added_birth, sum_births, axis=0)

# gives array with birth year of child on axis 0, age of mother on axis 1


# 44, because 44 ages in the data set
age_birth_array = make_array(added_birth, 44)
