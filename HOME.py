import streamlit as st

st.title("🍃 Comfort Place for Daelicent")
st.caption("This is my comfort place for Daelicent")

# 메인 이미지 (웹 이미지)
url = "https://github.com/yeeunkim423/my_blog/raw/main/images/alicent-daemon.jpg"
st.image(url, caption="1X01 The Heirs of the Dragon", use_container_width=True)

# 인물 정보
st.header("About Them")

people = [
    {
        "name": "Emily Carey",
        "Instagram": "https://www.instagram.com/theemilycarey/",
        "Wikipedia": "https://en.wikipedia.org/wiki/Emily_Carey",
        "Image": "data/emily2.gif"
    },
    {
        "name": "Olivia Cooke",
        "Instagram": "https://www.instagram.com/livkatecooke/",
        "Wikipedia": "https://en.wikipedia.org/wiki/Olivia_Cooke",
        "Image": "data/emily.gif"
    },
    {
        "name": "Matt Smith",
        "Instagram": None,
        "Wikipedia": "https://en.wikipedia.org/wiki/Matt_Smith",
        "Image": "data/matt.gif"
    },
]

cols = st.columns(3)

for col, person in zip(cols, people):
    with col:
        try:
            st.image(person["Image"], use_container_width=True)
        except:
            st.warning(f"⚠️ Could not load image for {person['name']}")
        
        st.subheader(person["name"])
        if person["Instagram"]:
            st.markdown(f"[📸 Instagram]({person['Instagram']})")
        else:
            st.write("Instagram: Not available")
        st.markdown(f"[🌐 Wikipedia]({person['Wikipedia']})")
