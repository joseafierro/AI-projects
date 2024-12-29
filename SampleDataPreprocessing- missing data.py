import pandas as pd

# Step 1: Load the dataset
df = pd.read_csv('/home/josefierro/Documents/data.csv')

# Step 2: Ensure proper data types
df['Age'] = pd.to_numeric(df['Age'], errors='coerce')
df['Salary'] = pd.to_numeric(df['Salary'], errors='coerce')
df['Department'] = df['Department'].astype(str).replace(['nan', 'None', 'null'], pd.NA)

# Step 3: Fill numerical columns with mean
df['Age'].fillna(df['Age'].mean(), inplace=True)
df['Salary'].fillna(df['Salary'].mean(), inplace=True)

# Step 4: Fill categorical columns with mode
if not df['Department'].mode().empty:
    df['Department'].fillna(df['Department'].mode()[0], inplace=True)
else:
    df['Department'].fillna('Unknown', inplace=True)

# Step 5: Verify no NaNs remain
print("\nMissing Values per Column After Cleaning:")
print(df.isnull().sum())

# Step 6: Display the cleaned dataset
print("\nCleaned Dataset:")
print(df)
