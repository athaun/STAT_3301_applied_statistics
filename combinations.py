import random

# Parameters
population_size = 435
sample_size = 15

# Step 1: Calculate the interval (m)
m = population_size // sample_size

# Step 2: Choose a random starting point (k) between 1 and m
k = 12

# Step 3: Generate the sample positions
sample_positions = [k + i * m for i in range(sample_size)]

# Print the results
print(f"Sampling interval (m): {m}")
print(f"Random starting point (k): {k}")
print(f"Sample positions: {sample_positions}")
