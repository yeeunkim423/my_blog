import streamlit as st

st.title("🍃 Comfort place for Daelicent")
st.caption("This is my comfort place for Daelicent")

url = "https://github.com/yeeunkim423/my_blog/raw/main/images/alicent-daemon.jpg"
# 이미지가 화면 너비에 맞춰 조정되도록 설정
st.image(url, caption="Image link", use_column_width=True)

st.header("Welcome to my page!")

with st.expander("Undress - Sombr"):
    st.write("""
    And I don't wanna learn another scent.  
    I don't want children of another man to have the eyes of the girl I won't forget.
    """)
    st.markdown("*Tags: #lyrics*")
