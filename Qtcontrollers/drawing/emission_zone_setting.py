import matplotlib.pyplot as plt

file_emz = "/Users/hannahlee/PycharmProjects/penProject/resources/text_emz.txt"


equation = open(file_emz, "r").readline()

plt.axvline(equation)

plt.show()