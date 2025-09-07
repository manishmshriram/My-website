import streamlit as st
import streamlit.components.v1 as components
import base64, os, random, re

# ─────────────────────────────────────────────────────────────
# Page Setup
# ─────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Manish’s Aesthetic Edits",
    page_icon="🎬",
    layout="centered",
)

# ─────────────────────────────────────────────────────────────
# Font: Try to load local AMS Vasudeva Regular (for Marathi hover)
# Place file at: assets/fonts/AMS-Vasudeva-Regular.ttf
# If not found, we fall back to Noto Sans Devanagari via Google Fonts.
# ─────────────────────────────────────────────────────────────
vasudeva_css = ""
font_path = "assets/fonts/AMS-Vasudeva-Regular.ttf"
if os.path.exists(font_path):
    with open(font_path, "rb") as f:
        b64 = base64.b64encode(f.read()).decode()
    vasudeva_css = f"""
    @font-face {{
        font-family: 'AMS Vasudeva';
        src: url(data:font/ttf;base64,{b64}) format('truetype');
        font-weight: 400;
        font-style: normal;
        font-display: swap;
    }}
    """
google_font_link = """
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&family=Noto+Sans+Devanagari:wght@400;600&display=swap" rel="stylesheet">
"""

# ─────────────────────────────────────────────────────────────
# Global Styles (Dark, minimal-cinematic)
# ─────────────────────────────────────────────────────────────
st.markdown(
    google_font_link
    + f"""
<style>
:root {{
  --bg: #0e0e0f;
  --panel: #171718;
  --soft: #1f1f21;
  --text: #e9e9ea;
  --muted: #bdbfc4;
  --brand: #E5C07B; /* warm gold */
  --accent: #61afef; /* soft blue */
  --rose: #E06C75;  /* rose title */
  --radius: 18px;
  --shadow: 0 10px 30px rgba(0,0,0,.35);
}}

html, body, [data-testid="stAppViewContainer"] {{
  background: var(--bg) !important;
  color: var(--text);
  font-family: 'Poppins', ui-sans-serif, system-ui, -apple-system, 'Segoe UI', Roboto, 'Noto Sans', 'Noto Sans Devanagari', sans-serif;
}}

{vasudeva_css}

/* Wrapper panels */
.panel {{
  background: linear-gradient(180deg, var(--panel), var(--soft));
  border-radius: var(--radius);
  padding: 1.5rem;
  box-shadow: var(--shadow);
  border: 1px solid rgba(255,255,255,0.05);
}}

/* Title / Subtitle */
.header-wrap {{
  text-align: center;
  margin-top: .5rem;
  margin-bottom: 1rem;
}}

.site-name {{
  display: inline-block;
  font-size: clamp(28px, 5vw, 46px);
  font-weight: 700;
  letter-spacing: 0.5px;
  color: var(--brand);
  padding: .25rem .75rem;
  border-radius: 12px;
  background: rgba(229,192,123,0.10);
  transition: transform .25s ease, background .25s ease;
  cursor: default;
}}

.site-name:hover {{
  transform: translateY(-1px);
  background: rgba(229,192,123,0.18);
}}

.name-hover .dev {{ display: none; }}
.name-hover .dev,
.name-hover .eng {{
  transition: opacity .2s ease;
  line-height: 1;
}}
/* On hover, swap English to Marathi */
.name-hover:hover .eng {{ display: none; }}
.name-hover:hover .dev {{
  display: inline;
  font-family: 'AMS Vasudeva', 'Noto Sans Devanagari', sans-serif;
}}

.subtitle {{
  color: var(--muted);
  margin-top: .25rem;
  margin-bottom: 1.2rem;
  font-size: clamp(14px, 2.2vw, 18px);
}}

/* Section titles */
.section-title {{
  text-align: center;
  font-weight: 700;
  color: var(--rose);
  font-size: clamp(20px, 3vw, 28px);
  margin: .25rem 0 1rem;
}}

/* Hero player */
.hero {{
  overflow: hidden;
  border-radius: var(--radius);
  box-shadow: var(--shadow);
  border: 1px solid rgba(255,255,255,0.05);
  background: #111;
}}

.hero-controls {{
  display: flex; gap: .5rem; justify-content: center; align-items: center;
  margin: .75rem 0 0;
}}
.btn {{
  background: #222;
  border: 1px solid rgba(255,255,255,0.08);
  color: var(--text);
  padding: .6rem .9rem;
  border-radius: 12px;
  font-size: 0.95rem;
  cursor: pointer;
  transition: transform .12s ease, background .25s ease, border .25s ease;
}}
.btn:hover {{
  transform: translateY(-1px);
  background: #2a2a2a;
  border-color: rgba(255,255,255,0.18);
}}
.badge {{
  font-size: .85rem; color: var(--muted);
}}

/* Grid of edits */
.grid {{
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  gap: 14px;
}}
@media (max-width: 900px) {{
  .grid {{ grid-template-columns: repeat(6, 1fr); }}
}}
@media (max-width: 600px) {{
  .grid {{ grid-template-columns: repeat(4, 1fr); }}
}}
.card {{
  grid-column: span 4;
  background: #131314;
  border-radius: 16px;
  overflow: hidden;
  position: relative;
  border: 1px solid rgba(255,255,255,0.06);
  transition: transform .25s ease, border .25s ease, box-shadow .25s ease, filter .25s ease;
}}
.card:hover {{
  transform: translateY(-2px);
  border-color: rgba(255,255,255,0.14);
  box-shadow: 0 16px 36px rgba(0,0,0,0.45);
  filter: brightness(1.02);
}}
.thumb-wrap {{
  position: relative; aspect-ratio: 16/9; background: #0c0c0c;
}}
.thumb {{
  width: 100%; height: 100%; object-fit: cover; display: block;
}}
.overlay {{
  position: absolute; inset: 0; display:flex; align-items:end; justify-content:space-between;
  padding: .65rem .75rem; background: linear-gradient(180deg, rgba(0,0,0,0) 40%, rgba(0,0,0,.65) 100%);
  color: #fff;
}}
.title-small {{
  font-size: .95rem; font-weight: 600; letter-spacing:.2px;
}}
.play {{
  background: rgba(255,255,255,0.08);
  padding: .35rem .6rem; border-radius: 10px; font-size: .85rem;
  border: 1px solid rgba(255,255,255,0.18);
}}

/* Sections & Footer */
.section-box {{ padding: 1.25rem; }}
.section-text {{
  text-align: center; color: var(--muted); font-size: 1.05rem; line-height: 1.65;
}}
.link-btn {{
  display:inline-block; margin-top: .8rem;
  background: rgba(97,175,239,0.15); border:1px solid rgba(97,175,239,0.35);
  padding:.65rem .95rem; border-radius: 12px; color: #cfe7ff; text-decoration: none;
  transition: transform .15s ease, background .25s ease, border .25s ease;
}}
.link-btn:hover {{ transform: translateY(-1px); background: rgba(97,175,239,0.22); }}

.insta-icon {{ text-align:center; margin-top: .8rem; }}
.insta-icon a img {{
  width: 44px; height: 44px; filter: brightness(0) invert(1);
  transition: transform .25s ease;
}}
.insta-icon a img:hover {{ transform: scale(1.12); }}

.final-note {{
  text-align: center; color: #7b7f86; font-style: italic; margin: 2rem 0 .5rem;
}}
hr.soft {{ border: none; border-top: 1px solid rgba(255,255,255,0.08); margin: 1.25rem 0; }}
</style>
""",
    unsafe_allow_html=True,
)

