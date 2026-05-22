
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import requests
import pickle
import os
from dotenv import load_dotenv

# Load local environment variables from .env file if present
load_dotenv()

# 1. Start the web app
app = FastAPI()

# Allow your website to talk to this Python code without security blocks
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# 2. Load the trained brain (Your .pkl files)
# We do this outside the function so it only loads once when the server starts, keeping it fast!
try:
    print("Loading machine learning models... Please wait.")
    tfidf_matrix = pickle.load(open('tfidf_matrix.pkl', 'rb'))
    indices = pickle.load(open('indices.pkl', 'rb'))
    df = pd.read_pickle('df.pkl')
    df['popularity'] = pd.to_numeric(df['popularity'], errors='coerce')
    print("Models loaded successfully!")
except FileNotFoundError:
    print("Error: Make sure tfidf_matrix.pkl, indices.pkl, and df.pkl are in this folder.")

# 3. Setup the API Key for images securely from environment variables
OMDB_API_KEY = os.getenv("OMDB_API_KEY", "352ae29e")

def fetch_omdb_data(movie_title):
    """
    This function takes a movie name, asks OMDb for the details, 
    and returns the poster link and rating.
    """
    url = "http://www.omdbapi.com/"
    
    # Pack the title and your key into the request
    params = {
        "t": movie_title,
        "apikey": OMDB_API_KEY
    }
    
    try:
        response = requests.get(url, params=params)
        data = response.json()
        
        # If OMDb finds the movie successfully
        if data.get("Response") == "True":
            poster = data.get("Poster")
            
            # If OMDb has no picture, use a placeholder image
            if poster == "N/A":
                poster = "https://via.placeholder.com/500x750?text=No+Poster"
                
            return {
                "poster_url": poster,
                "rating": data.get("imdbRating", "N/A"),
                "year": data.get("Year", "Unknown")
            }
    except Exception as e:
        print(f"OMDb Error for {movie_title}: {e}")
        
    # If anything goes wrong, return blank fallback data
    return {
        "poster_url": "https://via.placeholder.com/500x750?text=No+Poster",
        "rating": "N/A",
        "year": "Unknown"
    }


# 4. The Main Engine: Connecting the Math to the Web
@app.get("/recommend")
def get_recommendations(movie_name: str):
    """
    This is the link your website will call.
    It takes the search text, finds similar movies, and gets their posters.
    """
    
    # Step A: Make sure the movie exists in your Jupyter Notebook dataset
    if movie_name not in indices:
        match = next((m for m in indices.index if str(m).lower() == movie_name.lower()), None)
        if match:
            movie_name = match
        else:
            return {"error": f"Sorry, '{movie_name}' is not in the database."}

    # Step B: Get the row number (index) of the movie
    idx = indices[movie_name]
    
    # Sometimes a dataset has two movies with the exact same name. 
    # This grabs just the first one so the code doesn't crash.
    if isinstance(idx, pd.Series):
        idx = idx.iloc[0]
        
    # Step C: Run the Cosine Similarity math (from your notebook)
    sim_score = cosine_similarity(tfidf_matrix[idx], tfidf_matrix).flatten()
    
    # Step D: Get the top 5 most similar movies (skipping the 1st one, which is the searched movie itself)
    similar_idx = sim_score.argsort()[::-1][1:6] 
    
    # Step E: Convert those row numbers back into actual movie titles
    recommended_titles = df['title'].iloc[similar_idx].tolist()

    # Step F: Get the pictures for those 5 titles using OMDb
    final_results = []
    
    for title in recommended_titles:
        api_data = fetch_omdb_data(title)
        
        # Package everything nicely for the website to read
        final_results.append({
            "title": title,
            "poster": api_data["poster_url"],
            "rating": api_data["rating"],
            "year": api_data["year"]
        })

    # Send the final package back to the website
    return {"recommendations": final_results}

@app.get("/genre")
def get_movies_by_genre(genre_name: str):
    # Map friendly names to database names (e.g. Sci-Fi to Science Fiction)
    search_genre = genre_name
    if genre_name.lower() in ["sci-fi", "scifi"]:
        search_genre = "Science Fiction"

    # Find movies containing the genre, sort by popularity
    matches = df[df['genres'].str.contains(search_genre, case=False, na=False)]
    if matches.empty:
        return {"error": f"No movies found for genre: {genre_name}"}
    
    # Grab the top 10 most popular movies in this genre
    top_matches = matches.sort_values(by='popularity', ascending=False).head(10)
    titles = top_matches['title'].tolist()
    
    final_results = []
    for title in titles:
        api_data = fetch_omdb_data(title)
        final_results.append({
            "title": title,
            "poster": api_data["poster_url"],
            "rating": api_data["rating"],
            "year": api_data["year"]
        })
    return {"recommendations": final_results}

@app.get("/language")
def get_movies_by_language(language_code: str):
    # Filter by original_language
    matches = df[df['original_language'].str.lower() == language_code.lower()]
    if matches.empty:
        return {"error": f"No movies found for language: {language_code}"}
    
    # Grab the top 10 most popular movies in this language
    top_matches = matches.sort_values(by='popularity', ascending=False).head(10)
    titles = top_matches['title'].tolist()
    
    final_results = []
    for title in titles:
        api_data = fetch_omdb_data(title)
        final_results.append({
            "title": title,
            "poster": api_data["poster_url"],
            "rating": api_data["rating"],
            "year": api_data["year"]
        })
    return {"recommendations": final_results}

# 5. Serve Frontend Static Files
# This mounts the frontend files to the root '/' so they are served when visiting http://127.0.0.1:8000/
import os
from fastapi.staticfiles import StaticFiles

frontend_dir = os.path.join(os.path.dirname(__file__), "frontend", "stitch_cinematic_obsession", "cinephile_landing_page_animated_background")
if os.path.exists(frontend_dir):
    app.mount("/", StaticFiles(directory=frontend_dir, html=True), name="frontend")
else:
    print(f"Warning: Frontend directory not found at {frontend_dir}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)