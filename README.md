# 🎬 Cinephile AI - Movie Recommendation Engine

Cinephile AI is a high-performance machine learning backend built with **FastAPI** that powers a personalized movie recommendation system. It leverages natural language processing (NLP) to calculate similarity scores between movies using **TF-IDF Vectorization** and **Cosine Similarity** on a curated dataset.

---

## 🚀 Key Features

* **Machine Learning Recommendations**: Instantly finds similar movies using tf-idf metadata alignment.
* **Genre-based Recommendations**: Dynamically filters and returns the most popular movies in any requested genre.
* **Language-based Filtering**: Provides high-quality recommendations filtered by language codes.
* **FastAPI Server**: Lightning-fast, asynchronous Python backend with built-in CORS middleware.
* **Secure Configuration**: Uses `python-dotenv` to safely load API keys from environment variables rather than hardcoding them in source control.
* **OMDb Integration**: Fetches high-quality posters, ratings, and year details dynamically.

---

## 🛠️ Tech Stack

* **Backend Framework**: [FastAPI](https://fastapi.tiangolo.com/)
* **ASGI Server**: [Uvicorn](https://www.uvicorn.org/)
* **Data Processing & ML**: `pandas`, `scikit-learn`
* **HTTP Requests**: `requests`
* **Environment Configuration**: `python-dotenv`

---

## 📥 Getting Started (Local Development)

### 1. Prerequisite Setup
Make sure you have **Python 3.8+** installed on your system.

### 2. Clone the Repository
```bash
git clone https://github.com/Yashwanth-MS/movie-backend.git
cd movie-backend
```

### 3. Create a Virtual Environment & Install Dependencies
```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
# On Windows (PowerShell):
.venv\Scripts\Activate.ps1
# On macOS/Linux:
source .venv/bin/activate

# Install required packages
pip install -r requirements.txt
```

### 4. Configure Your Environment Variables
Create a file named `.env` in the root of the project:
```ini
OMDB_API_KEY=your_omdb_api_key_here
```
> [!IMPORTANT]
> The `.env` file contains sensitive credentials and is automatically ignored by Git (configured in `.gitignore`). **Never commit your `.env` file to GitHub.**

### 5. Start the Server
```bash
python main.py
```
The server will start running locally at **`http://127.0.0.1:8000`**. You can view the automatic interactive API documentation at `http://127.0.0.1:8000/docs`.

---

## 🌐 API Endpoints

### 1. Get Recommendations
* **URL**: `/recommend`
* **Method**: `GET`
* **Query Parameter**: `movie_name` (e.g. `Toy Story`)
* **Response**: Returns the top 5 most similar movies, including their OMDb posters, ratings, and release years.

### 2. Browse by Genre
* **URL**: `/genre`
* **Method**: `GET`
* **Query Parameter**: `genre_name` (e.g. `Sci-Fi` or `Action`)
* **Response**: Returns the top 10 most popular movies matching that genre.

### 3. Filter by Language
* **URL**: `/language`
* **Method**: `GET`
* **Query Parameter**: `language_code` (e.g. `en`, `ja`)
* **Response**: Returns the top 10 most popular movies matching that language.

---

## ☁️ Deployment

This backend is pre-configured and ready to be deployed to **[Render](https://render.com/)** or any other cloud provider.

1. **Build Command**: `pip install -r requirements.txt`
2. **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`
3. **Environment Variables**: Add your `OMDB_API_KEY` under your Render web service environment settings.
