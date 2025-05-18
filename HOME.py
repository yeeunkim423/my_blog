import streamlit as st

st.title("🍃 Comfort Place for Daelicent")
st.caption("This is my comfort place for Daelicent")

url = "https://github.com/yeeunkim423/my_blog/raw/main/images/alicent-daemon.jpg"
st.image(url, caption="1X01 The Heirs of the Dragon", use_container_width=True)

st.header("About Them")

# 각자 SNS 링크 (예시)
person1 = {
    "name": "Emily Carey",
    "Instagram": "https://www.instagram.com/theemilycarey/",
}

person2 = {
    "name": "Olivia Cooke",
    "Instagram": "https://www.instagram.com/livkatecooke/",
}

person3 = {
  "name": "Matt Smith",
}

col1, col2, col3 = st.columns(3)

with col1:
    st.header(person1["name"])
    st.markdown(f"[📸 Instagram]({person1['Instagram']})")

with col2:
    st.header(person2["name"])
    st.markdown(f"[📸 Instagram]({person2['Instagram']})")

with col3:
  st.header(person3["name"])
