import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Manish's Aesthetic Edits",
    page_icon="🎬",
    layout="centered",
    initial_sidebar_state="auto",
)

# --- 🌼 Custom CSS Styling ---
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
        text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.1);
        animation: fadeInUp 0.8s ease-out;
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
        border-radius: 20px;
        margin-bottom: 3em;
        box-shadow: 0 6px 16px rgba(0, 0, 0, 0.05);
    }
    .rescore-section {
        background: #FDF5E6;
        padding: 2em;
        border-left: 6px solid #F9A825;
        margin-top: 2em;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
    }
    .about-me-box {
        padding: 2rem;
        background: #FFF8E1;
        border-radius: 15px;
        margin: 3rem 0;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.05);
    }
    .about-me-title {
        font-size: 2.2rem;
        margin-bottom: 1.2rem;
        color: #BF360C;
        text-align: center;
    }
    .about-me-text {
        font-size: 1.05rem;
        line-height: 1.8;
        color: #4E342E;
        text-align: justify;
    }
    .music-player {
        position: fixed;
        bottom: 20px;
        right: 20px;
        z-index: 1000;
        cursor: pointer;
    }
    .music-icon {
        width: 50px;
        height: 50px;
        transition: transform 0.3s ease;
    }
    .music-icon.playing {
        animation: pulse 1.5s infinite;
    }
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.1); }
        100% { transform: scale(1); }
    }
    .final-note {
        text-align: center;
        color: #5D4037;
        font-style: italic;
        margin: 2em 0;
    }
    </style>
""", unsafe_allow_html=True)

# --- 🎵 Music Player HTML ---
components.html("""
<div class="music-player" onclick="toggleMusic()">
    <img id="musicIcon" class="music-icon" src="https://img.icons8.com/fluency/96/music.png"/>
</div>

<audio id="backgroundMusic" loop autoplay>
    <source src="https://raw.githubusercontent.com/manishmshriram/My-website/main/lalaland.mp3" type="audio/mpeg">
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

# --- 🎞️ Title & Subtitle ---
st.markdown("<div class='title'>🎞️ My Idiosyncratic Anthology: Songs & Scenes</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Intentional Idiosyncratic Compilation of song and the Scene</div>", unsafe_allow_html=True)

# --- 📺 Video Gallery ---
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
    st.markdown('<div class="video-box">', unsafe_allow_html=True)
    components.iframe(link, height=315)
    st.markdown('</div>', unsafe_allow_html=True)

# --- ✨ Poorly Rescored Section ---
st.markdown("""
<div class="rescore-section">
    <h3 style="color:#6D4C41;">🎼 A Poorly Rescored Oscar-Winning Disney Film</h3>
    <p style="color:#4E342E;">I re-scored Disney's Oscar-winning short <i>Paperman</i> with The Cinematic Orchestra's haunting "Arrival of the Birds", transforming its romance into an ethereal, bittersweet daydream.</p>
</div>
""", unsafe_allow_html=True)

components.iframe("https://www.youtube.com/embed/EI__XUxw8j8?si=PWMbJK7A6a1_ZvoC", height=315)

# --- 👤 About Me Section ---
st.markdown("""
<div class="about-me-box">
    <div class="about-me-title">About Me</div>
    <div class="about-me-text">
        I’ve spent years immersed in films and music, not chasing algorithms or metrics—just feelings. 
        These edits are fragments of a creative chaos, where late-night obsessions met visual poetry.
    </div>
    <div class="about-me-text">
        This space isn't curated for clicks or curated personas. It’s a quiet corner of honesty and 
        aesthetics. If you're here, stay a little. Let the scenes breathe and maybe—feel something.
    </div>
</div>
""", unsafe_allow_html=True)

# --- 🌌 Final Note ---
st.markdown("""
<div class="final-note">
    ◌◌◌ Found this corner? You'll scroll away, overthink, and likely return. <br>
    My presence lingers here - somewhere between the frames and frequencies. ◌◌◌
</div>
""", unsafe_allow_html=True)
