import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

file_contents = open("Deaths_1x1.txt").read()
file_contents = file_contents.replace('+', '')

with open("Deaths_1x1.txt", "w", encoding="utf-8") as file:
    file.write(file_contents)

raw_death_data = np.loadtxt(fname='Deaths_1x1.txt')
death_data = np.array(raw_death_data)
print(death_data)
print(death_data.shape)
