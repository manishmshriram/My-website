# app.py
import streamlit as st
import streamlit.components.v1 as components
import os, re, base64

# -------- PAGE CONFIG --------
st.set_page_config(page_title="Manish Shriram", layout="wide", page_icon="🎬")

# --------- Optional: embed AMS Vasudeva font if present ----------
def embed_local_font_css():
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

font_face_css = embed_local_font_css()

# --------- CORE CSS + HERO VIDEO + overlay (left menu) ----------
st.markdown(
    f"""
<style>
/* Embedded font (if present) */
{font_face_css}

/* Basic layout & colors */
:root {{
  --bg: #000000;
  --muted: #d0d2d6;
  --accent: #E5C07B;   /* warm gold */
  --accent2: #61afef;
}}

html, body, .stApp {{
  margin: 0; padding: 0; background: black; color: #fff;
  font-family: "Helvetica Neue", "Poppins", system-ui, -apple-system, "Segoe UI", Roboto, "Noto Sans", sans-serif;
}}

/* Full-screen hero video */
video.hero {{
  position: fixed;
  top: 0; left: 0;
  width: 100%;
  height: 100vh;
  object-fit: cover;
  z-index: -1; /* behind overlay and content */
  filter: brightness(0.55) saturate(1.02);
}}

/* translucent overlay to help text contrast (only on left area) */
.left-overlay {{
  position: fixed;
  top: 6vh;
  left: 3vw;
  max-width: 320px;
  z-index: 10;
  color: white;
  -webkit-font-smoothing: antialiased;
  text-rendering: optimizeLegibility;
}}

/* The name block */
.site-name {{
  font-size: clamp(26px, 4.5vw, 56px);
  font-weight: 800;
  line-height: 0.9;
  margin: 0 0 6px 0;
  letter-spacing: -1px;
  color: white;
}}

/* Title / subtitle */
.site-subtitle {{
  color: var(--accent);
  font-weight: 600;
  margin-bottom: 18px;
  font-size: clamp(12px, 1.4vw, 16px);
}}

/* Menu (vertical) */
.left-menu {{
  margin-top: 18px;
  display: flex;
  flex-direction: column;
  gap: 10px;
}}
.left-menu a {{
  color: #fff;
  text-decoration: none;
  font-size: clamp(15px, 1.8vw, 20px);
  transition: color .18s ease, transform .12s ease;
}}
.left-menu a:hover {{
  color: var(--accent);
  transform: translateX(4px);
}}

/* Add subtle left border to hint menu area */
.left-overlay::after {{
  content: "";
  position: absolute;
  left: -22px;
  top: -6px;
  bottom: -6px;
  width: 12px;
  background: linear-gradient(180deg, rgba(0,0,0,0.35), rgba(0,0,0,0.1));
  border-radius: 8px;
  display: none; /* optional; looks good on larger screens */
}}

/* Page content container: push content down so it doesn't overlap hero menu */
.content-wrapper {{
  position: relative;
  z-index: 5;
  padding-top: 100vh; /* ensures page content starts below the full-screen hero */
}}

/* Sections */
.section {{
  max-width: 980px;
  margin-left: auto;
  margin-right: auto;
  padding: 48px 24px;
  color: #e9e9ea;
}}
.section h2 {{
  margin: 0 0 18px 0;
  color: #f4eeee;
  font-size: 26px;
}}
.section .muted {{
  color: #bfbfbf;
  margin-bottom: 12px;
  line-height: 1.7;
  font-size: 15px;
}}

/* Grid for edits (responsive) */
.edit-grid {{
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 14px;
}}
@media (max-width: 980px) {{
  .edit-grid {{ grid-template-columns: repeat(2, 1fr); }}
}}
@media (max-width: 560px) {{
  .edit-grid {{ grid-template-columns: repeat(1, 1fr); }}
}}
.edit-card {{
  border-radius: 10px;
  overflow: hidden;
  background: rgba(255,255,255,0.03);
  border: 1px solid rgba(255,255,255,0.04);
}}
.thumbnail {{
  width: 100%;
  display: block;
  object-fit: cover;
}}
.card-meta {{ padding: 10px 12px; display:flex; justify-content:space-between; align-items:center; color:var(--muted); }}

/* CTA link */
.cta {{
  display:inline-block;
  padding:10px 14px;
  border-radius:10px;
  background: rgba(97,175,239,0.12);
  border: 1px solid rgba(97,175,239,0.22);
  color: #dff3ff;
  text-decoration:none;
}}

.final-note {{
  text-align:center;
  color:#9aa0a6;
  font-style: italic;
  margin: 36px 0 80px 0;
}}

/* Name hover swap: English -> Marathi */
.name-hover .marathi {{ display: none; }}
.name-hover:hover .english {{ display: none; }}
.name-hover:hover .marathi {{
  display:inline-block;
  font-family: 'AMS Vasudeva', 'Noto Sans Devanagari', sans-serif;
}}

/* small adjustments to keep content readable over video on small screens */
@media (max-width: 600px) {{
  .site-name {{ font-size: 28px; }}
  .left-overlay {{ left: 4vw; top: 4vh; max-width: 260px; }}
}}
</style>

<!-- HERO VIDEO -->
<video class="hero" autoplay loop muted playsinline>
  <source src="Hero.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

<!-- LEFT CORNER OVERLAY with menu -->
<div class="left-overlay">
  <div class="site-name name-hover">
    <span class="english">Manish Shriram</span>
    <span class="marathi">मनीष श्रीराम</span>
  </div>
  <div class="site-subtitle">Director | Visual Artist</div>

  <nav class="left-menu" aria-label="Main navigation">
    <a href="#edits">Edits</a>
    <a href="#shortstory">Short Story</a>
    <a href="#about">About Me</a>
    <a href="#instagram">Instagram</a>
  </nav>
</div>

<!-- Simple JS for smooth anchor scrolling -->
<script>
document.addEventListener('DOMContentLoaded', function() {{
  const anchors = document.querySelectorAll('a[href^="#"]');
  anchors.forEach(a => {{
    a.addEventListener('click', function(e) {{
      e.preventDefault();
      const id = this.getAttribute('href');
      const target = document.querySelector(id);
      if (target) {{
        target.scrollIntoView({{behavior: 'smooth', block: 'start'}});
      }}
    }});
  }});
}});
</script>
""",
    unsafe_allow_html=True,
)

