import streamlit as st

st.set_page_config(page_title="Daelicent 소개", layout="centered")

st.title("Daelicent 소개")
st.caption("House of the Dragon 드라마의 알리센트 하이터워와 다에몬 타르가르옌 캐릭터 소개")

# 알리센트 소개
st.header("알리센트 하이터워")
st.image("https://upload.wikimedia.org/wikipedia/en/9/98/Alicent_Hightower_House_of_the_Dragon.jpg",
         caption="알리센트 하이터워 (House of the Dragon)", use_container_width=True)
st.markdown("""
- **배우:** 에밀리 케리(어린 시절), 올리비아 쿡(성인 시절)  
- **역할:** 오토 하이터워의 딸, 왕 비세리스 1세의 아내, 타르가르옌 가문의 중요한 인물들 어머니  
- **성격:** 야심차고 정치적으로 능숙하며 복잡한 감정을 지닌 인물  
- **스토리 중요성:** 타르가르옌 내전(용들의 춤)에서 핵심적인 역할을 담당  
""")

st.markdown("---")

# 다에몬 소개
st.header("다에몬 타르가르옌")
st.image("https://upload.wikimedia.org/wikipedia/en/4/42/Daemon_Targaryen_House_of_the_Dragon.jpg",
         caption="다에몬 타르가르옌 (House of the Dragon)", use_container_width=True)
st.markdown("""
- **배우:** 맷 스미스  
- **역할:** 비세리스 1세의 동생, 타르가르옌 가문의 왕자  
- **성격:** 카리스마 있고 냉철하며 전투 능력이 뛰어나고 예측 불가능한 인물  
- **스토리 중요성:** 왕위 계승 갈등의 중심 인물이며 가족 및 동맹과 복잡한 관계를 형성  
""")

st.markdown("---")

