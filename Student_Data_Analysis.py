
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# 1. Load CSV file
folder_path = Path(__file__).parent
file_path = folder_path / "student_performance.csv"

df = pd.read_csv(file_path)

print("STUDENT PERFORMANCE DATA ANALYSIS")
print("----------------------------------")

# 2. Display original dataset
print("\nOriginal Dataset:")
print(df)

# 3. Display dataset information
print("\nDataset Information:")
print(df.info())

# 4. Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# 5. Remove duplicate records
df = df.drop_duplicates()

# 6. Handle missing values
for column in df.columns:
    if pd.api.types.is_numeric_dtype(df[column]):
        df[column] = df[column].fillna(df[column].mean())
    else:
        df[column] = df[column].fillna("Unknown")

print("\nCleaned Dataset:")
print(df)

# 7. Display summary statistics
print("\nSummary Statistics:")
print(df.describe(include="all"))

# 8. Filter data
numeric_columns = df.select_dtypes(include="number").columns

if len(numeric_columns) > 0:
    column = numeric_columns[0]
    filtered_data = df[df[column] > df[column].mean()]

    print("\nFiltered Data:")
    print(filtered_data)

# 9. Grouping data
categorical_columns = df.select_dtypes(
    include=["object", "category"]
).columns

if len(categorical_columns) > 0 and len(numeric_columns) > 0:
    group_column = categorical_columns[0]
    value_column = numeric_columns[0]

    grouped_data = df.groupby(group_column)[value_column].mean()

    print("\nGrouped Data:")
    print(grouped_data)

    # 10. Generate Graph
    grouped_data.plot(kind="bar", title="Average Performance")
    plt.xlabel(group_column)
    plt.ylabel("Average " + value_column)
    plt.tight_layout()
    plt.savefig(folder_path / "student_analysis_graph.png")
    plt.show()

print("\nData Analysis Completed Successfully!")
