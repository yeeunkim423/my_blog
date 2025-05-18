import streamlit as st
from streamlit_timeline import timeline

st.set_page_config(page_title="Daemon & Alicent Fanpage", layout="wide")

st.title("Daemon Targaryen & Alicent Hightower Fanpage")

option = st.selectbox(
    "Select a section:",
    ("Daemon", "Alicent", "Timeline")
)

if option == "Daemon":
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("data/daemon.gif", width=250)
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
    col1, col2 = st.columns([1, 1])
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

    events = {
        "events": [
            {
                "start_date": {"year": "81 AC"},
                "text": {
                    "headline": "Daemon Targaryen born",
                    "text": "Daemon Targaryen was born in 81 AC."
                }
            },
            {
                "start_date": {"year": "130 AC"},
                "text": {
                    "headline": "Daemon dies",
                    "text": "Daemon died at Gods Eye in 130 AC at age 49."
                }
            },
            {
                "start_date": {"year": "88 AC"},
                "text": {
                    "headline": "Alicent Hightower born",
                    "text": "Alicent Hightower was born in 88 AC."
                }
            },
            {
                "start_date": {"year": "Unknown"},
                "text": {
                    "headline": "Alicent marries King Viserys I",
                    "text": "Alicent became the wife of King Viserys I Targaryen."
                }
            },
            {
                "start_date": {"year": "133 AC"},
                "text": {
                    "headline": "Alicent dies",
                    "text": "Alicent died in King's Landing in 133 AC."
                }
            }
        ]
    }

    timeline(events)
