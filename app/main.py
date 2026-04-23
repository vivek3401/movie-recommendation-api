import logging
from fastapi import FastAPI, HTTPException
from app.recommender import recommend, search_movies, get_top_movies
from app.schema import MovieRequest

# Configure logging
logging.basicConfig(level=logging.INFO)

app = FastAPI(
    title="Movie Recommendation API",
    description="A backend service for movie recommendations using similarity matrix",
    version="1.0.0"
)

# -------------------- HOME --------------------
@app.get("/", tags=["General"])
def home():
    logging.info("Home endpoint called")
    return {"message": "Movie Recommendation API is running"}


# -------------------- GET RECOMMEND --------------------
@app.get("/recommend", tags=["Recommendation"])
def get_recommendation(movie: str):
    logging.info(f"GET /recommend called with movie: {movie}")

    result = recommend(movie)

    if result == ["Movie not found"]:
        logging.warning(f"Movie not found: {movie}")
        raise HTTPException(status_code=404, detail="Movie not found")

    return {
        "success": True,
        "movie": movie,
        "recommendations": result
    }


# -------------------- POST RECOMMEND --------------------
@app.post("/recommend", tags=["Recommendation"])
def recommend_post(request: MovieRequest):
    logging.info(f"POST /recommend called with movie: {request.movie}")

    result = recommend(request.movie)

    if result == ["Movie not found"]:
        logging.warning(f"Movie not found: {request.movie}")
        raise HTTPException(status_code=404, detail="Movie not found")

    return {
        "success": True,
        "movie": request.movie,
        "recommendations": result
    }


# -------------------- SEARCH --------------------
@app.get("/search", tags=["Search"])
def search(query: str):
    logging.info(f"/search called with query: {query}")

    results = search_movies(query)

    return {
        "success": True,
        "query": query,
        "count": len(results),
        "results": results
    }


# -------------------- TOP MOVIES --------------------
@app.get("/top-movies", tags=["Movies"])
def top_movies(limit: int = 10):
    logging.info(f"/top-movies called with limit: {limit}")

    movies = get_top_movies(limit)

    return {
        "success": True,
        "count": len(movies),
        "movies": movies
    }