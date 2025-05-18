import streamlit as st

st.set_page_config(page_title="Daelicent Comfort Page", layout="centered")

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
        "YouTube": "https://youtu.be/FFfjGsfCC-g?si=lPZRXIlnHs16wXHT",
    },
    {
        "name": "Olivia Cooke",
        "Instagram": "https://www.instagram.com/livkatecooke/",
        "Wikipedia": "https://en.wikipedia.org/wiki/Olivia_Cooke",
        "Image": "data/emily.gif",
        "YouTube": "https://youtu.be/R_FGY3vm6Ok?si=In2Q6wLtDIKGvtIX",
    },
    {
        "name": "Matt Smith",
        "Instagram": None,
        "Wikipedia": "https://en.wikipedia.org/wiki/Matt_Smith",
        "Image": "data/matt.gif",
        "YouTube": "https://youtu.be/kXkTiDNLChc?si=HUZ-X171jZMmES8q",
    },
]

# 배우별 정보 - expander 안에 표시
for person in people:
    with st.expander(person["name"]):
        try:
            st.image(person["Image"], caption=person["name"], use_container_width=True)
        except:
            st.warning(f"⚠️ Could not load image for {person['name']}")

        # 링크들
        if person["Instagram"]:
            st.markdown(f"[📸 Instagram]({person['Instagram']})")
        else:
            st.write("Instagram: Not available")
        st.markdown(f"[🌐 Wikipedia]({person['Wikipedia']})")

        # 유튜브
        st.markdown("**📺 Favorite YouTube Video**")
        st.video(person["YouTube"])

        st.markdown("---")

# (위에 너가 작성한 Streamlit 코드들...)

# 페이지 맨 아래 추가
st.markdown("""
    <style>
    .back-to-top {
        position: fixed;
        bottom: 40px;
        right: 30px;
        background-color: #f0f2f6;
        color: #444;
        padding: 10px 16px;
        border-radius: 10px;
        border: none;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
        cursor: pointer;
        z-index: 100;
    }
    .back-to-top:hover {
        background-color: #e0e2e6;
    }
    </style>

    <button class="back-to-top" onclick="window.scrollTo({top: 0, behavior: 'smooth'});">
        🔝 Back to Top
    </button>
""", unsafe_allow_html=True)
