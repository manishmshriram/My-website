import streamlit as st
from streamlit.components.v1 import html

st.set_page_config(
    page_title="Manish Shriram",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# -------------------- VIDEO LINKS --------------------
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

# -------------------- GLOBAL CSS --------------------
st.markdown("""
<style>
html, body {
    background-color: #0e0e0e;
    color: #e6c56f;
    font-family: 'Inter', sans-serif;
    overflow-x: hidden;
}

a {
    text-decoration: none;
    color: #e6c56f;
}

section {
    animation: fadeIn 0.9s ease-in-out;
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(10px);}
    to { opacity: 1; transform: translateY(0);}
}

/* Background Video */
#bg-video {
    position: fixed;
    top: 0;
    left: 0;
    min-width: 100%;
    min-height: 100%;
    object-fit: cover;
    z-index: -2;
    filter: brightness(0.55);
}

/* Overlay */
.overlay {
    position: fixed;
    inset: 0;
    background: rgba(0,0,0,0.35);
    z-index: -1;
}

/* Name Hover */
.name {
    position: fixed;
    top: 30px;
    right: 40px;
    font-size: 26px;
    font-weight: 500;
    cursor: pointer;
}

.name span {
    transition: opacity 0.4s ease;
}

.name .dev {
    position: absolute;
    opacity: 0;
}

.name:hover .eng {
    opacity: 0;
}

.name:hover .dev {
    opacity: 1;
}

/* Left Menu */
.menu {
    position: fixed;
    top: 40%;
    left: 40px;
    display: flex;
    flex-direction: column;
    gap: 18px;
    font-size: 18px;
}

.menu a:hover {
    opacity: 0.7;
}

/* Video Grid */
.grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
    gap: 20px;
}

.video iframe {
    width: 100%;
    height: 200px;
    border-radius: 8px;
    transition: transform 0.4s ease;
}

.video iframe:hover {
    transform: scale(1.05);
}

/* About */
.about {
    max-width: 700px;
    font-size: 18px;
    line-height: 1.7;
}

.about img {
    width: 200px;
    border-radius: 50%;
    margin-bottom: 20px;
}

/* Mobile */
@media (max-width: 768px) {
    .menu {
        top: auto;
        bottom: 30px;
        left: 20px;
        flex-direction: row;
        gap: 14px;
        font-size: 14px;
    }

    .name {
        font-size: 18px;
        right: 20px;
    }
}
</style>
""", unsafe_allow_html=True)

# -------------------- BACKGROUND VIDEO --------------------
html("""
<video autoplay muted loop id="bg-video">
    <source src="background.mp4" type="video/mp4">
</video>
<div class="overlay"></div>
""", height=0)

# -------------------- NAME (TOP RIGHT) --------------------
html("""
<div class="name">
    <span class="eng">Manish Shriram</span>
    <span class="dev">मनीष श्रीराम</span>
</div>
""")

# -------------------- LEFT MENU --------------------
html("""
<div class="menu">
    <a href="#edits">Edits</a>
    <a href="#story">Short Story</a>
    <a href="#about">About Me</a>
    <a href="https://www.instagram.com/yourprofilelink" target="_blank">Instagram</a>
</div>
""")

# -------------------- SPACER --------------------
st.markdown("<div style='height:120px'></div>", unsafe_allow_html=True)

# -------------------- EDITS SECTION --------------------
st.markdown("<section id='edits'></section>", unsafe_allow_html=True)
st.markdown("## Edits")

st.markdown("<div class='grid'>", unsafe_allow_html=True)
for link in video_links:
    st.markdown(f"""
    <div class="video">
        <iframe src="{link}" frameborder="0" allowfullscreen></iframe>
    </div>
    """, unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# -------------------- STORY SECTION --------------------
st.markdown("<div style='height:100px'></div>", unsafe_allow_html=True)
st.markdown("<section id='story'></section>", unsafe_allow_html=True)
st.markdown("## 100th Night")

html("""
<iframe src="https://manishshriram.art.blog/"
        width="100%"
        height="600"
        style="border:none; border-radius:10px;">
</iframe>
""")

# -------------------- ABOUT SECTION --------------------
st.markdown("<div style='height:100px'></div>", unsafe_allow_html=True)
st.markdown("<section id='about'></section>", unsafe_allow_html=True)
st.markdown("## About Me")

st.markdown("""
<div class="about">
    <img src="https://via.placeholder.com/300">
    <p>
    Welcome to my corner of the internet.<br><br>
    A storyteller, editor, and dreamer. My work lives in moments – between nostalgia and light.
    These edits are fragments of my memory reel.
    </p>
</div>
""", unsafe_allow_html=True)
