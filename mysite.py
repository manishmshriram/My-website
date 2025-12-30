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

    # ✅ EXTRA VIDEO (CHANGE HERE: replace VIDEO_ID with your new video id)
    # Example: https://www.youtube.com/watch?v=abcd1234 => VIDEO_ID = abcd1234
    "https://www.youtube.com/embed/VIDEO_ID",
]

SHORT_STORY_TITLE = "100th Night"
SHORT_STORY_URL = "https://manishshriram.art.blog/"   # NOTE: some sites can block iframe embedding. [web:93]
INSTAGRAM_URL = "https://www.instagram.com/yourprofilelink"  # CHANGE HERE later

ABOUT_IMAGE_URL = "https://images.unsplash.com/photo-1520975958225-4f11f3b95c95?auto=format&fit=crop&w=1200&q=60"  # CHANGE later

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
      /* Base */
      .stApp {{
        background: radial-gradient(1200px 650px at 20% 5%, {BG_2} 0%, {BG} 55%, {BG} 100%);
        color: {INK};
      }}

      /* Hide Streamlit chrome */
      #MainMenu {{visibility: hidden;}}
      footer {{visibility: hidden;}}
      header {{visibility: hidden;}}

      /* Layout width */
      div.block-container {{
        padding-top: 1.2rem;
        padding-bottom: 2.0rem;
        max-width: 1120px;
      }}

      /* ==========================
         CINEMATIC MOVING EFFECTS
         - film grain (fast jitter)
         - dust drift (slow float)
         ========================== */

      /* Grain layer */
      .stApp:before {{
        content: "";
        position: fixed;
        inset: -20%;
        z-index: 0;
        pointer-events: none;
        background-image:
          repeating-linear-gradient(0deg, rgba(0,0,0,0.06) 0px, rgba(0,0,0,0.06) 1px, transparent 2px, transparent 4px),
          repeating-linear-gradient(90deg, rgba(0,0,0,0.04) 0px, rgba(0,0,0,0.04) 1px, transparent 2px, transparent 6px);
        opacity: 0.10;
        mix-blend-mode: multiply;
        animation: grainJitter 0.9s steps(2) infinite;
      }}

      @keyframes grainJitter {{
        0%   {{ transform: translate(0,0) rotate(0deg); }}
        25%  {{ transform: translate(-0.7%, 0.4%) rotate(0.05deg); }}
        50%  {{ transform: translate(0.4%, -0.7%) rotate(-0.05deg); }}
        75%  {{ transform: translate(-0.3%, -0.2%) rotate(0.06deg); }}
        100% {{ transform: translate(0,0) rotate(0deg); }}
      }}

      /* Dust (floating particles) */
      .stApp:after {{
        content: "";
        position: fixed;
        inset: 0;
        z-index: 0;
        pointer-events: none;
        background-image:
          radial-gradient(rgba(18,18,20,0.16) 1px, transparent 1.5px),
          radial-gradient(rgba(18,18,20,0.10) 1px, transparent 1.8px),
          radial-gradient(rgba(255,255,255,0.10) 1px, transparent 2px);
        background-size: 140px 140px, 220px 220px, 320px 320px;
        background-position: 0 0, 40px 70px, 120px 40px;
        opacity: 0.35;
        mix-blend-mode: multiply;
        animation: dustDrift 18s linear infinite;
      }}

      @keyframes dustDrift {{
        0%   {{ background-position: 0 0, 40px 70px, 120px 40px; }}
        100% {{ background-position: 0 420px, 40px 620px, 120px 520px; }}
      }}

      /* Make content render ABOVE moving layers */
      div.block-container {{
        position: relative;
        z-index: 2;
      }}

      /* ==================================
         NAME (bigger + hover language swap)
         ================================== */
      .name {{
        font-family: ui-sans-serif, system-ui, -apple-system, "Segoe UI", Roboto, Arial;
        font-weight: 850;
        font-size: 2.05rem;
        letter-spacing: 0.4px;
        color: {INK};
        user-select: none;
        position: relative;
        display: inline-block;
        line-height: 1.08;
        margin-bottom: 0.45rem;
      }}
      .name .en {{ opacity: 1; transition: opacity 220ms ease; }}
      .name .hi {{
        position: absolute; left: 0; top: 0;
        opacity: 0; transition: opacity 220ms ease;
        white-space: nowrap;
      }}
      .name:hover .en {{ opacity: 0; }}
      .name:hover .hi {{ opacity: 1; }}

      .subline {{
        color: rgba(18,18,20,0.78);
        font-size: 1.05rem;
        margin-bottom: 0.85rem;
      }}

      /* ==================================
         NAV (pill menu)
         ================================== */
      div[data-baseweb="radio"] > div {{
        display: flex !important;
        flex-direction: row !important;
        flex-wrap: wrap !important;
        gap: 10px !important;
        align-items: center !important;
        margin-bottom: 8px !important;
      }}
      div[data-baseweb="radio"] label {{ margin: 0 !important; }}
      div[data-baseweb="radio"] label > div:first-child {{ display: none !important; }}
      div[data-baseweb="radio"] label > div:last-child {{
        padding: 10px 14px !important;
        border-radius: 999px !important;
        border: 1px solid rgba(18,18,20,0.22) !important;
        background: rgba(18,18,20,0.07) !important;
        color: {INK} !important;
        font-size: 1.02rem !important;
        font-weight: 700 !important;
        transition: transform 160ms ease, background 160ms ease, border 160ms ease;
      }}
      div[data-baseweb="radio"] label:hover > div:last-child {{
        transform: translateY(-1px);
        background: rgba(18,18,20,0.12) !important;
        border: 1px solid rgba(18,18,20,0.36) !important;
      }}
      div[data-baseweb="radio"] input:checked + div {{
        background: rgba(18,18,20,0.18) !important;
        border: 1px solid rgba(18,18,20,0.60) !important;
      }}

      /* Divider */
      .soft-divider {{
        height: 1px;
        background: rgba(18,18,20,0.14);
        margin: 14px 0 18px 0;
      }}

      /* ==================================
         PAGE TRANSITION (film flash + fade)
         ================================== */
      .transition-flash {{
        position: fixed;
        inset: 0;
        z-index: 3;
        pointer-events: none;
        background: radial-gradient(800px 450px at 30% 20%, rgba(255,255,255,0.16), transparent 62%);
        opacity: 0;
        animation: flashIn 420ms ease;
        mix-blend-mode: soft-light;
      }}
      @keyframes flashIn {{
        0%   {{ opacity: 0; }}
        18%  {{ opacity: 0.65; }}
        100% {{ opacity: 0; }}
      }}

      .page {{
        animation: reelIn 420ms ease both;
        transform-origin: top center;
      }}
      @keyframes reelIn {{
        0%   {{ opacity: 0; transform: translateY(10px); filter: blur(2px); }}
        100% {{ opacity: 1; transform: translateY(0px); filter: blur(0px); }}
      }}

      /* ==================================
         VIDEO CARDS (tight spacing + hover)
         ================================== */
      .section-title {{
        font-size: 1.55rem;
        font-weight: 900;
        margin: 0.2rem 0 0.85rem 0;
        color: {INK};
        letter-spacing: 0.2px;
      }}

      .video-card {{
        border-radius: 16px;
        overflow: hidden;
        background: rgba(18,18,20,0.06);
        border: 1px solid rgba(18,18,20,0.14);
        box-shadow: 0 10px 24px rgba(18,18,20,0.10);
        transform: translateY(0);
        transition: transform 180ms ease, box-shadow 180ms ease, border 180ms ease;
        position: relative;
      }}

      /* Subtle “cine vignette” overlay on hover (doesn't block clicks) */
      .video-card:after {{
        content: "";
        position: absolute;
        inset: 0;
        pointer-events: none;
        background:
          radial-gradient(140% 120% at 50% 50%, transparent 55%, rgba(0,0,0,0.20) 100%),
          linear-gradient(180deg, rgba(0,0,0,0.08), transparent 35%, rgba(0,0,0,0.12));
        opacity: 0.0;
        transition: opacity 180ms ease;
      }}

      .video-card:hover {{
        transform: translateY(-3px) scale(1.01);
        border: 1px solid rgba(18,18,20,0.35);
        box-shadow: 0 18px 40px rgba(18,18,20,0.16);
      }}
      .video-card:hover:after {{ opacity: 1; }}

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

      /* Make vertical gaps smaller (Streamlit default spacing is big) */
      div[data-testid="stVerticalBlock"] > div {{
        gap: 0.55rem;
      }}

      /* Mobile: cleaner, bigger, 1 column look automatically */
      @media (max-width: 640px) {{
        div.block-container {{
          padding-top: 1.0rem;
          padding-left: 1.0rem;
          padding-right: 1.0rem;
        }}
        .name {{ font-size: 2.35rem; }}
        .subline {{ font-size: 1.08rem; }}
        div[data-baseweb="radio"] label > div:last-child {{
          padding: 12px 14px !important;
          font-size: 1.08rem !important;
        }}
      }}
    </style>
    """,
    unsafe_allow_html=True,
)

# =========================================================
# [4] HEADER
# =========================================================
st.markdown(
    """
    <div class="name">
      <span class="en">Manish Shriram</span>
      <span class="hi">मनीष श्रीराम</span>
    </div>
    <div class="subline">Cinephile minimal — edits, stories, and memory reels.</div>
    """,
    unsafe_allow_html=True,
)

# =========================================================
# [5] NAV
# =========================================================
pages = ["🎬 Edits", "✍️ Short Story", "🙂 About Me", "📷 Instagram"]

prev = st.session_state.get("_prev_page", "🎬 Edits")
selected = st.radio(
    "Navigation",
    pages,
    index=pages.index(st.session_state.get("page", "🎬 Edits")) if st.session_state.get("page", "🎬 Edits") in pages else 0,
    horizontal=True,
    label_visibility="collapsed",
    key="page",
)

# Trigger transition only if page changed
page_changed = (selected != prev)
st.session_state["_prev_page"] = selected

st.markdown('<div class="soft-divider"></div>', unsafe_allow_html=True)

# Transition flash overlay (shows only on change)
if page_changed:
    st.markdown('<div class="transition-flash"></div>', unsafe_allow_html=True)

# =========================================================
# [6] HELPERS
# =========================================================
def title(text: str):
    st.markdown(f"<div class='section-title'>{text}</div>", unsafe_allow_html=True)

def youtube_card(embed_url: str):
    # IMPORTANT: The number below controls the "empty space" under the video.
    # Smaller = less gap. If any video gets cut off, increase a bit.
    # (This is the Streamlit iframe height reservation.) [web:99]
    components.html(
        f"""
        <div class="video-card">
          <div class="video-wrap">
            <iframe
              src="{embed_url}"
              title="YouTube video player"
              frameborder="0"
              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
              allowfullscreen
            ></iframe>
          </div>
        </div>
        """,
        height=330,   # ✅ tighter spacing than before
    )

# =========================================================
# [7] PAGES (content swaps inside the same app)
# =========================================================
st.markdown("<div class='page'>", unsafe_allow_html=True)

if selected == "🎬 Edits":
    title("Edits")

    # Two columns on desktop, stacks on mobile automatically (Streamlit responsive behavior). [web:108]
    cols = st.columns(2, gap="medium")
    for i, url in enumerate(video_links):
        with cols[i % 2]:
            youtube_card(url)

elif selected == "✍️ Short Story":
    title(SHORT_STORY_TITLE)
    st.markdown(
        "<div style='color:rgba(18,18,20,0.75); margin-bottom:10px;'>"
        "If the preview does not load, open the story using the link below."
        "</div>",
        unsafe_allow_html=True,
    )
    st.markdown(f"<a href='{SHORT_STORY_URL}' target='_blank'>Open story site →</a>", unsafe_allow_html=True)
    st.markdown("<div style='height:10px;'></div>", unsafe_allow_html=True)

    components.iframe(SHORT_STORY_URL, height=900, scrolling=True)  # blog preview [web:93]

elif selected == "🙂 About Me":
    title("About Me")
    c1, c2 = st.columns([1, 2], gap="large")

    with c1:
        st.image(ABOUT_IMAGE_URL, use_container_width=True)
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
        <div style="color:rgba(18,18,20,0.78); font-size:1.02rem; margin-bottom:12px;">
          Find me on Instagram.
        </div>

        <a href="https://www.instagram.com/m.m.shriram?igsh=MXNqaTFnODZ3b216ZA==" target="_blank"
           style="
             display:inline-block;
             padding:12px 16px;
             border-radius:999px;
             border:1px solid rgba(18,18,20,0.35);
             background: rgba(18,18,20,0.10);
             font-weight:800;
             text-decoration:none;
           ">
           Open Instagram →
        </a>
        """,
        unsafe_allow_html=True,
    )

st.markdown("</div>", unsafe_allow_html=True)
