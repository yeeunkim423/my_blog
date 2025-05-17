import streamlit as st

st.title("🍃 Comfort Place for Daelicent")
st.caption("This is my comfort place for Daelicent")

url = "https://github.com/yeeunkim423/my_blog/raw/main/images/alicent-daemon.jpg"
st.image(url, caption="1X01 The Heirs of the Dragon", use_container_width=True)

st.header("Welcome to my page!")

choice = st.radio("Who do you relate to more?", ("Daemon", "Alicent", "Both", "Neither"))

if choice == "Daemon":
    st.write("You’re a bold leader with a dash of chaos! 🐉")
elif choice == "Alicent":
    st.write("You balance the spotlight and your true self gracefully. 💚")
elif choice == "Both":
    st.write("You see the best in both worlds. ✨")
else:
    st.write("You march to your own beat. 🎵")
