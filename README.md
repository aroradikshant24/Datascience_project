# Datascience_project
Furniture Sales Analysis using Python and Pandas — Exploratory Data Analysis, data cleaning, missing-value analysis, IQR-based outlier detection, financial validation, and data-driven business insights from furniture transaction data.

# 🪑 Furniture Sales Analysis
### Improving Furniture Business Revenue Through Analysis of Past Sales Data

## 📌 Project Overview
This project focuses on analysing a furniture export sales dataset using Python to understand transaction data, identify missing values, detect outliers, validate financial calculations, and derive meaningful business insights.

The project follows fundamental Data Science practices, including data understanding, preprocessing, exploratory analysis, statistical methods, and data validation.

## 🎯 Objectives
- Understand the structure and attributes of the furniture sales dataset.
- Identify data types and missing values.
- Detect duplicate records.
- Apply appropriate data-cleaning and missing-value handling techniques.
- Detect outliers using the Interquartile Range (IQR) method.
- Validate financial calculations involving taxable value, GST, and total invoice value.
- Derive business insights from the analysis.

## 📊 Dataset Overview
- **Records:** 59 transactions
- **Attributes:** 14 columns
- **Dataset Type:** Structured, tabular data
- **Data Domain:** Furniture sales and export transactions

The dataset contains information related to transaction dates, furniture items, categories, quantities, costs, GST, shipping, warehouse stock, profit margins, and supplier lead times.

## 🛠️ Tools & Technologies
- Python
- Pandas
- Jupyter Notebook
- Statistical Analysis
- Data Cleaning
- Exploratory Data Analysis (EDA)

## 🔍 Methodology
1. Dataset loading and inspection
2. Data type identification
3. Missing-value analysis
4. Duplicate detection
5. Data cleaning and preprocessing
6. Outlier detection using IQR
7. Financial formula validation
8. Data visualization and interpretation

## 📈 Analysis Performed

### Missing Values
A total of 84 missing cells were identified out of 826 total cells, representing approximately **10.17%** missing data.

### Duplicate Detection
No fully duplicated rows were identified.

### Outlier Detection
The Interquartile Range (IQR) method was used.

- **Unit Cost:** 5 outliers
- **Quantity:** 7 outliers
- **Shipping Cost:** 0 outliers
- **Supplier Lead Time:** 0 outliers

Outliers were not automatically removed because they may represent genuine premium products or bulk orders.

### Financial Validation
The following formulas were tested:

- **Taxable Value = Quantity × Unit Cost**
- **GST Amount = Taxable Value × GST Rate / 100**
- **Total Value = Taxable Value + GST Amount**

| Validation | Records Checked | Mismatches |
|---|---:|---:|
| Taxable Value | 43 | 0 |
| GST Amount | 46 | 0 |
| Total Value | 51 | 0 |

All checkable records satisfied their respective financial formulas.

## 💡 Key Findings
- High unit costs may represent premium furniture products.
- High quantities may represent genuine bulk transactions.
- No financial formula mismatches were found in the checkable records.
- Shipping cost and supplier lead-time data showed no IQR-flagged outliers.
- Improved data collection, especially for stock and lead-time fields, could support better business decisions.

## ⚠️ Limitations
- The dataset contains only 59 records.
- Approximately 10.17% of cells are missing.
- The dataset is better suited to descriptive and exploratory analysis than reliable predictive modelling.
- Missing values and outliers require contextual investigation rather than indiscriminate replacement or deletion.

## 🚀 Future Scope
- Perform category-wise sales analysis.
- Analyse monthly sales trends.
- Build sales forecasting models using larger datasets.
- Improve data quality and completeness.
- Develop dashboards for business decision-making.

## 📂 Project Files
- `Project.ipynb` – Jupyter Notebook containing the analysis and code.
- Dataset – Furniture export transaction data.
- Project report and presentation – Documentation of methodology, results and findings.

## 👨‍💻 Contributors
- Dikshant
- Kanav Sachdeva

## 📚 Project Context
This project was developed as part of the **Fundamentals of Data Science** course, B.Tech CSE.
