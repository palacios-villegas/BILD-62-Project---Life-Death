import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

file_death_contents = open("Deaths_1x1.txt").read()
file_death_contents = file_death_contents.replace('+', '')

file_pop_contents = open('Population.txt').read()
file_pop_contents = file_pop_contents.replace('+', '')
file_pop_contents = file_pop_contents.replace('-', '')

file_birth_contents = open('DNKbirthsTR.txt').read()
file_birth_contents = file_birth_contents.replace('+', '')
file_birth_contents = file_birth_contents.replace('-', '')
file_birth_contents = file_birth_contents.replace(' . ', '0.00')
# cleans the data by removing special characters so it can be converted into float in the next code block

with open("Deaths_1x1.txt", "w", encoding="utf-8") as file:  # converts files from str to float
    file.write(file_death_contents)
with open("Population.txt", "w", encoding="utf-8") as file:
    file.write(file_pop_contents)
with open("DNKbirthsTR.txt", "w", encoding="utf-8") as file:
    file.write(file_birth_contents)

death_data = np.array(np.loadtxt(fname='Deaths_1x1.txt'))
total_deaths = death_data[:, 4]  # 1D arrays with 21201 columns
female_deaths = death_data[:, 2]
male_deaths = death_data[:, 3]

pop_data = np.array(np.loadtxt(fname='Population.txt'))
total_pop = pop_data[:, 4]
female_pop = pop_data[:, 2]
male_pop = pop_data[:, 3]

birth_data = np.array(np.loadtxt(fname='DNKbirthsTR.txt'))
total_births = birth_data[:, 3]


def make_array(float_data, num_columns):
    '''will turn 1D array into 2D array with year on axis=0 and age on axis=1'''
    new_row = np.empty([0])
    # print(new_row, new_row.shape)
    array_data = np.empty([0, num_columns])
    # print(array_data, array_data.shape)
    # print('space')
    counter = 0
    for x in float_data:
        if counter == num_columns:
            new_row = new_row[np.newaxis, :]
            # print('new_ row if', new_row.shape)
            array_data = np.append(array_data, new_row, axis=0)
            # print('array_data if', array_data, array_data.shape)
            new_row = np.empty([0])
            counter = 0
            x = np.array([x])
            # print('x if', x, x.shape)
            new_row = np.append(new_row, x, axis=0)
            # print('new_row if', new_row, new_row.shape)
            counter = counter + 1
        else:
            x = np.array([x])
            # print('x', x, x.shape)
            new_row = np.append(new_row, x, axis=0)
            # print('new_row', new_row, new_row.shape)
            counter = counter + 1
    return (array_data)


44
# save death & pop data in an array that is easily indexed
total_death_array = make_array(total_deaths, 111)
female_death_array = make_array(female_deaths, 111)
male_death_array = make_array(male_deaths, 111)

total_pop_array = make_array(total_pop, 111)
female_pop_array = make_array(female_pop, 111)
male_pop_array = make_array(male_pop, 111)
