import streamlit as st
from streamlit.components.v1 import html

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="Manish Shriram",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ------------------ STATE ------------------
if "section" not in st.session_state:
    st.session_state.section = "Edits"

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
    background-color: #0b0b0b;
    color: #e6c56f;
    font-family: Inter, sans-serif;
}

/* Remove Streamlit clutter */
#MainMenu, footer, header {
    visibility: hidden;
}

/* Name hover */
.name-box {
    position: fixed;
    top: 28px;
    left: 32px;
    font-size: 22px;
    font-weight: 500;
    color: #e6c56f;
    cursor: pointer;
    z-index: 1000;
}
.name-box span {
    transition: opacity 0.35s ease;
}
.name-box .dev {
    position: absolute;
    opacity: 0;
}
.name-box:hover .eng {
    opacity: 0;
}
.name-box:hover .dev {
    opacity: 1;
}

/* Navigation */
.nav {
    margin-top: 80px;
    display: flex;
    gap: 24px;
    flex-wrap: wrap;
}
.nav button {
    background: none;
    border: none;
    color: #e6c56f;
    font-size: 16px;
    cursor: pointer;
}
.nav button:hover {
    opacity: 0.7;
}

/* Section titles */
.section-title {
    font-size: 32px;
    margin: 60px 0 30px 0;
}

/* Video grid */
.video-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
    gap: 24px;
}
.video-grid iframe {
    width: 100%;
    height: 200px;
    border-radius: 8px;
}

/* About */
.about-wrap {
    display: flex;
    gap: 40px;
    flex-wrap: wrap;
}
.about-wrap img {
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

# ------------------ NAME ------------------
html("""
<div class="name-box">
    <span class="eng">Manish Shriram</span>
    <span class="dev">मनीष श्रीराम</span>
</div>
""")

# ------------------ NAVIGATION ------------------
st.markdown("<div class='nav'>", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)
with col1:
    if st.button("Edits"):
        st.session_state.section = "Edits"
with col2:
    if st.button("Short Story"):
        st.session_state.section = "Short Story"
with col3:
    if st.button("About Me"):
        st.session_state.section = "About Me"
with col4:
    if st.button("Instagram"):
        st.session_state.section = "Instagram"

st.markdown("</div>", unsafe_allow_html=True)

# ------------------ CONTENT ------------------
if st.session_state.section == "Edits":
    st.markdown("<div class='section-title'>Edits</div>", unsafe_allow_html=True)
    st.markdown("<div class='video-grid'>", unsafe_allow_html=True)
    for v in video_links:
        st.markdown(
            f"<iframe src='{v}' frameborder='0' allowfullscreen></iframe>",
            unsafe_allow_html=True
        )
    st.markdown("</div>", unsafe_allow_html=True)

elif st.session_state.section == "Short Story":
    st.markdown("<div class='section-title'>100th Night</div>", unsafe_allow_html=True)
    html("""
    <iframe src="https://manishshriram.art.blog/"
            width="100%"
            height="650"
            style="border:none; border-radius:8px;">
    </iframe>
    """)

elif st.session_state.section == "About Me":
    st.markdown("<div class='section-title'>About Me</div>", unsafe_allow_html=True)
    st.markdown("""
    <div class="about-wrap">
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

elif st.session_state.section == "Instagram":
    st.markdown("<div class='section-title'>Instagram</div>", unsafe_allow_html=True)
    st.markdown("""
    <p>Find me on Instagram</p>
    <a href="https://www.instagram.com/yourprofilelink" target="_blank">
        https://www.instagram.com/yourprofilelink
    </a>
    """, unsafe_allow_html=True)
