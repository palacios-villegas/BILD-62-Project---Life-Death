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
test = total_deaths[:5]
# deaths_final = np.zeros((191, 110))
# print(deaths_final)


# new_row = np.zeros((0, 0))
# counter = 0
# deaths_final = np.zeros((0))
# print(new_row.shape)
# x = total_deaths[0]
# print(np.array([x]))

# for x in total_deaths:
#    x = np.array([x])
#   new_row = np.append(new_row, x, axis=0)
#    counter = counter + 1
#    if counter == 111:
#        deaths_final = np.append(deaths_final, new_row, axis=0)
#        counter = 0
#        new_row = ''

new_row = np.empty([0])
print(new_row, new_row.shape)
deaths_final = np.empty([0])
print(deaths_final, deaths_final.shape)
print('space')
counter = 0
for x in test:
    if counter == 111:
        new_row = new_row[:, np.newaxis]
        deaths_final = np.array(deaths_final, new_row, axis=0)
        new_row = np.empty([0])
        counter = 0
        x = np.array([x])
        print(x, x.shape)
        # print(x)
        new_row = np.append(new_row, x, axis=0)
        print(new_row, new_row.shape)
        counter = counter + 1
    else:
        x = np.array([x])
        print('x', x, x.shape)
        new_row = np.append(new_row, x, axis=0)
        print('new_row', new_row, new_row.shape)
        counter = counter + 1


# print(deaths_final)
# print('space')
# print(new_row.shape)
# print(deaths_final.shape)
