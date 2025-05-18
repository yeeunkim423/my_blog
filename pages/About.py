import streamlit as st
import base64
import os

st.set_page_config(page_title="HOTD Timeline", layout="wide")
st.title("🔥 House of the Dragon — Daemon & Alicent 🔥")

IMAGE_FOLDER = "data"

# 캐릭터 데이터
daemon = {
    "Name": "Daemon Targaryen",
    "Aliases": ["Prince of the City", "Lord Flea Bottom", "The rogue prince"],
    "Titles": [
        "Prince", "Commander of the City Watch", "Master of coin",
        "King of the Stepstones and the Narrow Sea", "Protector of the Realm"
    ],
    "Allegiances": ["House Targaryen", "Blacks"],
    "Culture": "Crownlands",
    "Born": "81 AC",
    "Died": "130 AC at the Gods Eye",
    "Parents": {"Father": "Baelon Targaryen", "Mother": "Alyssa Targaryen"},
    "Spouses": ["Rhea Royce", "Laena Velaryon", "Rhaenyra Targaryen"],
    "Issue": ["Baela", "Rhaena", "Aegon III", "Viserys II", "Stillborn son", "Visenya"],
    "Portrayed by": "Matt Smith",
    "Image": "daemon.gif",
}

alicent = {
    "Name": "Alicent Hightower",
    "Aliases": ["The Queen in Chains"],
    "Titles": ["Queen", "Dowager Queen"],
    "Allegiances": ["House Hightower", "House Targaryen", "Greens"],
    "Culture": "Reach",
    "Born": "88 AC",
    "Died": "133 AC in King's Landing",
    "Parents": {"Father": "Otto Hightower"},
    "Spouses": ["King Viserys I Targaryen"],
    "Issue": ["Aegon II", "Helaena", "Aemond", "Daeron"],
    "Portrayed by": "Olivia Cooke / Emily Carey",
    "Images": ["alicent1.gif", "alicent2.gif"],
}

timeline_events = [
    ("81 AC", "Daemon Targaryen is born"),
    ("88 AC", "Alicent Hightower is born"),
    ("97 AC", "Daemon marries Rhea Royce of Runestone"),
    ("106 AC", "Viserys marries Alicent Hightower"),
    ("108 AC", "Daemon defeats the Crabfeeder at the Stepstones"),
    ("115 AC", "Rhea Royce dies mysteriously; Daemon returns to court"),
    ("116 AC", "Laena Velaryon dies; Daemon eventually marries Rhaenyra"),
    ("120 AC", "Daemon and Rhaenyra marry; tensions rise"),
    ("129 AC", "Viserys I dies — the Dance of the Dragons begins"),
    ("130 AC", "Daemon dies at the Gods Eye"),
    ("133 AC", "Alicent dies during the aftermath of the war"),
]

# 이미지 표시 함수
def show_gif(filename, max_width="100%"):
    path = os.path.join(IMAGE_FOLDER, filename)
    with open(path, "rb") as f:
        data = f.read()
    data_url = base64.b64encode(data).decode()
    st.markdown(f'<img src="data:image/gif;base64,{data_url}" style="max-width:{max_width}; border-radius: 10px;">', unsafe_allow_html=True)

# 캐릭터 출력 함수
def show_character(char):
    st.header(char["Name"])

    # 이미지
    if "Image" in char:
        show_gif(char["Image"], max_width="50%")
    elif "Images" in char:
        cols = st.columns(len(char["Images"]))
        for i, img in enumerate(char["Images"]):
            with cols[i]:
                show_gif(img)

    st.subheader("🌀 Aliases")
    st.write(", ".join(char.get("Aliases", [])))

    st.subheader("👑 Titles")
    st.markdown("<ul>" + "".join(f"<li>{t}</li>" for t in char["Titles"]) + "</ul>", unsafe_allow_html=True)

    st.subheader("🛡️ Allegiances")
    st.write(", ".join(char["Allegiances"]))

    st.subheader("📅 Born / Died")
    st.write(f"**Born**: {char['Born']} &nbsp;&nbsp;&nbsp; **Died**: {char['Died']}")

    st.subheader("🧬 Parents")
    for role, name in char["Parents"].items():
        st.write(f"{role}: {name}")

    st.subheader("💍 Spouses")
    st.write(", ".join(char.get("Spouses", [])))

    st.subheader("👶 Children")
    st.write(", ".join(char["Issue"]))

    st.subheader("🎭 Portrayed by")
    st.write(char["Portrayed by"])

# 타임라인 출력 함수
def show_timeline(events):
    st.markdown("""
        <style>
        .timeline-card {
            background-color: #f0f2f6;
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1rem;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }
        .year {
            font-size: 1.2rem;
            color: #d62828;
            font-weight: bold;
        }
        .event {
            font-size: 1rem;
            color: #333;
        }
        </style>
    """, unsafe_allow_html=True)

    st.header("📜 Timeline of Daemon & Alicent")

    for year, event in events:
        st.markdown(f"""
        <div class="timeline-card">
            <div class="year">{year}</div>
            <div class="event">{event}</div>
        </div>
        """, unsafe_allow_html=True)

# 선택 메뉴
option = st.selectbox("🔎 View", ["Daemon Targaryen", "Alicent Hightower", "Timeline"])

if option == "Daemon Targaryen":
    show_character(daemon)
elif option == "Alicent Hightower":
    show_character(alicent)
elif option == "Timeline":
    show_timeline(timeline_events)
