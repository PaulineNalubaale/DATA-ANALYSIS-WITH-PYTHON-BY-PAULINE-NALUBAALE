import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

netflix_df = pd.read_csv("netflix_data.csv", index_col=0)
movies = netflix_df[netflix_df["type"] == "Movie"]
print(netflix_df["type"].unique())
release_in_1990s = movies["release_year"]
release_btn_1990 = np.logical_and(release_in_1990s >= 1990, release_in_1990s < 2000)
released1990s = movies[release_btn_1990]
duration = int(released1990s["duration"].mode()[0])


#plt.hist(release_in_1990s[release_btn_1990], bins=10)
#plt.xlabel("Years")
#plt.ylabel("Number of movies")
#plt.title("Movies in 1990s")



import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

netflix_df = pd.read_csv("netflix_data.csv", index_col=0)
movies = netflix_df[netflix_df["type"] == "Movie"]
release_btn_1990 = np.logical_and(movies["release_year"] >= 1990, movies["release_year"] < 2000)
movies_1990s = movies[release_btn_1990]
action_movies = movies_1990s[movies_1990s["genre"] == "Action"]

#  Setting up a short movie counter
short_movie_count = 0
for label, row in action_movies.iterrows():
    if row["duration"] < 90:
        short_movie_count = short_movie_count + 1
    else:
        pass
print(short_movie_count)

