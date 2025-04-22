import streamlit as st
import streamlit.components.v1 as components

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
        overflow-x: hidden;
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
        color: #FF6F00;
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
        animation: glowing 1.5s ease-in-out infinite;
    }
    @keyframes glowing {
        0% { color: #D32F2F; text-shadow: 0 0 5px #FF0000, 0 0 10px #FF0000, 0 0 15px #FF0000; }
        50% { color: #FF5733; text-shadow: 0 0 5px #FF5733, 0 0 10px #FF5733, 0 0 15px #FF5733; }
        100% { color: #D32F2F; text-shadow: 0 0 5px #FF0000, 0 0 10px #FF0000, 0 0 15px #FF0000; }
    }
    .cta-box {
        text-align: center;
        font-size: 1.2em;
        margin-top: 3em;
        font-style: italic;
        color: #9E9D24;
        font-family: 'Courier New', Courier, monospace;
    }
    .cta-box:hover {
        color: #F57F17;
        cursor: pointer;
    }
    .transition {
        animation: fadeIn 2s ease-out;
    }
    @keyframes fadeIn {
        0% {
            opacity: 0;
        }
        100% {
            opacity: 1;
        }
    }
    .footer {
        font-size: 0.9em;
        color: #999;
        text-align: center;
        margin-top: 3em;
    }
    .cta-box {
        color: #D32F2F;
        font-style: italic;
        text-align: center;
        font-family: 'Courier New', Courier, monospace;
        font-size: 1.5em;
    }
    .cta-box:hover {
        color: #F57F17;
    }
    </style>
""", unsafe_allow_html=True)

# --- 🎞️ Title ---
st.markdown("<div class='title'>🎞️ Manish's Aesthetic Edits</div>", unsafe_allow_html=True)
st.markdown('<div class="subtitle">Soft, minimal edits of your favorite films and music</div>', unsafe_allow_html=True)

# --- 🎶 Audio Play/Pause Button ---
audio_url = "https://raw.githubusercontent.com/manishmshriram/My-website/main/lalaland.mp3"
st.markdown(f'<audio id="bgMusic" loop preload="auto" style="display:none;"><source src="{audio_url}" type="audio/mp3"></audio>', unsafe_allow_html=True)

st.markdown("""
<div style="text-align: center;">
    <button onclick="document.getElementById('bgMusic').play()">▶️ Play Music</button>
    <button onclick="document.getElementById('bgMusic').pause()">⏸️ Pause Music</button>
</div>
""", unsafe_allow_html=True)

# --- 📺 Display All YouTube Videos (10 Links) ---
video_links = [
    "https://www.youtube.com/embed/NNHJxvZxyoM?si=kcdUKDzW4Vk9cesv",
    "https://www.youtube.com/embed/oMDsZA73fJg?si=OtOy4C5yqhVqao6B",
    "https://www.youtube.com/embed/gs80fqMsU6M?si=sLRJacQA3CKUhTvG",
    "https://www.youtube.com/embed/OFvm21z8L-M?si=qrNKyNoF18leLjV1",
    "https://www.youtube.com/embed/o4XQkw0k5To?si=QWF7bE4sSozl5WG6",
    "https://www.youtube.com/embed/ZUhU4izZbi0?si=BIe30AuRAc5Xg2rL",
    "https://www.youtube.com/embed/wDzCeqzgmoA?si=PU97w3lVOss9w9sO",
    "https://www.youtube.com/embed/PPOYOUFk4Hw?si=RlBSKyqUT7Ud130L",
    "https://www.youtube.com/embed/WAsDEw1HKG4?si=TquTCxRYWOuArz7b",
    "https://www.youtube.com/embed/y6JbWgHx7po?si=POQlGXMWfEJUJPR3",
    "https://www.youtube.com/embed/aNFGiVwt4uE?si=GvQ5ro2-0tZSIs51"
]

for link in video_links:
    st.markdown('<div class="video-box transition">', unsafe_allow_html=True)
    components.iframe(link, height=315)
    st.markdown('</div>', unsafe_allow_html=True)

# --- 🔗 Link to YouTube Channel ---
st.markdown("""
<div style='text-align:center; margin-top:2em;' class="transition">
    🔗 Explore more on my YouTube Channel: <a href="https://www.youtube.com/@manishshriram" target="_blank">Manish Shriram on YouTube</a>
</div>
""", unsafe_allow_html=True)

# --- 🎬 "Poorly Rescored" Disney Film ---
st.markdown('<div class="story-box transition">', unsafe_allow_html=True)
st.markdown('<div class="story-title">A Poorly Rescored Oscar-Winning Disney Film</div>', unsafe_allow_html=True)
st.markdown("""
<div class="story-text">
    I've edited the Oscar-winning short *Paperman* and added one of my favorite tracks, "Arrival of the Birds" by The Cinematic Orchestra. Just a small edit to give the film a fresh feel with this beautiful piece of music.
</div>
""", unsafe_allow_html=True)
st.markdown('<div style="text-align:center;">', unsafe_allow_html=True)
components.iframe("https://www.youtube.com/embed/EI__XUxw8j8?si=tWWDaBgCvtU5QCJx", height=315)
st.markdown('</div>', unsafe_allow_html=True)

# --- ✍️ Short Story Section with Link ---
st.markdown('<div class="story-box transition" style="background-color: #FFEB3B;">', unsafe_allow_html=True)
st.markdown('<div class="story-title">My Short Story</div>', unsafe_allow_html=True)
st.markdown("""
<div class="story-text">
    Click below to read my short story and immerse yourself in a creative journey through words.
</div>
""", unsafe_allow_html=True)
st.markdown('<div class="cta-box transition"><a href="https://manishshriramart.blog" target="_blank">🔗 Read My Short Story</a></div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- 💡 About Me Section ---
st.markdown('<div class="about-me-box transition">', unsafe_allow_html=True)
st.markdown('<div class="about-me-title glowing-text">About Me</div>', unsafe_allow_html=True)
st.markdown("""
<div class="about-me-text glowing-text">
    I spent years watching films, getting lost in music, and skillfully ignoring any form of career trajectory. These edits? They're fragments from that beautifully chaotic phase where I made stuff without thinking about algorithms, audiences, or "success."
</div>
""", unsafe_allow_html=True)
st.markdown("""
<div class="about-me-text glowing-text">
    I know most people won’t watch this—and that’s fine. This isn’t some grand portfolio. It’s a memory archive. A mood board of my mind. An echo of late nights spent obsessing over frames and feelings instead of job titles.
</div>
""", unsafe_allow_html=True)
st.markdown("""
<div class="about-me-text glowing-text">
    If you’re here, watching—cool. You’re part of this little accidental time capsule now. Welcome to my personal corner of the internet, where nostalgia wears eyeliner and storytelling doesn’t try too hard to be deep (but sometimes accidentally is).
</div>
""", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# --- 📝 Footer ---
st.markdown("""
<div class="footer transition">
    Designed and created with love by <a href="https://manishshriramart.streamlit.app/" target="_blank">Manish Shriram</a>
</div>
""", unsafe_allow_html=True)

# --- Final Note ---
st.markdown("""
<div class="footer transition" style="color: #FF4081;">
    Found this corner of the internet? You’ll scroll back to Instagram, overthink, and probably end up here again. My presence lives here — somewhere between the lines.
</div>
""", unsafe_allow_html=True)
