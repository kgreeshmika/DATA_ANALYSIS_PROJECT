import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv("data/employee_dataset.csv")

print("first 5 rows:",data.head())
print("\nDataset shape:", data.shape)
print("\nColumn names:",data.columns)
print("\nDataset Information:")
data.info()
print("\nStatistical summary:",data.describe())

average_salary=data["Monthly_Salary"].mean()
print(f"\nAverage Monthly Salary: ₹{average_salary:,.2f}")
department_salary=data.groupby("Department")["Monthly_Salary"].mean()
print("\nAverage Salary by Department:",department_salary)


department_salary.plot(kind="bar")
plt.title("Average Monthly Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Monthly Salary (₹)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("output/bar_chart.png")
plt.show()


plt.figure()
plt.scatter(data["Experience_Years"],data["Monthly_Salary"])
plt.title("Experience vs Monthly Salary")
plt.xlabel("Experience (years)")
plt.ylabel("Monthly Salary (₹)")
plt.tight_layout()
plt.savefig("output/scatter_plot.png")
plt.show()


correlation=data["Experience_Years"].corr(data["Monthly_Salary"])
print(f"\nCorrelation between Experience and Monthly Salary: {correlation:.2f}")



correlation_matrix=data[["Age","Experience_Years","Monthly_Salary","Performance_Score"]].corr()
print("\nCorrelation Matrix:",correlation_matrix)
plt.figure(figsize=(8,6))
sns.heatmap(correlation_matrix,annot=True,cmap="coolwarm",fmt=".2f")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("output/heatmap.png")
plt.show()

highest_paid_department=department_salary.idxmax()
highest_department_salary=department_salary.max()
salary_performance_correlation=data["Monthly_Salary"].corr(data["Performance_Score"])
print("\n===== Key Insights =====")
print(f"1. The department with the highest average salary is '{highest_paid_department}' with an average salary of ₹{highest_department_salary:,.2f}.")
print(f"2. The correlation between monthly salary and performance score is {salary_performance_correlation:.2f}.")
print(f"3. Experience and monthly salary have a correlation of {correlation:.2f}.")
print(f"4. Monthly salary and performance score have a correlation of {salary_performance_correlation:.2f}.")