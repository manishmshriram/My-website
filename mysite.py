# Save as: app.py  (or replace your existing Streamlit app file)
import streamlit as st
import streamlit.components.v1 as components
import os, random, re, base64

# ---------- PAGE SETUP ----------
st.set_page_config(page_title="Manish's Aesthetic Edits", page_icon="🎬", layout="centered")

# ---------- ASSETS & VIDEOS ----------
# Put your videos here (embed URLs). The hero will autoplay muted for nicer UX.
VIDEO_EMBEDS = [
    "https://www.youtube.com/embed/oMDsZA73fJg?rel=0",
    "https://www.youtube.com/embed/NNHJxvZxyoM?rel=0",
    "https://www.youtube.com/embed/gs80fqMsU6M?rel=0",
    "https://www.youtube.com/embed/OFvm21z8L-M?rel=0",
    "https://www.youtube.com/embed/o4XQkw0k5To?rel=0",
    "https://www.youtube.com/embed/ZUhU4izZbi0?rel=0",
    "https://www.youtube.com/embed/wDzCeqzgmoA?rel=0",
    "https://www.youtube.com/embed/PPOYOUFk4Hw?rel=0",
    "https://www.youtube.com/embed/WAsDEw1HKG4?rel=0",
    "https://www.youtube.com/embed/y6JbWgHx7po?rel=0",
    "https://www.youtube.com/embed/aNFGiVwt4uE?rel=0",
    # Paperman rescored (kept in list)
    "https://www.youtube.com/embed/EI__XUxw8j8?rel=0",
]

# Optional friendly titles (same length as VIDEO_EMBEDS)
VIDEO_TITLES = [
    "Edit 1",
    "Edit 2",
    "Edit 3",
    "Edit 4",
    "Edit 5",
    "Edit 6",
    "Edit 7",
    "Edit 8",
    "Edit 9",
    "Edit 10",
    "Edit 11",
    "Paperman — Rescored",
]

# ---------- FONT: optional AMS Vasudeva ----------
# If you want the Marathi Devnagari font effect using AMS Vasudeva:
# Put the TTF file at: assets/fonts/AMS-Vasudeva-Regular.ttf in your repo.
# The code below will embed it only if it exists (safe).
def generate_font_face_css():
    font_path = "assets/fonts/AMS-Vasudeva-Regular.ttf"
    if os.path.exists(font_path):
        try:
            with open(font_path, "rb") as f:
                b64 = base64.b64encode(f.read()).decode()
            return f"""
            @font-face {{
                font-family: 'AMS Vasudeva';
                src: url(data:font/ttf;base64,{b64}) format('truetype');
                font-weight: 400;
                font-style: normal;
                font-display: swap;
            }}
            """
        except Exception:
            return ""
    return ""

font_face_css = generate_font_face_css()

