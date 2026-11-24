import matplotlib.pyplot as plt

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