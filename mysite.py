import streamlit as st
import streamlit.components.v1 as components

# --- Page Setup ---
st.set_page_config(
    page_title="Manish's Aesthetic Edits",
    page_icon="🎬",
    layout="centered",
)

# --- Sidebar Navigation ---
section = st.sidebar.radio("📂 Navigate", [
    "Short Story",
    "My Edits",
    "About Me"
])

st.sidebar.markdown("---")
st.sidebar.markdown("📸 [Instagram](https://www.instagram.com/yourprofilelink)", unsafe_allow_html=True)

# --- Custom Dark Styling ---
st.markdown("""
    <style>
    body {
        background-color: #0f0f0f;
        color: #f5f5f5;
        font-family: 'Helvetica Neue', sans-serif;
    }
    .title {
        font-size: 2.8em;
        text-align: center;
        color: #E5C07B;
        font-weight: bold;
        margin-top: 1em;
    }
    .subtitle {
        font-size: 1.2em;
        text-align: center;
        color: #abb2bf;
        margin-bottom: 2em;
    }
    .video-box {
        background: #1e1e1e;
        padding: 1.5em;
        border-radius: 15px;
        margin-bottom: 2em;
        box-shadow: 0 4px 12px rgba(0,0,0,0.2);
    }
    .section-box {
        background: #1a1a1a;
        padding: 2em;
        border-radius: 15px;
        margin: 2em 0;
    }
    .section-title {
        font-size: 1.6em;
        color: #E06C75;
        text-align: center;
        margin-bottom: 1em;
        font-weight: bold;
    }
    .section-text, .about-me-text {
        font-size: 1.1em;
        line-height: 1.6;
        color: #c0c0c0;
        text-align: center;
    }
    .final-note {
        text-align: center;
        color: #5c6370;
        font-style: italic;
        margin: 3em 0;
    }
    </style>
""", unsafe_allow_html=True)

# --- Main Sections ---
if section == "Short Story":
    st.markdown("<div class='title'>📝 Ek Sauvi Raat (The 100th Night)</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>A theatrical monologue in Hinglish — emotional, absurd, poetic</div>", unsafe_allow_html=True)

    st.markdown("""
    <div class='section-box'>
    <div class='section-title'>The Frog Who Dreamt of the Sky</div>
    <div class='section-text'>
        Ek raat… ek talaab… ek main-da, jise sapne sirf chand ke dikhte the.<br><br>
        This is a tale of a poetic frog, a mysterious she-frog, a soldier, a tortoise, and the 100th night that changed everything.
        It's absurd, emotional, and nostalgic — just like life.
    </div>
    </div>
    """, unsafe_allow_html=True)

elif section == "My Edits":
    st.markdown("<div class='title'>🎞️ My Idiosyncratic Anthology</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>Cinematic music meets unforgettable frames</div>", unsafe_allow_html=True)

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

    st.markdown("""
    <div class="section-box">
        <div class="section-title">🎬 A Poorly Rescored Oscar-Winning Disney Film</div>
        <div class="section-text">
            I re-scored Disney's Oscar-winning short <i>Paperman</i> with The Cinematic Orchestra’s haunting 
            <b>“Arrival of the Birds”</b>, transforming its romance into an ethereal, bittersweet daydream.
        </div><br>
        <div style='text-align: center;'>
            <iframe width="560" height="315" src="https://www.youtube.com/embed/EI__XUxw8j8?si=PWMbJK7A6a1_ZvoC" 
            frameborder="0" allowfullscreen></iframe>
        </div>
    </div>
    """, unsafe_allow_html=True)

elif section == "About Me":
    st.markdown("<div class='title'>👤 About Me</div>", unsafe_allow_html=True)

    st.markdown("""
    <div class="section-box">
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
    <div class="final-note">
        ◌◌◌ You’ll scroll away, overthink, and likely return.<br>
        My presence lingers here — somewhere between the frames and frequencies. ◌◌◌
    </div>
    """, unsafe_allow_html=True)
