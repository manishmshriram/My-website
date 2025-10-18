import streamlit as st

# ---------- CONFIG ----------
st.set_page_config(page_title="Manish Shriram", layout="wide", page_icon="🎬")

# ---------- LINKS & MEDIA ----------
BACKGROUND_IMAGE = "https://drive.google.com/uc?export=view&id=1boW3ZgpXPH__2hSF2qA-2pQT31JoyZVw"
WORDPRESS_LINK = "https://manishshriram.art.blog/"
INSTAGRAM_LINK = "https://instagram.com/"  # update later
YOUTUBE_LINKS = [
    "https://www.youtube.com/embed/3p9H3gZtD98",
    "https://www.youtube.com/embed/dQw4w9WgXcQ",
]

# ---------- CSS STYLING ----------
st.markdown(
    f"""
    <style>
    /* Import fonts */
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600&family=Poppins:wght@300;400&display=swap');

    html, body, [class*="stApp"] {{
        height: 100%;
        margin: 0;
        background-color: #000;
        color: #fff;
        font-family: 'Poppins', sans-serif;
        scroll-behavior: smooth;
        overflow-x: hidden;
    }}

    /* Background image styling */
    .bg-container {{
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100vh;
        z-index: -1;
        background: url('{BACKGROUND_IMAGE}') no-repeat center center/cover;
        filter: brightness(0.35);
    }}

    /* Overlay fade */
    .overlay {{
        position: absolute;
        top: 0; left: 0;
        width: 100%;
        height: 100vh;
        background: rgba(0,0,0,0.55);
        z-index: -1;
    }}

    /* Cinematic fade-in animation */
    @keyframes fadeIn {{
        from {{ opacity: 0; transform: translateY(20px); }}
        to {{ opacity: 1; transform: translateY(0); }}
    }}

    /* Name styling and Marathi hover transition */
    .main-name {{
        font-family: 'Playfair Display', serif;
        font-size: 4.5vw;
        text-align: center;
        position: relative;
        margin-top: 40vh;
        animation: fadeIn 2s ease-out forwards;
        color: #fff;
        cursor: pointer;
    }}
    .main-name::after {{
        content: "मनीष श्रीराम";
        position: absolute;
        left: 0; right: 0;
        top: 0;
        opacity: 0;
        transition: opacity 1s ease;
        font-family: 'Noto Serif Devanagari', serif;
    }}
    .main-name:hover::after {{
        opacity: 1;
    }}
    .main-name:hover {{
        color: rgba(255,255,255,0);
    }}

    /* Top-left labels */
    .top-labels {{
        position: absolute;
        top: 3vh;
        left: 3vw;
        font-size: 1rem;
        font-family: 'Poppins', sans-serif;
        animation: fadeIn 3s ease;
    }}
    .top-labels a {{
        display: block;
        color: #ddd;
        text-decoration: none;
        margin-bottom: 8px;
        transition: color 0.3s ease;
    }}
    .top-labels a:hover {{
        color: #fff;
    }}

    /* Section styling */
    .section {{
        padding: 10vh 10vw;
        text-align: center;
        animation: fadeIn 2s ease;
    }}
    .section h2 {{
        font-family: 'Playfair Display', serif;
        font-size: 2rem;
        margin-bottom: 1rem;
    }}
    .section p {{
        font-size: 1rem;
        max-width: 600px;
        margin: auto;
        color: #ccc;
    }}

    /* YouTube grid */
    .video-grid {{
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 2rem;
        margin-top: 3rem;
    }}
    .video-grid iframe {{
        width: 400px;
        height: 225px;
        border: none;
        border-radius: 10px;
        box-shadow: 0 0 20px rgba(255,255,255,0.1);
        transition: transform 0.5s ease;
    }}
    .video-grid iframe:hover {{
        transform: scale(1.05);
    }}

    /* Button */
    .story-button {{
        background: none;
        border: 1px solid #fff;
        color: #fff;
        padding: 0.6rem 1.2rem;
        margin-top: 1.5rem;
        text-decoration: none;
        border-radius: 25px;
        transition: all 0.3s ease;
    }}
    .story-button:hover {{
        background: #fff;
        color: #000;
    }}

    /* Instagram icon */
    .insta {{
        margin-top: 4rem;
    }}
    .insta a {{
        color: #fff;
        font-size: 2rem;
        transition: text-shadow 0.4s ease;
    }}
    .insta a:hover {{
        text-shadow: 0 0 10px #fff;
    }}

    /* Responsive */
    @media (max-width: 768px) {{
        .main-name {{
            font-size: 8vw;
            margin-top: 45vh;
        }}
        .video-grid iframe {{
            width: 90vw;
            height: 200px;
        }}
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------- HTML STRUCTURE ----------
st.markdown(
    f"""
    <div class="bg-container"></div>
    <div class="overlay"></div>

    <div class="top-labels">
        <a href="#edits">My Edits</a>
        <a href="#story">Short Story</a>
    </div>

    <div class="main-name">Manish Shriram</div>

    <div class="section" id="edits">
        <h2>My Edits</h2>
        <div class="video-grid">
            {''.join([f'<iframe src="{link}" allowfullscreen></iframe>' for link in YOUTUBE_LINKS])}
        </div>
    </div>

    <div class="section" id="story">
        <h2>Short Story</h2>
        <p>"Ek Sauvi Raat" — a cinematic monologue blending humor, emotion, and philosophy.</p>
        <a href="{WORDPRESS_LINK}" target="_blank" class="story-button">Read the Story</a>
    </div>

    <div class="section" id="about">
        <h2>About Me</h2>
        <p>I’m Manish — a storyteller, aesthetic editor, and lover of cinematic rhythm. My work blends emotion with visual poetry.</p>
        <div class="insta">
            <a href="{INSTAGRAM_LINK}" target="_blank">📸</a>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)
