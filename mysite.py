import streamlit as st
from pathlib import Path

# --- Page Config ---
st.set_page_config(page_title="Manish Shriram | Visual Artist", layout="wide")

# --- Custom CSS for minimal design ---
st.markdown("""
    <style>
    body {
        background-color: black;
        color: white;
        font-family: 'Helvetica Neue', sans-serif;
    }
    /* Hero Video */
    .hero-container {
        position: relative;
        height: 100vh;
        overflow: hidden;
    }
    video.hero-video {
        position: absolute;
        top: 50%;
        left: 50%;
        min-width: 100%;
        min-height: 100%;
        transform: translate(-50%, -50%);
        object-fit: cover;
        z-index: -1;
    }
    /* Overlay text */
    .overlay {
        position: absolute;
        top: 20px;
        left: 40px;
        color: white;
    }
    .overlay h1 {
        font-size: 3rem;
        margin: 0;
    }
    .overlay h2 {
        font-size: 1.2rem;
        font-weight: normal;
        color: #FFD700;
        margin: 5px 0 20px;
    }
    /* Menu links */
    .menu {
        margin-top: 20px;
    }
    .menu a {
        display: block;
        color: white;
        text-decoration: none;
        font-size: 1.2rem;
        margin: 8px 0;
    }
    .menu a:hover {
        color: #FFD700;
    }
    /* Section Headings */
    h2.section {
        margin-top: 60px;
        font-size: 2rem;
        border-bottom: 1px solid #444;
        padding-bottom: 10px;
    }
    /* Edit Grid */
    .grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: 20px;
    }
    .card {
        background: #111;
        padding: 10px;
        border-radius: 10px;
        text-align: center;
    }
    .card img {
        width: 100%;
        border-radius: 10px;
    }
    .play-btn {
        margin-top: 10px;
        background: #222;
        padding: 8px 16px;
        border-radius: 8px;
        color: white;
        cursor: pointer;
        display: inline-block;
    }
    .play-btn:hover {
        background: #FFD700;
        color: black;
    }
    /* Instagram Icon */
    .insta {
        position: fixed;
        bottom: 20px;
        left: 40px;
    }
    .insta a {
        color: white;
        font-size: 1.5rem;
        text-decoration: none;
    }
    </style>
""", unsafe_allow_html=True)

# --- Hero Section ---
st.markdown(f"""
<div class="hero-container">
    <video class="hero-video" autoplay muted loop playsinline>
        <source src="Hero.mp4" type="video/mp4">
    </video>
    <div class="overlay">
        <h1>मनीष श्रीराम</h1>
        <h2>Director | Visual Artist</h2>
        <div class="menu">
            <a href="#edits">Edits</a>
            <a href="#story">Short Story</a>
            <a href="#about">About Me</a>
            <a href="#insta">Instagram</a>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# --- Edits Section ---
st.markdown('<h2 id="edits" class="section">✂️ Amateur Edits</h2>', unsafe_allow_html=True)
st.write("A curated set of small edits — music, frames and memory. Click to play.")

# Example edits (replace thumbnails + links)
edits = [
    {"title": "Edit — 1", "thumb": "https://via.placeholder.com/400x250", "video": "https://youtu.be/bX-XT1kAlh4"},
    {"title": "Edit — 2", "thumb": "https://via.placeholder.com/400x250", "video": "https://youtu.be/bX-XT1kAlh4"},
    {"title": "Edit — 3", "thumb": "https://via.placeholder.com/400x250", "video": "https://youtu.be/bX-XT1kAlh4"},
]

cols = st.columns(len(edits))
for i, edit in enumerate(edits):
    with cols[i]:
        st.image(edit["thumb"], caption=edit["title"])
        if st.button("Play ▶", key=f"play_{i}"):
            st.video(edit["video"])

# --- Short Story ---
st.markdown('<h2 id="story" class="section">📖 Short Story</h2>', unsafe_allow_html=True)
st.write("Here comes your full short story in a clean, cinematic presentation...")

# --- About Me ---
st.markdown('<h2 id="about" class="section">👤 About Me</h2>', unsafe_allow_html=True)
st.write("""
I am Manish Shriram, a visual storyteller, blending films, art, and writing.  
This space is where I share my edits, my short story, and glimpses of my creative journey.
""")

# --- Instagram ---
st.markdown('<h2 id="insta" class="section">📷 Instagram</h2>', unsafe_allow_html=True)
st.write("Follow my journey on Instagram.")
st.markdown('<div class="insta"><a href="https://instagram.com/" target="_blank">📷</a></div>', unsafe_allow_html=True)
