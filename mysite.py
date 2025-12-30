import streamlit as st
import streamlit.components.v1 as components

# =========================================================
# [1] PAGE CONFIG
# =========================================================
st.set_page_config(
    page_title="Manish Shriram",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# =========================================================
# [2] CONTENT
# =========================================================
video_links = [
    "https://www.youtube.com/embed/oMDsZA73fJg",
    "https://www.youtube.com/embed/NNHJxvZxyoM",
    "https://www.youtube.com/embed/gs80fqMsU6M",
    "https://www.youtube.com/embed/OFvm21z8L-M",
]

SHORT_STORY_TITLE = "100th Night"
SHORT_STORY_URL = "https://manishshriram.art.blog/"

# ✅ FIXED PHOTO URL (RAW)
ABOUT_IMAGE_URL = "https://raw.githubusercontent.com/manishmshriram/My-website/main/My%20Images.jpg"

ABOUT_TEXT = """Welcome to my corner of the internet.

A storyteller, editor, and dreamer.
My work lives between nostalgia and light.
These edits are fragments of my memory reel.
"""

# =========================================================
# [3] STYLE (cinematic, soft, rounded)
# =========================================================
st.markdown("""
<style>
.stApp {
  background: radial-gradient(1200px 650px at 20% 5%, #e2c36c 0%, #caa24a 55%, #caa24a 100%);
}

.video-card {
  border-radius: 22px;
  overflow: hidden;
  transition: transform 0.35s ease, box-shadow 0.35s ease;
  box-shadow: 0 14px 40px rgba(0,0,0,0.18);
  margin-bottom: 28px;
}

.video-card:hover {
  transform: scale(1.035);
  box-shadow: 0 22px 60px rgba(0,0,0,0.28);
}

.video-wrap {
  position: relative;
  width: 100%;
  padding-top: 56.25%;
}

.video-wrap iframe {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  border-radius: 22px;
}

.about-img img {
  border-radius: 26px;
  box-shadow: 0 18px 45px rgba(0,0,0,0.25);
}
</style>
""", unsafe_allow_html=True)

# =========================================================
# [4] HEADER
# =========================================================
st.markdown("""
<h1>Manish Shriram</h1>
<p>Cinephile minimal — edits, stories, and memory reels.</p>
<hr>
""", unsafe_allow_html=True)

# =========================================================
# [5] NAV
# =========================================================
page = st.radio(
    "",
    ["🎬 Edits", "✍️ Short Story", "🙂 About Me"],
    horizontal=True
)

# =========================================================
# [6] VIDEO CARD (ONE AT A TIME)
# =========================================================
def youtube_card(url):
    components.html(
        f"""
        <div class="video-card">
          <div class="video-wrap">
            <iframe
              src="{url}"
              frameborder="0"
              allow="autoplay; encrypted-media"
              allowfullscreen>
            </iframe>
          </div>
        </div>
        """,
        height=360
    )

# =========================================================
# [7] PAGES
# =========================================================
if page == "🎬 Edits":
    for url in video_links:
        youtube_card(url)

elif page == "✍️ Short Story":
    st.markdown(f"### {SHORT_STORY_TITLE}")
    st.markdown(f"[Read the full story →]({SHORT_STORY_URL})", unsafe_allow_html=True)

elif page == "🙂 About Me":
    col1, col2 = st.columns([1, 2], gap="large")
    with col1:
        st.markdown("<div class='about-img'>", unsafe_allow_html=True)
        st.image(ABOUT_IMAGE_URL, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)
    with col2:
        st.markdown(ABOUT_TEXT)
