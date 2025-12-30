import streamlit as st
import streamlit.components.v1 as components

# =========================================================
# [1] PAGE CONFIG (keep as-is)
# =========================================================
st.set_page_config(
    page_title="Manish Shriram",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# =========================================================
# [2] YOUR CONTENT (CHANGE HERE)
# =========================================================
video_links = [
    "https://www.youtube.com/embed/oMDsZA73fJg?enablejsapi=1&mute=1",
    "https://www.youtube.com/embed/NNHJxvZxyoM?enablejsapi=1&mute=1",
    "https://www.youtube.com/embed/gs80fqMsU6M?enablejsapi=1&mute=1",
    "https://www.youtube.com/embed/OFvm21z8L-M?enablejsapi=1&mute=1",
    "https://www.youtube.com/embed/o4XQkw0k5To?enablejsapi=1&mute=1",
    "https://www.youtube.com/embed/ZUhU4izZbi0?enablejsapi=1&mute=1",
    "https://www.youtube.com/embed/wDzCeqzgmoA?enablejsapi=1&mute=1",
    "https://www.youtube.com/embed/PPOYOUFk4Hw?enablejsapi=1&mute=1",
    "https://www.youtube.com/embed/WAsDEw1HKG4?enablejsapi=1&mute=1",
    "https://www.youtube.com/embed/y6JbWgHx7po?enablejsapi=1&mute=1",
    "https://www.youtube.com/embed/aNFGiVwt4uE?enablejsapi=1&mute=1",
]

SHORT_STORY_TITLE = "100th Night"
SHORT_STORY_URL = "https://manishshriram.art.blog/"
INSTAGRAM_URL = "https://www.instagram.com/yourprofilelink"

# ✅ ADDED — YOUR PHOTO (RAW GITHUB IMAGE)
ABOUT_IMAGE_URL = "https://raw.githubusercontent.com/manishmshriram/My-website/main/My%20Images.jpg"

ABOUT_TEXT = """Welcome to my corner of the internet.

A storyteller, editor, and dreamer. My work lives in moments – between nostalgia and light.
These edits are fragments of my memory reel.
"""

# =========================================================
# [3] THEME + CINEMATIC MOVING BACKGROUND (keep as-is)
# =========================================================
BG = "#caa24a"
BG_2 = "#e2c36c"
INK = "#121214"
INK_MUTED = "#2a2a2f"

st.markdown(
    f"""
    <style>
      .video-card {{
        border-radius: 22px;
        overflow: hidden;
        background: transparent;
        border: none;
        box-shadow: 0 12px 28px rgba(18,18,20,0.14);
        transition: transform 220ms ease, box-shadow 220ms ease;
      }}

      .video-card:hover {{
        transform: translateY(-4px) scale(1.035);
        box-shadow: 0 20px 44px rgba(18,18,20,0.22);
      }}

      .video-wrap {{
        position: relative;
        width: 100%;
        padding-top: 56.25%;
      }}

      .video-wrap iframe {{
        position: absolute;
        inset: 0;
        width: 100%;
        height: 100%;
        border-radius: 22px;
      }}

      img {{
        border-radius: 22px;
        box-shadow: 0 16px 36px rgba(18,18,20,0.20);
      }}
    </style>
    """,
    unsafe_allow_html=True,
)

# =========================================================
# [6] HELPERS
# =========================================================
def youtube_card(embed_url: str):
    components.html(
        f"""
        <div class="video-card"
             onmouseenter="playVideo(this)"
             onmouseleave="pauseVideo(this)">
          <div class="video-wrap">
            <iframe
              src="{embed_url}"
              frameborder="0"
              allow="autoplay; encrypted-media"
              allowfullscreen
            ></iframe>
          </div>
        </div>

        <script>
          function playVideo(card) {{
            const iframe = card.querySelector("iframe");
            iframe.contentWindow.postMessage(
              '{{"event":"command","func":"unMute","args":""}}',
              '*'
            );
            iframe.contentWindow.postMessage(
              '{{"event":"command","func":"playVideo","args":""}}',
              '*'
            );
          }}

          function pauseVideo(card) {{
            const iframe = card.querySelector("iframe");
            iframe.contentWindow.postMessage(
              '{{"event":"command","func":"pauseVideo","args":""}}',
              '*'
            );
            iframe.contentWindow.postMessage(
              '{{"event":"command","func":"mute","args":""}}',
              '*'
            );
          }}
        </script>
        """,
        height=300,
    )

# =========================================================
# [7] PAGES
# =========================================================
selected = st.session_state.get("page", "🎬 Edits")

if selected == "🎬 Edits":
    for url in video_links:
        youtube_card(url)

elif selected == "🙂 About Me":
    c1, c2 = st.columns([1, 2], gap="large")
    with c1:
        st.image(ABOUT_IMAGE_URL, use_container_width=True)
    with c2:
        st.markdown(ABOUT_TEXT)
