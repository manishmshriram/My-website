import streamlit as st
import streamlit.components.v1 as components

# -------------------------
# PAGE CONFIG (must be at top)
# -------------------------
st.set_page_config(
    page_title="Manish Shriram",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# -------------------------
# YOUR CONTENT (edit these safely)
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

# Optional: replace later with your image
ABOUT_IMAGE_URL = "https://images.unsplash.com/photo-1520975958225-4f11f3b95c95?auto=format&fit=crop&w=1200&q=60"

ABOUT_TEXT = """Welcome to my corner of the internet.

A storyteller, editor, and dreamer. My work lives in moments – between nostalgia and light.
These edits are fragments of my memory reel.
"""

# -------------------------
# THEME (golden background + cinelover minimal)
# -------------------------
BG = "#caa24a"          # golden background
BG_2 = "#e2c36c"        # lighter golden for gradient
INK = "#121214"         # primary text on gold
INK_MUTED = "#2a2a2f"   # muted text on gold
PILL_BG = "rgba(18,18,20,0.07)"
PILL_BORDER = "rgba(18,18,20,0.20)"
PILL_BG_HOVER = "rgba(18,18,20,0.12)"
PILL_BORDER_HOVER = "rgba(18,18,20,0.35)"
CARD_BG = "rgba(18,18,20,0.06)"
CARD_BORDER = "rgba(18,18,20,0.14)"

st.markdown(
    f"""
    <style>
      /* App background (gold gradient + subtle "film" texture) */
      .stApp {{
        background: radial-gradient(1200px 600px at 20% 10%, {BG_2} 0%, {BG} 55%, {BG} 100%);
        color: {INK};
      }}

      /* Soft grain overlay (CSS-only, very subtle) */
      .stApp:before {{
        content: "";
        position: fixed;
        inset: 0;
        pointer-events: none;
        background-image:
          radial-gradient(rgba(0,0,0,0.06) 1px, transparent 1px);
        background-size: 3px 3px;
        opacity: 0.14;
        mix-blend-mode: multiply;
      }}

      /* Hide Streamlit chrome */
      #MainMenu {{visibility: hidden;}}
      footer {{visibility: hidden;}}
      header {{visibility: hidden;}}

      /* Container width + spacing */
      div.block-container {{
        padding-top: 1.4rem;
        padding-bottom: 2.0rem;
        max-width: 1120px;
      }}

      /* Big name hover effect (English -> Devanagari) */
      .name {{
        font-family: ui-sans-serif, system-ui, -apple-system, "Segoe UI", Roboto, Arial;
        font-weight: 700;
        font-size: 1.65rem;
        letter-spacing: 0.4px;
        color: {INK};
        user-select: none;
        position: relative;
        display: inline-block;
        line-height: 1.15;
        margin-bottom: 0.6rem;
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

      .subline {{
        color: {INK_MUTED};
        font-size: 0.98rem;
        margin-bottom: 0.9rem;
      }}

      /* Navigation radio -> pill menu */
      div[data-baseweb="radio"] > div {{
        display: flex !important;
        flex-direction: row !important;
        flex-wrap: wrap !important;
        gap: 12px !important;
        align-items: center !important;
        margin-bottom: 8px !important;
      }}

      div[data-baseweb="radio"] label {{
        margin: 0 !important;
      }}

      /* Hide default radio circle */
      div[data-baseweb="radio"] label > div:first-child {{
        display: none !important;
      }}

      /* Pill */
      div[data-baseweb="radio"] label > div:last-child {{
        padding: 10px 14px !important;
        border-radius: 999px !important;
        border: 1px solid {PILL_BORDER} !important;
        background: {PILL_BG} !important;
        color: {INK} !important;
        font-size: 1.03rem !important;
        font-weight: 600 !important;
        letter-spacing: 0.2px !important;
        transition: transform 160ms ease, background 160ms ease, border 160ms ease;
      }}

      div[data-baseweb="radio"] label:hover > div:last-child {{
        transform: translateY(-1px);
        background: {PILL_BG_HOVER} !important;
        border: 1px solid {PILL_BORDER_HOVER} !important;
      }}

      /* Selected (best-effort) */
      div[data-baseweb="radio"] input:checked + div {{
        background: rgba(18,18,20,0.16) !important;
        border: 1px solid rgba(18,18,20,0.55) !important;
      }}

      /* Section title */
      .section-title {{
        font-size: 1.55rem;
        font-weight: 800;
        margin: 0.2rem 0 0.9rem 0;
        color: {INK};
        letter-spacing: 0.2px;
      }}

      /* Video card with hover effect */
      .video-card {
  border-radius: 20px;
  overflow: hidden;
  background: transparent;
  border: 1.2px solid rgba(18,18,20,0.35);
  box-shadow: none;
  transform: translateY(0);
  transition: transform 420ms ease, box-shadow 420ms ease;
}

     .video-card:hover {
  transform: scale(1.045);
  box-shadow: 0 25px 60px rgba(18,18,20,0.22);
}


      /* Responsive 16:9 wrapper */
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
      }}

      /* Links */
      a, a:visited {{
        color: {INK};
        text-decoration: underline;
        text-underline-offset: 3px;
      }}
      a:hover {{
        opacity: 0.85;
      }}

      /* Mobile improvements (bigger, cleaner) */
      @media (max-width: 640px) {{
        div.block-container {{
          padding-top: 1.1rem;
          padding-left: 1.0rem;
          padding-right: 1.0rem;
        }}
        .name {{
          font-size: 2.05rem;
        }}
        .subline {{
          font-size: 1.05rem;
        }}
        div[data-baseweb="radio"] label > div:last-child {{
          padding: 12px 14px !important;
          font-size: 1.08rem !important;
        }}
      }}
    </style>
    """,
    unsafe_allow_html=True,
)

# -------------------------
# HEADER
# -------------------------
st.markdown(
    """
    <div class="name">
      <span class="en">Manish Shriram</span>
      <span class="hi">मनिष श्रीराम</span>
    </div>
    <div class="subline">Cinelover minimal — edits, stories, and memory reels.</div>
    """,
    unsafe_allow_html=True,
)

# -------------------------
# NAV (icons included)
# -------------------------
pages = ["🎬 Edits", "✍️ Short Story", "🙂 About Me", "📷 Instagram"]

default_page = st.session_state.get("page", "🎬 Edits")
if default_page not in pages:
    default_page = "🎬 Edits"

selected = st.radio(
    "Navigation",
    pages,
    index=pages.index(default_page),
    horizontal=True,
    label_visibility="collapsed",
    key="page",
)

# subtle divider
st.markdown(
    '<div style="height:1px;background:rgba(18,18,20,0.14);margin:14px 0 18px 0;"></div>',
    unsafe_allow_html=True,
)

# -------------------------
# HELPERS
# -------------------------
def title(text: str):
    st.markdown(f"<div class='section-title'>{text}</div>", unsafe_allow_html=True)

def youtube_card(embed_url: str):
    components.html(
        f"""
        <div style="
            position: relative;
            border-radius: 18px;
            overflow: hidden;
            border: 1.4px solid rgba(30,30,35,0.45);
            background: black;
        ">

            <!-- Film Top Strip -->
            <div style="
                position: absolute;
                top: 0;
                left: 0;
                width: 100%;
                height: 28px;
                background: linear-gradient(
                    to bottom,
                    rgba(0,0,0,0.85),
                    rgba(0,0,0,0.25)
                );
                z-index: 5;
            "></div>

            <!-- Film Bottom Strip -->
            <div style="
                position: absolute;
                bottom: 0;
                left: 0;
                width: 100%;
                height: 28px;
                background: linear-gradient(
                    to top,
                    rgba(0,0,0,0.85),
                    rgba(0,0,0,0.25)
                );
                z-index: 5;
            "></div>

            <!-- Video -->
            <div style="
                position: relative;
                width: 100%;
                padding-top: 56.25%;
            ">
                <iframe
                    src="{embed_url}"
                    style="
                        position: absolute;
                        inset: 0;
                        width: 100%;
                        height: 100%;
                        border: none;
                    "
                    allowfullscreen
                ></iframe>
            </div>

        </div>
        """,
        height=500,
    )


# -------------------------
# PAGES
# -------------------------
if selected == "🎬 Edits":
    title("Edits")

    # Two columns on desktop, automatically stacks on small screens.
    cols = st.columns(2, gap="large")
    for i, url in enumerate(video_links):
        with cols[i % 2]:
            youtube_card(url)
            st.markdown("<div style='height:16px'></div>", unsafe_allow_html=True)

elif selected == "✍️ Short Story":
    title(SHORT_STORY_TITLE)

    st.markdown(
        "<div style='color:rgba(18,18,20,0.75); margin-bottom:10px;'>"
        "If the preview does not load, open it using the link below."
        "</div>",
        unsafe_allow_html=True,
    )

    st.markdown(f"<a href='{SHORT_STORY_URL}' target='_blank'>Open story site</a>", unsafe_allow_html=True)
    st.markdown("<div style='height:12px'></div>", unsafe_allow_html=True)

    # Embedded preview
    components.iframe(SHORT_STORY_URL, height=900, scrolling=True)

elif selected == "🙂 About Me":
    title("About Me")
    c1, c2 = st.columns([1, 2], gap="large")

    with c1:
        st.image(
            "My Images.jpg",
            use_container_width=True
        )

    with c2:
        st.markdown(
            f"<div style='font-size:1.08rem; line-height:1.7; color:{INK};'>"
            f"{ABOUT_TEXT.replace(chr(10), '<br>')}"
            f"</div>",
            unsafe_allow_html=True,
        )



elif selected == "📷 Instagram":
    title("Instagram")

    st.markdown(
        f"""
        <div style="color:{INK_MUTED}; font-size:1.02rem; margin-bottom:12px;">
          Find me on Instagram.
        </div>

        <a href='https://www.instagram.com/m.m.shriram?igsh=MXNqaTFnODZ3b216ZA==' target="_blank"
           style="
             display:inline-block;
             padding:12px 16px;
             border-radius:999px;
             border:1px solid rgba(18,18,20,0.35);
             background: rgba(18,18,20,0.10);
             font-weight:700;
           ">
           Open Instagram →
        </a>
        """,
        unsafe_allow_html=True,
    )
