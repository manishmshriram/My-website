import streamlit as st
from streamlit.components.v1 import html

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="Manish Shriram",
    layout="wide",
)

# ------------------ DATA ------------------
video_links = [
    "https://www.youtube.com/embed/oMDsZA73fJg",
    "https://www.youtube.com/embed/NNHJxvZxyoM",
    "https://www.youtube.com/embed/gs80fqMsU6M",
    "https://www.youtube.com/embed/OFvm21z8L-M",
    "https://www.youtube.com/embed/o4XQkw0k5To",
    "https://www.youtube.com/embed/ZUhU4izZbi0",
    "https://www.youtube.com/embed/wDzCeqzgmoA",
    "https://www.youtube.com/embed/PPOYOUFk4Hw",
    "https://www.youtube.com/embed/WAsDEw1HKG4",
    "https://www.youtube.com/embed/y6JbWgHx7po",
    "https://www.youtube.com/embed/aNFGiVwt4uE",
]

# ------------------ GLOBAL CSS ------------------
st.markdown("""
<style>
html, body {
    background-color: #0c0c0c;
    color: #e6c56f;
    font-family: Inter, sans-serif;
}

/* Remove Streamlit clutter */
#MainMenu, footer, header {
    visibility: hidden;
}

/* Name */
.name {
    margin-top: 40px;
    margin-left: 40px;
    font-size: 24px;
    font-weight: 500;
}
.name a {
    color: #e6c56f;
    text-decoration: none;
}
.name a:hover {
    opacity: 0.7;
}

/* Section spacing */
.section {
    max-width: 1100px;
    margin: 120px auto;
    padding: 0 24px;
}

.section-title {
    font-size: 32px;
    margin-bottom: 32px;
}

/* Edits grid */
.video-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
    gap: 28px;
}
.video-grid iframe {
    width: 100%;
    height: 200px;
    border-radius: 6px;
}

/* Story */
.story-preview iframe {
    width: 100%;
    height: 800px;
    border: none;
    border-radius: 8px;
}

/* About */
.about {
    display: flex;
    gap: 40px;
    flex-wrap: wrap;
}
.about img {
    width: 220px;
    border-radius: 6px;
}
.about-text {
    max-width: 520px;
    font-size: 17px;
    line-height: 1.7;
}

/* Mobile */
@media (max-width: 768px) {
    .section-title {
        font-size: 26px;
    }
    .video-grid iframe {
        height: 190px;
    }
}
</style>
""", unsafe_allow_html=True)

# ------------------ NAME (LINKED TO STORY) ------------------
st.markdown("""
<div class="name">
    <a href="https://manishshriram.art.blog/" target="_blank">
        Manish Shriram
    </a>
</div>
""", unsafe_allow_html=True)

# ================== EDITS ==================
st.markdown("<div class='section'>", unsafe_allow_html=True)
st.markdown("<div class='section-title'>Edits</div>", unsafe_allow_html=True)

st.markdown("<div class='video-grid'>", unsafe_allow_html=True)
for v in video_links:
    st.markdown(
        f"<iframe src='{v}' frameborder='0' allowfullscreen></iframe>",
        unsafe_allow_html=True
    )
st.markdown("</div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# ================== SHORT STORY ==================
st.markdown("<div class='section'>", unsafe_allow_html=True)

st.markdown("""
<div class="section-title">
    <a href="https://manishshriram.art.blog/" target="_blank"
       style="color:#e6c56f; text-decoration:none;">
        100th Night
    </a>
</div>
""", unsafe_allow_html=True)

html("""
<div class="story-preview">
    <iframe src="https://manishshriram.art.blog/"></iframe>
</div>
""")

st.markdown("</div>", unsafe_allow_html=True)

# ================== ABOUT ME ==================
st.markdown("<div class='section'>", unsafe_allow_html=True)
st.markdown("<div class='section-title'>About Me</div>", unsafe_allow_html=True)

st.markdown("""
<div class="about">
    <img src="https://via.placeholder.com/400">
    <div class="about-text">
        <p>Welcome to my corner of the internet.</p>
        <p>
        A storyteller, editor, and dreamer. My work lives in moments –
        between nostalgia and light. These edits are fragments of my memory reel.
        </p>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