# ---------- CSS (clean, cinematic) ----------
st.markdown(
    f"""
<style>
{font_face_css}

/* Basic colors */
:root {{
  --bg: #0f0f10;
  --card: #121214;
  --muted: #bdbfc4;
  --accent: #E5C07B;
  --accent2: #61afef;
  --rose: #E06C75;
  --radius: 14px;
}}

/* Page base */
body, .stApp {{
  background: linear-gradient(180deg, var(--bg), #0b0b0c);
  color: #e9e9ea;
  font-family: 'Poppins', 'Segoe UI', Roboto, 'Noto Sans', sans-serif;
}}

/* Header */
.header {{
  text-align: center;
  padding-top: 18px;
  margin-bottom: 6px;
}}
.site-name {{
  display:inline-block;
  font-size: clamp(26px, 4.2vw, 42px);
  font-weight:700;
  color: var(--accent);
  padding: .25rem .6rem;
  border-radius: 10px;
  background: rgba(229,192,123,0.06);
}}
.site-sub {{
  color: var(--muted);
  margin-top:6px;
  font-size: 15px;
}}

/* hover name swap */
.name-hover .marathi {{ display:none; }}
.name-hover:hover .english {{ display:none; }}
.name-hover:hover .marathi {{
  display:inline-block;
  font-family: 'AMS Vasudeva', 'Noto Sans Devanagari', serif;
}}

/* Hero */
.hero-wrap {{
  width:100%;
  border-radius: 16px;
  overflow:hidden;
  margin: 12px 0 18px;
  box-shadow: 0 18px 36px rgba(0,0,0,0.6);
  border: 1px solid rgba(255,255,255,0.04);
}}
.controls {{
  display:flex; gap:8px; justify-content:center; align-items:center; margin-top:8px;
}}
.btn {{
  background:#1a1a1b; padding:.5rem .8rem; border-radius:10px; border:1px solid rgba(255,255,255,0.06);
  cursor:pointer; color: #eaeaea;
}}
.btn:hover {{ transform: translateY(-2px); }}

/* Grid */
.grid {{
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 12px;
}}
@media (max-width: 900px) {{
  .grid {{ grid-template-columns: repeat(2, 1fr); }}
}}
@media (max-width: 560px) {{
  .grid {{ grid-template-columns: repeat(1, 1fr); }}
}}
.card {{
  background: var(--card);
  border-radius: 12px;
  overflow:hidden; position:relative; border:1px solid rgba(255,255,255,0.04);
}}
.thumb{{ width:100%; height:160px; object-fit:cover; display:block; }}
.card .meta {{ padding:.6rem .75rem; font-size:14px; color:var(--muted); display:flex; justify-content:space-between; align-items:center; }}

/* section title */
.section-title {{ text-align:center; color:var(--rose); font-weight:700; margin:8px 0; font-size:18px; }}

/* CTA button */
.cta {{
  display:inline-block; padding:.55rem .9rem; border-radius:10px; margin-top:8px;
  background: linear-gradient(90deg, rgba(97,175,239,0.12), rgba(229,192,123,0.06));
  border:1px solid rgba(255,255,255,0.04); color:#dff0ff; text-decoration:none;
}}

/* final note */
.final-note {{
  text-align:center; color:#7b7f86; font-style:italic; margin: 22px 0;
}}
</style>
""",
    unsafe_allow_html=True,
)

# ---------- HELPER FUNCTIONS ----------
def yt_id_from_embed(url):
    # expects /embed/<id>
    m = re.search(r"/embed/([\\w-]+)", url)
    return m.group(1) if m else ""

def thumb_for(embed):
    vid = yt_id_from_embed(embed)
    return f"https://img.youtube.com/vi/{vid}/hqdefault.jpg" if vid else ""

# Initialize session state
if "playlist" not in st.session_state:
    st.session_state.playlist = VIDEO_EMBEDS.copy()
    random.shuffle(st.session_state.playlist)
if "current_idx" not in st.session_state:
    st.session_state.current_idx = 0

