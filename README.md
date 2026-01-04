# Movie_Recommender_System
A content-based movie recommendation engine that suggests five similar movies based on user selection. This project uses machine learning (Natural Language Processing) and the TMDB API to provide real-time posters, ratings, and plot overviews.
## Live Demo
https://movierecommendersystem-a5vgb9qtc6x2iks5ayhpbz.streamlit.app
## Features
- Personalized Recommendations: Suggests 5 movies similar to your search.

- Real-time Data: Fetches live posters, IMDb-style ratings, and movie overviews via TMDB API.

- Optimized Performance: Precomputed similarity indices ensure the app loads instantly on cloud servers.

- Clean UI: Responsive layout using Streamlit columns and expanders for a professional look.

## Technical Implementation
### Data Preprocessing:
- Vectorization: Used CountVectorizer from scikit-learn to convert movie tags into 5,000-dimensional vectors.

- Cosine Similarity: Calculated the mathematical distance between vectors to find the most similar films.

- Index Alignment: Implemented reset_index(drop=True) to fix gaps in the TMDB dataset, ensuring accurate poster retrieval.
### Deployment:
- The application is officially deployed and hosted using Streamlit Cloud for seamless access.
## 📂 Project Structure

```text
├── app.py                      # Main Streamlit web application
├── movie_recommendation.ipynb  # Jupyter Notebook with data cleaning & ML logic
├── movie_dict.pkl              # Cleaned movie data exported as a dictionary
├── similarity_indices.pkl      # Optimized precomputed top-5 recommendation indices
└── README.md                   # Project documentation and setup guide
