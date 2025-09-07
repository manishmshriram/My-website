import streamlit as st
import streamlit.components.v1 as components

# --- Page Setup ---
st.set_page_config(
    page_title="Manish's Aesthetic Edits",
    page_icon="🎬",
    layout="centered",
)

# --- Dark Theme Styling ---
st.markdown("""
    <style>
    body {
        background-color: #0f0f0f;
        color: #f5f5f5;
        font-family: 'Helvetica Neue', sans-serif;
    }
    .title {
        font-size: 2.5em;
        text-align: center;
        color: #E5C07B;
        font-weight: bold;
        margin-top: 1em;
    }
    .subtitle {
        font-size: 1.2em;
        text-align: center;
        color: #abb2bf;
        margin-bottom: 2em;
    }
    .edit-link {
        font-size: 1.2em;
        color: #61afef;
        cursor: pointer;
        text-align: center;
        margin: 0.5em 0;
        transition: color 0.3s ease;
    }
    .edit-link:hover {
        color: #E06C75;
    }
    .popup {
        position: fixed;
        top: 0; left: 0;
        width: 100%; height: 100%;
        background: rgba(0,0,0,0.85);
        display: flex;
        align-items: center;
        justify-content: center;
        z-index: 9999;
    }
    .popup-content {
        background: #1e1e1e;
        padding: 1em;
        border-radius: 12px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.5);
        text-align: center;
    }
    .close-btn {
        color: #fff;
        font-size: 1.2em;
        margin-top: 0.5em;
        cursor: pointer;
    }
    </style>
""", unsafe_allow_html=True)

# --- 🎬 Edits Section ---
st.markdown("<div class='title'>🎞️ My Idiosyncratic Anthology</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Cinematic music meets unforgettable frames</div>", unsafe_allow_html=True)

video_dict = {
    "Moonlight Montage": "https://www.youtube.com/embed/oMDsZA73fJg?si=OtOy4C5yqhVqao6B",
    "Whispers in the Metro": "https://www.youtube.com/embed/NNHJxvZxyoM?si=kcdUKDzW4Vk9cesv",
    "The Silent Waltz": "https://www.youtube.com/embed/gs80fqMsU6M?si=sLRJacQA3CKUhTvG",
    "Fragments of Summer": "https://www.youtube.com/embed/OFvm21z8L-M?si=qrNKyNoF18leLjV1"
}

# --- State to track popup ---
if "popup" not in st.session_state:
    st.session_state.popup = None

for name, link in video_dict.items():
    if st.button(name, key=name):
        st.session_state.popup = link

# --- Show popup if active ---
if st.session_state.popup:
    popup_html = f"""
    <div class="popup">
        <div class="popup-content">
            <iframe width="560" height="315" src="{st.session_state.popup}" frameborder="0" allowfullscreen></iframe>
            <div class="close-btn" onclick="window.parent.postMessage('close','*')">✖ Close</div>
        </div>
    </div>
    <script>
    window.addEventListener('message', (e) => {{
        if (e.data === 'close') {{
            window.location.reload();
        }}
    }});
    </script>
    """
    components.html(popup_html, height=600)

# --- 📖 Short Story ---
st.markdown("""
<div class='section-box'>
    <div class='section-title'>📖 Ek Sauvi Raat (The 100th Night)</div>
    <div class='section-text'>
        Ek raat… ek talaab… ek main-da, jise sapne sirf chand ke dikhte the. <br><br>
        This is a tale of a poetic frog, a mysterious she-frog, a soldier, a tortoise, and the 100th night that changed everything.
    </div>
    <br>
    <div class='section-text'>
        📝 Read the full story on my <a href="https://manishshriram.art.blog/" target="_blank" style="color:#61afef;">blog</a>.
    </div>
</div>
""", unsafe_allow_html=True)

# --- 👤 About Me ---
st.markdown("""
<div class="section-box">
    <div class="section-title">👤 About Me</div>
    <div class="about-me-text">
        These edits aren’t a portfolio; they’re stitched memories — nostalgia in motion.
    </div>
</div>
""", unsafe_allow_html=True)
