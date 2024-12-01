import matplotlib.pyplot as plt
from collections import Counter

# Data: provided numbers
data = [13, 13, 10, 10, 11, 10, 11, 10, 15, 13, 13, 12, 10, 13, 10]

# a. Calculate frequency and relative frequency distributions
freq_dist = Counter(data)
total_count = len(data)
rel_freq_dist = {key: value / total_count for key, value in freq_dist.items()}

# Print Frequency Distribution and Relative Frequencies
print("Frequency Distribution:")
for value, freq in sorted(freq_dist.items()):
    print(f"Value {value}: Frequency = {freq}, Relative Frequency = {rel_freq_dist[value]:.3f}")

# b. Construct the dot plot
plt.figure(figsize=(8, 4))

# Sort the data for better visualization
data_sorted = sorted(data)

# Dot plot: we scatter the sorted data along the x-axis (values), with increasing y-values for repeated points
for value in set(data_sorted):
    occurrences = data_sorted.count(value)
    plt.plot([value] * occurrences, range(1, occurrences + 1), 'ro', markersize=10)  # 'ro' makes red circles

plt.title("Dot Plot of Data")
plt.xlabel("Values")
plt.ylabel("Frequency (as dots)")
plt.xticks(range(min(data), max(data) + 1))
plt.grid(True, axis='x', linestyle='--', alpha=0.6)

plt.show()
