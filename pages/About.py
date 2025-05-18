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

    # 타임라인 스타일 CSS
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
