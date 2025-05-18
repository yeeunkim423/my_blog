import streamlit as st
import base64
import os

st.set_page_config(page_title="HOTD Fanpage", layout="wide")
st.title("🔥 House of the Dragon Fanpage 🔥")

IMAGE_FOLDER = "data"

# 캐릭터 데이터
daemon = {
    "Name": "Daemon Targaryen",
    "Aliases": ["Prince of the City", "Lord Flea Bottom", "The rogue prince"],
    "Titles": [
        "Prince", "Ser", "Commander of the City Watch",
        "Master of coin", "Master of laws",
        "King of the Stepstones and the Narrow Sea",
        "Lord of Runestone (claimant; briefly)",
        "Protector of the Realm"
    ],
    "Allegiances": ["House Targaryen", "Blacks"],
    "Culture": "Crownlands",
    "Born": "81 AC",
    "Died": "130 AC at the Gods Eye",
    "Parents": {"Father": "Baelon Targaryen", "Mother": "Alyssa Targaryen"},
    "Spouses": ["Lady Rhea Royce", "Lady Laena Velaryon", "Princess Rhaenyra Targaryen"],
    "Issue": ["Baela", "Rhaena", "Stillborn son", "Aegon III", "Viserys II", "Visenya"],
    "Portrayed by": "Matt Smith",
    "Image": "daemon.gif",
}

alicent = {
    "Name": "Alicent Hightower",
    "Aliases": ["The Queen in Chains"],
    "Titles": ["Lady", "Queen", "Dowager Queen"],
    "Allegiances": ["House Hightower", "House Targaryen", "Greens"],
    "Culture": "Reach",
    "Born": "88 AC",
    "Died": "133 AC in King's Landing",
    "Parents": {"Father": "Otto Hightower"},
    "Spouses": ["King Viserys I Targaryen"],
    "Issue": ["Aegon II", "Helaena", "Aemond", "Daeron"],
    "Portrayed by": "Olivia Cooke / Emily Carey (young)",
    "Images": ["alicent1.gif", "alicent2.gif"],
}

# 이미지 표시 함수
def show_gif(filename, max_width="100%"):
    path = os.path.join(IMAGE_FOLDER, filename)
    with open(path, "rb") as f:
        data = f.read()
    data_url = base64.b64encode(data).decode()
    st.markdown(f'<img src="data:image/gif;base64,{data_url}" style="max-width:{max_width};">', unsafe_allow_html=True)

# 캐릭터 출력 함수
def show_character(char):
    st.header(char["Name"])

    if "Image" in char:
        show_gif(char["Image"], max_width="50%")
    elif "Images" in char:
        cols = st.columns(len(char["Images"]))
        for i, img in enumerate(char["Images"]):
            with cols[i]:
                show_gif(img, max_width="100%")

    st.subheader("Aliases")
    st.write(", ".join(char.get("Aliases", [])))

    st.subheader("Titles")
    for title in char["Titles"]:
        st.markdown(f"- {title}")

    st.subheader("Allegiances & Culture")
    st.write(", ".join(char["Allegiances"]) + f" (Culture: {char['Culture']})")

    st.subheader("Born / Died")
    st.write(f"🟢 Born: {char['Born']}")
    st.write(f"🔴 Died: {char['Died']}")

    st.subheader("Parents")
    for role, name in char["Parents"].items():
        st.write(f"{role}: {name}")

    st.subheader("Spouse(s)")
    st.write(", ".join(char.get("Spouses", [])))

    st.subheader("Children")
    st.write(", ".join(char["Issue"]))

    st.subheader("Portrayed by")
    st.write(char["Portrayed by"])

# 타임라인 이벤트 리스트
timeline_events = [
    ("81 AC", "Daemon Targaryen born"),
    ("88 AC", "Alicent Hightower born"),
    ("97 AC", "Daemon marries Rhea Royce"),
    ("106 AC", "Viserys marries Alicent / Daemon in Stepstones"),
    ("108 AC", "Daemon kills Craghas Drahar"),
    ("109 AC", "Daemon becomes King of the Stepstones"),
    ("114 AC", "Princess Rhaenyra marries"),
    ("115 AC", "Rhea Royce dies"),
    ("116 AC", "Baela and Rhaena are born"),
    ("120 AC", "Daemon marries Rhaenyra / Laena Velaryon dies"),
    ("129 AC", "King Viserys I dies"),
    ("130 AC", "Daemon dies at Gods Eye"),
    ("133 AC", "Alicent dies in King’s Landing"),
]

# 타임라인 출력 함수
def show_timeline(events):
    st.header("📜 Daemon & Alicent Timeline")

    for year, event in events:
        with st.expander(f"{year} — {event}"):
            st.markdown(f"**Year**: {year}<br>**Event**: {event}", unsafe_allow_html=True)

# 사이드바 메뉴
menu = st.sidebar.radio("Select Section", ("Daemon Targaryen", "Alicent Hightower", "Timeline"))

if menu == "Daemon Targaryen":
    show_character(daemon)
elif menu == "Alicent Hightower":
    show_character(alicent)
elif menu == "Timeline":
    show_timeline(timeline_events)
