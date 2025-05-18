import streamlit as st
import base64
import os

st.set_page_config(page_title="HOTD Fanpage", layout="wide")
st.title("House of the Dragon Fanpage")

IMAGE_FOLDER = "data"

daemon = {
    "Name": "Daemon Targaryen",
    "Aliases": ["Prince of the City", "Lord Flea Bottom", "The rogue prince"],
    "Titles": [
        "Prince",
        "Ser",
        "Commander of the City Watch",
        "Master of coin",
        "Master of laws",
        "King of the Stepstones and the Narrow Sea",
        "Lord of Runestone (claimant; briefly)",
        "Protector of the Realm"
    ],
    "Allegiances": ["House Targaryen", "Blacks"],
    "Culture": "Crownlands",
    "Born": "81 AC",
    "Died": "22nd day of the 5th moon of 130 AC (aged 49) at the Gods Eye",
    "Parents": {"Father": "Baelon Targaryen", "Mother": "Alyssa Targaryen"},
    "Spouses": ["Lady Rhea Royce", "Lady Laena Velaryon", "Princess Rhaenyra Targaryen"],
    "Issue": ["Baela Targaryen", "Rhaena Targaryen", "Stillborn son", "Aegon III Targaryen", "Viserys II Targaryen", "Visenya Targaryen"],
    "Portrayed by": "Matt Smith",
    "Image": "daemon.gif",
}

alicent = {
    "Name": "Alicent Hightower",
    "Alias": ["The Queen in Chains"],
    "Titles": ["Lady", "Queen", "Dowager Queen"],
    "Allegiances": ["House Hightower", "House Targaryen", "Greens"],
    "Culture": "Reach",
    "Born": "88 AC",
    "Died": "133 AC in King's Landing",
    "Parents": {"Father": "Otto Hightower"},
    "Spouse": "King Viserys I Targaryen",
    "Issue": ["Aegon II Targaryen", "Helaena Targaryen", "Aemond Targaryen", "Daeron Targaryen"],
    "Portrayed by": "Olivia Cooke / Emily Carey (young)",
    "Images": ["alicent1.gif", "alicent2.gif"],
}

def show_gif(filename, max_width="100%"):
    path = os.path.join(IMAGE_FOLDER, filename)
    with open(path, "rb") as f:
        data = f.read()
    data_url = base64.b64encode(data).decode()
    gif_html = f'<img src="data:image/gif;base64,{data_url}" alt="gif" style="max-width:{max_width};">'
    st.markdown(gif_html, unsafe_allow_html=True)

def show_character(char):
    st.header(char["Name"])
    if "Image" in char:
        show_gif(char["Image"], max_width="60%")
    elif "Images" in char:
        cols = st.columns(len(char["Images"]))
        for i, img_file in enumerate(char["Images"]):
            with cols[i]:
                show_gif(img_file)

    st.subheader("Aliases")
    st.write(", ".join(char.get("Aliases", char.get("Alias", []))))
    st.subheader("Titles")
    for title in char["Titles"]:
        st.write("- " + title)
    st.subheader("Allegiances and Culture")
    st.write(", ".join(char["Allegiances"]) + f" (Culture: {char['Culture']})")
    st.subheader("Born and Died")
    st.write(f"Born: {char['Born']}")
    st.write(f"Died: {char['Died']}")
    st.subheader("Parents")
    for relation, name in char["Parents"].items():
        st.write(f"{relation}: {name}")
    st.subheader("Spouse(s)")
    spouses = char.get("Spouses") or char.get("Spouse")
    if isinstance(spouses, list):
        st.write(", ".join(spouses))
    else:
        st.write(spouses)
    st.subheader("Children")
    st.write(", ".join(char["Issue"]))
    st.subheader("Portrayed by")
    st.write(char["Portrayed by"])

character_choice = st.sidebar.selectbox(
    "Choose a section",
    ("Daemon Targaryen", "Alicent Hightower", "Timeline")
)

if character_choice in ["Daemon Targaryen", "Alicent Hightower"]:
    show_character(daemon if character_choice == "Daemon Targaryen" else alicent)

