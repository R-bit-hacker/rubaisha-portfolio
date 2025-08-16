import streamlit as st

# Portfolio Data
projects = [
    {
        "title": "Enterprise Churn Prediction System",
        "description": "Machine learning system predicting churn probability with ROI simulations. Includes Streamlit dashboard and Flask API integration.",
        "tech": ["Python", "Flask", "Streamlit", "Logistic Regression"],
        "impact": "Shifted focus from raw models → business outcomes. Businesses buy fewer breakups ❤️ not just algorithms.",
        "image": "images/churn.png",
    },
    {
        "title": "Tweets Depression Detection App",
        "description": "Streamlit app that detects depressive signals in tweets. Logistic Regression with TF-IDF, SMOTE balancing, deployed with Streamlit.",
        "tech": ["Python", "scikit-learn", "Streamlit", "SMOTE"],
        "impact": "3 days of debugging → one sukoon moment 😌 when it finally ran successfully.",
        "image": "images/depression.jpeg",
    },
    {
        "title": "Spotify Hit Prediction",
        "description": "Predicted hit songs using Spotify dataset with Random Forest. Achieved 91% accuracy with SMOTE class balancing.",
        "tech": ["Python", "Pandas", "RandomForest", "SMOTE"],
        "impact": "Revealed hits aren’t just about danceability — it’s a balance of multiple signals like valence & energy.",
        "image": "images/spotify.jpeg",
    },
    {
        "title": "Netflix EDA Project",
        "description": "Analyzed 8,000+ Netflix titles to uncover trends by country, genre, and year. Found content peaked in 2019.",
        "tech": ["Python", "Pandas", "Matplotlib", "Seaborn"],
        "impact": "USA & India lead in content production. Movies nearly double TV shows in volume.",
        "image": "images/netflix.png",
    },
]

# Streamlit UI
st.set_page_config(page_title="Rubaisha Munir Portfolio", page_icon="🚀", layout="wide")

# Header
col1, col2 = st.columns([1,3])
with col1:
    st.image("images/profile.jpeg", use_container_width=True)  # ✅ Fixed profile image
with col2:
    st.title("🌟 Rubaisha Munir")
    st.subheader("Machine Learning & Data Science Enthusiast 🚀")
    st.markdown("[💻 GitHub](https://github.com/R-bit-hacker) | [🔗 LinkedIn](https://www.linkedin.com/in/rubaishamunir/)")

# About
st.write("""
Hi, I’m **Rubaisha Munir** — passionate about turning messy data into meaningful insights. 
From predicting churn to detecting depression signals in tweets, I build projects that combine **data + creativity** to solve real-world problems.
""")

st.markdown("---")

# Projects Section
st.header("🚀 Featured Projects")
for proj in projects:
    with st.expander(proj["title"], expanded=False):
        col1, col2 = st.columns([1,3])
        with col1:
            if proj.get("image"):
                st.image(proj["image"], use_container_width=True)  # ✅ Updated everywhere
        with col2:
            st.write(proj["description"])
            st.write(f"**Tech Stack:** {', '.join(proj['tech'])}")
            st.info(proj["impact"])

# Footer
st.markdown("---")
st.write("© 2025 Rubaisha Munir — Built with ❤️ and Streamlit")

