import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

file_death_contents = open("Deaths_1x1.txt").read()
file_death_contents = file_death_contents.replace('+', '')
file_pop_contents = open('Population.txt').read()
file_pop_contents = file_pop_contents.replace('+', '')
file_birth_contents = open('DNKbirthsTR.txt').read()
file_birth_contents = file_birth_contents.replace('+', '')
file_birth_contents = file_birth_contents.replace('-', '')
# cleans the data so it can be converted into float in the next code block

with open("Deaths_1x1.txt", "w", encoding="utf-8") as file:
    file.write(file_death_contents)
with open("Population.txt", "w", encoding="utf-8") as file:
    file.write(file_pop_contents)
with open("Deaths_1x1.txt", "w", encoding="utf-8") as file:
    file.write(file_death_contents)

raw_death_file = np.loadtxt(fname='Deaths_1x1.txt')
death_data = np.array(raw_death_file)
# print(death_data)
# print(death_data.shape)  # (21201,5)
# need to make array with year axis, age axis
# year_age_death = death_data[:, 0:2]
# total_death = np.append(year_age_death, death_data[:, 4], axis=1)
# male_death = death_data[:, 0:2] + death_data[:, 3]
# female_death = death_data[:, 0:3]
# print(total_death)
total_deaths = death_data[:, 4]
new_row = np.zeros((0, 0))
deaths_final = np.zeros((0, 0))
counter = 0


def array_convert(data):
    for x in data:
        new_row = new_row + x
        counter = counter + 1
        if counter == 111:
            deaths_final = np.append(deaths_final, new_row, axis=0)
            counter = 0
            new_row = np.zeros((0, 0))
    print(deaths_final)
