# app.py
import streamlit as st
import streamlit.components.v1 as components

# -------------------------
# Config
# -------------------------
st.set_page_config(
    page_title="Manish Shriram",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# -------------------------
# Data
# -------------------------
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
    "https://www.youtube.com/embed/aNFGiVwt4uE?si=GvQ5ro2-0tZSIs51",
]

SHORT_STORY_TITLE = "100th Night"
SHORT_STORY_URL = "https://manishshriram.art.blog/"
INSTAGRAM_URL = "https://www.instagram.com/yourprofilelink"

# -------------------------
# Styles (Dark + Yellow Aesthetic)
# -------------------------
YELLOW = "#d8b14c"   # warm yellow / golden
BG = "#07090f"       # near black
MUTED = "#a9b0bd"    # muted text

st.markdown(
    f"""
    <style>
      /* Base app background */
      .stApp {{
        background: {BG};
        color: #e9edf6;
      }}

      /* Remove Streamlit chrome */
      #MainMenu {{visibility: hidden;}}
      footer {{visibility: hidden;}}
      header {{visibility: hidden;}}

      /* Reduce default padding */
      div.block-container {{
        padding-top: 1.4rem;
        padding-bottom: 2.2rem;
        max-width: 1120px;
      }}

      /* Top Name Hover Effect */
      .name-wrap {{
        display: flex;
        justify-content: space-between;
        align-items: flex-start;
        gap: 16px;
        margin-bottom: 0.75rem;
      }}

      .name {{
        font-family: ui-sans-serif, system-ui, -apple-system, "Segoe UI", Roboto, Arial;
        font-size: 0.95rem;
        letter-spacing: 0.5px;
        color: {YELLOW};
        user-select: none;
        position: relative;
        display: inline-block;
        line-height: 1.1;
        opacity: 0.95;
      }}

      .name .en {{
        opacity: 1;
        transition: opacity 220ms ease;
      }}

      .name .hi {{
        position: absolute;
        left: 0;
        top: 0;
        opacity: 0;
        transition: opacity 220ms ease;
        white-space: nowrap;
      }}

      .name:hover .en {{ opacity: 0; }}
      .name:hover .hi {{ opacity: 1; }}

      /* Subtitle / small muted text */
      .muted {{
        color: {MUTED};
        font-size: 0.9rem;
      }}

      /* Nav: style the st.radio to look like clean links */
      div[data-baseweb="radio"] > div {{
        display: flex !important;
        flex-direction: row !important;
        flex-wrap: wrap !important;
        gap: 12px !important;
        align-items: center !important;
      }}

      /* Each option container */
      div[data-baseweb="radio"] label {{
        margin: 0 !important;
      }}

      /* Pill button look */
      div[data-baseweb="radio"] label > div:first-child {{
        display: none !important; /* hide the default circle */
      }}

      div[data-baseweb="radio"] label > div:last-child {{
        padding: 8px 12px !important;
        border-radius: 999px !important;
        border: 1px solid rgba(216, 177, 76, 0.25) !important;
        background: rgba(255,255,255,0.02) !important;
        color: {YELLOW} !important;
        font-size: 0.92rem !important;
        letter-spacing: 0.2px !important;
        transition: transform 160ms ease, background 160ms ease, border 160ms ease;
      }}

      div[data-baseweb="radio"] label:hover > div:last-child {{
        transform: translateY(-1px);
        background: rgba(216, 177, 76, 0.08) !important;
        border: 1px solid rgba(216, 177, 76, 0.55) !important;
      }}

      /* Selected state (best-effort selectors; Streamlit DOM can change) */
      div[data-baseweb="radio"] input:checked + div {{
        background: rgba(216, 177, 76, 0.14) !important;
        border: 1px solid rgba(216, 177, 76, 0.8) !important;
      }}

      /* Headings */
      h1, h2, h3 {{
        color: {YELLOW};
        letter-spacing: 0.2px;
      }}

      /* Responsive video wrapper */
      .video-wrap {{
        position: relative;
        width: 100%;
        padding-top: 56.25%; /* 16:9 */
        border-radius: 14px;
        overflow: hidden;
        border: 1px solid rgba(255,255,255,0.06);
        background: rgba(255,255,255,0.02);
      }}

      .video-wrap iframe {{
        position: absolute;
        top: 0; left: 0;
        width: 100%;
        height: 100%;
      }}

      /* Content section spacing */
      .section {{
        margin-top: 0.8rem;
      }}

      /* Make links yellow-ish */
      a, a:visited {{
        color: {YELLOW};
        text-decoration: none;
      }}
      a:hover {{
        text-decoration: underline;
      }}

      /* Mobile tweaks */
      @media (max-width: 640px) {{
        div.block-container {{
          padding-top: 1.1rem;
        }}
        .name {{
          font-size: 0.95rem;
        }}
      }}
    </style>
    """,
    unsafe_allow_html=True,
)

