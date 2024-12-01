import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import ttest_rel, probplot

print("Loading the dataset...")
file_path = 'blood_serum.csv'
data = pd.read_csv(file_path)
print(f"Dataset loaded successfully with {data.shape[0]} rows and {data.shape[1]} columns.\n")

print("Dataset preview:")
print(data.head(), "\n")

# Set Seaborn Style with Enhanced Palette
sns.set(style="whitegrid", palette="muted")
color_palette = sns.color_palette("Set2")

# Step 1: Descriptive Statistics
print("Step 1: Calculating descriptive statistics...\n")
groups = data.groupby(['cell', 'serum'])
descriptive_stats = groups['growth'].agg(['mean', 'std', 'count']).reset_index()
print("Descriptive statistics for each group:")
print(descriptive_stats, "\n")

# Set Seaborn style for better aesthetics
sns.set(style="whitegrid")

# Plot for LNCaP cells
fig, ax = plt.subplots(figsize=(10, 6))  # Create a figure for LNCaP
sns.kdeplot(data=data[(data['cell'] == 'LNCaP') & (data['serum'] == 'before')], 
            x='growth', hue='serum', fill=True, common_norm=False, 
            palette='Blues', ax=ax, alpha=0.6, linewidth=2, legend=False)
sns.kdeplot(data=data[(data['cell'] == 'LNCaP') & (data['serum'] == 'after')], 
            x='growth', hue='serum', fill=True, common_norm=False, 
            palette='Greens', ax=ax, alpha=0.6, linewidth=2, legend=False)

# Title and labels for LNCaP plot
ax.set_title("LNCaP Growth Rate Distribution", fontsize=14)
ax.set_xlabel("Growth Rate", fontsize=12)
ax.set_ylabel("Density", fontsize=12)

# Add legends manually for clarity (serum condition)
ax.legend(title="Serum Condition", labels=["Before Exposure", "After Exposure"], loc='upper right')

# Save the LNCaP plot
plt.tight_layout();
plt.savefig('LNCaP_growth_distribution.png')  # Save as PNG file
plt.close(fig)  # Close the plot to avoid overlap with the next one

# Plot for NIH3T3 cells
fig, ax = plt.subplots(figsize=(10, 6))  # Create a figure for NIH3T3
sns.kdeplot(data=data[(data['cell'] == 'NIH3T3') & (data['serum'] == 'before')], 
            x='growth', hue='serum', fill=True, common_norm=False, 
            palette='Blues', ax=ax, alpha=0.6, linewidth=2, legend=False)
sns.kdeplot(data=data[(data['cell'] == 'NIH3T3') & (data['serum'] == 'after')], 
            x='growth', hue='serum', fill=True, common_norm=False, 
            palette='Greens', ax=ax, alpha=0.6, linewidth=2, legend=False)

# Title and labels for NIH3T3 plot
ax.set_title("NIH3T3 Growth Rate Distribution", fontsize=14)
ax.set_xlabel("Growth Rate", fontsize=12)
ax.set_ylabel("Density", fontsize=12)

# Add legends manually for clarity (serum condition)
ax.legend(title="Serum Condition", labels=["Before Exposure", "After Exposure"], loc='upper right')

# Save the NIH3T3 plot
plt.tight_layout();
plt.savefig('NIH3T3_growth_distribution.png')  # Save as PNG file
plt.close(fig)  # Close the plot


# Step 3: Statistical Testing
print("Step 3: Statistical Testing\n")

# Normality Check for LNCaP before and after exposure
for serum_condition in ['before', 'after']:
    group = data[(data['cell'] == 'LNCaP') & (data['serum'] == serum_condition)]['growth']
    fig, ax = plt.subplots(figsize=(6, 6))
    probplot(group, dist="norm", plot=ax)
    ax.set_title(f"LNCaP Growth Rate Q-Q Plot ({serum_condition.capitalize()} Exposure)")
    plt.tight_layout()
    plt.savefig(f'LNCaP_{serum_condition}_qq_plot.png')
    plt.close(fig)

# Normality Check for NIH3T3 before and after exposure
for serum_condition in ['before', 'after']:
    group = data[(data['cell'] == 'NIH3T3') & (data['serum'] == serum_condition)]['growth']
    fig, ax = plt.subplots(figsize=(6, 6))
    probplot(group, dist="norm", plot=ax)
    ax.set_title(f"NIH3T3 Growth Rate Q-Q Plot ({serum_condition.capitalize()} Exposure)")
    plt.tight_layout()
    plt.savefig(f'NIH3T3_{serum_condition}_qq_plot.png')
    plt.close(fig)

# Save summary statistics to a file
descriptive_stats.to_csv('descriptive_statistics.csv', index=False)
print("Summary statistics saved to 'descriptive_statistics.csv'")
