import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_excel("furniture_export_data.xlsx")

outlier_counts = {
    'Unit Cost': 5,
    'Quantity': 7,
    'Shipping Cost': 0,
    'Supplier Lead Time': 0
}

plt.figure(figsize=(8, 5))
plt.bar(outlier_counts.keys(), outlier_counts.values())
plt.title("Outliers Detected in Numerical Variables")
plt.xlabel("Variables")
plt.ylabel("Number of Outliers")
plt.show()

checks = ['Taxable Value', 'GST Amount', 'Total Value']
checked_records = [43, 46, 51]
mismatches = [0, 0, 0]

plt.figure(figsize=(8, 5))
plt.bar(checks, checked_records, label='Checked Records')
plt.bar(checks, mismatches, label='Mismatches')

plt.title("Financial Validation Results")
plt.xlabel("Financial Checks")
plt.ylabel("Number of Records")
plt.legend()
plt.show()

# 1. Histogram — Distribution of Unit Cost
# Purpose: To understand how unit costs are distributed and where most transactions fall.

plt.figure(figsize=(8, 5))
plt.hist(df['Unit Cost'].dropna(), bins=10, edgecolor='black')
plt.title('Distribution of Unit Cost')
plt.xlabel('Unit Cost (₹)')
plt.ylabel('Frequency')
plt.show()

# 2. Box Plot — Unit Cost
# Purpose: Visual identification of spread, median, quartiles and potential outliers.

plt.figure(figsize=(8, 5))
plt.boxplot(df['Unit Cost'].dropna())
plt.title('Box Plot of Unit Cost')
plt.ylabel('Unit Cost (₹)')
plt.show()

# 3. Scatter Plot — Quantity vs Unit Cost
# Purpose: To examine the relationship between quantity sold and unit cost.

plt.figure(figsize=(8, 5))
plt.scatter(df['Quantity'], df['Unit Cost'])
plt.title('Quantity vs Unit Cost')
plt.xlabel('Quantity')
plt.ylabel('Unit Cost (₹)')
plt.show()


# 4. Bar Chart — Revenue by Furniture Category
# Purpose: To compare sales across categories.

category_revenue = df.groupby('Category')['Total Value incl GST'].sum()

plt.figure(figsize=(8, 5))
plt.bar(category_revenue.index, category_revenue.values)
plt.title('Revenue by Furniture Category')
plt.xlabel('Category')
plt.ylabel('Total Revenue (₹)')
plt.xticks(rotation=45)
plt.show()


# 5. Line Chart — Sales Over Time
# Purpose: To observe trends in sales over time.

df['Transaction Date'] = pd.to_datetime(df['Transaction Date'])

daily_sales = df.groupby('Transaction Date')['Total Value incl GST'].sum()

plt.figure(figsize=(10, 5))
plt.plot(daily_sales.index, daily_sales.values, marker='o')
plt.title('Sales Trend Over Time')
plt.xlabel('Transaction Date')
plt.ylabel('Sales Value (₹)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()