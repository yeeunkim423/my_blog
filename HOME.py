import streamlit as st

st.title("🍃 Comfort Place for Daelicent")
st.caption("This is my comfort place for Daelicent")

# 메인 이미지
url = "https://github.com/yeeunkim423/my_blog/raw/main/images/alicent-daemon.jpg"
st.image(url, caption="1X01 The Heirs of the Dragon", use_container_width=True)

# 인물 정보
st.header("About Them")

people = [
    {
        "name": "Emily Carey",
        "Instagram": "https://www.instagram.com/theemilycarey/",
        "Wikipedia": "https://en.wikipedia.org/wiki/Emily_Carey",
        "Image": "data/emily2.gif",
        "YouTube": "https://youtu.be/FFfjGsfCC-g?si=lPZRXIlnHs16wXHT"  # 예시: Emily 인터뷰
    },
    {
        "name": "Olivia Cooke",
        "Instagram": "https://www.instagram.com/livkatecooke/",
        "Wikipedia": "https://en.wikipedia.org/wiki/Olivia_Cooke",
        "Image": "data/emily.gif",
        "YouTube": "https://youtu.be/R_FGY3vm6Ok?si=In2Q6wLtDIKGvtIX"  # 예시: Olivia 인터뷰
    },
    {
        "name": "Matt Smith",
        "Instagram": None,
        "Wikipedia": "https://en.wikipedia.org/wiki/Matt_Smith",
        "Image": "data/matt.gif",
        "YouTube": "https://youtu.be/kXkTiDNLChc?si=HUZ-X171jZMmES8q"  # 예시: Matt 인터뷰
    },
]

cols = st.columns(3)

for col, person in zip(cols, people):
    with col:
        # 이미지
        try:
            st.image(person["Image"], caption=person["name"], use_container_width=True)
        except:
            st.warning(f"⚠️ Could not load image for {person['name']}")
        
        # 이름과 링크
        st.subheader(person["name"])
        if person["Instagram"]:
            st.markdown(f"[📸 Instagram]({person['Instagram']})")
        else:
            st.write("Instagram: Not available")
        st.markdown(f"[🌐 Wikipedia]({person['Wikipedia']})")

        # 유튜브 영상
        st.markdown("**📺 Favorite YouTube Video**")
        st.video(person["YouTube"]) 
