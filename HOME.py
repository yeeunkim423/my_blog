import streamlit as st

st.title("🍃 Comfort place for Daelicent")
st.caption("This is my comfort place for Daelicent")

url = "https://github.com/yeeunkim423/my_blog/raw/main/images/alicent-daemon.jpg"
# 최신 방식으로 이미지 반응형 설정
st.image(url, caption="Image link", use_container_width=True)

st.header("Welcome to my page!")

with st.expander("Undress - Sombr"):
    st.write("""
    And I don't wanna learn another scent.  
    I don't want children of another man to have the eyes of the girl I won't forget.
    """)
    st.markdown("*Tags: #lyrics*")
