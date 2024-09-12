import pandas as pd

# Load the Excel file
df = pd.read_excel('FY Accruals.xlsx')

# Load the CSV file
decimals_df = pd.read_csv('employee_decimals.csv')

# Merge the dataframes based on employee numbers
merged_df = df.merge(decimals_df, left_on='Employee ID', right_on='Employee ID', how='left')

# Update the target column with corresponding decimal values
df['Target Column'] = merged_df['Decimal Value'].fillna(0).apply(lambda x: "{:,.2f}".format(x))

# Convert date columns to MM/DD/YYYY format
df['Date Column'] = pd.to_datetime(df['Date Column']).dt.strftime('%m/%d/%Y')

# Remove unwanted columns
columns_to_keep = ['Employee ID', 'Target Column', 'Date Column']
df = df[columns_to_keep]

# Save the updated DataFrame to a new Excel file
df.to_excel('Updated_FY_Accruals2.xlsx', index=False)




