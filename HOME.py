import streamlit as st

st.title("🍃 Comfort Place for Daelicent")
st.caption("This is my comfort place for Daelicent")

url = "https://github.com/yeeunkim423/my_blog/raw/main/images/alicent-daemon.jpg"
st.image(url, caption="1X01 The Heirs of the Dragon", use_container_width=True)

import streamlit as st

st.header("About Them")

people = [
    {"name": "Emily Carey", "Instagram": "https://www.instagram.com/theemilycarey/", "Wikipedia": "https://en.wikipedia.org/wiki/Emily_Carey"},
    {"name": "Olivia Cooke", "Instagram": "https://www.instagram.com/livkatecooke/", "Wikipedia": "https://en.wikipedia.org/wiki/Olivia_Cooke"},
    {"name": "Matt Smith", "Instagram": None, "Wikipedia": "https://en.wikipedia.org/wiki/Matt_Smith"},
]

cols = st.columns(3)

for col, person in zip(cols, people):
    with col:
        st.header(person["name"])
        if person["Instagram"]:
            st.markdown(f"[📸 Instagram]({person['Instagram']})")
        else:
            st.write("Instagram: Not available"

        st.markdown(f"[Wikipedia]([person['Wikipedia']}")


