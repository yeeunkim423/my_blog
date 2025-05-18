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
        st.markdown(
            '<img src="data/daemon.gif" width="250" alt="Daemon GIF">',
            unsafe_allow_html=True
        )
    with col2:
        st.header("Daemon Targaryen")
        st.markdown("""
        <style>
        .desc {
            font-size: 16px;
            line-height: 1.6;
            color: #333333;
        }
        </style>
        <div class="desc">
        <p><strong>Aliases:</strong> Prince of the City, Lord Flea Bottom, The rogue prince</p>
        <p><strong>Titles:</strong> Prince, Ser, Commander of the City Watch, Master of Coin, Master of Laws, King of the Stepstones and the Narrow Sea, Protector of the Realm</p>
        <p><strong>Allegiances:</strong> House Targaryen (Blacks)</p>
        <p><strong>Born:</strong> 81 AC</p>
        <p><strong>Died:</strong> 130 AC (aged 49) at Gods Eye</p>
        <p><strong>Parents:</strong> Baelon Targaryen & Alyssa Targaryen</p>
        <p><strong>Spouses:</strong> Lady Rhea Royce, Lady Laena Velaryon, Princess Rhaenyra Targaryen</p>
        <p><strong>Issue:</strong> Baela, Rhaena, Stillborn son, Aegon III, Viserys II, Visenya</p>
        <p><strong>Played by:</strong> Matt Smith</p>
        </div>
        """, unsafe_allow_html=True)

elif option == "Alicent":
    col1, col2 = st.columns([1, 1])
    with col1:
        st.markdown(
            '<img src="data/alicent1.gif" width="300" alt="Alicent GIF 1">',
            unsafe_allow_html=True
        )
    with col2:
        st.markdown(
            '<img src="data/alicent2.gif" width="300" alt="Alicent GIF 2">',
            unsafe_allow_html=True
        )
    st.header("Alicent Hightower")
    st.markdown("""
    <style>
    .desc {
        font-size: 16px;
        line-height: 1.6;
        color: #333333;
    }
    </style>
    <div class="desc">
    <p><strong>Alias:</strong> The Queen in Chains</p>
    <p><strong>Titles:</strong> Lady, Queen, Dowager Queen</p>
    <p><strong>Allegiances:</strong> House Hightower, House Targaryen (Greens)</p>
    <p><strong>Born:</strong> 88 AC</p>
    <p><strong>Died:</strong> 133 AC in King's Landing</p>
    <p><strong>Father:</strong> Otto Hightower</p>
    <p><strong>Spouse:</strong> King Viserys I Targaryen</p>
    <p><strong>Issue:</strong> Aegon II, Helaena, Aemond, Daeron</p>
    <p><strong>Played by:</strong> Olivia Cooke / Emily Carey (young)</p>
    </div>
    """, unsafe_allow_html=True)

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
