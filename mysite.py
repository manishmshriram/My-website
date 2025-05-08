import streamlit as st
import streamlit.components.v1 as components

# --- Page Configuration ---
st.set_page_config(
    page_title="Manish's Aesthetic Edits",
    page_icon="🎬",
    layout="centered"
)

# --- Custom CSS Styling ---
st.markdown("""
<style>
body {
    background-color: #FFF9E5;
    color: #333;
    font-family: 'Helvetica Neue', sans-serif;
    overflow-x: hidden;
}
.title {
    font-size: 3em;
    font-weight: 700;
    text-align: center;
    margin-bottom: 1em;
    color: #F9A825;
}
.subtitle {
    font-size: 1.5em;
    text-align: center;
    margin-bottom: 2em;
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
    transform: scale(1.03);
}
.story-box {
    background: #FFECB3;
    padding: 1.5em;
    border-radius: 15px;
    margin: 3em 0;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}
.about-me-box {
    padding: 2rem;
    background: #FFF8F0;
    border-left: 5px solid #D32F2F;
    border-radius: 10px;
    margin: 2rem 0;
}
.about-me-title {
    font-size: 2.2rem;
    margin-bottom: 1rem;
    color: #D32F2F;
    text-align: center;
}
.about-me-text {
    font-size: 1.1rem;
    line-height: 1.7;
    color: #4E342E;
    margin: 0.8rem 0;
}
.music-player {
    position: fixed;
    top: 20px;
    right: 20px;
    z-index: 1000;
    cursor: pointer;
}
.music-icon {
    width: 40px;
    height: 40px;
    transition: transform 0.3s ease;
}
.music-icon.playing {
    transform: scale(1.1);
}
.final-note {
    text-align: center;
    color: #5D4037;
    font-style: italic;
    margin: 2em 0;
    font-size: 1.1rem;
}
</style>
""", unsafe_allow_html=True)

# --- Working Interactive Music Player ---
components.html("""
<div class="music-player" onclick="toggleMusic()">
    <img id="musicIcon" class="music-icon" src="https://img.icons8.com/fluency/96/music.png" />
</div>
<audio id="backgroundMusic" loop>
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
            audio.play().then(() => {
                icon.classList.add('playing');
            }).catch(e => {
                alert("Click once anywhere on page to enable audio.");
            });
        }
        isPlaying = !isPlaying;
    }
</script>
""", height=0)

# --- Header Section ---
st.markdown("<div class='title'>🎞️ My Idiosyncratic Anthology: Songs & Scenes</div>", unsafe_allow_html=True)
st.markdown('<div class="subtitle">Intentional Idiosyncratic Compilation of Song and Scene</div>', unsafe_allow_html=True)

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

# --- Story Section ---
st.markdown("""
<div class="story-box">
    <div class="about-me-title">A Poorly Rescored Oscar-Winning Disney Film</div>
    <div class="about-me-text">
        I re-scored Disney's Oscar-winning short <i>Paperman</i> with The Cinematic Orchestra's haunting "Arrival of the Birds", 
        transforming its romance into an ethereal, bittersweet daydream.
    </div>
</div>
""", unsafe_allow_html=True)

# --- About Me Section ---
st.markdown("""
<div class="about-me-box">
    <div class="about-me-title">About Me</div>
    <div class="about-me-text">
        I spent years watching films, getting lost in music, and skillfully ignoring career trajectories. These edits? 
        Fragments from a chaotic phase of creating without algorithms, audiences, or "success" in mind.
    </div>
    <div class="about-me-text">
       I know most won't watch this—and that's fine. This isn't a portfolio. It's a memory archive. A mood board of late nights 
        obsessing over frames and feelings, not job titles.
    </div>
    <div class="about-me-text">
        If you're here: welcome to my internet corner. Where nostalgia wears eyeliner and storytelling isn't trying to be deep 
        (but sometimes accidentally is).
    </div>
</div>
""", unsafe_allow_html=True)

# --- Final Note Section ---
st.markdown("""
<div class="final-note">
    ◌◌◌ Found this corner? You'll scroll away, overthink, and likely return. <br>
    My presence lingers here — somewhere between the frames and frequencies. ◌◌◌
</div>
""", unsafe_allow_html=True)
