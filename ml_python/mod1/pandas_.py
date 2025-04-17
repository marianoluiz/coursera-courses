# Pandas library for data manipulation and analysis.
import pandas as pd

# Define a dictionary with real data
data = {
  'column 1': [1, 2, 3],
  'column 2': ['A', 'B', 'C'],
}

df = pd.DataFrame(data)

print('\n',df)

# Accessing Columns

  # Single column
new_df = df[['column 1']]

  # Multiple columns
new_df = df[['column 1', 'column 2']]

print('\n',new_df)


# Accessing Data with iloc and loc

  # Using iloc: Access data by row and column index.
first_value = df.iloc[0, 0]

second_value = df.iloc[1, 0]

print("\niloc [0,0]: ", first_value)
print("iloc [0,1]: ", second_value)

  # Using loc: Access data by row index label and column name.

# Add a custom index column
df_custom_index = df
df_custom_index.index = ['a', 'b', 'c']

  # Access row with index 'a', column 'artist'
artist_value = df_custom_index.loc['a', 'column 2']

print('\n loc[index, coln]: ', artist_value)

# Slicing DataFrames

  # Assign the first two rows and the first three columns to a new variable
z = df_custom_index.iloc[0:2, 0:3]

print("\n", z)

  # Using loc to select specific rows and columns
z = df_custom_index.loc['a':, 'column 1':]


print("\n", z)