# --------- CONTENT STARTS BELOW HERO (push down so hero remains background) ----------
st.markdown('<div class="content-wrapper">', unsafe_allow_html=True)

# ---------- Data: your edits (YouTube embed URLs and titles) ----------
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
    "https://www.youtube.com/embed/EI__XUxw8j8?rel=0",  # Paperman rescored
]
VIDEO_TITLES = [
    "Edit — 1",
    "Edit — 2",
    "Edit — 3",
    "Edit — 4",
    "Edit — 5",
    "Edit — 6",
    "Edit — 7",
    "Edit — 8",
    "Edit — 9",
    "Edit — 10",
    "Edit — 11",
    "Paperman — Rescored",
]

def yt_id_from_embed(url):
    m = re.search(r"/embed/([\\w-]+)", url)
    return m.group(1) if m else None

def thumb_for(embed):
    vid = yt_id_from_embed(embed)
    return f"https://img.youtube.com/vi/{vid}/hqdefault.jpg" if vid else ""

# Session state for selected edit
if "selected_idx" not in st.session_state:
    st.session_state.selected_idx = 0

# ------- Edits Section (anchor) -------
st.markdown('<div id="edits" class="section">', unsafe_allow_html=True)
st.markdown("<h2>✂️ Amateur Edits</h2>", unsafe_allow_html=True)
st.markdown('<div class="muted">A curated set of small edits — music, frames and memory. Click a thumbnail to open that edit below.</div>', unsafe_allow_html=True)

