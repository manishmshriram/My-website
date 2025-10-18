import streamlit as st

# --- PAGE SETUP ---
st.set_page_config(
    page_title="Manish's Site",
    page_icon="🎬",
    layout="wide"
)

# --- BACKGROUND VIDEO & STYLE ---
st.markdown("""
    <style>
    /* Remove default padding and margins */
    .block-container {padding: 0!important; margin: 0!important;}
    body {margin:0; padding:0; overflow-x:hidden;}

    /* Full-screen video background */
    .video-background {
        position: fixed;
        top: 0; left: 0;
        width: 100%; height: 100%;
        object-fit: cover;
        z-index: -1;
        filter: brightness(45%);
    }

    /* Name transition styles */
    .name-container {
        height: 100vh;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        text-align: center;
    }

    .name {
        font-family: 'Playfair Display', serif;
        font-size: 4em;
        color: #f5f5f5;
        font-weight: 600;
        transition: all 0.6s ease-in-out;
    }

    .name:hover {
        content: attr(data-alt);
        color: #f2b531;
    }

    .name:hover::after {
        content: attr(data-alt);
        display: block;
        color: #f2b531;
        font-family: 'Noto Sans Devanagari', serif;
    }

    /* Top-left Nav */
    .top-left {
        position: absolute;
        top: 20px;
        left: 30px;
        font-family: 'Poppins', sans-serif;
        color: #e6e6e6;
        font-size: 1.2em;
        line-height: 1.5em;
        z-index: 3;
    }

    .top-left span {
        display: block;
        cursor: pointer;
        color: #cccccc;
        transition: color 0.3s ease;
    }

    .top-left span:hover {
        color: #f5c518;
    }

    /* Section base */
    .section {
        min-height: 100vh;
        color: #ffffff;
        background-color: #0f0f0f;
        padding: 5em 2em;
        text-align: center;
    }

    .section-title {
        font-size: 2em;
        color: #f2b531;
        margin-bottom: 1.2em;
        font-weight: bold;
    }

    .section-text {
        font-size: 1.1em;
        color: #ccc;
        line-height: 1.6;
        max-width: 700px;
        margin: 0 auto 2em auto;
    }

    /* Instagram icon */
    .insta {
        margin-top: 2em;
    }

    .insta img {
        width: 40px;
        transition: transform 0.3s ease;
        filter: brightness(0) invert(1);
    }

    .insta img:hover {
        transform: scale(1.2);
        filter: brightness(0.8) invert(0.9) sepia(1) hue-rotate(320deg);
    }

    </style>
""", unsafe_allow_html=True)

# --- BACKGROUND VIDEO (replace with your file or url) ---
st.markdown("""
<video autoplay loop muted playsinline class="video-background">
    <source src="background.mp4" type="video/mp4">
</video>
""", unsafe_allow_html=True)

# --- MAIN NAME + HOVER EFFECT ---
st.markdown("""
<div class="name-container">
    <div class="top-left">
        <span>My Edits</span>
        <span><a href="#short-story" style="text-decoration:none; color:inherit;">Short Story</a></span>
    </div>
    <div class="name" data-alt="मनीष श्रीराम">Manish Shriram</div>
</div>
""", unsafe_allow_html=True)

# --- EDITS SECTION ---
st.markdown("""
<div id="edits" class="section">
    <div class="section-title">My Edits</div>
    <div class="section-text">Short cinematic edits blending visuals with emotional resonance.</div>
    <iframe width="560" height="315" src="https://www.youtube.com/embed/oMDsZA73fJg" 
            frameborder="0" allowfullscreen></iframe>
</div>
""", unsafe_allow_html=True)

# --- SHORT STORY SECTION ---
st.markdown("""
<div id="short-story" class="section">
    <div class="section-title">Short Story</div>
    <div class="section-text">
        Read my short story <a href="https://manishshriram.art.blog/" target="_blank" style="color:#f2b531;">here</a>.
    </div>
</div>
""", unsafe_allow_html=True)

# --- ABOUT ME SECTION ---
st.markdown("""
<div class="section">
    <div class="section-title">About Me</div>
    <div class="section-text">
        A storyteller lost between frames and frequencies. I edit not for clients, but for catharsis.
    </div>
</div>
""", unsafe_allow_html=True)

# --- INSTAGRAM ICON ---
st.markdown("""
<div class="section">
    <div class="section-title">Connect</div>
    <div class="insta">
        <a href="https://www.instagram.com/yourprofilelink" target="_blank">
            <img src="https://img.icons8.com/ios-filled/50/ffffff/instagram-new.png" alt="Instagram"/>
        </a>
    </div>
</div>
""", unsafe_allow_html=True)
