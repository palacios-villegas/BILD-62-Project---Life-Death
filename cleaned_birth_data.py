import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

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
print(total_births.shape)

c = 0
while c < 9288:
    birth_data[c, 2] = float(birth_data[c+1, 2])
    birth_data[c+85, 2] = float(birth_data[c+84, 2])
    c = c + 86
print(birth_data[:90, :])