# Grid of thumbnails
cols = st.columns(3)
for i, embed in enumerate(VIDEO_EMBEDS):
    col = cols[i % 3]
    thumb = thumb_for(embed)
    title = VIDEO_TITLES[i] if i < len(VIDEO_TITLES) else f"Edit {i+1}"
    with col:
        # Card HTML
        st.markdown(
            f"""
            <div class="edit-card">
              <img class="thumbnail" src="{thumb}" alt="{title}" />
              <div class="card-meta">
                <div style="font-weight:600">{title}</div>
                <form>
                  <button class="cta" name="play_{i}" type="submit">Play ▶</button>
                </form>
              </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        # Robust server-side button to change selected video
        if st.button(f"play_btn_{i}", key=f"play_btn_{i}"):
            st.session_state.selected_idx = i
            st.rerun()

st.markdown("</div>", unsafe_allow_html=True)

# Player area (shows the selected video)
selected_embed = VIDEO_EMBEDS[st.session_state.selected_idx]
st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown("<h2>▶ Now Playing</h2>", unsafe_allow_html=True)
# large embedded player
components.iframe(selected_embed, height=480)
st.markdown("</div>", unsafe_allow_html=True)

# ------- Short Story Section -------
st.markdown('<div id="shortstory" class="section">', unsafe_allow_html=True)
st.markdown("<h2>📖 Short Story — Ek Sauvi Raat (The 100th Night)</h2>", unsafe_allow_html=True)
st.markdown(
    """
    <div class="muted">
      Ek raat… ek talaab… ek main-da, jise sapne sirf chand ke dikhte the.  
      This is a small strange story of a poetic frog, a soldier, a mysterious she-frog, and the 100th night that rearranged things quietly.
    </div>
    <p style="margin-top:10px;">
      <a class="cta" href="https://manishshriram.art.blog/" target="_blank" rel="noopener">Read the full story on my blog ↗</a>
    </p>
    """,
    unsafe_allow_html=True,
)
st.markdown("</div>", unsafe_allow_html=True)

# ------- About Me Section -------
st.markdown('<div id="about" class="section">', unsafe_allow_html=True)
st.markdown("<h2>👤 About Me</h2>", unsafe_allow_html=True)
st.markdown(
    """
    <div class="muted">
      I’ve spent years getting lost in frames, melodies, and midnight edits. These clips aren’t for jobs, clicks, or clout — they’re stitched memories, felt deeply and shared freely.
    </div>
    <div style="margin-top:8px; color:#cfcfcf;">
      I know most won’t watch — and that’s okay. This isn’t a portfolio; it’s a private theater with an open door.
    </div>
    """,
    unsafe_allow_html=True,
)
st.markdown("</div>", unsafe_allow_html=True)

# ------- Instagram Section -------
st.markdown('<div id="instagram" class="section">', unsafe_allow_html=True)
st.markdown("<h2>📸 Instagram</h2>", unsafe_allow_html=True)
st.markdown(
    """
    <div style="margin-top:6px;">
      <a href="https://www.instagram.com/yourprofilelink" target="_blank" rel="noopener">
        <img src="https://img.icons8.com/ios-filled/60/ffffff/instagram-new.png" alt="Instagram" style="width:56px;height:56px;filter:brightness(0) invert(1);">
      </a>
    </div>
    """,
    unsafe_allow_html=True,
)
st.markdown("</div>", unsafe_allow_html=True)

# ------- FINAL NOTE (always last) -------
st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown(
    """
    <div class="final-note">
      ◌◌◌ You’ll scroll away, overthink, and likely return.<br>
      My presence lingers here — somewhere between the frames and frequencies. ◌◌◌
    </div>
    """,
    unsafe_allow_html=True,
)
st.markdown("</div>", unsafe_allow_html=True)  # close content-wrapper
