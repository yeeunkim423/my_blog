import streamlit as st

st.title("🍃 Comfort Place for Daelicent")
st.caption("This is my comfort place for Daelicent")

url = "https://github.com/yeeunkim423/my_blog/raw/main/images/alicent-daemon.jpg"
st.image(url, caption="1X01 The Heirs of the Dragon", use_container_width=True)

st.header("Welcome to my page!")

st.subheader("Characters")
st.write("""
**Daemon Targaryen**  
- The charismatic and complex CEO  
- Known for his boldness and charm

**Alicent Hightower**  
- Influencer and daughter of a powerful politician  
- Balances public image and private desires
""")

