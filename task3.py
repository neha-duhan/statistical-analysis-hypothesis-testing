import pandas as pd
from scipy.stats import ttest_ind
import kagglehub
import os
 
# Download Dataset
path = kagglehub.dataset_download(
    "rkiattisak/salaly-prediction-for-beginer"
)
print("Dataset Path:", path)
print("Files:", os.listdir(path))
 
# Load Dataset
csv_file = os.path.join(path, "Salary Data.csv")
df = pd.read_csv(csv_file)
print("\nFirst 5 Rows:")
print(df.head())
print("\nDataset Information:")
print(df.info())
 
# Data Cleaning
print("\nMissing Values:")
print(df.isnull().sum())

# Remove rows with missing Gender or Salary
df = df.dropna(subset=["Gender", "Salary"])
 
# Hypothesis
print("\n========== HYPOTHESIS ==========")
print("Null Hypothesis (H0):")
print("There is no difference in average salary between male and female employees.")
print("\nAlternative Hypothesis (H1):")
print("There is a difference in average salary between male and female employees.")
 
# Basic Statistics
male_salary = df[df["Gender"] == "Male"]["Salary"]
female_salary = df[df["Gender"] == "Female"]["Salary"]
male_mean = male_salary.mean()
female_mean = female_salary.mean()
print("\n========== BASIC STATISTICS ==========")
print(f"Average Male Salary: ${male_mean:,.2f}")
print(f"Average Female Salary: ${female_mean:,.2f}")

# T-Test
t_statistic, p_value = ttest_ind(
    male_salary,
    female_salary,
    equal_var=False
)
print("\n========== T-TEST RESULTS ==========")
print("T-Statistic:", round(t_statistic, 4))
print("P-Value:", round(p_value, 6))
 
# Conclusion
print("\n========== CONCLUSION ==========")

if p_value < 0.05:
    print("Reject the Null Hypothesis (H0).")
    print("There is a statistically significant difference in salaries between male and female employees.")
else:
    print("Fail to Reject the Null Hypothesis (H0).")
    print("There is no statistically significant difference in salaries between male and female employees.")
 
# Business Report
print("\n========== BUSINESS REPORT ==========")

if p_value < 0.05:
    print(
        f"The average salary for male employees is ${male_mean:,.2f}, "
        f"while the average salary for female employees is ${female_mean:,.2f}. "
        f"The statistical test produced a p-value of {p_value:.6f}, which is less than 0.05. "
        f"This indicates that the salary difference is statistically significant and is unlikely to be due to random chance."
    )
else:
    print(
        f"The average salary for male employees is ${male_mean:,.2f}, "
        f"while the average salary for female employees is ${female_mean:,.2f}. "
        f"The statistical test produced a p-value of {p_value:.6f}, which is greater than 0.05. "
        f"This indicates that any salary difference observed is likely due to random variation and is not statistically significant."
    )