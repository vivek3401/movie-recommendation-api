import streamlit as st
import requests

# 🔗 Replace with your Render URL
API_URL = "https://movie-recommendation-api-8iux.onrender.com"

st.set_page_config(page_title="Movie Recommender", page_icon="🎬")

st.title("🎬 Movie Recommendation System")

movie_name = st.text_input("Enter a movie name")

if st.button("Recommend"):
    if movie_name.strip() == "":
        st.warning("Please enter a movie name")
    else:
        try:
            response = requests.get(
                f"{API_URL}/recommend",
                params={"movie": movie_name}
            )

            if response.status_code == 200:
                data = response.json()
                st.success(f"Recommendations for '{movie_name}':")

                for movie in data["recommendations"]:
                    st.write("👉", movie)

            else:
                st.error("Movie not found")

        except Exception as e:
            st.error("API connection failed")