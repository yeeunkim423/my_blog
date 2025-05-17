import streamlit as st

st.title("🍃 Comfort Place for Daelicent")
st.caption("This is my comfort place for Daelicent")

url = "https://github.com/yeeunkim423/my_blog/raw/main/images/alicent-daemon.jpg"
st.image(url, caption="1X01 The Heirs of the Dragon", use_container_width=True)

st.header("Welcome to my page!")

st.subheader("Latest Social Posts")
st.markdown("""
- 🌟 @daemon: "Taking over the boardroom today. #CEOlife"  
- 💚 @alicent: "Balancing fame and freedom, one step at a time."  
- 🔥 @daemon: "Power moves only. Watch this space."  
- 💬 @alicent: "Sometimes being yourself is the hardest role to play."
""")
