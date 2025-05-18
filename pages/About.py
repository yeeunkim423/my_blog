import streamlit as st

st.set_page_config(page_title="Daemon & Alicent Fanpage", layout="wide")

st.title("Daemon Targaryen & Alicent Hightower Fanpage")

option = st.selectbox(
    "Select a section:",
    ("Daemon", "Alicent", "Timeline")
)

if option == "Daemon":
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("data/daemon.gif", width=220)
    with col2:
        st.header("Daemon Targaryen")
        st.markdown("""
**Aliases:** Prince of the City, Lord Flea Bottom, The rogue prince  
**Titles:** Prince, Ser, Commander of the City Watch, Master of Coin, Master of Laws, King of the Stepstones and the Narrow Sea, Protector of the Realm  
**Allegiances:** House Targaryen (Blacks)  
**Born:** 81 AC  
**Died:** 130 AC (aged 49) at Gods Eye  
**Parents:** Baelon Targaryen & Alyssa Targaryen  
**Spouses:** Lady Rhea Royce, Lady Laena Velaryon, Princess Rhaenyra Targaryen  
**Issue:** Baela, Rhaena, Stillborn son, Aegon III, Viserys II, Visenya  
**Played by:** Matt Smith
""")

elif option == "Alicent":
    col1, col2 = st.columns(2)
    with col1:
        st.image("data/alicent1.gif", width=300)
    with col2:
        st.image("data/alicent2.gif", width=300)
    st.header("Alicent Hightower")
    st.markdown("""
**Alias:** The Queen in Chains  
**Titles:** Lady, Queen, Dowager Queen  
**Allegiances:** House Hightower, House Targaryen (Greens)  
**Born:** 88 AC  
**Died:** 133 AC in King's Landing  
**Father:** Otto Hightower  
**Spouse:** King Viserys I Targaryen  
**Issue:** Aegon II, Helaena, Aemond, Daeron  
**Played by:** Olivia Cooke / Emily Carey (young)
""")

elif option == "Timeline":
    st.header("Daemon & Alicent Timeline")

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
  background-color: #bbb;
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
  border: 4px solid #FF5733;
  top: 15px;
  border-radius: 50%;
  z-index: 1;
}
.right::before {
  left: -16px;
}
.content {
  padding: 20px 30px;
  background-color: #FFDDC1;
  position: relative;
  border-radius: 6px;
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

    timeline_html = """
<div class="timeline">
  <div class="container left">
    <div class="content">
      <h3>81 AC - Daemon Born</h3>
      <p>Daemon Targaryen was born.</p>
    </div>
  </div>
  <div class="container right">
    <div class="content">
      <h3>88 AC - Alicent Born</h3>
      <p>Alicent Hightower was born.</p>
    </div>
  </div>
  <div class="container left">
    <div class="content">
      <h3>130 AC - Daemon Dies</h3>
      <p>Daemon died at Gods Eye at age 49.</p>
    </div>
  </div>
  <div class="container right">
    <div class="content">
      <h3>133 AC - Alicent Dies</h3>
      <p>Alicent died in King's Landing.</p>
    </div>
  </div>
</div>
"""

    st.markdown(timeline_css + timeline_html, unsafe_allow_html=True)
