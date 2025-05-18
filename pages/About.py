import streamlit as st

st.set_page_config(page_title="Daemon & Alicent Fanpage", layout="wide")

# --- CSS for timeline with better colors ---
timeline_css = """
<style>
.timeline {
  position: relative;
  max-width: 700px;
  margin: 0 auto;
  padding: 10px 0;
}
.timeline::after {
  content: '';
  position: absolute;
  width: 4px;
  background-color: #888;  /* 은은한 회색 */
  top: 0;
  bottom: 0;
  left: 50%;
  margin-left: -2px;
}
.container {
  padding: 10px 40px;
  position: relative;
  background-color: inherit;
  width: 50%;
}
.left {
  left: 0;
}
.right {
  left: 50%;
}
.left::before, .right::before {
  content: " ";
  position: absolute;
  width: 25px;
  height: 25px;
  right: -17px;
  background-color: white;
  border: 4px solid #555; /* 진한 회색 테두리 */
  top: 15px;
  border-radius: 50%;
  z-index: 1;
}
.right::before {
  left: -16px;
}
.content {
  padding: 20px 30px;
  background-color: #f0f0f0; /* 연한 회색 배경 */
  color: #111; /* 진한 검정 텍스트 */
  position: relative;
  border-radius: 6px;
  box-shadow: 1px 1px 5px rgba(0,0,0,0.1); /* 은은한 그림자 */
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}
@media screen and (max-width: 600px) {
  .timeline::after {
    left: 31px;
  }
  .container {
    width: 100%;
    padding-left: 70px;
    padding-right: 25px;
  }
  .container::before {
    left: 60px;
  }
  .left, .right {
    left: 0%;
  }
  .right::before {
    left: 60px;
  }
}
</style>
"""

# --- Timeline HTML content ---
timeline_html = """
<div class="timeline">
  <div class="container left">
    <div class="content">
      <h3>81 AC - Birth of Daemon Targaryen</h3>
      <p>Daemon was born to Baelon and Alyssa Targaryen.</p>
    </div>
  </div>
  <div class="container right">
    <div class="content">
      <h3>88 AC - Birth of Alicent Hightower</h3>
      <p>Born to Otto Hightower in the Reach.</p>
    </div>
  </div>
  <div class="container left">
    <div class="content">
      <h3>Rhaenyra's Reign and the Dance of the Dragons</h3>
      <p>Daemon serves as a commander and key figure during this period.</p>
    </div>
  </div>
  <div class="container right">
    <div class="content">
      <h3>Alicent Becomes Queen</h3>
      <p>She marries King Viserys I Targaryen and becomes the Queen in Chains.</p>
    </div>
  </div>
  <div class="container left">
    <div class="content">
      <h3>130 AC - Death of Daemon Targaryen</h3>
      <p>Daemon dies at age 49 near the Gods Eye.</p>
    </div>
  </div>
  <div class="container right">
    <div class="content">
      <h3>133 AC - Death of Alicent Hightower</h3>
      <p>She dies in King's Landing.</p>
    </div>
  </div>
</div>
"""

st.title("Daemon Targaryen & Alicent Hightower Fanpage")

option = st.selectbox("Select character or timeline to view:", ["Daemon", "Alicent", "Timeline"])

if option == "Daemon":
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("data/daemon.gif", width=220)
    with col2:
        st.subheader("Daemon Targaryen")
        st.markdown("""
**Aliases:** Prince of the City, Lord Flea Bottom, The rogue prince  
**Titles:** Prince, Ser, Commander of the City Watch, Master of coin, Master of laws, King of the Stepstones and the Narrow Sea, Lord of Runestone (claimant), Protector of the Realm  
**Allegiances:** House Targaryen (Blacks)  
**Race:** Valyrian  
**Culture:** Crownlands  
**Born:** 81 AC  
**Died:** 130 AC (aged 49), the Gods Eye  
**Father:** Baelon Targaryen  
**Mother:** Alyssa Targaryen  
**Spouses:** Lady Rhea Royce, Lady Laena Velaryon, Princess Rhaenyra Targaryen  
**Issue:** Baela Targaryen, Rhaena Targaryen, Stillborn son, Aegon III Targaryen, Viserys II Targaryen, Visenya Targaryen  
**Played by:** Matt Smith (TV series House of the Dragon)
        """)

elif option == "Alicent":
    col1, col2 = st.columns(2)
    with col1:
        st.image("data/alicent1.gif", width=250)
        st.image("data/alicent2.gif", width=250)
    with col2:
        st.subheader("Alicent Hightower")
        st.markdown("""
**Alias:** The Queen in Chains  
**Titles:** Lady, Queen, Dowager Queen  
**Allegiances:** House Hightower, House Targaryen (Greens)  
**Culture:** Reach  
**Born:** 88 AC  
**Died:** 133 AC, King's Landing  
**Father:** Otto Hightower  
**Spouse:** King Viserys I Targaryen  
**Issue:** Aegon II Targaryen, Helaena Targaryen, Aemond Targaryen, Daeron Targaryen  
**Played by:** Olivia Cooke, Emily Carey (young) (TV series House of the Dragon)
        """)

else:  # Timeline
    st.subheader("Timeline of Daemon Targaryen and Alicent Hightower")
    st.markdown(timeline_css, unsafe_allow_html=True)
    st.markdown(timeline_html, unsafe_allow_html=True)
