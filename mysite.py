import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Manish's Aesthetic Edits",
    page_icon="🎬",
    layout="centered",
    initial_sidebar_state="auto",
)

# Custom CSS for artistic aesthetics and transitions
st.markdown("""
    <style>
    body {
        background-color: #FFF9E5;
        color: #333333;
        font-family: 'Helvetica Neue', sans-serif;
        transition: background-color 0.5s ease-in-out, color 0.5s ease-in-out;
    }
    .title {
        font-size: 3em;
        font-weight: 700;
        text-align: center;
        margin-bottom: 1em;
        color: #F9A825;  /* Warm Gold */
        text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.3);
        transition: color 0.5s ease-in-out;
    }
    .subtitle {
        font-size: 1.5em;
        text-align: center;
        margin-bottom: 3em;
        color: #5D4037;  /* Rich Brown */
        transition: color 0.5s ease-in-out;
    }
    .video-box {
        background: #FFF3C7;
        padding: 1.5em;
        border-radius: 25px;
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
        margin-bottom: 3em;
        transition: transform 0.3s ease-in-out;
    }
    .video-box:hover {
        transform: scale(1.05);
    }
    .story-box {
        background: #FFECB3;
        padding: 1.5em;
        border-radius: 15px;
        margin-top: 3em;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    }
    .story-title {
        font-size: 2.5em;
        font-weight: 700;
        color: #6A1B9A;  /* Purple for artistic touch */
        text-align: center;
        margin-bottom: 1em;
    }
    .story-text {
        font-size: 1.2em;
        color: #4E342E;
        line-height: 1.8;
        text-align: justify;
        margin-top: 1em;
        max-width: 80%;
        margin-left: auto;
        margin-right: auto;
    }
    .about-me-box {
        background: #FFEBEE;
        padding: 2em;
        border-radius: 15px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        margin-top: 3em;
    }
    .about-me-title {
        font-size: 2.5em;
        font-weight: 700;
        color: #D32F2F;
        text-align: center;
        margin-bottom: 1em;
    }
    .about-me-text {
        font-size: 1.2em;
        color: #4E342E;
        line-height: 1.8;
        text-align: justify;
    }
    .comment-section {
        margin-top: 3em;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# Title and subtitle
st.markdown("<div class=\"title\">🎞️ Manish's Aesthetic Edits</div>", unsafe_allow_html=True)
st.markdown('<div class="subtitle">Soft, minimal edits of your favorite films and music</div>', unsafe_allow_html=True)

# Video links - Replace these with actual YouTube video links
video_links = [
    "https://www.youtube.com/embed/dQw4w9WgXcQ",  # Example placeholder
    "https://www.youtube.com/embed/3JZ_D3ELwOQ",
    "https://www.youtube.com/embed/tgbNymZ7vqY"
]

# Display each video in a styled box
for link in video_links:
    st.markdown('<div class="video-box">', unsafe_allow_html=True)
    components.iframe(link, height=315)
    st.markdown('</div>', unsafe_allow_html=True)

# SoundCloud Music Embed: La La Land Instrumental
st.markdown("""
    <div style="text-align:center; margin-top: 2em;">
        <h3>Background Music: "City of Stars" - La La Land Instrumental</h3>
        <iframe width="100%" height="166" scrolling="no" frameborder="no" 
            src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/296768506&color=%23ffcc00&auto_play=true&hide_related=false&show_comments=true&show_user=true&show_reposts=false&sharing=true">
        </iframe>
    </div>
""", unsafe_allow_html=True)

# About Me Section
st.markdown('<div class="about-me-box">', unsafe_allow_html=True)
st.markdown('<div class="about-me-title">About Me</div>', unsafe_allow_html=True)
st.markdown("""
    <div class="about-me-text">
        I’m someone who spent way too much time watching films, listening to music, and ignoring career goals—now I’m putting all that mess to use. 
        These videos are special to me; they’re like a nostalgic reminder of the days I created without worrying about ‘being productive.’ 
        Now, I’m finally sharing it all in one place—because why not turn my procrastination into something vaguely resembling a portfolio?
    </div>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Comment Section
st.markdown('<div class="comment-section">', unsafe_allow_html=True)
st.text_area("Leave a comment:", "Comments are welcome—just make sure they’re almost as good as this content.")
st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("""
    <hr>
    <div style='text-align:center; font-size: 0.9em; color: #999;'>
        © 2025 Manish Shriram | Aesthetic Edits
    </div>
""", unsafe_allow_html=True)
