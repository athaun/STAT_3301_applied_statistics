# import matplotlib.pyplot as plt
# from collections import Counter

# # Data (cleaned and combined as one string of space-separated values)
# data = """
# 1 3 2 1 1 0 1 1
# 3 0 2 2 1 2 0 2
# 1 2 2 1 0 1 1 1
# 1 1 0 2 0 3 4 2
# 0 2 1 1 2 1 1 0
# """

# # Clean and split data into individual elements
# data_list = data.split()

# # a. Frequency Distribution
# freq_dist = Counter(data_list)

# # b. Relative-Frequency Distribution
# total_count = len(data_list)
# rel_freq_dist = {key: value / total_count for key, value in freq_dist.items()}
# print(total_count)

# # c. Pie Chart
# letters = list(freq_dist.keys())
# frequencies = list(freq_dist.values())
# relative_frequencies = list(rel_freq_dist.values())

# plt.figure(figsize=(12, 6))

# # Pie chart for relative frequency distribution
# plt.subplot(1, 2, 1)
# plt.pie(relative_frequencies, labels=letters, autopct='%1.1f%%', startangle=140)
# plt.title("Pie Chart of Directions")

# # d. Bar Chart
# plt.subplot(1, 2, 2)
# plt.bar(letters, frequencies, color='lightcoral')
# plt.title("Bar Chart of Direction Frequencies")
# plt.xlabel("Directions")
# plt.ylabel("Frequency")

# plt.tight_layout()
# plt.show()

# # Print frequency and relative frequency distributions
# print("Frequency Distribution:", freq_dist)
# print("Relative-Frequency Distribution:", rel_freq_dist)


import matplotlib.pyplot as plt

values = [0, 1, 2, 3, 4]
frequencies = [8, 17, 11, 3, 1]
total = 40

relative_frequencies = [i / total for i in frequencies]

plt.hist(values, bins=[0, 1, 2, 3, 4, 5], weights=relative_frequencies, color='blue', edgecolor='black')

plt.title("Relative Frequency Histogram")
plt.xlabel("Values")
plt.ylabel("Relative Frequency")

plt.show()