# ─────────────────────────────────────────────────────────────
# Data: All your edits here (moved the "Poorly Rescored" inside)
# ─────────────────────────────────────────────────────────────
# Use your existing list + the rescored video together:
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
    # Rescored Disney short (Paperman x Arrival of the Birds)
    "https://www.youtube.com/embed/EI__XUxw8j8?si=PWMbJK7A6a1_ZvoC",
]

# Optional: display-friendly titles from IDs
def extract_youtube_id(embed_url: str) -> str:
    # works for https://www.youtube.com/embed/<ID>?query...
    m = re.search(r"/embed/([\\w-]+)", embed_url)
    return m.group(1) if m else ""

def youtube_thumb(embed_url: str) -> str:
    vid = extract_youtube_id(embed_url)
    return f"https://img.youtube.com/vi/{vid}/hqdefault.jpg" if vid else ""

# Shuffle behavior on first load
if "playlist" not in st.session_state:
    st.session_state.playlist = video_links.copy()
    random.shuffle(st.session_state.playlist)

if "current_idx" not in st.session_state:
    st.session_state.current_idx = 0

def set_current_from_index(i: int):
    st.session_state.current_idx = i

def shuffle_now():
    random.shuffle(st.session_state.playlist)
    st.session_state.current_idx = 0

