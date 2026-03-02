import streamlit as st
from streamlit.components.v1 import html
import base64

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Birthday Surprise 🎂", page_icon="🎁")

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

# ---------------- SESSION STATES FOR BUTTONS ----------------
if "show_gift" not in st.session_state:
    st.session_state.show_gift = False
if "show_photos" not in st.session_state:
    st.session_state.show_photos = False
if "show_video" not in st.session_state:
    st.session_state.show_video = False
if "show_letter" not in st.session_state:
    st.session_state.show_letter = False
if "show_final" not in st.session_state:
    st.session_state.show_final = False

# ---------------- TITLE ----------------
st.markdown(
    "<h1 style='text-align:center; color:#ff4b4b;'>🎂 Happy Birthday Annaya 🎉</h1>",
    unsafe_allow_html=True
)

st.markdown("<h3 style='text-align:center;'> 💖To My LOvely Barre...😁</h3>", unsafe_allow_html=True)

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
    st.session_state.show_gift = True
    st.balloons()
    st.success("Your Surprise Awaits 💖")

if st.session_state.show_gift:

    # -------- BUTTON TO REVEAL PHOTOS --------
    if st.button("📸 Reveal Our Memories"):
        st.session_state.show_photos = True

    if st.session_state.show_photos:
        st.markdown("## 📸 Our Beautiful Memories")
        col1, col2 = st.columns(2)

        with col1:
            st.image("photo1.jpg", use_container_width=True)
            st.image("photo2.jpg", use_container_width=True)

        with col2:
            st.image("photo3.jpg", use_container_width=True)
            st.image("photo4.jpg", use_container_width=True)

    # -------- BUTTON TO REVEAL VIDEO --------
    if st.button("🎥 Play Special Video"):
        st.session_state.show_video = True

    if st.session_state.show_video:
        st.markdown("## 🎥 A Special Video For You , Already Pampina Ankunta kani malli chudu")
        st.video("birthday-video.mp4")

    # -------- BUTTON TO REVEAL LETTER --------
    if st.button("💌 Read My Letter"):
        st.session_state.show_letter = True

    if st.session_state.show_letter:
        st.markdown("## 💌 A Letter From My Heart")
        st.markdown("""
        To my Handsome Barre 💙,

        Happy Birthday to the most Craziest and Lovely person in my life!  
        You are not just my brother, my protector, and my best friend.

        Every memory with you is my biggest treasure and i feel soo happy to be with you.  
        Thank you for always supporting, Loving, and caring for me.

        May your life be filled with success, happiness, and endless smiles 🌟  
        I am truly lucky to have a brother like you!
        Your Chelli Loves You Sooooooooooooo Much & She will be Always there for you !! No Matter What 🫂💖

        Happy Birthday once again 🎂🎉  
        With lots of love,  
        From Your Chelli🫂🫂💕
        """)

    # -------- FINAL SPECIAL BUTTON --------
    if st.button("💖 Final Surprise 💖"):
        st.session_state.show_final = True

    if st.session_state.show_final:
        hearts_html = """
        <div style="text-align:center; font-size:40px;">
            ❤️ 💖 💕 💗 💓 💞 💘
        </div>

        <h1 style="text-align:center; color:#ff4b4b;">
        🎂 Happy Birthday 🎂
        </h1>

        <h2 style="text-align:center; color:#ff69b4;">
        🎉 Happy 22 🎉
        </h2>

        <h3 style="text-align:center;">
        Love from your Chelli 💖
        </h3>
        """
        html(hearts_html, height=300)
        st.balloons()