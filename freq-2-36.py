import matplotlib.pyplot as plt

# Data: Drug types and their frequencies
drugs = ['Marijuana', 'Crack cocaine', 'Powder cocaine', 'Ecstasy', 'Methamphetamine', 'Heroin', 'Other']
frequencies = [73, 62, 45, 20, 17, 5, 4]

# a. Obtain a relative-frequency distribution
total_count = sum(frequencies)
relative_frequencies = [f / total_count for f in frequencies]

print(total_count)
print(relative_frequencies)

# b. Draw a pie chart
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.pie(relative_frequencies, labels=drugs, autopct='%1.1f%%', startangle=140)
plt.title("Pie Chart of Drug Types Sold")

# c. Construct a bar chart
plt.subplot(1, 2, 2)
plt.bar(drugs, frequencies, color='lightgreen')
plt.title("Bar Chart of Drug Types Sold")
plt.xlabel("Drug Types")
plt.ylabel("Frequency")

plt.tight_layout()
plt.show()

# Print frequency and relative frequency distributions
print("Frequency Distribution:")
for drug, freq in zip(drugs, frequencies):
    print(f"{drug}: {freq}")

print("\nRelative-Frequency Distribution:")
for drug, rel_freq in zip(drugs, relative_frequencies):
    print(f"{drug}: {rel_freq:.2%}")