# ---------- HEADER ----------
st.markdown(
    """
    <div class="header">
      <div class="site-name name-hover">
        <span class="english">Manish Shriam</span>
        <span class="marathi">मनीष श्रीराम</span>
      </div>
      <div class="site-sub">Cinematic music ⋅ midnight edits ⋅ short stories</div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ---------- AMATEUR EDITS: HERO ----------
st.markdown('<div class="section-title">🎬 Amateur Edits</div>', unsafe_allow_html=True)

def hero_iframe(embed_url, autoplay=True, height=480):
    extra = "&autoplay=1&mute=1&playsinline=1" if autoplay else ""
    return f"""
    <div class="hero-wrap">
      <iframe width="100%" height="{height}" src="{embed_url}{extra}" frameborder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
        allowfullscreen></iframe>
    </div>
    """

current = st.session_state.playlist[st.session_state.current_idx]
st.markdown(hero_iframe(current, autoplay=True), unsafe_allow_html=True)

# Controls
cols = st.columns([1,1,1])
with cols[0]:
    if st.button("◀ Previous", key="prev"):
        st.session_state.current_idx = (st.session_state.current_idx - 1) % len(st.session_state.playlist)
        st.experimental_rerun()
with cols[1]:
    if st.button("🔀 Shuffle", key="shuffle"):
        random.shuffle(st.session_state.playlist)
        st.session_state.current_idx = 0
        st.experimental_rerun()
with cols[2]:
    if st.button("Next ▶", key="next"):
        st.session_state.current_idx = (st.session_state.current_idx + 1) % len(st.session_state.playlist)
        st.experimental_rerun()

st.markdown("<br/>", unsafe_allow_html=True)

# ---------- GRID OF THUMBNAILS ----------
st.markdown('<div class="section-title">All Edits</div>', unsafe_allow_html=True)
# Display grid using columns to control responsive layout
num_cols = 3
thumbs = st.session_state.playlist
# map embed -> title if provided
embed_to_title = {VIDEO_EMBEDS[i]: VIDEO_TITLES[i] for i in range(min(len(VIDEO_EMBEDS), len(VIDEO_TITLES)))}

rows = []
for i in range(0, len(thumbs), num_cols):
    row = st.columns(num_cols)
    for j, col in enumerate(row):
        idx = i + j
        if idx >= len(thumbs):
            col.write("")
            continue
        embed = thumbs[idx]
        thumb = thumb_for(embed)
        title = embed_to_title.get(embed, f"Edit {idx+1}")
        with col:
            st.markdown(
                f"""
                <div class="card">
                  <img class="thumb" src="{thumb}" alt="{title}">
                  <div class="meta">
                    <div style="font-weight:600">{title}</div>
                    <form><button class="btn" name="play_{idx}" type="submit">Play ▶</button></form>
                  </div>
                </div>
                """,
                unsafe_allow_html=True,
            )
            # Each thumbnail gets a server-side button below so it works robustly
            if st.button(f"Play {idx+1}", key=f"play_btn_{idx}"):
                st.session_state.current_idx = idx
                st.experimental_rerun()

st.markdown("<hr/>", unsafe_allow_html=True)

# ---------- SHORT STORY ----------
st.markdown('<div class="section-title">📖 Short Story</div>', unsafe_allow_html=True)
st.markdown(
    """
    <div style="text-align:center; max-width:720px; margin-left:auto; margin-right:auto;">
      <p style="color:#c8cbd0; font-size:16px; line-height:1.7;">
        <strong>Ek Sauvi Raat (The 100th Night)</strong> — a small, strange, tender story of a frog, a soldier, a mysterious she-frog, and a night that quietly rearranged everything.
      </p>
      <p style="color:#bdbfc4; font-size:15px;">Click through to read the full piece — if you like cinematic melancholy, you'll stay.</p>
      <a class="cta" href="https://manishshriram.art.blog/" target="_blank" rel="noopener">Read the full story on my blog ↗</a>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown("<hr/>", unsafe_allow_html=True)

# ---------- ABOUT ME (माझ्या बद्दल) ----------
st.markdown('<div class="section-title">👤 माझ्या बद्दल</div>', unsafe_allow_html=True)
st.markdown(
    """
    <div style="max-width:860px; margin-left:auto; margin-right:auto; background:#0f0f10; padding:14px; border-radius:12px; border:1px solid rgba(255,255,255,0.03)">
      <p style="color:#c9ccd0; font-size:15px; line-height:1.7;">
        I’ve spent years getting lost in frames, melodies, and midnight edits. These clips aren’t for jobs, clicks, or clout — they are stitched memories,
        quietly crafted and shared. If something here feels familiar, it's because nostalgia likes to wear eyeliner.
      </p>
      <p style="color:#bdbfc4; font-size:14px; margin-top:6px;">
        This corner is private theater with an open door. Sit, watch, leave — return whenever.
      </p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown("<hr/>", unsafe_allow_html=True)

# ---------- INSTAGRAM ----------
st.markdown('<div class="section-title">📸 Instagram</div>', unsafe_allow_html=True)
st.markdown(
    """
    <div style="text-align:center;">
      <a href="https://www.instagram.com/yourprofilelink" target="_blank" rel="noopener">
        <img src="https://img.icons8.com/ios-filled/50/ffffff/instagram-new.png" style="width:46px;height:46px;filter:brightness(0) invert(1);">
      </a>
    </div>
    """,
    unsafe_allow_html=True,
)

# ---------- FINAL NOTE ----------
st.markdown(
    """
    <div class="final-note">
      ◌◌◌ You’ll scroll away, overthink, and likely return.<br>
      My presence lingers here — somewhere between the frames and frequencies. ◌◌◌
    </div>
    """,
    unsafe_allow_html=True,
)
