import streamlit as st
import streamlit.components.v1 as components

# Page setup
st.set_page_config(
    page_title="Manish's Aesthetic Edits",
    page_icon="🎬",
    layout="centered",
)

# --- CSS Styling ---
st.markdown("""
    <style>
    body {
        background-color: #FFF9E5;
        font-family: 'Helvetica Neue', sans-serif;
        color: #333;
        overflow-x: hidden;
    }
    .title {
        font-size: 3em;
        text-align: center;
        color: #F9A825;
        font-weight: bold;
        margin-top: 1em;
        margin-bottom: 0.2em;
    }
    .subtitle {
        font-size: 1.3em;
        text-align: center;
        color: #5D4037;
        margin-bottom: 3em;
    }
    .video-box {
        background: #FFF3C7;
        padding: 1.5em;
        border-radius: 20px;
        margin-bottom: 2.5em;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        transition: transform 0.3s ease-in-out;
    }
    .video-box:hover {
        transform: scale(1.02);
    }
    .section-box {
        background: #FFF3E0;
        padding: 2em;
        border-radius: 15px;
        margin: 2.5em 0;
        box-shadow: 0 6px 18px rgba(0,0,0,0.08);
    }
    .section-title {
        font-size: 1.8em;
        color: #BF360C;
        text-align: center;
        margin-bottom: 1em;
        font-weight: 600;
    }
    .section-text {
        font-size: 1.1em;
        line-height: 1.7;
        color: #4E342E;
        text-align: center;
    }
    .about-me-text {
        font-size: 1.1rem;
        color: #5D4037;
        line-height: 1.8;
        text-align: center;
        margin-top: 1rem;
    }
    .final-note {
        text-align: center;
        color: #5D4037;
        font-style: italic;
        margin: 3em 0;
    }
    .music-player {
        position: fixed;
        top: 20px;
        right: 20px;
        z-index: 999;
        cursor: pointer;
    }
    .music-icon {
        width: 40px;
        height: 40px;
        transition: transform 0.3s ease;
        filter: drop-shadow(0 2px 5px rgba(0,0,0,0.2));
    }
    .music-icon.playing {
        animation: pulse 1.5s infinite;
    }
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.1); }
        100% { transform: scale(1); }
    }
    </style>
""", unsafe_allow_html=True)

# --- 🎵 Music Player ---
components.html("""
<div class="music-player" onclick="toggleMusic()">
    <img id="musicIcon" class="music-icon" src="https://img.icons8.com/fluency/96/music.png"/>
</div>

<audio id="backgroundMusic" loop>
    <source src="/static/lalaland.mp3" type="audio/mpeg">
</audio>

<script>
let isPlaying = false;
const audio = document.getElementById('backgroundMusic');
const icon = document.getElementById('musicIcon');

function toggleMusic() {
    if (isPlaying) {
        audio.pause();
        icon.classList.remove('playing');
    } else {
        audio.play().catch(() => {
            alert('Click anywhere on the page first to enable audio');
        });
        icon.classList.add('playing');
    }
    isPlaying = !isPlaying;
}
</script>
""", height=0)

# --- Header ---
st.markdown("<div class='title'>🎞️ My Idiosyncratic Anthology: Songs & Scenes</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Intentional Idiosyncratic Compilation of song and the Scene</div>", unsafe_allow_html=True)

# --- Video Gallery ---
video_links = [
    "https://www.youtube.com/embed/oMDsZA73fJg?si=OtOy4C5yqhVqao6B",
    "https://www.youtube.com/embed/NNHJxvZxyoM?si=kcdUKDzW4Vk9cesv",
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
    with st.container():
        st.markdown('<div class="video-box">', unsafe_allow_html=True)
        components.iframe(link, height=315)
        st.markdown('</div>', unsafe_allow_html=True)

# --- Poorly Rescored Section ---
st.markdown("""
<div class="section-box">
    <div class="section-title">A Poorly Rescored Oscar-Winning Disney Film</div>
    <div class="section-text">
        I re-scored Disney's Oscar-winning short <i>Paperman</i> with The Cinematic Orchestra's haunting 
        <b>"Arrival of the Birds"</b>, transforming its romance into an ethereal, bittersweet daydream.
    </div><br>
    <div style='text-align: center;'>
        <iframe width="560" height="315" src="https://www.youtube.com/embed/EI__XUxw8j8?si=PWMbJK7A6a1_ZvoC" 
        frameborder="0" allowfullscreen></iframe>
    </div>
</div>
""", unsafe_allow_html=True)

# --- About Me Section ---
st.markdown("""
<div class="section-box">
    <div class="section-title">About Me</div>
    <div class="about-me-text">
        I’ve spent years getting lost in frames, melodies, and midnight edits. These clips aren’t for jobs, clicks, or clout — 
        they’re stitched memories, felt deeply and shared freely.
    </div>
    <div class="about-me-text">
        I know most won’t watch — and that’s okay. This isn’t a portfolio; it’s a private theater with an open door.
    </div>
    <div class="about-me-text">
        Welcome to my corner of the internet — a place where nostalgia wears eyeliner and storytelling forgets to explain itself.
    </div>
</div>
""", unsafe_allow_html=True)

# --- Final Note ---
st.markdown("""
<div class="final-note">
    ◌◌◌ Found this corner? You’ll scroll away, overthink, and likely return. <br>
    My presence lingers here — somewhere between the frames and frequencies. ◌◌◌
</div>
""", unsafe_allow_html=True)
