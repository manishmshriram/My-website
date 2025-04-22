import streamlit as st
import streamlit.components.v1 as components
import requests

# Set page configuration
st.set_page_config(
    page_title="Manish's Aesthetic Edits",
    page_icon="🎬",
    layout="centered",
    initial_sidebar_state="auto",
)

# --- 🎨 Custom CSS for Aesthetic Vibe ---
st.markdown("""
    <style>
    body {
        background-color: #FFF9E5;
        color: #333333;
        font-family: 'Helvetica Neue', sans-serif;
    }
    .title {
        font-size: 3em;
        font-weight: 700;
        text-align: center;
        margin-bottom: 1em;
        color: #F9A825;
        text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.3);
    }
    .subtitle {
        font-size: 1.5em;
        text-align: center;
        margin-bottom: 3em;
        color: #5D4037;
    }
    .video-box {
        background: #FFF3C7;
        padding: 1.5em;
        border-radius: 25px;
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
        margin-bottom: 3em;
        transition: transform 0.3s ease-in-out;
    }
    .video-box:hover {
        transform: scale(1.05);
    }
    .story-box {
        background: #FFECB3;
        padding: 1.5em;
        border-radius: 15px;
        margin-top: 3em;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    }
    .story-title {
        font-size: 2.5em;
        font-weight: 700;
        color: #6A1B9A;
        text-align: center;
        margin-bottom: 1em;
    }
    .story-text {
        font-size: 1.2em;
        color: #4E342E;
        line-height: 1.8;
        text-align: justify;
        max-width: 80%;
        margin-left: auto;
        margin-right: auto;
    }
    .about-me-box {
        background: #FFEBEE;
        padding: 2em;
        border-radius: 15px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        margin-top: 3em;
    }
    .about-me-title {
        font-size: 2.5em;
        font-weight: 700;
        color: #D32F2F;
        text-align: center;
        margin-bottom: 1em;
    }
    .about-me-text {
        font-size: 1.2em;
        color: #4E342E;
        line-height: 1.8;
        text-align: justify;
    }
    </style>
""", unsafe_allow_html=True)

# --- 🎞️ Title ---
st.markdown("<div class='title'>🎞️ Manish's Aesthetic Edits</div>", unsafe_allow_html=True)
st.markdown('<div class="subtitle">Soft, minimal edits of your favorite films and music</div>', unsafe_allow_html=True)

# --- 🎶 Background Music from GitHub ---
st.markdown("#### Background Music: *City of Stars - Instrumental* 🎵")
audio_url = "https://raw.githubusercontent.com/manishmshriram/My-website/main/lalaland.mp3"
try:
    audio_bytes = requests.get(audio_url).content
    st.audio(audio_bytes, format="audio/mp3")
except:
    st.warning("Couldn't load background music. Please check the link.")

# --- 📺 Your YouTube Video Embeds ---
video_links = [
    "https://www.youtube.com/embed/oMDsZA73fJg?si=tKgC-NLJK2nH-D_l",
    "https://www.youtube.com/embed/oMDsZA73fJg?si=2Z_C95B7Z9gegmMn",
    "https://www.youtube.com/embed/OOFqwoGpQZY?si=oRrG6iJ80pp8EUIv",
    "https://www.youtube.com/embed/aNFGiVwt4uE?si=sgbrqyBvK2-BpOHj"
]

for link in video_links:
    st.markdown('<div class="video-box">', unsafe_allow_html=True)
    components.iframe(link, height=315)
    st.markdown('</div>', unsafe_allow_html=True)

# --- 📺 Link to YouTube Channel ---
st.markdown("""
<div style='text-align:center; margin-top:2em;'>
    🔗 Visit my YouTube Channel: <a href="https://www.youtube.com/@manishshriram" target="_blank">Manish Shriram on YouTube</a>
</div>
""", unsafe_allow_html=True)

# --- ✍️ Short Story Section ---
st.markdown('<div class="story-box">', unsafe_allow_html=True)
st.markdown('<div class="story-title">My Short Story</div>', unsafe_allow_html=True)
st.markdown("""
<div class="story-text">
I’m someone who spent way too much time watching films, listening to music, and ignoring career goals—now I’m putting all that mess to use. 
These videos are special to me; they’re like a nostalgic reminder of the days I created without worrying about ‘being productive.’ 
Now, I’m finally sharing it all in one place—because why not turn my procrastination into something vaguely resembling a portfolio?
</div>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- 📝 Blog Link ---
st.markdown("""
<div style="text-align:center; margin-top: 3em;">
    📖 Read more on my Blog: <a href="https://manish.shriram.art.blog" target="_blank">manish.shriram.art.blog</a>
</div>
""", unsafe_allow_html=True)

# --- 💬 Comment Placeholder (optional Disqus link can go here) ---
st.markdown("""
<hr>
<div style='text-align:center; font-size: 1.1em; margin-top: 2em;'>
💬 Comments are welcome—just make sure they’re almost as good as this content.
</div>
""", unsafe_allow_html=True)

# --- 👣 Footer ---
st.markdown("""
    <hr>
    <div style='text-align:center; font-size: 0.9em; color: #999;'>
        © 2025 Manish Shriram | Aesthetic Edits
    </div>
""", unsafe_allow_html=True)
