import os
import requests
import pickle
import pandas as pd

# -----------------------------
# Download utility
# -----------------------------
def download_file(url, filename):
    if not os.path.exists(filename):
        print(f"Downloading {filename}...")
        r = requests.get(url)
        r.raise_for_status()
        with open(filename, 'wb') as f:
            f.write(r.content)

# -----------------------------
# Hugging Face model URLs
# -----------------------------
MODEL_URL = "https://huggingface.co/Vivek3401/movie-recommendation-model/resolve/main/model.pkl"
SIMILARITY_URL = "https://huggingface.co/Vivek3401/movie-recommendation-model/resolve/main/similarity.pkl"

# -----------------------------
# Download files (ONLY once)
# -----------------------------
download_file(MODEL_URL, "model.pkl")
download_file(SIMILARITY_URL, "similarity.pkl")

# -----------------------------
# Load data
# -----------------------------
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("similarity.pkl", "rb") as f:
    similarity = pickle.load(f)

# Convert dict → DataFrame
movies = pd.DataFrame(model)

# -----------------------------
# Recommendation function
# -----------------------------
def recommend(movie_name: str):
    try:
        movie_index = movies[
            movies['title'].str.lower() == movie_name.lower()
        ].index[0]

        distances = similarity[movie_index]

        movie_list = sorted(
            list(enumerate(distances)),
            key=lambda x: x[1],
            reverse=True
        )

        movie_list = [m for m in movie_list if m[0] != movie_index][:5]

        recommended_movies = [
            movies.iloc[i[0]].title for i in movie_list
        ]

        return recommended_movies

    except Exception as e:
        print("Error:", e)
        return ["Movie not found"]

# -----------------------------
# Search function
# -----------------------------
def search_movies(query: str):
    try:
        results = movies[
            movies['title'].str.lower().str.contains(query.lower())
        ]
        return results['title'].head(10).tolist()
    except:
        return []

# -----------------------------
# Top movies
# -----------------------------
def get_top_movies(limit: int = 10):
    try:
        return movies['title'].head(limit).tolist()
    except:
        return []