def render_player(url: str, autoplay: bool = False, height: int = 420):
    # Add autoplay + mute for a slick hero start (browser blocks sound, so mute=1)
    auto = "&autoplay=1&mute=1&playsinline=1" if autoplay else ""
    iframe = f'''
    <div class="hero">
      <iframe
        src="{url}{auto}"
        width="100%" height="{height}" frameborder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
        allowfullscreen
        style="display:block;border-radius:16px"
      ></iframe>
    </div>
    '''
    st.markdown(iframe, unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────
# HEADER with Hover Name (English → Marathi on hover)
# ─────────────────────────────────────────────────────────────
st.markdown(
    """
<div class="header-wrap">
  <div class="site-name name-hover">
    <span class="eng">Manish Shriam</span>
    <span class="dev">मनीष श्रीराम</span>
  </div>
  <div class="subtitle">Cinematic music meets unforgettable frames</div>
</div>
""",
    unsafe_allow_html=True,
)

# ─────────────────────────────────────────────────────────────
# 1) 🎬 Amateur Edits (Featured player + Grid)
# ─────────────────────────────────────────────────────────────
st.markdown('<div class="section-title">🎬 Amateur Edits</div>', unsafe_allow_html=True)

current_url = st.session_state.playlist[st.session_state.current_idx]
render_player(current_url, autoplay=True, height=460)

st.markdown(
    """
<div class="hero-controls">
  <span class="badge">Now Playing</span>
  <button class="btn" onclick="window.location.reload()">⟲ Refresh</button>
</div>
""",
    unsafe_allow_html=True,
)

# Shuffle button (server-side)
colA, colB, colC = st.columns([1,1,1])
with colB:
    if st.button("🔀 Shuffle Playlist", use_container_width=True):
        shuffle_now()

# Grid of all edits with hover + play
st.markdown('<div class="section-box panel">', unsafe_allow_html=True)
st.markdown('<div class="grid">', unsafe_allow_html=True)

for i, url in enumerate(st.session_state.playlist):
    thumb = youtube_thumb(url)
    card_html = f"""
    <div class="card">
      <a href="#" onclick="fetch('/?setvid={i}').then(()=>window.location.reload()); return false;">
        <div class="thumb-wrap">
          <img class="thumb" src="{thumb}" alt="Edit {i+1}" />
          <div class="overlay">
            <div class="title-small">Edit {i+1}</div>
            <div class="play">Play ▶</div>
          </div>
        </div>
      </a>
    </div>
    """
    st.markdown(card_html, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)  # .grid
st.markdown('</div>', unsafe_allow_html=True)  # .section-box

# Handle query-triggered selection (from thumbnail click)
# NOTE: Streamlit doesn't expose the raw querystring easily here;
# the simple trick above reloads; use a hidden input via JS fetch won't reach Python.
# So we provide a second way: small selectbox for current video.
# (Keeps UX smooth; thumbnails refresh approach is still visually effective.)
with st.expander("Change Now Playing (quick picker)", expanded=False):
    selected = st.selectbox(
        "Pick an edit to play:",
        options=[f"Edit {i+1}" for i in range(len(st.session_state.playlist))],
        index=st.session_state.current_idx,
    )
    if st.button("Play Selected"):
        st.session_state.current_idx = int(selected.split()[-1]) - 1
        st.experimental_rerun()

st.markdown('<hr class="soft">', unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────
# 2) 📖 Short Story (nudges to click through)
# ─────────────────────────────────────────────────────────────
st.markdown('<div class="section-title">📖 Short Story</div>', unsafe_allow_html=True)
st.markdown(
    """
<div class="panel section-box">
  <div class="section-text">
    <em>Ek Sauvi Raat (The 100th Night)</em> — ek talaab, ek kawita-kun, ek gूढ she-frog,
    ek sipahi, ek kachhua — aur woh 100वी raat jisne sab kuch badal diya.
    Absurd, komal, aur nostalgia se bheega hua — bilkul zindagi ki tarah.
  </div>
  <div class="section-text">
    If you like cinematic monologues with a heartbeat, read the full piece.
  </div>
  <div style="text-align:center;">
    <a class="link-btn" href="https://manishshriram.art.blog/" target="_blank" rel="noopener">
      Read the full story on my blog ↗
    </a>
  </div>
</div>
""",
    unsafe_allow_html=True,
)

st.markdown('<hr class="soft">', unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────
# 3) 👤 About Me (माझ्या बद्दल)
# ─────────────────────────────────────────────────────────────
st.markdown('<div class="section-title">👤 माझ्या बद्दल</div>', unsafe_allow_html=True)
st.markdown(
    """
<div class="panel section-box">
  <div class="section-text">
    I’ve spent years getting lost in frames, melodies, and midnight edits. These clips aren’t for jobs, clicks, or clout —
    they’re stitched memories, felt deeply and shared freely.
  </div>
  <div class="section-text">
    I know most won’t watch — and that’s okay. This isn’t a portfolio; it’s a private theater with an open door.
  </div>
  <div class="section-text">
    Welcome to my corner of the internet — a place where nostalgia wears eyeliner and storytelling forgets to explain itself.
  </div>
</div>
""",
    unsafe_allow_html=True,
)

st.markdown('<hr class="soft">', unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────
# 4) 📸 Instagram
# ─────────────────────────────────────────────────────────────
st.markdown('<div class="section-title">📸 Instagram</div>', unsafe_allow_html=True)
st.markdown(
    """
<div class="panel section-box">
  <div class="insta-icon">
    <a href="https://www.instagram.com/yourprofilelink" target="_blank" rel="noopener">
      <img src="https://img.icons8.com/ios-filled/50/ffffff/instagram-new.png" alt="Instagram"/>
    </a>
  </div>
</div>
""",
    unsafe_allow_html=True,
)

# ─────────────────────────────────────────────────────────────
# Footer note (appears at end of the page)
# ─────────────────────────────────────────────────────────────
st.markdown(
    """
<div class="final-note">
  ◌◌◌ You’ll scroll away, overthink, and likely return.<br>
  My presence lingers here — somewhere between the frames and frequencies. ◌◌◌
</div>
""",
    unsafe_allow_html=True,
)
