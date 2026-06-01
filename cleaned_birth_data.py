import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

file_birth_contents = open('DNKbirthsTR_01.txt').read()
file_birth_contents = file_birth_contents.replace('+', '')
file_birth_contents = file_birth_contents.replace('-', '')
file_birth_contents = file_birth_contents.replace('  . ', '0000 ')
print(file_birth_contents)

with open("DNKbirthsTR.txt_01", "w", encoding="utf-8") as file:
    file.write(file_birth_contents)

birth_data = np.array(np.loadtxt(fname='DNKbirthsTR_01.txt'))
total_births = birth_data[:, 3]
print(birth_data)
