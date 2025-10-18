import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="Manish Shriram", page_icon="🎬", layout="wide")

# --- CSS STYLING ---
st.markdown("""
    <style>
    /* Reset default padding */
    .block-container {padding: 0!important; margin: 0!important;}
    body {margin: 0; padding: 0; overflow-x: hidden; background: black;}

    /* Background video for top section */
    .bg-video {
        position: fixed;
        top: 0; left: 0;
        width: 100%; height: 100%;
        object-fit: cover;
        z-index: -2;
        filter: brightness(40%);
    }

    .overlay {
        position: fixed;
        top: 0; left: 0;
        width: 100%; height: 100%;
        background: linear-gradient(180deg, rgba(0,0,0,0.35), rgba(0,0,0,0.85));
        z-index: -1;
    }

    /* Title */
    .hero {
        height: 100vh;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        text-align: center;
        color: white;
        font-family: 'Poppins', sans-serif;
    }

    /* Font swap on hover (smooth) */
    .hero-name {
        font-size: 4.2em;
        letter-spacing: 2px;
        font-family: 'Playfair Display', serif;
        transition: 0.8s ease-in-out;
        position: relative;
        cursor: pointer;
    }

    .hero-name::after {
        content: "मनीष श्रीराम";
        font-family: 'Noto Sans Devanagari', serif;
        font-size: 4.2em;
        position: absolute;
        top: 0; left: 0;
        color: #f2b531;
        opacity: 0;
        transition: opacity 0.8s ease-in-out;
    }

    .hero-name:hover {
        color: transparent;
    }

    .hero-name:hover::after {
        opacity: 1;
    }

    /* Top-left label */
    .top-left {
        position: absolute;
        top: 25px; left: 35px;
        font-family: 'Poppins', sans-serif;
        font-size: 1.1em;
        color: #dcdcdc;
    }
    .top-left span {
        display: block;
        margin-bottom: 4px;
        transition: 0.3s;
    }
    .top-left span:hover {
        color: #f2b531;
    }

    /* Sections */
    .section {
        min-height: 100vh;
        background: #0a0a0a;
        color: white;
        padding: 5em 2em;
        text-align: center;
    }
    .section h2 {
        color: #f2b531;
        font-family: 'Playfair Display', serif;
        margin-bottom: 1em;
    }
    .section p {
        color: #bdbdbd;
        max-width: 700px;
        margin: 0 auto;
        line-height: 1.6em;
    }

    .insta img {
        width: 40px;
        margin-top: 1.5em;
        filter: brightness(0) invert(1);
        transition: transform 0.3s ease;
    }
    .insta img:hover {
        transform: scale(1.2);
        filter: brightness(0.9) sepia(1) hue-rotate(320deg);
    }
    </style>
""", unsafe_allow_html=True)

# --- BACKGROUND VIDEO ---
st.markdown("""
<video autoplay loop muted playsinline class="bg-video">
    <source src="background.mp4" type="video/mp4">
</video>
<div class="overlay"></div>
""", unsafe_allow_html=True)

# --- HERO SECTION ---
st.markdown("""
<div class="hero">
    <div class="top-left">
        <span>My Edits</span>
        <span>Short Story</span>
    </div>
    <div class="hero-name">Manish Shriram</div>
</div>
""", unsafe_allow_html=True)

# --- SECTIONS BELOW ---
st.markdown("""
<div class="section">
    <h2>My Edits</h2>
    <p>Short cinematic edits where emotion meets frame and silence holds rhythm.</p>
    <iframe width="560" height="315" src="https://www.youtube.com/embed/oMDsZA73fJg" frameborder="0" allowfullscreen></iframe>
</div>

<div class="section">
    <h2>Short Story</h2>
    <p>Read the full story on 
        <a href="https://manishshriram.art.blog/" target="_blank" style="color:#f2b531;">my WordPress</a>.
    </p>
</div>

<div class="section">
    <h2>About Me</h2>
    <p>A storyteller, editor, and dreamer. My work lives in moments – 
    between nostalgia and light. These edits are fragments of my memory reel.</p>

    <div class="insta">
        <a href="https://www.instagram.com/yourprofilelink" target="_blank">
            <img src="https://img.icons8.com/ios-filled/50/ffffff/instagram-new.png" alt="Instagram"/>
        </a>
    </div>
</div>
""", unsafe_allow_html=True)
