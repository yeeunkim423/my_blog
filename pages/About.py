import streamlit as st
import base64
import os

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
        if char["Name"] == "Daemon Targaryen":
            show_gif(char["Image"], max_width="60%")  # Daemon 이미지 크기 줄임
        else:
            show_gif(char["Image"])
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

if character_choice == "Daemon Targaryen":
    show_character(daemon)
elif character_choice == "Alicent Hightower":
    show_character(alicent)
elif character_choice == "Timeline":
    st.header("Daemon & Alicent Timeline")

    events = [
        {"year": "81 AC", "headline": "Daemon Targaryen born", "text": "Daemon Targaryen was born in 81 AC."},
        {"year": "88 AC", "headline": "Alicent Hightower born", "text": "Alicent Hightower was born in 88 AC."},
        {"year": "97 AC", "headline": "Daemon marries Lady Rhea Royce", "text": "Daemon married Lady Rhea Royce."},
        {"year": "103-104 AC", "headline": "Daemon serves as Master of Coin and Master of Laws", "text": "Daemon briefly served as Master of Coin from 103 to 104 AC, and Master of Laws for six months after."},
        {"year": "106 AC", "headline": "Viserys and Alicent's wedding & Daemon's Stepstones campaign", "text": (
            "King Viserys I Targaryen married Alicent Hightower. "
            "Daemon allied with Corlys Velaryon to wage war for the Stepstones, "
            "leading an army with his dragon Caraxes." )},
        {"year": "108 AC", "headline": "Daemon kills Craghas Drahar", "text": "Daemon made enemies in Lys, Myr, and Tyrosh and slew Craghas Drahar."},
        {"year": "109 AC", "headline": "Daemon declares himself King of the Stepstones and Narrow Sea", "text": "After conquering most islands, Daemon proclaimed himself king."},
        {"year": "111 AC", "headline": "Daemon returns to King's Landing", "text": "Bored with ruling, Daemon returned to the capital."},
        {"year": "114 AC", "headline": "Princess Rhaenyra married", "text": "Princess Rhaenyra Targaryen got married."},
        {"year": "115 AC", "headline": "Rhea Royce dies", "text": "Daemon's wife, Rhea Royce, died from a horse fall."},
        {"year": "116 AC", "headline": "Birth of Baela and Rhaena Targaryen", "text": "Baela and Rhaena were born in Pentos."},
        {"year": "120 AC", "headline": "Daemon marries Rhaenyra Targaryen", "text": "At age 39, Daemon married his niece Rhaenyra, the Princess of Dragonstone."},
        {"year": "120 AC", "headline": "Laena Velaryon dies", "text": "Laena Velaryon, Daemon's wife, died."},
        {"year": "129 AC", "headline": "Death of King Viserys I", "text": "King Viserys I Targaryen died in his sleep on the third day of the third moon."},
        {"year": "130 AC", "headline": "Death of Daemon Targaryen", "text": "Daemon died at Gods Eye at age 49."},
        {"year": "133 AC", "headline": "Death of Alicent Hightower", "text": "Alicent died in King's Landing."},
    ]

    def year_to_int(year):
        try:
            return int(year.split()[0])
        except:
            return 0

    events.sort(key=lambda e: year_to_int(e["year"]))

    n = len(events)

    st.markdown(f"""
    <style>
    .timeline-container {{
        width: 100%;
        max-width: 900px;
        margin: 40px auto;
        position: relative;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
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
        cursor: pointer;
        transition: background-color 0.3s, transform 0.3s;
        z-index: 2;
    }}
    .timeline-point:hover {{
        background-color: #4a90e2;
        transform: translate(-50%, -50%) scale(1.3);
        border-color: white;
    }}
    .timeline-label {{
        position: absolute;
        width: 200px;
        font-size: 0.9rem;
        color: #2c3e50;
        text-align: center;
        left: 50%;
        transform: translateX(-50%);
        cursor: default;
    }}
    .label-below {{
        top: 70px;
    }}
    .label-above {{
        bottom: 120px;
    }}
    .timeline-year {{
        font-weight: 700;
        color: #4a90e2;
        margin-bottom: 4px;
    }}
    .timeline-headline {{
        font-weight: 600;
        margin: 2px 0;
    }}
    .timeline-text {{
        font-size: 0.85rem;
        color: #555;
        margin-top: 4px;
    }}
    </style>

    <div class="timeline-container">
        <div class="timeline-line"></div>
    """ + "\n".join(
        f'''
        <div class="timeline-point" style="left: {100*i/(n-1)}%;"></div>
        <div class="timeline-label {'label-below' if i % 2 == 0 else 'label-above'}" style="left: {100*i/(n-1)}%;">
            <div class="timeline-year">{events[i]['year']}</div>
            <div class="timeline-headline">{events[i]['headline']}</div>
            <div class="timeline-text">{events[i]['text']}</div>
        </div>
        ''' for i in range(n)
    ) + """
    </div>
    """, unsafe_allow_html=True)
