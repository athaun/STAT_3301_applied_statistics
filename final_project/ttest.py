import pandas as pd
import numpy as np
from scipy.stats import ttest_rel, t

# Load the dataset
file_path = 'blood_serum.csv'
data = pd.read_csv(file_path)

# Function to calculate paired t-test with confidence interval
def paired_ttest_with_ci(before, after, alpha=0.05):
    # Ensure both 'before' and 'after' are numeric
    before = pd.to_numeric(before, errors='coerce').dropna()
    after = pd.to_numeric(after, errors='coerce').dropna()

    # Check that both arrays have the same length
    if len(before) != len(after):
        raise ValueError("The 'before' and 'after' data must have the same length.")
    
    # Calculate differences using a loop
    differences = []
    for i in range(len(before)):
        diff = before.iloc[i] - after.iloc[i]
        differences.append(diff)
    
    # Basic statistics
    mean_diff = np.mean(differences)
    std_diff = np.std(differences, ddof=1)
    n = len(differences)
    
    # Perform paired t-test
    t_stat, p_value = ttest_rel(before, after)
    
    # Calculate standard error
    std_error = std_diff / np.sqrt(n)
    
    # Calculate t-critical value
    t_crit = t.ppf(1 - alpha/2, df=n-1)
    
    # Calculate confidence interval
    ci_lower = mean_diff - t_crit * std_error
    ci_upper = mean_diff + t_crit * std_error
    
    return {
        't_statistic': t_stat,
        'p_value': p_value,
        'mean_difference': mean_diff,
        'confidence_interval': (ci_lower, ci_upper),
        'standard_error': std_error
    }

# Extract growth rates for LNCaP cells before and after treatment
lncap_before = data[(data['cell'] == 'LNCaP') & (data['serum'] == 'before')]['growth']
lncap_after = data[(data['cell'] == 'LNCaP') & (data['serum'] == 'after')]['growth']

# Extract growth rates for NIH3T3 cells before and after treatment
nih3t3_before = data[(data['cell'] == 'NIH3T3') & (data['serum'] == 'before')]['growth']
nih3t3_after = data[(data['cell'] == 'NIH3T3') & (data['serum'] == 'after')]['growth']

lncap_results = paired_ttest_with_ci(lncap_before, lncap_after)
nih3t3_results = paired_ttest_with_ci(nih3t3_before, nih3t3_after)

def report_results(cell_name, results):
    print(f"\n{cell_name} Analysis:")
    print(f"T-Statistic: {results['t_statistic']:.4f}")
    print(f"P-Value: {results['p_value']:.4f}")
    print(f"Mean Difference: {results['mean_difference']:.4f}")
    print(f"95% Confidence Interval: ({results['confidence_interval'][0]:.4f}, {results['confidence_interval'][1]:.4f})")
    print(f"Standard Error: {results['standard_error']:.4f}")
    
    if results['p_value'] < 0.05:
        print("Conclusion: Statistically significant difference detected")
    else:
        print("Conclusion: No statistically significant difference")

report_results("LNCaP", lncap_results)
report_results("NIH3T3", nih3t3_results)

