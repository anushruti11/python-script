import pandas as pd

# Loads the dataset into a Pandas DataFrame
netflix_data = pd.read_csv("netflix_titles.csv")

# Filters out rows with missing or empty 'cast' information
netflix_data = netflix_data[netflix_data['cast'].notna()]

# Ensures that the "cast" column is not empty and fill missing values with an empty string
netflix_data['cast'] = netflix_data['cast'].fillna('')

# Function to split the cast column into a list of actors
def extract_actors(cast_string):
    return cast_string.split(', ')

# Splits the cast column into a list of actors and create a new column
netflix_data['actors'] = netflix_data['cast'].apply(extract_actors)

# Creates a list of all actors
all_actors = [actor for actors_list in netflix_data['actors'] for actor in actors_list]

# Uses the Counter class to count the frequency of each actor
from collections import Counter
actor_counts = Counter(all_actors)

# Lists the top 10 actors by frequency
top_10_actors = actor_counts.most_common(10)

# Prints the results
print("Top 10 actors on Netflix and their appearance frequency:")
for actor, frequency in top_10_actors:
    print(f"{actor}: {frequency}")
