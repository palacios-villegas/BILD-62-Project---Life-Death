import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

# Print the folder Python is currently looking at
print("Current Working Directory:", os.getcwd())

# List all files Python sees in that specific folder
print("Files visible here:", os.listdir("."))

# cleans the data by removing special characters that
# cannot be converted into float, rewrites the original file
file_death_contents = open("Deaths_1x1.txt").read()
file_death_contents = file_death_contents.replace('+', '')

file_pop_contents = open('Population.txt').read()
file_pop_contents = file_pop_contents.replace('+', '')
file_pop_contents = file_pop_contents.replace('-', '')

with open("Deaths_1x1.txt", "w", encoding="utf-8") as file:
    file.write(file_death_contents)
with open("Population.txt", "w", encoding="utf-8") as file:
    file.write(file_pop_contents)


# creates an array out of the edited file
# stores as array with 4 columns and lots of rows
# indexed to isolate only the data we care about!
# the array is 1D, and the data cycles from year to year
# with no clear break
death_data = np.array(np.loadtxt(fname='Deaths_1x1.txt'))
# 4 refers to 4th column that holds the total death data
total_deaths = death_data[:, 4]
female_deaths = death_data[:, 2]
male_deaths = death_data[:, 3]

pop_data = np.array(np.loadtxt(fname='Population.txt'))
total_pop = pop_data[:, 4]
female_pop = pop_data[:, 2]
male_pop = pop_data[:, 3]
# document!!


def make_array(array_1D, num_columns):
    """
    Turns 1D array into 2D array with year on axis = 0 and age on axis = 1

    Parameters
    ----------
    array_1D: array
        1D array containing all the data
    num_columns : integer
        Number of age groups that are placed on the x-axis of the new array

    Returns
    -------
    2D array
    """
    new_row = np.empty([0])
    array_data = np.empty([0, num_columns])
    counter = 0
    for x in array_1D:
        if counter == num_columns:
            new_row = new_row[np.newaxis, :]  # adds dimension to new_row
            array_data = np.append(array_data, new_row, axis=0)
            new_row = np.empty([0])
            counter = 0
            x = np.array([x])
            new_row = np.append(new_row, x, axis=0)
            counter = counter + 1
        else:
            x = np.array([x])
            new_row = np.append(new_row, x, axis=0)
            counter = counter + 1
    return (array_data)


# save death & pop data in an array that is easily indexed
# year on axis 0, age on axis 1
# data spans 1835-2025
total_death_array = make_array(total_deaths, 111)
female_death_array = make_array(female_deaths, 111)
male_death_array = make_array(male_deaths, 111)

total_pop_array = make_array(total_pop, 111)
female_pop_array = make_array(female_pop, 111)
male_pop_array = make_array(male_pop, 111)
