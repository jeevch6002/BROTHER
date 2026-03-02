import streamlit as st
from streamlit.components.v1 import html
import base64

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Birthday Surprise 🎂", page_icon="🎁")

# ---------------- AUTOPLAY MUSIC FUNCTION ----------------
def autoplay_audio(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f"""
        <audio autoplay loop>
        <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
        </audio>
        """
        html(md, height=0)

# ---------------- PASSWORD & CLUE ----------------
PASSWORD = "Barre"   # change password
CLUE = "💡 Clue: The word you call me everytime that irritates me..."

if "unlocked" not in st.session_state:
    st.session_state.unlocked = False

# ---------------- LOCK SCREEN ----------------
if not st.session_state.unlocked:
    st.markdown("<h1 style='text-align:center;'>🔒 Birthday Surprise Locked</h1>", unsafe_allow_html=True)
    
    st.info(CLUE)

    pwd = st.text_input("🔑 Enter the Secret Password", type="password")

    if st.button("Unlock Surprise 🎁"):
        if pwd == PASSWORD:
            st.session_state.unlocked = True
            st.success("Correct! Surprise Unlocked 🎉")
            st.balloons()
        else:
            st.error("Oops! Wrong Password 😅 Try Again")

    st.stop()

# ---------------- AUTOPLAY MUSIC ----------------
autoplay_audio("birthday.mp3")

# ---------------- TITLE ----------------
st.markdown(
    "<h1 style='text-align:center; color:#ff4b4b;'>🎂 Happy Birthday Dear Brother 🎉</h1>",
    unsafe_allow_html=True
)

st.markdown("<h3 style='text-align:center;'>You are my Hero, My Guide & My Best Friend 💖</h3>", unsafe_allow_html=True)

# ---------------- GIFT BOX ANIMATION ----------------
gift_html = """
<div style="text-align:center;">
    <img src="https://media.giphy.com/media/l0MYt5jPR6QX5pnqM/giphy.gif" width="220">
    <h3>Click the Gift to Reveal Your Surprise 🎁</h3>
</div>
"""
html(gift_html, height=300)

# ---------------- BUTTON TO OPEN GIFT ----------------
if st.button("🎁 Open Gift"):
    st.balloons()

    # ---------- PHOTO GALLERY ----------
    st.markdown("## 📸 Our Beautiful Memories")
    col1, col2 = st.columns(2)

    with col1:
        st.image("photo1.jpg", use_column_width=True)
        st.image("photo2.jpg", use_column_width=True)

    with col2:
        st.image("photo3.jpg", use_column_width=True)
        st.image("photo4.jpg", use_column_width=True)

    # ---------- VIDEO ----------
    st.markdown("## 🎥 A Special Video For You")
    st.video("birthday-video.mp4")

    # ---------- LETTER ----------
    st.markdown("## 💌 A Letter From My Heart")
    st.markdown("""
    Dear Brother 💙,

    Happy Birthday to the most amazing person in my life!  
    You are not just my brother, you are my hero, my protector, and my best friend.

    Every memory with you is my biggest treasure.  
    Thank you for always supporting, guiding, and caring for me.

    May your life be filled with success, happiness, and endless smiles 🌟  
    I am truly lucky to have a brother like you!

    Happy Birthday once again 🎂🎉  
    With lots of love,  
    Your Sister 💕
    """)

    st.balloons()