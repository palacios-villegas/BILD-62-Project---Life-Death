
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
test = birth_data[:90, :]
# print(test)
# print(total_births.shape)

c = 0
while c < 9288:
    birth_data[c, 2] = float(birth_data[c+1, 2])
    birth_data[c+85, 2] = float(birth_data[c+84, 2])
    c = c + 86
# print(birth_data[:90, :])


birth_column = birth_data[:, 3]
test = birth_column[:40]

# def age_sort(data):
added_birth = np.empty([0])
border = np.empty([0])
# print(added_birth, added_birth.shape)
array_data = np.empty([0, 4])
# print(array_data, array_data.shape)
# print('space')

for index, births in enumerate(birth_column):
    if birth_data[index, 1] == 12 or birth_data[index, 1] == 55:
        births = np.array(births)
        # print('border', births)
        births = births[np.newaxis]
        # print('border', births)
        border = np.append(border, births, axis=0)
        # print('border', border)
        added_birth = np.append(added_birth, border, axis=0)
        border = np.empty([0])

    elif birth_data[index, 1] == birth_data[index+1, 1]:
        sum_births = np.array(birth_data[index, 3] + birth_data[index+1, 3])
        sum_births = sum_births[np.newaxis]
        # print(sum_births)
        added_birth = np.append(added_birth, sum_births, axis=0)

# gives array with birth year of child on axis 0, age of mother on axis 1
# if you need array with birth year of child on axis 0 and birth year of mother on axis 1,
# i can create a new array, the data will be slightly differet


age_birth_array = make_array(added_birth, 44)
print(age_birth_array)
print(age_birth_array.shape)