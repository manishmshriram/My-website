# app.py
# Streamlit cinematic portfolio styled after indrajeetmore.com
# - Drop-in variables at top to change video / story / insta links
# - Uses custom CSS via st.markdown(..., unsafe_allow_html=True)
# - YouTube embeds list at top (yt_ids)
# - Uses the provided Drive image as poster/background for now

import streamlit as st
import streamlit.components.v1 as components

# -------------------------
# Config / Replaceable URLs
# -------------------------
VIDEO_SRC = ""  # e.g. "https://your-blob-or-cdn/video.mp4" (leave empty to use poster image)
POSTER_IMAGE = "https://drive.google.com/uc?export=view&id=1boW3ZgpXPH__2hSF2qA-2pQT31JoyZVw"  # user-supplied Google Drive preview -> direct view format
STORY_URL = "https://your-wordpress-story.example.com"  # replace with your WordPress story link
INSTAGRAM_URL = "https://instagram.com/yourinstagram"  # replace with your Instagram
# List of YouTube IDs to embed in "My Edits". Use only the video id (after v=)
YT_IDS = [
    "dQw4w9WgXcQ",  # placeholder — replace with your YouTube video ids
    "9bZkp7q19f0",
    "kXYiU_JCYtU"
]

# -------------------------
# Page config
# -------------------------
st.set_page_config(
    page_title="Manish Shriram — Edits & Story",
    page_icon="🎞️",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Keep Streamlit UI minimal by hiding menu & footer
hide_streamlit_style = """
    <style>
    /* hide default header and footer */
    #MainMenu, footer, header {visibility: hidden;}
    html, body, [data-testid="stAppViewContainer"] {
        background: #0b0b0b; /* deep dark background */
    }
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# -------------------------
# CSS, fonts, animations
# -------------------------
# Note: Google Fonts loaded inside CSS block so fonts are available
css = f"""
<!-- Fonts -->
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&family=Poppins:wght@300;400;600&family=Noto+Sans+Devanagari:wght@400;700&display=swap" rel="stylesheet">

<style>
:root {{
    --accent: #ffffff;
    --muted: rgba(255,255,255,0.66);
    --overlay: rgba(6,6,6,0.55);
    --glass: rgba(255,255,255,0.03);
}}

/* Full-viewport hero with video or poster */
.hero {{
    position: relative;
    width: 100%;
    height: 100vh;
    min-height: 560px;
    overflow: hidden;
    display: flex;
    align-items: center;
    justify-content: center;
    color: var(--accent);
}}

/* video sits as background cover */
.hero video, .hero .poster {{
    position: absolute;
    top: 50%;
    left: 50%;
    width: auto;
    height: 120%;
    min-width: 120%;
    transform: translate(-50%, -50%);
    object-fit: cover;
    z-index: 0;
    filter: brightness(0.54) saturate(0.9);
}

/* fallback poster image */
.hero .poster {{
    background-image: url("{POSTER_IMAGE}");
    background-size: cover;
    background-position: center center;
    width: 100%;
    height: 100%;
}}

/* soft dark overlay for text readability */
.hero::after {{
    content: "";
    position: absolute;
    inset: 0;
    background: linear-gradient(180deg, rgba(4,4,4,0.48) 0%, rgba(4,4,4,0.72) 100%);
    z-index: 1;
}}

/* type / title container centered */
.title-wrap {{
    position: relative;
    z-index: 2;
    text-align: center;
    width: 100%;
    padding: 30px;
    pointer-events: auto;
}}

/* cinematic serif for name */
.main-name {{
    font-family: 'Playfair Display', serif;
    font-size: clamp(40px, 8vw, 98px);
    letter-spacing: -0.02em;
    line-height: 0.95;
    font-weight: 700;
    margin: 0 auto 8px auto;
    display: inline-block;
    color: white;
    text-rendering: geometricPrecision;
    transition: transform 0.6s cubic-bezier(.22,.9,.32,1);
}

/* two-layer text for hover morph */
.name-layer {{
    position: relative;
    display:inline-block;
    overflow: visible;
}}
.name-front, .name-back {{
    display:block;
    transition: opacity 0.9s cubic-bezier(.22,.9,.32,1), transform 0.9s cubic-bezier(.22,.9,.32,1);
    transform-origin: center;
}
/* front = latin, back = devanagari */
.name-front {{
    opacity: 1;
}}
.name-back {{
    position: absolute;
    left: 0;
    top: 0;
    width: 100%;
    opacity: 0;
    transform: translateY(6%) scale(0.98);
    font-family: 'Noto Sans Devanagari', 'Playfair Display', serif;
    font-size: inherit;
    pointer-events: none;
}

/* organic 'morph' on hover */
.name-layer:hover .name-front {{
    opacity: 0;
    transform: translateY(-6%) scale(0.98);
}}
.name-layer:hover .name-back {{
    opacity: 1;
    transform: translateY(0) scale(1);
}}

/* small top-left label similar to 'Film is my thing' */
.top-left {{
    position: absolute;
    left: 36px;
    top: 36px;
    z-index: 3;
    font-family: 'Poppins', sans-serif;
    font-size: 14px;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    color: var(--muted);
    opacity: 0.95;
}}

/* second small link under top-left */
.top-left .sub {{
    display:block;
    margin-top: 8px;
    font-size: 13px;
    color: rgba(255,255,255,0.78);
    text-decoration: none;
}}

/* subtle CTA arrow beneath name */
.scroll-down {{
    margin-top: 20px;
    font-family: 'Poppins', sans-serif;
    color: var(--muted);
    font-size: 13px;
    letter-spacing: 0.08em;
    display: inline-flex;
    align-items: center;
    gap: 10px;
    opacity: 0.95;
}}

/* content container sections */
.container {{
    max-width: 1100px;
    margin: 72px auto;
    padding: 8px 22px 80px 22px;
    color: var(--muted);
    font-family: 'Poppins', sans-serif;
}}

/* Edits grid */
.edits-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 20px;
    align-items: start;
}}

/* YouTube embed wrapper to preserve aspect ratio */
.yt-wrap {{
    position: relative;
    width: 100%;
    padding-bottom: 56.25%;
    background: #070707;
    border-radius: 8px;
    overflow: hidden;
    box-shadow: 0 8px 30px rgba(0,0,0,0.6);
}}

/* short story card */
.story-card {{
    background: linear-gradient(180deg, rgba(255,255,255,0.02), rgba(255,255,255,0.01));
    border-radius: 12px;
    padding: 22px;
    color: var(--muted);
    box-shadow: 0 10px 40px rgba(2,2,2,0.6);
    backdrop-filter: blur(6px);
}}

/* About me - centered with soft fade-up animation */
.about {{
    text-align:center;
    padding: 30px;
    margin-top: 10px;
    animation: fadeUp 0.9s ease both;
    color: var(--muted);
    font-size: 16px;
}}
@keyframes fadeUp {{
    from {{ opacity: 0; transform: translateY(12px); }}
    to   {{ opacity: 1; transform: translateY(0); }}
}}

/* Instagram minimal icon */
.insta {{
    display:flex;
    align-items:center;
    justify-content:center;
    font-size: 20px;
    margin-top: 14px;
}}
.insta a {{
    color: white;
    text-decoration: none;
    display:inline-flex;
    align-items:center;
    justify-content:center;
    width: 48px;
    height: 48px;
    border-radius: 999px;
    background: rgba(255,255,255,0.02);
    box-shadow: 0 6px 18px rgba(0,0,0,0.6);
    transition: transform .25s ease, box-shadow .25s ease;
}}
.insta a:hover {{
    transform: translateY(-6px) scale(1.02);
    box-shadow: 0 12px 30px rgba(255,255,255,0.06);
    filter: drop-shadow(0 0 10px rgba(255,255,255,0.08));
}}

/* responsive tweaks */
@media (max-width: 640px) {{
    .top-left {{ left: 18px; top: 18px; font-size: 12px; }}
    .title-wrap {{ padding: 18px; }}
    .main-name {{ font-size: clamp(34px, 12vw, 56px); }}
}}
</style>
"""

# -------------------------
# Hero HTML (video or poster)
# -------------------------
# Build hero block with either a <video> element or background poster image fallback
hero_html = f"""
{css}
<div class="hero" id="home">
    {"<video autoplay muted loop playsinline class='bg-video' src='" + VIDEO_SRC + "'>" if VIDEO_SRC else ""}
    {"</video>" if VIDEO_SRC else ""}
    <div class="poster" style="background-image: url('{POSTER_IMAGE}');"></div>

    <div class="top-left">
        <div>My Edits</div>
        <a class="sub" href="#short-story">Short Story</a>
    </div>

    <div class="title-wrap">
        <!-- Animated name: Latin -> Devanagari on hover -->
        <div class="main-name">
            <span class="name-layer" title="Manish Shriram — hover to see Marathi">
                <span class="name-front">Manish Shriram</span>
                <span class="name-back">मनीष श्रीराम</span>
            </span>
        </div>

        <div class="scroll-down">
            <a href="#edits" style="color: rgba(255,255,255,0.8); text-decoration:none;">Explore edits ↓</a>
        </div>
    </div>
</div>
"""
# Render hero
st.markdown(hero_html, unsafe_allow_html=True)

# -------------------------
# Content sections (edits, story, about, insta)
# -------------------------
# Container start
st.markdown('<div class="container">', unsafe_allow_html=True)

# Edits Section
st.markdown('<section id="edits">', unsafe_allow_html=True)
st.markdown('<h2 style="color: white; font-family: Playfair Display, serif; font-size:28px; margin-bottom:12px;">Edits</h2>', unsafe_allow_html=True)
# grid container
st.markdown('<div class="edits-grid">', unsafe_allow_html=True)

# Embed YouTube thumbnails/iframes. Use aspect-ratio preserving wrappers.
for vid in YT_IDS:
    # iframe embed HTML
    iframe = f"""
    <div class="yt-wrap">
        <iframe src="https://www.youtube.com/embed/{vid}?rel=0&modestbranding=1" 
            frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
            allowfullscreen style="position:absolute; inset:0; width:100%; height:100%; border:0;"></iframe>
    </div>
    """
    st.markdown(iframe, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)  # edits-grid
st.markdown('</section>', unsafe_allow_html=True)

# Short Story Section
st.markdown('<section id="short-story" style="margin-top:44px;">', unsafe_allow_html=True)
st.markdown('<h2 style="color: white; font-family: Playfair Display, serif; font-size:28px; margin-bottom:12px;">Short Story</h2>', unsafe_allow_html=True)
story_html = f"""
<div class="story-card">
    <h3 style="font-family: Playfair Display, serif; color: white; margin-top:0;">Ek Sauvi Raat — A short excerpt</h3>
    <p style="color:var(--muted); line-height:1.6;">
        A cinematic, whimsical short story blending humor and quiet melancholy. This is a small taste —
        click through to read the full story on WordPress.
    </p>
    <a href="{STORY_URL}" target="_blank" style="display:inline-block; margin-top:12px; padding:10px 14px; border-radius:8px; 
       background: rgba(255,255,255,0.04); color: white; text-decoration:none; font-family: Poppins, sans-serif;">
       Read the full story →
    </a>
</div>
"""
st.markdown(story_html, unsafe_allow_html=True)
st.markdown('</section>', unsafe_allow_html=True)

# About Me Section
st.markdown('<section id="about" style="margin-top:56px;">', unsafe_allow_html=True)
st.markdown('<h2 style="color: white; font-family: Playfair Display, serif; font-size:28px; margin-bottom:12px;">About Me</h2>', unsafe_allow_html=True)
about_text = """
<div class="about">
    <p style="max-width:900px; margin:0 auto; color:var(--muted); font-size:15px;">
        Hello — I'm Manish Shriram. I make aesthetic edits, write short stories, and explore cinematic imagery.
        My work lives at the intersection of memory, music and motion. I favor minimal palettes, smooth transitions,
        and a quiet, resonant mood.
    </p>
</div>
"""
st.markdown(about_text, unsafe_allow_html=True)
st.markdown('</section>', unsafe_allow_html=True)

# Instagram icon centered
insta_html = f"""
<div style="display:flex; justify-content:center; align-items:center; margin-top:28px;">
    <div class="insta">
        <a href="{INSTAGRAM_URL}" target="_blank" aria-label="Instagram">
            <!-- simple inline SVG instagram icon -->
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" aria-hidden="true" xmlns="http://www.w3.org/2000/svg">
                <rect x="2" y="2" width="20" height="20" rx="5" stroke="white" stroke-opacity="0.95" stroke-width="1.2" fill="transparent"/>
                <circle cx="12" cy="12" r="3.2" stroke="white" stroke-opacity="0.95" stroke-width="1.2" fill="transparent"/>
                <circle cx="17.5" cy="6.5" r="0.7" fill="white" fill-opacity="0.95"/>
            </svg>
        </a>
    </div>
</div>
"""
st.markdown(insta_html, unsafe_allow_html=True)

# Container end
st.markdown('</div>', unsafe_allow_html=True)

# -------------------------
# Optional: background audio toggle (kept minimal)
# -------------------------
# Only activates if user wants to provide a music file. Many browsers block autoplay of audio;
# the toggle lets user start sound intentionally. Replace AUDIO_SRC with your audio link to enable.
AUDIO_SRC = ""  # e.g. "https://your-cdn/music.mp3"
if AUDIO_SRC:
    audio_html = f"""
    <div style="position: fixed; right: 18px; bottom: 18px; z-index: 9999;">
        <button id="audio-btn" style="padding:10px 12px; background: rgba(255,255,255,0.03); color: white; border-radius: 10px; border: none;">
            ▶ Music
        </button>
        <audio id="bg-audio" src="{AUDIO_SRC}" loop></audio>
    </div>
    <script>
        const btn = document.getElementById('audio-btn');
        const audio = document.getElementById('bg-audio');
        btn.addEventListener('click', () => {{
            if (audio.paused) {{
                audio.play();
                btn.innerText = "🔊 Music";
            }} else {{
                audio.pause();
                btn.innerText = "▶ Music";
            }}
        }});
    </script>
    """
    st.markdown(audio_html, unsafe_allow_html=True)

# -------------------------
# Accessibility / Quick nav (invisible but useful)
# -------------------------
nav_html = """
<style>
.skip-nav {position: absolute; left:-9999px; top:auto; width:1px; height:1px; overflow:hidden;}
</style>
<a class="skip-nav" href="#edits">Skip to edits</a>
"""
st.markdown(nav_html, unsafe_allow_html=True)

# -------------------------
# Footer small credits
# -------------------------
st.markdown("""
<div style="text-align:center; color: rgba(255,255,255,0.45); padding:28px 0; font-family:Poppins, sans-serif;">
    Designed & coded with care — minimal cinematic UI for Manish. Replace media & links at the top of app.py.
</div>
""", unsafe_allow_html=True)
