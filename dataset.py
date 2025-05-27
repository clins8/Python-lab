import pandas as pd

# Load the dataset (creating a new CSV file)
file_path = r"D:\movie.csv"

# Creating a dataset of movies
data = {
    'Movie': ['Inception', 'Titanic', 'Avatar', 'Interstellar', 'Joker', 'The Dark Knight', 'Gladiator'],
    'Genre': ['Sci-Fi', 'Romance', 'Sci-Fi', 'Sci-Fi', 'Thriller', 'Action', 'Historical'],
    'Director': ['Christopher Nolan', 'James Cameron', 'James Cameron', 'Christopher Nolan', 'Todd Phillips', 'Christopher Nolan', 'Ridley Scott'],
    'IMDB_Rating': [8.8, 7.8, 7.9, 8.6, 8.4, 9.0, 8.5],
    'Box_Office_Million': [829, 2187, 2847, 677, 1074, 1005, 460],
    'Release_Year': [2010, 1997, 2009, 2014, 2019, 2008, 2000]
}

# Creating DataFrame
df = pd.DataFrame(data)

# Saving to CSV
df.to_csv(file_path, index=False)

# Display the DataFrame
print("Original DataFrame")
print(df)

# Adding a new column for Awards
Awards = ['Oscar', 'Oscar', 'Oscar', 'None', 'Oscar', 'Oscar', 'Oscar']
df['Awards'] = Awards

print("\nDataFrame after adding a column (Awards)")
print(df)

# Identifying and Displaying missing values (NaN)
print("\nNull values in DataFrame:")
print(df.isnull())

# Count of null values in each column
print("\nCount of null values in each column:")
print(df.isnull().sum())

# Display a summary of the DataFrame
print("\nSummary of DataFrame")
print(df.describe())

# Descriptions of a particular column
print("\nDescription of Particular Column")
print(df['Movie'].describe())

# The number of rows and columns using .shape
print("\nNumber of Rows and Columns")
print(df.shape)

# Number of dimensions using .ndim
print("\nNumber of Dimensions")
print(df.ndim)

# To check the types of each column
print("\nData types of each column")
print(df.dtypes)

# head - shows the top 5 rows of data in the DataFrame
print("\nFirst 5 rows of DataFrame")
print(df.head())

# Display the first few rows of the DataFrame
print("\nFirst few rows of DataFrame")
print(df.head(2))

# tail - shows the last 5 rows of data in the DataFrame
print("\nLast 5 rows of DataFrame")
print(df.tail())

# Prints last 2 rows instead
print("\nLast few rows of DataFrame")
print(df.tail(2))

# Selecting columns using dot notation
print("\nSelecting a particular column")
print(df.Movie)

# Series summary operations on dataframe
print("\nSeries summary operations on dataframe")
print([
    df['Box_Office_Million'].sum(),    # Total sum of the column values
    df['Box_Office_Million'].mean(),   # Mean of the column values
    df['Box_Office_Million'].median(), # Median of the column values
    df['Box_Office_Million'].nunique(),# Number of unique entries
    df['Box_Office_Million'].max(),    # Maximum of the column values
    df['Box_Office_Million'].min()     # Minimum of the column values
])

# Renaming the column
df_renamed = df.rename(columns={"Movie": "Movie_Title"})
print("\nRenamed DataFrame:")
print(df_renamed)

# Grouping operation
print("\nGroup by Genre:")
print(df.groupby('Genre').size())

# Define a new dictionary containing movie details
df1 = {'Movie_Title': ['Inception', 'Titanic'], 'Lead_Actor': ['Leonardo DiCaprio', 'Leonardo DiCaprio']}
print("\nNew DataFrame")
print(df1)

# Merging of dataframes
df1 = pd.DataFrame(df1)
result = pd.merge(df_renamed, df1, on="Movie_Title")
print("\nMerged DataFrame")
print(result)

# Concatenation of dataframes
res1 = pd.concat([df_renamed, df1])
print("\nConcatenation of DataFrame")
print(res1)

# Select rows 0 and 2, and columns 0 and 2
print("\nIndexing using iloc")
print(df.iloc[[0, 2], [0, 2]])

# Slicing columns and rows at the same time
print("\nSlicing using iloc")
print(df.iloc[0:2, 2:4])

# **Delete Operation**
# Dropping the 'Awards' column
df.drop(columns=['Awards'], inplace=True)
print("\nDataFrame after deleting the 'Awards' column:")
print(df)

# Dropping a row (e.g., remove 'Joker' from the dataset)
df = df[df.Movie != 'Joker']
print("\nDataFrame after deleting a row (Joker):")
print(df)

# Saving the final modified DataFrame
output_file = r"D:\movie.csv"
df.to_csv(output_file, index=False)
print(f"\nCSV file saved successfully at {output_file}")
