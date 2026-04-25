# 🎬 MovieLens Pro

[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)

> **AI-powered movie recommendation system** built with FastAPI, Streamlit, and scikit-learn. Discover personalized movie suggestions based on content similarity.

---

## ✨ Features

- 🔍 **Smart Search** — Autocomplete movie search with real-time suggestions
- 🎯 **Personalized Recommendations** — Get top 5 similar movies using ML similarity matrix
- 🏆 **Top Movies** — Browse the highest-rated movies from the dataset
- 🌙 **Cinematic UI** — Dark-themed, glassmorphic Streamlit interface with hover animations
- ⚡ **FastAPI Backend** — High-performance REST API with automatic docs
- 🤖 **ML-Powered** — Content-based filtering using a pre-trained similarity model

---

## 🛠 Tech Stack

| Layer | Technology |
|-------|------------|
| **Backend** | FastAPI, Uvicorn, Pydantic |
| **Frontend** | Streamlit, Custom CSS |
| **ML / Data** | scikit-learn, pandas, numpy |
| **Model Storage** | Hugging Face Hub |
| **Deployment** | Render (Backend) |

---

## 📁 Project Structure

```
Movie/
├── app/
│   ├── main.py           # FastAPI application & endpoints
│   ├── ui.py             # Streamlit frontend interface
│   ├── recommender.py    # ML logic: download, load, recommend
│   └── schema.py         # Pydantic request/response models
├── data/                 # Dataset & local model files
├── requirements.txt      # Python dependencies
├── TODO.md               # Development roadmap
├── .gitignore
└── README.md             # You are here!
```

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/Vivek3401/movie-recommendation-api.git
cd movie-recommendation-api
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate        # On Linux/Mac
venv\Scripts\activate           # On Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

### Run the Backend (FastAPI)

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at:
- **Base URL:** `http://localhost:8000`
- **Interactive Docs:** `http://localhost:8000/docs`
- **ReDoc:** `http://localhost:8000/redoc`

### Run the Frontend (Streamlit)

In a new terminal:

```bash
streamlit run app/ui.py
```

The UI will open automatically at `http://localhost:8501`.

> **Note:** Update the `API_URL` in `app/ui.py` to point to your local backend (`http://localhost:8000`) if running both locally.

---

## 🔌 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | Health check — confirms API is running |
| `GET` | `/recommend?movie={name}` | Get top 5 recommendations for a movie |
| `POST` | `/recommend` | Same as above but accepts JSON body (`MovieRequest`) |
| `GET` | `/search?query={text}` | Search movies by partial title match |
| `GET` | `/top-movies?limit={n}` | Retrieve top N movies from the dataset |

### Example Request

```bash
curl "http://localhost:8000/recommend?movie=Inception"
```

### Example Response

```json
{
  "success": true,
  "movie": "Inception",
  "recommendations": [
    "The Dark Knight",
    "Interstellar",
    "The Prestige",
    "Shutter Island",
    "Memento"
  ]
}
```

---

## 🌍 Deployment

- **Backend** is deployed on **Render**: `https://movie-recommendation-api-8iux.onrender.com`
- **ML Artifacts** (model.pkl + similarity.pkl) are hosted on [Hugging Face Hub](https://huggingface.co/Vivek3401/movie-recommendation-model) and downloaded automatically on startup.

---

## 🖼️ Screenshots

*Coming soon — add screenshots of the Streamlit UI here!*

---

## 📋 Roadmap

See [TODO.md](TODO.md) for the full development checklist.

- [x] Professional cinematic Streamlit UI with dark theme
- [x] Search autocomplete integration
- [x] Top movies browsing
- [ ] Local testing & bug fixes
- [ ] Add unit tests
- [ ] Dockerize the application

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

<p align="center">Made with ❤️ using FastAPI + Streamlit</p>

