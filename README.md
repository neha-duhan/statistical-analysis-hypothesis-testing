# Statistical Analysis and Hypothesis Testing

## Project Objective

This project uses statistical analysis to determine whether there is a significant difference in salaries between male and female employees.

## Tools Used

- Python
- Pandas
- SciPy
- KaggleHub

## Hypothesis

### Null Hypothesis (H₀)
There is no difference in average salary between male and female employees.

### Alternative Hypothesis (H₁)
There is a difference in average salary between male and female employees.

## Results

- Average Male Salary: $103,867.78
- Average Female Salary: $97,011.17
- P-Value: 0.16904

## Conclusion

Based on the t-test results:

- If p-value < 0.05 → Reject H₀
- If p-value ≥ 0.05 → Fail to Reject H₀

Interpretation

The p-value helps determine whether the observed salary difference is statistically significant.

If the P-Value is Less Than 0.05

Since the p-value is less than 0.05, the null hypothesis is rejected. This means there is strong statistical evidence that the salary difference between male and female employees is real and not due to random chance.

If the P-Value is Greater Than or Equal to 0.05

Since the p-value is greater than or equal to 0.05, the null hypothesis cannot be rejected. This means there is not enough evidence to conclude that a real salary difference exists between male and female employees. Any difference observed in the averages may simply be due to natural variation in the dataset.

## Business Report

The purpose of this analysis was to determine whether the observed salary difference between male and female employees is statistically significant.

A statistical t-test was performed on employee salary data. The average salary of male employees was compared with the average salary of female employees.

The resulting p-value was 0.16904.

Based on this result, the salary difference was found to be statistically significant / not statistically significant.

This means the observed difference is either likely to represent a real difference in salaries or is likely due to normal variation in the data.

The analysis provides evidence-based insights that can help management make informed decisions regarding employee compensation policies.
