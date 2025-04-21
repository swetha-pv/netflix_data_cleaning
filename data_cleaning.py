import pandas as pd
dataset=pd.read_csv("Best Movie by Year Netflix.csv")  #here we loaded the netflix dataset
print("before cleaning data")
print(dataset.head()) #to view few rows at top

print(dataset.columns)
print(dataset.info())


print("Before remove null value records")
print(dataset.isnull().sum())

dataset['TITLE'] = dataset['TITLE'].fillna('Unknown')
dataset['RELEASE YEAR'] = dataset['RELEASE YEAR'].fillna(dataset['RELEASE YEAR'].median())
print(dataset.isnull().sum())

dataset=dataset.dropna()
print("After remove null value records")
print(dataset.columns)
print(dataset.isnull().sum())



duplicates = dataset.duplicated()
print(f"Number of duplicate rows: {duplicates.sum()}")
dataset = dataset.drop_duplicates()
print(f"After removing duplicates, number of rows: {len(dataset)}")

# Replace country abbreviations with full names if necessary
dataset['MAIN PRODUCTION'] = dataset['MAIN PRODUCTION'].replace({
    'US': 'United States',
    'GB': 'United Kingdom',
    'IN': 'India',
    'DE': 'Germany',
    'FR': 'France',
    'JP': 'Japan',
    'HK': 'Hong Kong'
})
print(dataset.head())


dataset['RELEASE YEAR'] = dataset['RELEASE YEAR'].astype(int)
dataset['release_date'] = pd.to_datetime(dataset['RELEASE YEAR'].astype(str) + '-01-01', format='%Y-%m-%d')
print(dataset['release_date'].dtype)
print(dataset[['RELEASE YEAR', 'release_date']].head())

dataset.columns = dataset.columns.str.lower().str.replace(' ', '_').str.replace('[^a-z0-9_]', '', regex=True)
print(dataset.columns)

print(dataset.shape)         # Shows number of rows and columns
print(dataset.info())        # Shows data types and memory usage

# Save the cleaned dataset
dataset.to_csv("cleaned_netflix_dataset.csv", index=False)