# -------------------------
# Header
# -------------------------
st.markdown(
    """
    <div class="name-wrap">
      <div>
        <div class="name">
          <span class="en">Manish Shriram</span>
          <span class="hi">मनीष श्रीराम</span>
        </div>
      </div>
      <div class="muted"></div>
    </div>
    """,
    unsafe_allow_html=True,
)

# -------------------------
# Navigation (4 items)
# -------------------------
pages = ["Edits", "Short Story", "About Me", "Instagram"]

default_page = st.session_state.get("page", "Edits")
if default_page not in pages:
    default_page = "Edits"

selected = st.radio(
    "Navigation",
    pages,
    index=pages.index(default_page),
    horizontal=True,
    label_visibility="collapsed",
    key="page",
)

# Divider line (subtle)
st.markdown(
    '<div style="height:1px;background:rgba(255,255,255,0.06);margin:14px 0 18px 0;"></div>',
    unsafe_allow_html=True,
)

# -------------------------
# Helpers
# -------------------------
def render_youtube_embed(embed_url: str):
    components.html(
        f"""
        <div class="video-wrap">
          <iframe
            src="{embed_url}"
            title="YouTube video player"
            frameborder="0"
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
            allowfullscreen
          ></iframe>
        </div>
        """,
        height=420,  # wrapper scales; height just reserves space in Streamlit layout
    )

def h2(title: str):
    st.markdown(f"<h2 style='margin:0 0 0.7rem 0;'>{title}</h2>", unsafe_allow_html=True)

# -------------------------
# Pages
# -------------------------
if selected == "Edits":
    h2("Edits")
    st.markdown("<div class='section'></div>", unsafe_allow_html=True)

    # Layout: on desktop use 2 columns; on mobile it stacks automatically
    cols = st.columns(2, gap="large")
    for i, url in enumerate(video_links):
        with cols[i % 2]:
            render_youtube_embed(url)
            st.markdown("<div style='height:14px'></div>", unsafe_allow_html=True)

elif selected == "Short Story":
    h2(SHORT_STORY_TITLE)
    st.markdown(
        f"<div class='muted' style='margin-bottom:10px;'>Read directly here (if embed is blocked, use the link below).</div>",
        unsafe_allow_html=True,
    )

    # Some sites disable embedding via X-Frame-Options/CSP. Provide link as fallback.
    st.markdown(f"<a href='{SHORT_STORY_URL}' target='_blank'>Open: {SHORT_STORY_URL}</a>", unsafe_allow_html=True)
    st.markdown("<div style='height:12px'></div>", unsafe_allow_html=True)

    try:
        components.iframe(SHORT_STORY_URL, height=900, scrolling=True)
    except Exception:
        st.warning("This site may block embedding. Use the link above to open it.")

elif selected == "About Me":
    h2("About Me")

    col1, col2 = st.columns([1, 2], gap="large")

    with col1:
        # Replace with your real photo later (e.g., st.image("static/profile.jpg"))
        st.image(
            "https://images.unsplash.com/photo-1520975958225-4f11f3b95c95?auto=format&fit=crop&w=800&q=60",
            caption="(Replace this with your photo)",
            use_container_width=True,
        )

    with col2:
        st.markdown(
            f"""
            <div style="color:#e9edf6; font-size:1.05rem; line-height:1.65;">
              <div style="margin-bottom:12px;">Welcome to my corner of the internet.</div>
              <div style="color:{MUTED};">
                A storyteller, editor, and dreamer. My work lives in moments – between nostalgia and light.
                These edits are fragments of my memory reel.
              </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

elif selected == "Instagram":
    h2("Instagram")
    st.markdown(
        f"""
        <div class="muted" style="margin-bottom:12px;">Find me on Instagram.</div>
        <a href="{INSTAGRAM_URL}" target="_blank"
           style="
             display:inline-block;
             padding:10px 14px;
             border-radius:999px;
             border:1px solid rgba(216,177,76,0.55);
             background: rgba(216,177,76,0.10);
           ">
           Open Instagram
        </a>
        """,
        unsafe_allow_html=True,
    )