elif character_choice == "Timeline":
    st.header("Daemon & Alicent Timeline")

    events = [
        {"year": "81 AC", "headline": "Daemon Targaryen born", "text": "Daemon Targaryen was born in 81 AC."},
        {"year": "88 AC", "headline": "Alicent Hightower born", "text": "Alicent Hightower was born in 88 AC."},
        {"year": "97 AC", "headline": "Daemon marries Lady Rhea Royce", "text": "Daemon married Lady Rhea Royce."},
        {"year": "103-104 AC", "headline": "Daemon serves as Master of Coin and Master of Laws", "text": "Daemon briefly served as Master of Coin and Master of Laws."},
        {"year": "106 AC", "headline": "Viserys and Alicent's wedding & Daemon's Stepstones campaign", "text": "King Viserys I married Alicent. Daemon fought in the Stepstones."},
        {"year": "108 AC", "headline": "Daemon kills Craghas Drahar", "text": "Daemon slew Craghas Drahar."},
        {"year": "109 AC", "headline": "Daemon declares himself King of the Stepstones", "text": "Daemon proclaimed himself king of the Stepstones."},
        {"year": "111 AC", "headline": "Daemon returns to King's Landing", "text": "Daemon returned from the Stepstones."},
        {"year": "114 AC", "headline": "Princess Rhaenyra married", "text": "Rhaenyra Targaryen was married."},
        {"year": "115 AC", "headline": "Rhea Royce dies", "text": "Daemon's wife Rhea died."},
        {"year": "116 AC", "headline": "Baela and Rhaena born", "text": "Baela and Rhaena were born."},
        {"year": "120 AC", "headline": "Daemon marries Rhaenyra", "text": "Daemon married Rhaenyra."},
        {"year": "120 AC", "headline": "Laena Velaryon dies", "text": "Laena Velaryon died."},
        {"year": "129 AC", "headline": "King Viserys dies", "text": "King Viserys I died."},
        {"year": "130 AC", "headline": "Daemon dies", "text": "Daemon died at the Gods Eye."},
        {"year": "133 AC", "headline": "Alicent dies", "text": "Alicent Hightower died in King's Landing."},
    ]

    def year_to_int(year):
        try:
            return int(year.split()[0])
        except:
            return 0

    events.sort(key=lambda e: year_to_int(e["year"]))
    n = len(events)

    # HTML + CSS timeline
    st.markdown(f"""
    <style>
    .timeline-container {{
        width: 100%;
        max-width: 1000px;
        margin: 40px auto;
        position: relative;
    }}
    .timeline-line {{
        position: relative;
        height: 6px;
        background: #4a90e2;
        border-radius: 3px;
        margin: 60px 0 100px 0;
    }}
    .timeline-point {{
        position: absolute;
        top: 50%;
        width: 18px;
        height: 18px;
        background: white;
        border: 4px solid #4a90e2;
        border-radius: 50%;
        transform: translate(-50%, -50%);
        z-index: 2;
    }}
    .timeline-label {{
        position: absolute;
        width: 200px;
        font-size: 0.9rem;
        color: #2c3e50;
        text-align: center;
        left: 50%;
        transform: translateX(-50%);
    }}
    .label-below {{ top: 70px; }}
    .label-above {{ bottom: 120px; }}
    .timeline-year {{ font-weight: bold; color: #4a90e2; }}
    .timeline-headline {{ font-weight: 600; }}
    .timeline-text {{ font-size: 0.85rem; color: #555; }}
    </style>

    <div class="timeline-container">
        <div class="timeline-line"></div>
    """ + "\n".join(
        f'''
        <div class="timeline-point" style="left: {100*i/(n-1)}%;"></div>
        <div class="timeline-label {'label-below' if i%2==0 else 'label-above'}" style="left: {100*i/(n-1)}%;">
            <div class="timeline-year">{event["year"]}</div>
            <div class="timeline-headline">{event["headline"]}</div>
            <div class="timeline-text">{event["text"]}</div>
        </div>
        ''' for i, event in enumerate(events)
    ) + "</div>", unsafe_allow_html=True)
