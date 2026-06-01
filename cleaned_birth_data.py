import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

file_birth_contents = open('DNKbirthsTR.txt').read()
file_birth_contents = file_birth_contents.replace('+', '')
file_birth_contents = file_birth_contents.replace('-', '')
file_birth_contents = file_birth_contents.replace(' 0.00 ', '.')

with open("DNKbirthsTR.txt", "w", encoding="utf-8") as file:
    file.write(file_birth_contents)

birth_data = np.array(np.loadtxt(fname='DNKbirthsTR.txt'))
total_births = birth_data[:, 3]
print(birth_data)
