import streamlit as st
import requests
import time

# 🔗 Replace with your Render URL
API_URL = "https://movie-recommendation-api-8iux.onrender.com"

# Page config
st.set_page_config(
    page_title="Movie Recommender Pro",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for professional cinematic theme
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    .main {
        background: linear-gradient(135deg, #0c0c0c 0%, #1a1a2e 50%, #16213e 100%);
        padding: 2rem;
    }
    
    .stApp {
        background: transparent;
    }
    
    h1 {
        font-family: 'Inter', sans-serif;
        font-weight: 700;
        font-size: 3.5rem;
        background: linear-gradient(135deg, #ff6b6b, #4ecdc4, #45b7d1);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 1rem;
    }
    
    .hero-text {
        font-family: 'Inter', sans-serif;
        font-weight: 400;
        font-size: 1.3rem;
        color: #b8b8b8;
        text-align: center;
        margin-bottom: 3rem;
    }
    
    .movie-card {
        background: rgba(255,255,255,0.05);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 1.5rem;
        margin: 1rem 0;
        border: 1px solid rgba(255,255,255,0.1);
        transition: all 0.3s ease;
        cursor: pointer;
    }
    
    .movie-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 20px 40px rgba(0,0,0,0.3);
        border-color: rgba(255,107,107,0.3);
    }
    
    .rank-badge {
        background: linear-gradient(135deg, #ff6b6b, #4ecdc4);
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 50px;
        font-weight: 600;
        font-size: 0.9rem;
        display: inline-block;
        margin-bottom: 1rem;
    }
    
    .btn-primary {
        background: linear-gradient(135deg, #ff6b6b, #4ecdc4);
        border: none;
        border-radius: 50px;
        padding: 1rem 2rem;
        font-weight: 600;
        font-size: 1.1rem;
        transition: all 0.3s ease;
        width: 100%;
        height: 60px;
    }
    
    .btn-primary:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 30px rgba(255,107,107,0.4);
    }
    
    .search-select {
        background: rgba(255,255,255,0.1);
        border-radius: 15px;
        border: 2px solid rgba(255,255,255,0.2);
        padding: 1rem;
    }
    
    .metric-card {
        background: rgba(255,255,255,0.05);
        backdrop-filter: blur(10px);
        border-radius: 15px;
        padding: 1.5rem;
        text-align: center;
        border: 1px solid rgba(255,255,255,0.1);
    }
    
    .footer {
        background: rgba(0,0,0,0.5);
        padding: 2rem;
        text-align: center;
        border-radius: 20px;
        margin-top: 3rem;
    }
    
    .status-badge {
        padding: 0.5rem 1rem;
        border-radius: 20px;
        font-weight: 500;
        font-size: 0.9rem;
    }
    
    .status-online { background: rgba(76, 205, 196, 0.2); color: #4ecdc4; border: 1px solid #4ecdc4; }
    .status-offline { background: rgba(255, 107, 107, 0.2); color: #ff6b6b; border: 1px solid #ff6b6b; }
</style>
""", unsafe_allow_html=True)

def check_api_status():
    """Check if API is reachable"""
    try:
        response = requests.get(f"{API_URL}/", timeout=5)
        return response.status_code == 200
    except:
        return False

# Header Section
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown("""
    # 🎬 MovieLens Pro
    ### Discover personalized movie recommendations powered by AI
    """, unsafe_allow_html=True)

# API Status
api_status = check_api_status()
status_class = "status-online" if api_status else "status-offline"
st.markdown(f"""
<div class="status-badge {status_class}">
    {'🟢 API Online' if api_status else '🔴 API Offline'}
</div>
""", unsafe_allow_html=True)

if not api_status:
    st.error("⚠️ API is currently offline. Please check your Render deployment.")
    st.stop()

# Main Layout
tab1, tab2 = st.tabs(["🎯 Get Recommendations", "🔍 Browse Movies"])

with tab1:
    # Search with autocomplete
    st.markdown("### Search for a movie")
    
    # Get search suggestions
    search_query = st.text_input("Type to search...", key="search_input")
    search_results = []
    
    if search_query:
        try:
            with st.spinner("Searching movies..."):
                response = requests.get(f"{API_URL}/search", params={"query": search_query}, timeout=5)
                if response.status_code == 200:
                    data = response.json()
                    search_results = data.get("results", [])[:10]
        except:
            st.warning("Search temporarily unavailable")
    
    selected_movie = st.selectbox(
        "Select a movie:",
        options=[""] + search_results,
        index=0,
        help="Choose from search results or type your own movie name"
    )
    
    # Recommend button
    if st.button("🎥 Get Recommendations", key="recommend_btn"):
        if selected_movie.strip():
            with st.spinner("🤖 Generating recommendations..."):
                try:
                    response = requests.get(
                        f"{API_URL}/recommend",
                        params={"movie": selected_movie},
                        timeout=10
                    )
                    
                    if response.status_code == 200:
                        data = response.json()
                        recommendations = data.get("recommendations", [])
                        
                        if recommendations:
                            st.success(f"✨ Top recommendations for **{selected_movie}**")
                            
                            # Display as professional cards
                            for i, movie in enumerate(recommendations[:5], 1):
                                st.markdown(f"""
                                <div class="movie-card">
                                    <span class="rank-badge">#{i}</span>
                                    <h3 style="color: white; margin: 1rem 0 0 0;">{movie}</h3>
                                    <p style="color: #b8b8b8; margin: 0.5rem 0 0 0;">
                                        Perfect match for your taste!
                                    </p>
                                </div>
                                """, unsafe_allow_html=True)
                        else:
                            st.warning("No recommendations found for this movie.")
                    else:
                        st.error("Movie not found in our database 😔")
                        
                except requests.exceptions.Timeout:
                    st.error("⏱️ Request timed out. Please try again.")
                except Exception as e:
                    st.error("❌ Connection error. Please check your internet.")
        else:
            st.warning("👆 Please select a movie first!")

with tab2:
    st.markdown("### 🔥 Top Movies")
    
    cols = st.columns(2)
    with cols[0]:
        limit = st.slider("Show top movies:", 5, 20, 10)
    
    try:
        with st.spinner("Loading top movies..."):
            response = requests.get(f"{API_URL}/top-movies", params={"limit": limit}, timeout=5)
            if response.status_code == 200:
                data = response.json()
                top_movies = data.get("movies", [])
                
                for i, movie in enumerate(top_movies, 1):
                    st.markdown(f"""
                    <div class="movie-card" style="padding: 1rem;">
                        <span class="rank-badge">#{i}</span> {movie}
                    </div>
                    """, unsafe_allow_html=True)
    except:
        st.error("Could not load top movies")

# Footer
st.markdown("""
<div class="footer">
    <h4 style="color: #4ecdc4; margin-bottom: 1rem;">Made with ❤️ using Streamlit + FastAPI</h4>
    <p style="color: #b8b8b8;">
        Powered by MovieLens dataset • AI-driven similarity matching
    </p>
</div>
""", unsafe_allow_html=True)
